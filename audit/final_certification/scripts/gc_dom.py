"""gc_dom.py: immediate dominators of the live exact-edge graph rooted at riemannHypothesis.
If the live graph is a DAG, idom(v) = LCA in the dominator tree of all live predecessors of v, taken in
topological order (exact for DAGs). Cycles, if any, are reported and their nodes handled by iterating.
Writes /home/claude/idx/gc_idom.npy (idom index, -1 for root/dead) and gc_depth.npy."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
L=np.load('/home/claude/idx/gc_live.npy'); n=len(q.names)
ptr,d=q.graph("fwd"); rptr,rd=q.graph("rev")
# Kahn topological order on the live subgraph
indeg=np.zeros(n,np.int64)
live=np.nonzero(L)[0]
for x in live:
    for y in d[ptr[x]:ptr[x+1]]:
        if L[y]: indeg[y]+=1
order=[]; st=[q.ROOT] if indeg[q.ROOT]==0 else []
print("root indegree", indeg[q.ROOT])
st=[int(x) for x in live if indeg[x]==0]
print("live sources:", len(st), [q.names[i] for i in st[:5]])
while st:
    x=st.pop(); order.append(x)
    for y in d[ptr[x]:ptr[x+1]]:
        if L[y]:
            indeg[y]-=1
            if indeg[y]==0: st.append(int(y))
print("topologically ordered", len(order), "of", len(live), "-> cyclic nodes", len(live)-len(order))
idom=np.full(n,-1,np.int64); depth=np.full(n,-1,np.int64)
depth[q.ROOT]=0
def lca(a,b):
    while a!=b:
        while depth[a]>depth[b]: a=idom[a]
        while depth[b]>depth[a]: b=idom[b]
        if a!=b: a=idom[a]; b=idom[b]
    return a
for v in order:
    if v==q.ROOT: continue
    cur=-1
    for u in rd[rptr[v]:rptr[v+1]]:
        u=int(u)
        if not L[u] or depth[u]<0: continue
        cur=u if cur<0 else lca(cur,u)
    if cur>=0: idom[v]=cur; depth[v]=depth[cur]+1
print("dominated nodes", (depth>=0).sum(), "max depth", depth.max())
np.save('/home/claude/idx/gc_idom.npy',idom); np.save('/home/claude/idx/gc_depth.npy',depth)
