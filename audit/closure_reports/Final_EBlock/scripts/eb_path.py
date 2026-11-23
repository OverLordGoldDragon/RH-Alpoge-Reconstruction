"""eb_path.py A B [avoid...]: shortest exact-edge path A -> B, optionally avoiding listed declarations; A may be 'ROOT'."""
import sys; A,B=sys.argv[1],sys.argv[2]; AV=sys.argv[3:]; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q
from collections import deque
g=q.graph("fwd")
a=q.ROOT if A=='ROOT' else q.resolve(A)[0]; b=q.names.index(B) if B in q.names else q.resolve(B)[0]
ban=set(q.resolve(n)[0] for n in AV)
prev={a:-1}; dq=deque([a])
while dq:
    x=dq.popleft()
    if x==b: break
    for y in q.nbrs(g,x):
        y=int(y)
        if y not in prev and y not in ban: prev[y]=x; dq.append(y)
if b not in prev: print("NO PATH"); sys.exit()
for j in q.path(prev,b): print(q.names[j], "%s:%d"%q.locs[j][:2])
