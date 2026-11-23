"""gc_live.py: live closure of riemannHypothesis on the rebuilt graph.
Exact edges (the certification graph) and exact+dot edges (upper bound for generalized field notation).
Writes /home/claude/idx/gc_live.npy (exact) and gc_live_dot.npy, and prints kind / top-directory counts."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
from collections import Counter
def closure(gr):
    ptr,d=gr; seen=np.zeros(len(q.names),bool); seen[q.ROOT]=True; stack=[q.ROOT]
    while stack:
        x=stack.pop()
        for y in d[ptr[x]:ptr[x+1]]:
            if not seen[y]: seen[y]=True; stack.append(int(y))
    return seen
L=closure(q.graph("fwd")); np.save('/home/claude/idx/gc_live.npy',L)
LD=closure(q.graph("fwdd")); np.save('/home/claude/idx/gc_live_dot.npy',LD)
print("total decls",len(q.names),"live exact",L.sum(),"live exact+dot",LD.sum())
k=Counter(q.kinds[i] for i in np.nonzero(L)[0]); print("kinds (exact):",dict(k))
top=Counter(q.locs[i][0].split('/')[0] for i in np.nonzero(L)[0]); print("top dirs:",dict(top))
print("theorem/lemma live:", sum(v for kk,v in k.items() if kk in('theorem','lemma')))
