import sys, pickle; cls=sys.argv[1]; mn=int(sys.argv[2]); sys.argv=['q','x','x']
sys.path.insert(0,'/home/claude/scripts')
import q
from collections import deque
g=q.graph("fwd")
F=pickle.load(open('/home/claude/kl/d123_final.pkl','rb'))
A=set(F['mech'][cls])
th=lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
def clos(i):
    seen={i}; dq=deque([i])
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in A and y not in seen: seen.add(y); dq.append(y)
    return seen
# blocks: walk from top; print nodes whose closure >= mn and whose parent chain is a wrapper; depth-first with dedupe
called=set()
for j in A:
    for y in q.nbrs(g,j):
        y=int(y)
        if y in A and y!=j: called.add(y)
top=sorted([j for j in A if j not in called],key=lambda j:-th(clos(j)))
seen=set()
def show(i,d):
    s=th(clos(i))
    if s<mn or i in seen: return
    seen.add(i)
    n=q.names[i]
    print("  "*d+f"{s:4d} {n}")
    for y in sorted({int(y) for y in q.nbrs(g,i) if int(y) in A and int(y)!=i},key=lambda j:-th(clos(j))): show(y,d+1)
for t in top: show(t,0)
