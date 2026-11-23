#!/usr/bin/env python3
"""Declaration indexer for the RH-Alpoge Lean archive.

For every declaration it records: full name, file, start line, end line,
namespace stack, active opens, kind, and the set of identifier tokens in
its text (comments and strings stripped).  Output: one TSV per worker.

Usage: index_decls.py ROOT OUTPREFIX WORKER NWORKERS
"""
import os, re, sys

ROOT, OUT, W, NW = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])

LETTER = r"A-Za-z_Ͱ-ΟΡΤ-κμ-Ͽἀ-῾℀-⅏ᴀ-ᶿ"
REST = LETTER + r"0-9'!?₀-ₜᵢ-ᵪ⁰-ⁿ"
IDENT = re.compile(r"@?(?:«[^»]*»|[" + LETTER + r"][" + REST + r"]*)(?:\.(?:«[^»]*»|[" + LETTER + r"][" + REST + r"]*))*")
KW = re.compile(r"^(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|partial|unsafe|nonrec|scoped|local)\s+)*"
                r"(theorem|lemma|def|abbrev|instance|structure|class|inductive|opaque|axiom|example|irreducible_def|class\s+inductive)\b\s*(.*)$")
CONT = ("|", "where", "termination_by", "decreasing_by", "deriving", "with", ")", "}", "]", "⟩", "·", "  ")

def strip_comments(text):
    out, i, n, depth = [], 0, len(text), 0
    while i < n:
        if depth == 0 and text.startswith("--", i):
            j = text.find("\n", i)
            if j < 0: break
            i = j; continue
        if text.startswith("/-", i):
            depth += 1; i += 2; continue
        if depth > 0 and text.startswith("-/", i):
            depth -= 1; i += 2; continue
        if depth > 0:
            if text[i] == "\n": out.append("\n")
            i += 1; continue
        if text[i] == '"':
            j = i + 1
            while j < n and text[j] != '"':
                if text[j] == "\\": j += 1
                j += 1
            out.append('""'); i = j + 1; continue
        out.append(text[i]); i += 1
    return "".join(out)

def parse_open(rest):
    rest = rest.split(" in ")[0] if " in" in rest else rest
    rest = re.sub(r"\([^)]*\)", " ", rest)
    toks = [t for t in rest.split() if t not in ("scoped", "hiding", "renaming", "in", "→")]
    return [t.lstrip("_root_.") if t.startswith("_root_.") else t for t in toks if IDENT.fullmatch(t)]

def files():
    allf = []
    for d, _, fs in os.walk(ROOT):
        for f in fs:
            if f.endswith(".lean"):
                allf.append(os.path.join(d, f))
    allf.sort()
    return allf[W::NW]

def main():
    out = open(f"{OUT}.{W}.tsv", "w")
    for path in files():
        rel = os.path.relpath(path, ROOT)
        try:
            raw = open(path, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        lines = strip_comments(raw).split("\n")
        stack = []  # entries: [kind, nameparts, opens, attrs]
        pending_open, pending_ns = [], []
        cur = None
        def ns():
            parts = []
            for e in stack:
                if e[0] == "namespace": parts += e[1]
            return parts
        def opens():
            o = []
            for e in stack: o += e[2]
            return o
        def attr_insts():
            a = []
            for e in stack: a += e[3]
            return a
        def flush(endline):
            nonlocal cur
            if cur is None: return
            name, kind, start, nsp, ops, extra, buf = cur
            text = "\n".join(buf)
            toks = set(m.group(0).lstrip("@") for m in IDENT.finditer(text))
            toks |= set(extra)
            out.write("\t".join([name, kind, rel, str(start), str(endline), ".".join(nsp), " ".join(ops), " ".join(sorted(toks))]) + "\n")
            cur = None
        top = [""]
        for ln, line in enumerate(lines, 1):
            s = line.rstrip()
            if not s.strip():
                if cur: cur[6].append(s)
                continue
            if s[0] in " \t" or s.startswith(CONT):
                if cur: cur[6].append(s)
                continue
            # new command at column 0
            m = KW.match(s)
            if m:
                flush(ln - 1)
                kind = m.group(1).split()[0]
                rest = m.group(2)
                nm = re.match(r"(_root_\.)?([^\s:({\[⦃]+)", rest)
                nsp = ns()
                if kind == "instance" and (nm is None or nm.group(2) in ("where", ":=")):
                    full = f"inst@{rel}:{ln}"
                elif kind == "example" or nm is None:
                    full = f"anon@{rel}:{ln}"
                else:
                    if nm.group(1):
                        full = nm.group(2)
                    else:
                        full = ".".join(nsp + [nm.group(2)])
                    if kind == "instance" and nm.group(2).startswith("["):
                        full = f"inst@{rel}:{ln}"
                ops = opens() + pending_open
                extra = attr_insts()
                cur = [full, kind, ln, nsp, ops, extra, [s]]
                pending_open = []
                continue
            if s.startswith("set_option") and s.endswith(" in"):
                flush(ln - 1); continue
            if s.startswith("open "):
                flush(ln - 1)
                if s.endswith(" in"):
                    pending_open += parse_open(s[5:-3])
                else:
                    if stack: stack[-1][2] += parse_open(s[5:])
                    else: top.append(" ".join(parse_open(s[5:])))
                    if not stack: stack.append(["section", [], parse_open(s[5:]), []])
                continue
            if s.startswith("namespace "):
                flush(ln - 1)
                stack.append(["namespace", s.split()[1].split("."), [], []]); continue
            if s.startswith("section") or s.startswith("noncomputable section"):
                flush(ln - 1)
                stack.append(["section", [], [], []]); continue
            if s.startswith("end"):
                flush(ln - 1)
                # Lean requires `end X` to match the innermost open scope
                if stack: stack.pop()
                continue
            if s.startswith("attribute"):
                flush(ln - 1)
                mm = re.match(r"attribute\s*\[([^\]]*)\]\s*(.*)", s)
                if mm and "instance" in mm.group(1) and stack:
                    stack[-1][3] += [t for t in mm.group(2).split() if IDENT.fullmatch(t)]
                continue
            # any other column-0 command ends the current declaration
            flush(ln - 1)
        flush(len(lines))
    out.close()

main()
