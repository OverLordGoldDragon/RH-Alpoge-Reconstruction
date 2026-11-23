"""gc_cut.py: the cut test.  H = live theorems that a report cites (depth >= 4 in the dominator tree) or that this
certification owns (E/W/D-agent/upstream).  ABOVE = theorems reachable from riemannHypothesis without entering H
(the assembly layer, which the human route must reconstruct directly).  BELOW = everything else: every route from
the root to it passes through a cited head.  For each RESIDUAL of gc_classify, report whether it is above the cut."""
import sys, pickle; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
from collections import Counter
L=np.load('/home/claude/idx/gc_live.npy'); lab=np.load('/home/claude/idx/gc_comp.npy'); dep=np.load('/home/claude/idx/gc_cdepth.npy')
named=pickle.load(open('/home/claude/idx/gc_named.pkl','rb')); S=pickle.load(open('/home/claude/idx/gc_status.pkl','rb'))
istheo=lambda i: q.kinds[i] in('theorem','lemma')
H=np.zeros(len(q.names),bool)
for i in named:
    if istheo(i) and L[i] and dep[lab[i]]>=4: H[i]=True
for i in np.nonzero(L)[0]:
    if S['status'][i]=='CLOSED' or S['status'][i]=='EXTERNAL' and istheo(i): H[i]=True
ptr,d=q.graph("fwd"); seen=np.zeros(len(q.names),bool); seen[q.ROOT]=True; st=[q.ROOT]
while st:
    x=st.pop()
    for y in d[ptr[x]:ptr[x+1]]:
        if not seen[y]:
            seen[y]=True
            if not H[y]: st.append(int(y))
above=[i for i in np.nonzero(seen&~H)[0] if istheo(i)]
print("cited/owned heads:",int(H.sum())," above-cut theorems:",len(above))
print("above-cut by status:",Counter(S['status'][i] for i in above))
print("above-cut namespaces:",Counter('.'.join(q.names[i].split('.')[:3]) for i in above).most_common(30))
res=[i for i in np.nonzero(L)[0] if S['status'][i]=='RESIDUAL']
ab=set(above); print("RESIDUAL total",len(res),"of which above cut",sum(1 for i in res if i in ab))
pickle.dump({'H':np.nonzero(H)[0],'above':above},open('/home/claude/idx/gc_cut.pkl','wb'))
