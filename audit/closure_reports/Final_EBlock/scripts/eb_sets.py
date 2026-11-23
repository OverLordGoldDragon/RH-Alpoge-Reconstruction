"""eb_sets.py: E-block head sub-closures.
E = exclusive set of the class-data block clsPinD_of_famCol_of_trueW (exclusive.py output);
J = joint exclusive set of the three PC4.13 blocks (bwit_exists_alt, colSide_alt, clsPinD).
For each head: sub-closure inside E, inside E u (J minus the other two blocks' exclusive sets)."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, pickle
from collections import deque
g=q.graph("fwd")
def load(F): 
    S=set(l.split('\t')[0] for l in open('/home/claude/idx/excl_%s.txt'%F))
    return set(i for i,n in enumerate(q.names) if n in S)
E=load('clsPinD_of_famCol_of_trueW'); BW=load('bwit_exists_alt'); CS=load('colSide_alt'); J=load('joint')
JO=J-BW-CS-E
def th(S): return sum(1 for j in S if q.kinds[j] in('theorem','lemma'))
def clos(ids,dom):
    seen=set(ids); dq=deque(ids)
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in dom and y not in seen: seen.add(y); dq.append(y)
    return seen
def ids(ns): return [q.resolve(n)[0] for n in ns]
HEADS={
 'E1a':['GlobalTheory.KerTup.kernel_identity_tuple'],
 'E1c':['GlobalTheory.AdForm.LevLaw.lev_law','GlobalTheory.KJRealLive.clsKL_real'],
 'E1kval':['GlobalTheory.AdForm.ClsKLive.kval'],
 'E1':['GlobalTheory.KerLaws.clsKL_is'],
 'E2':['GlobalTheory.AdForm.exists_clsT_of_pinTop'],
 'E3':['GlobalTheory.AdForm.JetScales.exists_jetS'],
 'E4':['GlobalTheory.AdForm.realOf_is'],
 'E5':['GlobalTheory.AdForm.exists_readsG_of_level'],
}
print("E thm",th(E),"J thm",th(J),"J-only (not in any block) thm",th(JO))
D=E|JO
res={}
for k,v in HEADS.items():
    i=ids(v)
    for n,j in zip(v,i): assert q.names[j]==n or q.names[j].endswith(n), (n,q.names[j])
    SE=clos(i,E|set(i)); SD=clos(i,D|set(i)); SF=clos(i,set(range(len(q.names))))
    res[k]=(SE,SD)
    print(f"{k:7s} inE {th(SE):4d}  inE+Jonly {th(SD):4d}  Jonly part {th(SD-E):4d}  full fwd closure {len(SF)}")
ks=['E1','E2','E3','E4','E5']
print("pairwise overlaps (thm) inside E+Jonly:")
for a in ks:
    print(a, [th(res[a][1]&res[b][1]) for b in ks])
U=set().union(*[res[k][1] for k in ks]); UE=set().union(*[res[k][0] for k in ks])
print("union inE",th(UE),"union inE+Jonly",th(U),"sum of heads inE",sum(th(res[k][0]) for k in ks))
print("E not under any head:",th(E-UE), sorted(q.names[j] for j in E-UE if q.kinds[j] in('theorem','lemma'))[:20])
pickle.dump({k:(sorted(a),sorted(b)) for k,(a,b) in res.items()},open('/home/claude/idx/eb_sets.pkl','wb'))
