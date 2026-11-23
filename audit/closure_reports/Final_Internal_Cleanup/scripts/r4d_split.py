import sys; sys.argv = ['q','x','x']
import q
from collections import deque
g = q.graph("fwd")
names = set(l.split('\t')[0] for l in open('/home/claude/idx/excl_colSide_alt.txt'))
S = set(i for i, n in enumerate(q.names) if n in names)
def sub(i):
    seen = {i}; dq = deque([i])
    while dq:
        x = dq.popleft()
        for y in q.nbrs(g, x):
            y = int(y)
            if y in S and y not in seen: seen.add(y); dq.append(y)
    return seen
th = lambda X: sum(1 for j in X if q.kinds[j] in ('theorem','lemma'))
tr = sub(q.resolve('GlobalTheory.T.seeSawTwistPlaceLaws_of_rootOfUnityRescaling')[0])
rest = S - tr
print("R4-D exclusive", th(S), "transferred (seesaw laws)", th(tr), "remaining", th(rest), "lines", sum(q.locs[j][2]-q.locs[j][1]+1 for j in rest))
