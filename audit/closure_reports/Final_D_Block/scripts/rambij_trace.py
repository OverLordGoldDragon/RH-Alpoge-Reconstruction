"""rambij_trace.py: forward closure of ramBijective_holds and a live path from riemannHypothesis
that avoids the three residual block roots."""
import sys,pickle; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/scripts')
import q
from collections import deque
gf=q.graph("fwd")
th=lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
R=lambda n: q.resolve(n)[0]
t=R('GlobalTheory.FinPl.ramBijective_holds')
def clos(i):
    seen={i}; dq=deque([i])
    while dq:
        x=dq.popleft()
        for y in q.nbrs(gf,x):
            y=int(y)
            if y not in seen: seen.add(y); dq.append(y)
    return seen
F=clos(t); print("forward closure of ramBijective_holds:", len(F), "decls,", th(F), "theorems")
po=q.resolve('GlobalTheory.PairOp.pairOperatorStatement'); print("pairOperatorStatement", [q.locs[i] for i in po])
# BFS from RH avoiding block roots
blocks=[R(n) for n in ['GlobalTheory.AdForm.bwit_exists_alt','GlobalTheory.AdForm.colSide_alt','GlobalTheory.AdForm.clsPinD_of_famCol_of_trueW']] if False else []
names=['bwit_exists_alt','colSide_alt','clsPinD_of_famCol_of_trueW']
blk=set(i for i,n in enumerate(q.names) if n.rsplit('.',1)[-1] in names)
print("block roots:", [q.names[i] for i in blk])
def path(avoid):
    prev={q.ROOT:-1}; dq=deque([q.ROOT])
    while dq:
        x=dq.popleft()
        if x==t: break
        for y in q.nbrs(gf,x):
            y=int(y)
            if y in avoid or y in prev: continue
            prev[y]=x; dq.append(y)
    if t not in prev: return None
    p=[t]
    while prev[p[-1]]!=-1: p.append(prev[p[-1]])
    return [q.names[i] for i in reversed(p)]
p1=path(set()); print("path from RH:", len(p1) if p1 else None); 
for n in (p1 or []): print("   ",n)
p2=path(blk); print("path avoiding blocks:", len(p2) if p2 else None)
for n in (p2 or []): print("   ",n)
# direct users
gr=q.graph("rev")
print("direct users:", [q.names[int(y)] for y in q.nbrs(gr,t)])
