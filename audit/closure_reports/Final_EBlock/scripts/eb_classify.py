"""eb_classify.py: assign each theorem of the E-block union (sub-closures of the five heads inside
E u J-only, see eb_sets.py) to the first mechanism (M1..M8, in order) whose root closure contains it;
report per-head counts, unique-union counts, shared theorems, and write eb_classes.tsv."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, pickle
from collections import deque, OrderedDict, Counter
g=q.graph("fwd")
P=pickle.load(open('/home/claude/idx/eb_sets.pkl','rb'))
HEADS=['E1','E2','E3','E4','E5']
HS={k:set(P[k][1]) for k in HEADS}
U=set().union(*HS.values())
th=lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
def clos(roots):
    ids=[]
    for r in roots:
        rr=[i for i,n in enumerate(q.names) if n==r] or q.resolve(r)
        assert rr, r; ids.append(rr[0])
    seen=set(i for i in ids if i in U); dq=deque(seen)
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in U and y not in seen: seen.add(y); dq.append(y)
    return seen
M=OrderedDict([
 ('M2 datum transport (local constancy + equivariance of the finite datum)',[
   'GlobalTheory.T.movedDatum_eq_finiteDatum_representativePair','GlobalTheory.AdForm.TwResid.xiAt_transport_tw',
   'GlobalTheory.AdForm.CongAtIdem.cong_at_idem','GlobalTheory.AdForm.exists_rat_half_approx',
   'GlobalTheory.T.idempotentHalf_eq_rational_add_nsmul_standardHom','GlobalTheory.AdForm.ReadLaw.transport_base']),
 ('M1 split-place Schroedinger comparison (Prop E and its leaves)',[
   'GlobalTheory.T.thetaKernel_splitPlaces_eq_jet_classicalTheta','GlobalTheory.SplitMove.isThetaAt_move',
   'GlobalTheory.T.classicalThetaOfDatum_smul_move','GlobalTheory.T.tupleLevel_pos_odd_badPrimes_prime_to_level']),
 ('M4 characters at determinant roots',[
   'GlobalTheory.T.chainMove_characters_eq_rho_up_to_base','GlobalTheory.AdForm.MovedLaw.chr_root_eq_prod','GlobalTheory.DetRootRead.chr_at_detRoot']),
 ('M5 archimedean Fock calculus',[
   'GlobalTheory.AdForm.JetRead.pureTensorO_zero_eq_jetP','GlobalTheory.KJReal.om_pureTensorO_onb','GlobalTheory.KerTup.jetP_cast',
   'GlobalTheory.AdForm.stdPair_world','GlobalTheory.T.exists_charExponent_infinity_kernel_shift']),
 ('M6 class points of a definite unitary group (algebraic modular forms)',[
   'GlobalTheory.T.chartLevels_reps_represent_unitaryDoubleCosets','GlobalTheory.T.last_space_moved_level_class_points_representatives',
   'GlobalTheory.AdForm.TwDat.Is.evz_decomp','GlobalTheory.T.readingVector_fixed_by_class_stabiliser_character',
   'GlobalTheory.T.form_translate_real_point_read_by_period','GlobalTheory.T.trueChainKernel_eq_classSum_jets',
   'GlobalTheory.AdForm.LevChiTop.emb_mem_chi','GlobalTheory.T.exists_coefficientVector_reading_realRepresentation_form',
   'GlobalTheory.T.exists_rowForm_prescribed_values_class_representatives']),
 ('M7 branching at the top step',[
   'GlobalTheory.T.trueColumns_branchingMap_equivariant_nonzero_common','GlobalTheory.T.lastGroup_embedding_real_components_block_form']),
 ('M3 level-pair eigen-law',['GlobalTheory.AdForm.LevLaw.lev_law']),
 ('M8 existence of the twist datum',['GlobalTheory.T.exists_tupleChain_adelicData']),
])
assign={}
for m,roots in M.items():
    for j in clos(roots):
        assign.setdefault(j,m)
for j in U: assign.setdefault(j,'A  assembly of the head (bodies of the head and its wrappers)')
# per-mechanism
mech=sorted(set(assign.values()))
print("UNION theorems:",th(U))
for m in mech:
    S={j for j in U if assign[j]==m}
    row=[th(S&HS[h]) for h in HEADS]
    print(f"{th(S):4d}  per-head {row}  {m}")
print("per-head totals", {h:th(HS[h]) for h in HEADS}, "sum", sum(th(HS[h]) for h in HEADS))
cnt=Counter()
for j in U:
    if q.kinds[j] not in ('theorem','lemma'): continue
    k=sum(1 for h in HEADS if j in HS[h]); cnt[k]+=1
print("theorems by number of heads using them:", dict(cnt))
sh=[(q.names[j],[h for h in HEADS if j in HS[h]],assign[j][:3]) for j in U if q.kinds[j] in ('theorem','lemma') and sum(1 for h in HEADS if j in HS[h])>1]
open('/home/claude/eblock/out_shared.tsv','w').write("\n".join(f"{n}\t{','.join(h)}\t{m}" for n,h,m in sorted(sh)))
E=set(l.split('\t')[0] for l in open('/home/claude/idx/excl_clsPinD_of_famCol_of_trueW.txt'))
with open('/home/claude/eblock/eb_classes.tsv','w') as f:
    f.write("declaration\tkind\tfile:line\theads\tmechanism\tset\n")
    for j in sorted(U,key=lambda j:q.names[j]):
        f.write(f"{q.names[j]}\t{q.kinds[j]}\t{q.locs[j][0]}:{q.locs[j][1]}\t{','.join(h for h in HEADS if j in HS[h])}\t{assign[j]}\t{'E' if q.names[j] in E else 'J'}\n")
print("shared theorems:",len(sh))
