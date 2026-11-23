"""liveavoid.py TARGET BANNED...: shortest exact path from riemannHypothesis to TARGET avoiding BANNED nodes."""
import sys; T = sys.argv[1]; B = sys.argv[2:]; sys.argv = ['q','x','x']
import q
from collections import deque
g = q.graph("fwd")
ban = set()
for b in B: ban |= set(q.resolve(b))
tid = set(q.resolve(T))
prev = {q.ROOT: -1}; dq = deque([q.ROOT]); hit = None
while dq:
    x = dq.popleft()
    if x in tid: hit = x; break
    for y in q.nbrs(g, x):
        y = int(y)
        if y not in prev and y not in ban: prev[y] = x; dq.append(y)
if hit is None: print("NOT REACHED avoiding", B)
else:
    for j in q.path(prev, hit): print(q.names[j], "%s:%d" % q.locs[j][:2])
