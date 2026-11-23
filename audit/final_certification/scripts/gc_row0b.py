"""gc_row0b.py: region of the Row0b supplier.  X = live declarations reachable from riemannHypothesis only through
UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter (proof of Row0b: Galois representations of regular algebraic
polarized cuspidal representations of GL_a over CM fields, with local-global compatibility).  Then the above-cut set
minus X, i.e. what remains of the assembly layer."""
import sys, pickle; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
from collections import Counter
L=np.load('/home/claude/idx/gc_live.npy'); N={n:i for i,n in enumerate(q.names)}
C=pickle.load(open('/home/claude/idx/gc_cut.pkl','rb')); H=np.zeros(len(q.names),bool); H[C['H']]=True
S=pickle.load(open('/home/claude/idx/gc_status.pkl','rb'))
ptr,d=q.graph("fwd")
def reach(starts,ban=None,stop=None):
    seen=np.zeros(len(q.names),bool); st=[]
    for s in starts:
        if ban is None or not ban[s]: seen[s]=True; st.append(s)
    while st:
        x=st.pop()
        if stop is not None and stop[x] and x not in starts: continue
        for y in d[ptr[x]:ptr[x+1]]:
            if not seen[y] and (ban is None or not ban[y]): seen[y]=True; st.append(int(y))
    return seen
g=N['UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter']
ban=np.zeros(len(q.names),bool); ban[g]=True
U=reach([g]); X=U & ~reach([q.ROOT],ban)
th=lambda m:[i for i in np.nonzero(m)[0] if q.kinds[i] in('theorem','lemma')]
print("Row0b supplier closure:",len(th(U)),"theorems; exclusive:",len(th(X)),"theorems,",int(X.sum()),"decls")
print("status of exclusive part:",Counter(S['status'][i] for i in np.nonzero(X)[0]))
A=np.zeros(len(q.names),bool); A[C['above']]=True
rest=[i for i in np.nonzero(A&~X)[0]]
print("above-cut theorems outside Row0b-exclusive:",len(rest))
print(Counter('.'.join(q.names[i].split('.')[:3]) for i in rest).most_common(25))
# what heads in H does the Row0b supplier closure hit (shared with packages)?
hit=[i for i in np.nonzero(U&H)[0]]
print("cited heads inside the Row0b supplier closure:",len(hit))
pickle.dump({'X':np.nonzero(X)[0],'U':np.nonzero(U)[0],'rest':rest},open('/home/claude/idx/gc_row0b.pkl','wb'))
