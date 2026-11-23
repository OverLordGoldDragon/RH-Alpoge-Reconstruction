#!/usr/bin/env python3
"""Query tool over the declaration graph.

  q.py show NAME            text of a declaration (exact name or unique suffix)
  q.py find SUFFIX          all declarations whose name ends with SUFFIX
  q.py deps NAME            exact out-edges
  q.py rdeps NAME [dot]     in-edges (exact; with 'dot' also dot-notation edges)
  q.py live NAME [dot]      shortest forward path from riemannHypothesis
  q.py closure NAME         forward closure size (exact edges)
  q.py rclosure NAME CAP    reverse closure (exact+dot) up to CAP nodes; reports if root reached
"""
import sys, pickle, numpy as np
from collections import deque
G = "/home/claude/idx/g2"  # graph prefix written by build_graph.py
SRC = "/home/claude/lean_src/lean/src/"
meta = pickle.load(open(G + "_meta.pkl", "rb"))
names, kinds, locs = meta["names"], meta["kinds"], meta["locs"]
N = len(names)

def csr(src, dst):
    order = np.argsort(src, kind="stable")
    s, d = src[order], dst[order]
    ptr = np.zeros(N + 1, dtype=np.int64)
    np.add.at(ptr, s + 1, 1)
    return np.cumsum(ptr), d

_cache = {}
def graph(which):
    if which not in _cache:
        es = np.load(G + "_ex_src.npy"); ed = np.load(G + "_ex_dst.npy")
        if which == "fwd": _cache[which] = csr(es, ed)
        elif which == "rev": _cache[which] = csr(ed, es)
        else:
            ds = np.load(G + "_dt_src.npy"); dd = np.load(G + "_dt_dst.npy")
            if which == "fwdd": _cache[which] = csr(np.concatenate([es, ds]), np.concatenate([ed, dd]))
            if which == "revd": _cache[which] = csr(np.concatenate([ed, dd]), np.concatenate([es, ds]))
    return _cache[which]

def nbrs(g, i):
    ptr, d = g
    return d[ptr[i]:ptr[i + 1]]

def resolve(name):
    ids = [i for i, n in enumerate(names) if n == name]
    if ids: return ids
    return [i for i, n in enumerate(names) if n.endswith("." + name)]

def text(i):
    f, a, b = locs[i]
    L = open(SRC + f, encoding="utf-8", errors="replace").read().split("\n")
    return f"-- {names[i]}  [{kinds[i]}]  {f}:{a}-{b}\n" + "\n".join(L[a - 1:b])

ROOT = resolve("riemannHypothesis")[0]

def bfs(g, start, targets=None, cap=None):
    prev = {start: -1}; dq = deque([start])
    while dq:
        x = dq.popleft()
        if targets is not None and x in targets: return prev, x
        for y in nbrs(g, x):
            y = int(y)
            if y not in prev:
                prev[y] = x; dq.append(y)
                if cap and len(prev) > cap: return prev, None
    return prev, None

def path(prev, x):
    p = []
    while x != -1:
        p.append(x); x = prev[x]
    return p[::-1]

if __name__ == "__main__":
    cmd, arg = sys.argv[1], sys.argv[2]
    ids = resolve(arg) if cmd != "find" else None
    if cmd == "find":
        for i, n in enumerate(names):
            if n == arg or n.endswith("." + arg): print(n, kinds[i], "%s:%d" % locs[i][:2])
    elif cmd == "show":
        for i in ids: print(text(i)); print()
    elif cmd == "deps":
        for i in ids:
            for j in sorted(set(int(x) for x in nbrs(graph("fwd"), i)), key=lambda j: names[j]): print(names[j], kinds[j], "%s:%d" % locs[j][:2])
    elif cmd == "rdeps":
        g = graph("revd" if len(sys.argv) > 3 else "rev")
        for i in ids:
            for j in sorted(set(int(x) for x in nbrs(g, i)), key=lambda j: names[j]): print(names[j], "%s:%d" % locs[j][:2])
    elif cmd == "live":
        g = graph("fwdd" if len(sys.argv) > 3 else "fwd")
        prev, hit = bfs(g, ROOT, set(ids))
        if hit is None: print("NOT REACHED; forward closure size", len(prev))
        else:
            for j in path(prev, hit): print(names[j], "%s:%d" % locs[j][:2])
    elif cmd == "closure":
        prev, _ = bfs(graph("fwd"), ids[0]); print(len(prev))
    elif cmd == "rclosure":
        cap = int(sys.argv[3])
        prev, hit = bfs(graph("revd"), ids[0], {ROOT}, cap)
        if hit is not None:
            for j in path(prev, hit)[::-1]: print(names[j], "%s:%d" % locs[j][:2])
            print("ROOT REACHED")
        else:
            print("closure", len(prev), "CAPPED" if len(prev) > cap else "EXHAUSTED")
            if len(prev) <= 200:
                for j in prev: print("  ", names[j], "%s:%d" % locs[j][:2])
