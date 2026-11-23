"""d5_final.py: closes the remainder of D5 (AdForm.twS_ramL) and recomputes the colSide heads."""
import sys, pickle; sys.argv=['q','x','x']
sys.path.insert(0,'/home/claude/scripts')
import q
from collections import deque
g=q.graph("fwd")
th=lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
R=lambda n: q.resolve(n)[0]
ex=set(l.split('\t')[0] for l in open('/home/claude/idx/excl_colSide_alt.txt'))
E=set(i for i,n in enumerate(q.names) if n in ex)
def clos(roots,A):
    seen=set(r for r in roots if r in A); dq=deque(seen)
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in A and y not in seen: seen.add(y); dq.append(y)
    return seen
C3=set(pickle.load(open('/home/claude/kl/d2r_final.pkl','rb'))['C3'])
D5=clos([R('GlobalTheory.AdForm.twS_ramL')],E)
C4=C3|D5
print("D5 new", th(D5-C3))
H={'D7':clos([R('GlobalTheory.QVecJoin.step_mid'),R('GlobalTheory.QVecJoin.step_top')],E),
 'D8':clos([R('GlobalTheory.T.true_geometry_row_column_entry_alt')],E),
 'D9':clos([R('GlobalTheory.T.true_geometry_twist_value_alt')],E)}
for h,S in H.items(): print(h, th(S-C3), "->", th(S-C4))
U=set().union(*H.values()); print("R4-D distinct remaining", th(U-C4))
pickle.dump({'C4':sorted(C4)},open('/home/claude/kl/d5_final.pkl','wb'))
