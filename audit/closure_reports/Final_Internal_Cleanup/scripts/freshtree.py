"""freshtree.py TARGET DEPTH: tree of fresh declarations (see fresh.py) below TARGET,
each with the size of its fresh sub-closure (theorems), to the given depth; nodes
already printed are not expanded again."""
import sys; T, D = sys.argv[1], int(sys.argv[2]); MIN = int(sys.argv[3]) if len(sys.argv) > 3 else 20
sys.argv = ['q','x','x']
import q
from collections import deque
fresh = {}
for l in open('/home/claude/idx/fresh_%s.txt' % T.rsplit('.',1)[-1]):
    n = l.split('\t')[0]
    fresh[n] = 1
fid = set(i for i, n in enumerate(q.names) if n in fresh)
g = q.graph("fwd")
def sub(i):
    seen = {i}; dq = deque([i])
    while dq:
        x = dq.popleft()
        for y in q.nbrs(g, x):
            y = int(y)
            if y in fid and y not in seen: seen.add(y); dq.append(y)
    return sum(1 for j in seen if q.kinds[j] in ('theorem','lemma'))
printed = set()
def rec(i, d):
    kids = sorted({int(y) for y in q.nbrs(g, i) if int(y) in fid}, key=lambda j: -sub(j))
    for j in kids:
        s = sub(j)
        if s < MIN: continue
        mark = " (seen)" if j in printed else ""
        print("  " * d + f"{s:5d}  {q.names[j]}  [{q.locs[j][0].rsplit('/',1)[-1]}:{q.locs[j][1]}]{mark}")
        if j in printed or d + 1 >= D: continue
        printed.add(j); rec(j, d + 1)
rec(q.resolve(T)[0], 0)
