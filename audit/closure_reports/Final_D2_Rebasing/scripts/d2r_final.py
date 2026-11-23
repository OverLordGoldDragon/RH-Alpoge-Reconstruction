"""d2r_final.py: closes D2's two rebasing steps (commutation identity/property) and recomputes heads."""
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
C2=set(pickle.load(open('/home/claude/kl/lvl_final.pkl','rb'))['C2'])
R1=clos([R('GlobalTheory.T.true_geometry_commutation_identity_alt')],E)
R2=clos([R('GlobalTheory.T.true_geometry_commutation_property_alt')],E)
print("commutation_identity", th(R1), "new", th(R1-C2), " commutation_property", th(R2), "new", th(R2-C2), " union new", th((R1|R2)-C2))
C3=C2|R1|R2
nm={n:i for i,n in enumerate(q.names)}
def load(f): return set(nm[l.split('\t')[0].strip()] for l in open('/home/claude/kl/sub_'+f+'.txt') if l.split('\t')[0].strip() in nm)
H={'D1':set().union(*[load(p) for p in ['true_geometry_row_pair_property_alt','true_geometry_row_pair_relation_alt_alt','true_geometry_twist_quadratic_value_alt']]),
 'D2':set().union(*[load(p) for p in ['exists_good','true_geometry_commutation_identity_alt','true_geometry_commutation_property_alt']]),
 'D3':set().union(*[load(p) for p in ['true_geometry_chain_step_value_alt','true_geometry_chain_step_identity_alt','exists_volume_constant_of_true_geometry']]),
 'D5':clos([R('GlobalTheory.AdForm.twS_ramL')],E),
 'D7':clos([R('GlobalTheory.QVecJoin.step_mid'),R('GlobalTheory.QVecJoin.step_top')],E),
 'D8':clos([R('GlobalTheory.T.true_geometry_row_column_entry_alt')],E),
 'D9':clos([R('GlobalTheory.T.true_geometry_twist_value_alt')],E)}
for h,S in H.items(): print(h, th(S-C2), "->", th(S-C3))
U=set().union(*H.values()); print("R4-D distinct", th(U-C2), "->", th(U-C3))
pickle.dump({'C3':sorted(C3)},open('/home/claude/kl/d2r_final.pkl','wb'))
