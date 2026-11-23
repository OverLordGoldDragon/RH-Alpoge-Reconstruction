"""gc_tree.py PKL KEY ROOT DEPTH MIN: tree of ROOT's sub-closure inside the set stored under KEY in PKL (gc_excl output)."""
import sys; P,K,R,DEP,MIN=sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5])
sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, pickle
from collections import deque
g=q.graph("fwd"); DOM=set(int(i) for i in pickle.load(open(P,'rb'))[K])
memo={}
def sub(i):
    if i in memo: return memo[i]
    seen={i}; dq=deque([i])
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in DOM and y not in seen: seen.add(y); dq.append(y)
    memo[i]=sum(1 for j in seen if q.kinds[j] in('theorem','lemma')); return memo[i]
pr=set()
def rec(i,d):
    for j in sorted({int(y) for y in q.nbrs(g,i) if int(y) in DOM},key=lambda j:-sub(j)):
        if sub(j)<MIN: continue
        print("  "*d+f"{sub(j):4d} {q.names[j]}  ({q.locs[j][0].rsplit('/',1)[-1]}:{q.locs[j][1]}-{q.locs[j][2]})"+(" (seen)" if j in pr else ""))
        if j in pr or d+1>=DEP: continue
        pr.add(j); rec(j,d+1)
r=[i for i,n in enumerate(q.names) if n==R] or q.resolve(R); print(q.names[r[0]],sub(r[0])); rec(r[0],0)
