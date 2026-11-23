"""d123_T.py: breakdown of the twist-dictionary layer by its top declarations."""
import sys, pickle; sys.argv=['q','x','x']
sys.path.insert(0,'/home/claude/scripts')
import q
from collections import deque
g=q.graph("fwd")
T=set(pickle.load(open('/home/claude/kl/layerT.pkl','rb')))
D={k:set(v) for k,v in pickle.load(open('/home/claude/kl/d123.pkl','rb')).items()}
th=lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
def clos(i):
    seen={i}; dq=deque([i])
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in T and y not in seen: seen.add(y); dq.append(y)
    return seen
called=set()
for j in T:
    for y in q.nbrs(g,j):
        y=int(y)
        if y in T and y!=j: called.add(y)
top=[j for j in T if j not in called]
own=set()
for j in sorted(top,key=lambda j:-th(clos(j))):
    C=clos(j); new=C-own; own|=C
    print(f"{th(C):4d} ({th(new):4d} new) {q.names[j]} [{q.locs[j][0].rsplit('/',1)[-1]}:{q.locs[j][1]}] {[k for k in D if j in D[k]]}")
