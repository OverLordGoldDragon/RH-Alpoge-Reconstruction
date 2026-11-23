"""why.py A B : which tokens of declaration A resolve to declaration B, and whether
the token is bound locally in A (a binder or `have`/`obtain`/`fun` name), which
would make the edge false."""
import sys, subprocess, re
sys.argv_save = sys.argv[:]; A, B = sys.argv[1], sys.argv[2]
sys.argv = ['q', 'x', 'x']
import q
def tsv_line(name):
    for fn in ["/home/claude/idx/decls.0.tsv", "/home/claude/idx/decls.1.tsv"]:
        out = subprocess.run(["rg", "-m", "1", "^" + re.escape(name) + "\t", fn], capture_output=True, text=True).stdout
        if out: return out.rstrip("\n").split("\t")
def prefixes(parts): return [".".join(parts[:k]) for k in range(len(parts), 0, -1)]
def resolve_tok(p, t):
    nsparts = p[5].split(".") if p[5] else []
    own = p[0].split(".")[:-1]; opens = p[6].split() if p[6] else []
    scopes = prefixes(nsparts) + [s for s in prefixes(own) if s not in prefixes(nsparts)]
    ob = []
    for o in opens:
        ob.append(o); ob += [s + "." + o for s in prefixes(nsparts)]
    sc = scopes + ob
    if t.startswith("_root_."): cands = [t[7:]]
    else: cands = [s + "." + t for s in sc] + [t]
    for c in cands:
        if c in idset: return c, "exact"
    base = t[7:] if t.startswith("_root_.") else t
    comps = base.split(".")
    for k in range(len(comps) - 1, 0, -1):
        stem = ".".join(comps[:k])
        cc = [stem] if t.startswith("_root_.") else [s + "." + stem for s in sc] + [stem]
        for c in cc:
            if c in idset: return c, "stripped"
    return None, None
from collections import defaultdict
_priv = q.meta.get("priv")
_by = defaultdict(list)
for _i, _n in enumerate(q.names): _by[_n].append(_i)
class _V:
    def __contains__(self, c):
        for j in _by.get(c, []):
            if not _priv[j] or q.locs[j][0] == pa[2]: return True
        return False
idset = None
pa = tsv_line(A)
idset = _V()
toks = pa[7].split(" ")
txt = q.text(q.resolve(A)[0])
for t in toks:
    r, how = resolve_tok(pa, t)
    if r == B:
        head = t.split(".")[0]
        if t.startswith("_root_.") or (how == "exact" and "." in t and head[0].isupper()):
            cls = "QUALIFIED"
        else:
            bound = re.search(r"(\(|\{|⦃|\[|fun |have |obtain ⟨[^⟩]*|intro [^\n]*|rintro [^\n]*|⟨[^⟩]*|∀ |∃ |let )\s*[^\n]*?\b" + re.escape(head) + r"\b\s*[:,⟩)}\]=]", txt) is not None
            cls = "SHORT, head possibly a local binder" if bound else "SHORT, not locally bound"
        print(f"  token {t!r} -> {B} ({how}; {cls})")
