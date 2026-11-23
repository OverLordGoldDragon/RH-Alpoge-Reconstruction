"""gc_dom2.py: dominators of the live graph via SCC condensation (scipy strong components), then the DAG
LCA method on the condensed graph. Every declaration gets the idom of its component; members of a nontrivial
component are recorded with the component id. Writes gc_comp.npy, gc_cidom.npy (component idom), gc_cdepth.npy."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
L=np.load('/home/claude/idx/gc_live.npy'); n=len(q.names)
es=np.load('/home/claude/idx/g2_ex_src.npy'); ed=np.load('/home/claude/idx/g2_ex_dst.npy')
m=L[es]&L[ed]; es,ed=es[m],ed[m]
A=csr_matrix((np.ones(len(es),np.int8),(es,ed)),shape=(n,n))
nc,lab=connected_components(A,directed=True,connection='strong')
lab=np.where(L,lab,-1)
sizes=np.bincount(lab[L]); big=np.sort(sizes)[::-1][:10]
print("components",len(np.unique(lab[L])),"largest",big.tolist(),"nodes in nontrivial comps",int(sizes[sizes>1].sum()))
cs,cd=lab[es],lab[ed]; k=cs!=cd; cs,cd=cs[k],cd[k]
pairs=np.unique(np.stack([cs,cd],1),axis=0); cs,cd=pairs[:,0],pairs[:,1]
C=lab.max()+1
order_idx=np.argsort(cs); fptr=np.zeros(C+1,np.int64); np.add.at(fptr,cs+1,1); fptr=np.cumsum(fptr); fd=cd[order_idx]
order_idx=np.argsort(cd); rptr=np.zeros(C+1,np.int64); np.add.at(rptr,cd+1,1); rptr=np.cumsum(rptr); rs=cs[order_idx]
indeg=np.diff(rptr).copy(); root=lab[q.ROOT]
st=[root] ; order=[]
while st:
    x=st.pop(); order.append(x)
    for y in fd[fptr[x]:fptr[x+1]]:
        indeg[y]-=1
        if indeg[y]==0: st.append(int(y))
print("condensed nodes ordered",len(order))
idom=np.full(C,-1,np.int64); depth=np.full(C,-1,np.int64); depth[root]=0
def lca(a,b):
    while a!=b:
        while depth[a]>depth[b]: a=idom[a]
        while depth[b]>depth[a]: b=idom[b]
        if a!=b: a=idom[a]; b=idom[b]
    return a
for v in order:
    if v==root: continue
    cur=-1
    for u in rs[rptr[v]:rptr[v+1]]:
        u=int(u)
        if depth[u]<0: continue
        cur=u if cur<0 else lca(cur,u)
    idom[v]=cur; depth[v]=depth[cur]+1
print("max depth",depth.max())
np.save('/home/claude/idx/gc_comp.npy',lab); np.save('/home/claude/idx/gc_cidom.npy',idom); np.save('/home/claude/idx/gc_cdepth.npy',depth)
big_comp=np.argsort(sizes)[::-1][:5]
for c in big_comp:
    mem=np.nonzero(lab==c)[0][:6]; print("comp",c,"size",sizes[c],[q.names[i] for i in mem])
