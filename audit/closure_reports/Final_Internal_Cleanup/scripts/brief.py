"""brief.py NAME...: statement head (to ':= by', cut) and the theorem-valued callees of each declaration,
with their closure sizes in theorems (exact graph)."""
import sys; args = sys.argv[1:]; sys.argv = ['q','x','x']
import q, re
from collections import deque
g = q.graph("fwd")
memo = {}
def csize(i):
    if i in memo: return memo[i]
    prev, _ = q.bfs(g, i); memo[i] = sum(1 for j in prev if q.kinds[j] in ('theorem','lemma')); return memo[i]
for a in args:
    for i in q.resolve(a)[:1]:
        t = q.text(i)
        body = t.split("\n", 1)[1]
        head = body.split(":= by")[0] if ":= by" in body else body.split(":=")[0]
        head = re.sub(r"\s+", " ", head)
        print("=" * 100); print(q.names[i], f"[{q.locs[i][0]}:{q.locs[i][1]}-{q.locs[i][2]}]", "closure", csize(i))
        print("STATEMENT:", head[:1800])
        kids = sorted({int(y) for y in q.nbrs(g, i) if q.kinds[int(y)] in ('theorem','lemma')}, key=lambda j: -csize(j))
        print("CALLS:", "; ".join(f"{q.names[j]}({csize(j)})" for j in kids[:25]))
