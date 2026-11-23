"""d123_final.py: final classification of D1 ∪ D2 ∪ D3 into reconstructed mechanisms and statement-level
leaves, plus the effect on the other colSide heads (D5, D7, D8, D9)."""
import sys, pickle, json; sys.argv=['q','x','x']
sys.path.insert(0,'/home/claude/scripts')
import q
from collections import deque
g=q.graph("fwd")
th=lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
R=lambda n: q.resolve(n)[0]
D={k:set(v) for k,v in pickle.load(open('/home/claude/kl/d123.pkl','rb')).items()}
U=D['D1']|D['D2']|D['D3']
T=set(pickle.load(open('/home/claude/kl/layerT.pkl','rb')))
S=set(pickle.load(open('/home/claude/kl/layerS.pkl','rb')))
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
LEAVES={
 'L1':['GlobalTheory.Fam.ratDatum_dT_levelPrime_alt'],
 'L2':['GlobalTheory.PenLevPrime.uloc_le_of_std'],
 'L3':['GlobalTheory.PenLevTyp.uloc_le_alt'],
 'L4':['GlobalTheory.AdForm.exists_twDat_baseStd'],
}
LS={k:clos([R(n) for n in v],U) for k,v in LEAVES.items()}
Rz=set().union(*LS.values())
C=U-Rz
loc=clos([R(n) for n in ['GlobalTheory.QExtEx.exists_qExt','GlobalTheory.QTw.Inh.exists_ext_of_reps',
   'GlobalTheory.QTw.StepChar.comp_eq_muAt_and_tame']],C)-T-S
mech={'C-tw (twist-prime dictionary)':(T&C),'C-ty (G-place dictionary)':(S&C),'L (local data at a split place)':loc,
      'A (assembly over places)':C-T-S-loc}
out={}
print("union",th(U),"closed",th(C),"residual",th(Rz))
for k,v in mech.items(): print(f"  {k}: {th(v)}  by head {[th(v&D[h]) for h in D]}"); out[k]=th(v)
for k,v in LS.items(): print(f"  leaf {k} {LEAVES[k][0]}: {th(v)} heads {[h for h in D if v&D[h]]}")
for h in D: print(h, "graph", th(D[h]), "closed", th(D[h]&C), "left", th(D[h]&Rz))
# other heads
OTH={'D5':['GlobalTheory.AdForm.twS_ramL'],'D7':['GlobalTheory.QVecJoin.step_mid','GlobalTheory.QVecJoin.step_top'],
     'D8':['GlobalTheory.T.true_geometry_row_column_entry_alt'],'D9':['GlobalTheory.T.true_geometry_twist_value_alt']}
for k,v in OTH.items():
    try: X=clos([R(n) for n in v],E)
    except Exception as e: print(k,"unresolved",e); continue
    print(k, "recount", th(X), "meets closed", th(X&C), "meets leaves", th(X&Rz))
pickle.dump({'C':sorted(C),'Rz':sorted(Rz),'mech':{k:sorted(v) for k,v in mech.items()},'LS':{k:sorted(v) for k,v in LS.items()}},open('/home/claude/kl/d123_final.pkl','wb'))
with open('/home/claude/kl/d123_classes.tsv','w') as f:
    f.write("declaration\tkind\tfile\tline\theads\tclass\n")
    cls={}
    for k,v in mech.items():
        for j in v: cls[j]=k
    for k,v in LS.items():
        for j in v: cls[j]=('leaf '+k)
    for j in sorted(U,key=lambda j:q.names[j]):
        f.write(f"{q.names[j]}\t{q.kinds[j]}\t{q.locs[j][0]}\t{q.locs[j][1]}\t{','.join(h for h in D if j in D[h])}\t{cls[j]}\n")
