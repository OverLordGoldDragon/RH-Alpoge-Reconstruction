import sys; F, R, D, MIN = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
sys.argv = ['q','x','x']
import q
from collections import deque
ex = set(l.split('\t')[0] for l in open('/home/claude/idx/excl_%s.txt' % F))
fid = set(i for i, n in enumerate(q.names) if n in ex)
g = q.graph("fwd")
memo = {}
def sub(i):
    if i in memo: return memo[i]
    seen = {i}; dq = deque([i])
    while dq:
        x = dq.popleft()
        for y in q.nbrs(g, x):
            y = int(y)
            if y in fid and y not in seen: seen.add(y); dq.append(y)
    memo[i] = (sum(1 for j in seen if q.kinds[j] in ('theorem','lemma')), sum(q.locs[j][2]-q.locs[j][1]+1 for j in seen)); return memo[i]
printed = set()
def rec(i, d):
    kids = sorted({int(y) for y in q.nbrs(g, i) if int(y) in fid}, key=lambda j: -sub(j)[0])
    for j in kids:
        s, L = sub(j)
        if s < MIN: continue
        print("  " * d + f"{s:5d} thm {L:6d} ln  {q.names[j]}  [{q.locs[j][0].rsplit('/',1)[-1]}:{q.locs[j][1]}-{q.locs[j][2]}]" + (" (seen)" if j in printed else ""))
        if j in printed or d + 1 >= D: continue
        printed.add(j); rec(j, d + 1)
rec(q.resolve(R)[0], 0)
