"""gc_cut2.py: cut test with the Row0b supplier treated as an external stop (human route cites the published theorem)."""
import sys, pickle; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
from collections import Counter, deque
N={n:i for i,n in enumerate(q.names)}
C=pickle.load(open('/home/claude/idx/gc_cut.pkl','rb')); H=np.zeros(len(q.names),bool); H[C['H']]=True
H[N['UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter']]=True
ptr,d=q.graph("fwd"); par={q.ROOT:-1}; dq=deque([q.ROOT])
while dq:
    x=dq.popleft()
    for y in d[ptr[x]:ptr[x+1]]:
        y=int(y)
        if y not in par:
            par[y]=x
            if not H[y]: dq.append(y)
above=[i for i in par if not H[i] and q.kinds[i] in('theorem','lemma')]
print("above-cut theorems:",len(above))
for i in above:
    p=[];j=i
    while j!=-1: p.append(q.names[j].rsplit('.',1)[-1]); j=par[j]
    print("  ",q.names[i],"|",' > '.join(p[::-1]))
heads=sorted(set(i for i in par if H[i]))
print("heads hit directly from the assembly layer:",len(heads))
for i in heads: print("   H",q.names[i])
pickle.dump({'H2':np.nonzero(H)[0],'above2':above,'heads2':heads},open('/home/claude/idx/gc_cut2.pkl','wb'))
