#!/usr/bin/env python3
"""Resolve identifier tokens of every declaration to declaration ids.

Resolution of a token t occurring in a declaration with namespace N and
opens O (Lean 4 rules, approximated):
  * `_root_.X` resolves to X only;
  * otherwise try, for every prefix P of N (longest first), of the
    declaration's own dotted name, and of every open (and the open
    taken relative to every prefix of N), the name P.t; then t itself;
  * if t = a.b.c does not resolve, strip trailing components
    (projections, `.mk`, `.eq_1`, dot notation on a constant);
  * if the head component of t is not a constant (a local variable),
    the remaining components are generalized-field-notation names:
    each is matched by last component against all declarations, kept
    when the bucket has at most CAP members (marked 'dot' edges).
Edges are written as two numpy arrays (exact edges, dot edges).
"""
import sys, numpy as np, pickle, re
from collections import defaultdict

FILES = sys.argv[1:-1]
OUT = sys.argv[-1]
CAP = 40

names, kinds, locs, nss, opss = [], [], [], [], []
for fn in FILES:
    with open(fn) as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            names.append(p[0]); kinds.append(p[1]); locs.append((p[2], int(p[3]), int(p[4])))
priv = set(l.strip() for l in open("/home/claude/idx/private.txt"))
is_priv = [("%s:%d" % (locs[i][0], locs[i][1])) in priv for i in range(len(names))]
by_name = defaultdict(list)
for i, n in enumerate(names):
    by_name[n].append(i)
class Lookup:
    """name -> declaration id visible from file `cur` (private ones only in their own file)."""
    cur = None
    def get(self, n):
        ids = by_name.get(n)
        if not ids: return None
        best = None
        for j in ids:
            if is_priv[j]:
                if locs[j][0] == self.cur: return j
            elif best is None:
                best = j
        return best
id_of = Lookup()
last = defaultdict(list)
for i, n in enumerate(names):
    last[n.rsplit(".", 1)[-1]].append(i)

def prefixes(parts):
    return [".".join(parts[:k]) for k in range(len(parts), 0, -1)]

ex_src, ex_dst, dt_src, dt_dst = [], [], [], []
unres = 0
i = -1
for fn in FILES:
    with open(fn) as f:
        for line in f:
            i += 1
            p = line.rstrip("\n").split("\t")
            id_of.cur = p[2]
            nsparts = p[5].split(".") if p[5] else []
            own = p[0].split(".")[:-1]
            opens = p[6].split() if p[6] else []
            scopes = prefixes(nsparts)
            for s in prefixes(own):
                if s not in scopes: scopes.append(s)
            ob = []
            for o in opens:
                ob.append(o)
                for s in prefixes(nsparts):
                    ob.append(s + "." + o)
            scopes_all = scopes + ob
            toks = p[7].split(" ") if len(p) > 7 and p[7] else []
            out = set(); outd = set()
            for t in toks:
                if t.startswith("_root_."):
                    cands = [t[7:]]
                    base = t[7:]
                else:
                    cands = [s + "." + t for s in scopes_all] + [t]
                    base = t
                hit = None
                for c in cands:
                    j = id_of.get(c)
                    if j is not None:
                        hit = j; break
                if hit is None:
                    comps = base.split(".")
                    # strip trailing components
                    for k in range(len(comps) - 1, 0, -1):
                        stem = ".".join(comps[:k])
                        cc = [stem] if t.startswith("_root_.") else [s + "." + stem for s in scopes_all] + [stem]
                        for c in cc:
                            j = id_of.get(c)
                            if j is not None:
                                hit = j; break
                        if hit is not None: break
                    if hit is None and len(comps) > 1:
                        # local head: generalized field notation
                        for comp in comps[1:]:
                            b = last.get(comp)
                            if b and len(b) <= CAP:
                                outd.update(b)
                    if hit is None:
                        unres += 1
                if hit is not None and hit != i:
                    out.add(hit)
            for j in out:
                ex_src.append(i); ex_dst.append(j)
            for j in outd - out:
                dt_src.append(i); dt_dst.append(j)

np.save(OUT + "_ex_src.npy", np.array(ex_src, dtype=np.int32))
np.save(OUT + "_ex_dst.npy", np.array(ex_dst, dtype=np.int32))
np.save(OUT + "_dt_src.npy", np.array(dt_src, dtype=np.int32))
np.save(OUT + "_dt_dst.npy", np.array(dt_dst, dtype=np.int32))
with open(OUT + "_meta.pkl", "wb") as f:
    pickle.dump({"names": names, "kinds": kinds, "locs": locs, "priv": is_priv}, f)
print("decls", len(names), "exact", len(ex_src), "dot", len(dt_src), "unresolved tokens", unres)
