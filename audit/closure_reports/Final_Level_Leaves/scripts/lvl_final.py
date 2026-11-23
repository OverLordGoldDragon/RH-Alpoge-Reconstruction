"""lvl_final.py: closes the four D123 leaves (L1-L4) and recomputes the colSide heads."""
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
F=pickle.load(open('/home/claude/kl/d123_final.pkl','rb')); C=set(F['C'])
LV={'L1':'GlobalTheory.Fam.ratDatum_dT_levelPrime_alt','L2':'GlobalTheory.PenLevPrime.uloc_le_of_std',
    'L3':'GlobalTheory.PenLevTyp.uloc_le_alt','L4':'GlobalTheory.AdForm.exists_twDat_baseStd'}
LC={k:clos([R(v)],E) for k,v in LV.items()}
C2=C.union(*LC.values())
for k,v in LC.items(): print(k, th(v))
print("newly closed", th(C2-C))
nm={n:i for i,n in enumerate(q.names)}
def load(f): return set(nm[l.split('\t')[0].strip()] for l in open('/home/claude/kl/sub_'+f+'.txt') if l.split('\t')[0].strip() in nm)
heads={'D1':[load(p) for p in ['true_geometry_row_pair_property_alt','true_geometry_row_pair_relation_alt_alt','true_geometry_twist_quadratic_value_alt']],
 'D2':[load(p) for p in ['exists_good','true_geometry_commutation_identity_alt','true_geometry_commutation_property_alt']],
 'D3':[load(p) for p in ['true_geometry_chain_step_value_alt','true_geometry_chain_step_identity_alt','exists_volume_constant_of_true_geometry']],
 'D5':[clos([R('GlobalTheory.AdForm.twS_ramL')],E)],
 'D7':[clos([R('GlobalTheory.QVecJoin.step_mid'),R('GlobalTheory.QVecJoin.step_top')],E)],
 'D8':[clos([R('GlobalTheory.T.true_geometry_row_column_entry_alt')],E)],
 'D9':[clos([R('GlobalTheory.T.true_geometry_twist_value_alt')],E)]}
out={}
for h,parts in heads.items():
    S=set().union(*parts)
    out[h]=(th(S),th(S-C),th(S-C2))
    print(h,"recount",th(S),"after D123",th(S-C),"after leaves",th(S-C2))
pickle.dump({'C2':sorted(C2),'LC':{k:sorted(v) for k,v in LC.items()},'heads':out},open('/home/claude/kl/lvl_final.pkl','wb'))
# what remains of D5
S=heads['D5'][0]-C2
called=set()
for j in S:
    for y in q.nbrs(g,j):
        if int(y) in S and int(y)!=j: called.add(int(y))
print([q.names[j] for j in S if j not in called and q.kinds[j] in ('theorem','lemma')][:5])
