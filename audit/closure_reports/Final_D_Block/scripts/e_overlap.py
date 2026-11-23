"""e_overlap.py: overlap of the D5/D7/D8/D9 closures with the closure of the R4-E heads."""
import sys,pickle,re; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/scripts')
import q
from collections import deque
g=q.graph("fwd")
th=lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
nm={n:i for i,n in enumerate(q.names)}
def load(f):
    s=set(l.split('\t')[0] for l in open('/home/claude/idx/'+f)); return set(nm[n] for n in s if n in nm)
EX={k:load(f) for k,f in [('col','excl_colSide_alt.txt'),('cls','excl_clsPinD_of_famCol_of_trueW.txt'),('joint','excl_joint.txt'),('bwit','excl_bwit_exists_alt.txt')]}
ALL=set().union(*EX.values())
def clos(roots,A):
    seen=set(r for r in roots if r in A); dq=deque(seen)
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in A and y not in seen: seen.add(y); dq.append(y)
    return seen
pat=re.compile(r"(thetaKernel_eq_jet_thC|tw_resid_datum|chr_moves_eq_rho_base|LevLaw\.lev_law$|clsKL_real$|exists_clsT_of_pinTop$|JetScales\.exists_jetS$|AdForm\.realOf_is$|exists_readsG_of_level$|kernel_identity_tuple$)")
Eroots=[i for i in ALL if pat.search(q.names[i])]
print([q.names[i] for i in Eroots])
Eset=clos(Eroots,ALL); print("E closure in exclusive sets", th(Eset))
C4=set(pickle.load(open('/home/claude/kl/d5_final.pkl','rb'))['C4'])
heads={'D5':['GlobalTheory.AdForm.twS_ramL'],'D7':['GlobalTheory.QVecJoin.step_mid','GlobalTheory.QVecJoin.step_top'],'D8':['GlobalTheory.T.true_geometry_row_column_entry_alt'],'D9':['GlobalTheory.T.true_geometry_twist_value_alt']}
for h,v in heads.items():
    r=[nm[n] for n in v]
    S=clos(r,ALL); Sc=clos(r,EX['col'])
    print(h,"all-excl",th(S),"colSide",th(Sc),"S&E",th(S&Eset),"Sc&E",th(Sc&Eset),"S-colSide",th(S-EX['col']), "in joint", th(S&EX['joint']))
    pickle.dump({'S':sorted(S),'SE':sorted(S&Eset)},open(f'/home/claude/kl/{h}_E.pkl','wb'))
pickle.dump(sorted(Eset),open('/home/claude/kl/Eset.pkl','wb'))
