"""kl_classify.py: classify the exclusive material (block-exclusive and joint-exclusive) under the three
kernel-law heads by the component of the common kernel law (Proposition KL) that owns it."""
import sys; sys.argv = ['q','x','x']
import q
from collections import deque, OrderedDict
g = q.graph("fwd")
def ids(names):
    out = []
    for n in names:
        r = q.resolve(n)
        if not r: print("unresolved", n); continue
        out.append(r[0])
    return out
def clos(roots, allowed):
    seen = set(r for r in roots if r in allowed); dq = deque(seen)
    while dq:
        x = dq.popleft()
        for y in q.nbrs(g, x):
            y = int(y)
            if y in allowed and y not in seen: seen.add(y); dq.append(y)
    return seen
th = lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
joint = set(l.split('\t')[0] for l in open('/home/claude/idx/excl_joint.txt'))
J = set(i for i, n in enumerate(q.names) if n in joint)
COMP = OrderedDict([
 ("K2 base vector (EqP, chi factor, smoothness)", ["Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.SqG.eqP_car","Formalism.L2.Ker.Cd.CarC.eqLaw_ambOf_of","Formalism.L2.Ker.Cd.CarC.eqLaw_ambOf","Formalism.L2.Ker.eqLaw_ambOf","Formalism.L2.Ker.Cd.CarC.chiLaw_ambOf_of","Formalism.L2.Ker.Cd.CarC.chiLaw_ambOf","Formalism.L2.Ker.chiLaw_ambOf","GlobalTheory.Mem.Col2.ChiFacLaw.chiLaw_ambOf","Formalism.L2.Ker.Cd.CarC.eOmega_ambOf_of","Formalism.L2.Ker.Cd.CarC.eOmega_ambOf","Formalism.L2.Ker.eOmega_ambOf"]),
 ("K1 transport (Heisenberg naturality)", ["Formalism.L2.Ker.theta_coset_indicator_natural","Formalism.L2.Ker.Cd.CarC.thIndEq_ambOf_car","GlobalTheory.Mem.Col2.IndEq.thIndEq_of_vacEq","GlobalTheory.KerDia.Eqv.thCEq_of_ind","Formalism.L2.Ker.thIndEq_ambOf_of"]),
 ("K3 Heisenberg lattice data (LaHyp)", ["Formalism.L2.Ker.Cd.laHyp_ambOf_top","Formalism.L2.Ker.laHyp_ambOf_top","Formalism.L2.Ker.heisHyp_of"]),
 ("K4 jet chain rule and weights", ["Formalism.L2.Ker.TE.jetMap_pullD","Formalism.L2.Ker.TE.jetMap_pull","GlobalTheory.KerT.RatLaw.jetMap_pull","GlobalTheory.KerDia.Eqv.opOf_equiv","GlobalTheory.KerDia.Eqv.opOf_move","Formalism.L2.Ker.jet_in_weight_space_chain","Formalism.L2.Ker.wtLaw_step","Formalism.L2.Ker.jet_local_rationality","GlobalTheory.KerDia.Eqv.th_contDiff"]),
 ("K5 scalar bookkeeping (product formula, det laws, Xi characters)", ["Formalism.L2.Ker.muProdLaw_of","GlobalTheory.KerT.RatLaw.muProdLaw","Formalism.L2.Ker.muDetLaw_chain","Formalism.L2.Ker.unitInv_rho","GlobalTheory.KerDia.Eqv.xiAt_law","Formalism.L2.Ker.lawTies_of_ok"]),
 ("K6 assembly of the step law", ["Formalism.L2.Ker.thEquivP_ofD","Formalism.L2.Ker.thEquivP_stepT_ofD","Formalism.L2.Ker.Cd.CarC.thEquivP_ambOf_tiesD","GlobalTheory.KerDia.Eqv.scal_theta","GlobalTheory.KerDia.Eqv.th_move","GlobalTheory.KerDia.Eqv.ent_smul","GlobalTheory.T.kernelEntry_rationalEquivariance_transports","Formalism.L2.Ker.chThT_laws_of","GlobalTheory.KerDia.Eqv.ana"]),
 ("K7 Jacobi-group intertwining of the reading map (E1)", ["GlobalTheory.T.thetaKernel_splitPlaces_eq_jet_classicalTheta","GlobalTheory.KJInf.CoreG.thetaKernel_eq_jet_thC","GlobalTheory.AdForm.DatumRead.reads_datum_eq_thC","GlobalTheory.T.datumReading_splitPlaces_eq_classicalTheta","GlobalTheory.SplitMove.isThetaAt_move","GlobalTheory.MovedVac.vac_moved"]),
 ("K8 diamond invariance (D6 extra)", ["GlobalTheory.DiaTheta.th_dia","GlobalTheory.KerDia.RhoDia.rho_dia","GlobalTheory.KRamT.ent_dia"]),
])
heads = [("X1 core","bwit_exists_alt",["GlobalTheory.Mem.Col2.TC.RcHyp.hyps_of_isTw"]),
         ("X1 colRecC","bwit_exists_alt",["GlobalTheory.Mem.R3.SelC.colRecC"]),
         ("D6","colSide_alt",["GlobalTheory.KRamT.kernel_keeps_ramT"]),
         ("E1","clsPinD_of_famCol_of_trueW",["GlobalTheory.KerTup.kernel_identity_tuple"])]
compRoots = {c: ids(v) for c, v in COMP.items()}
allJ_or = None
for lab, F, h in heads:
    ex = set(l.split('\t')[0] for l in open('/home/claude/idx/excl_%s.txt' % F))
    E = set(i for i, n in enumerate(q.names) if n in ex)
    A = E | J
    hid = ids(h)
    S = clos(hid, A)
    print(f"== {lab}: sub-closure in (block-excl ∪ joint-excl): {th(S)} thm (block-excl part {th(S & E)}, joint-only part {th(S - E)})")
    owned = set()
    for c, roots in compRoots.items():
        C = clos(roots, A) & S
        new = C - owned
        owned |= C
        if th(C): print(f"   {c}: {th(C)} thm in closure ({th(new)} new)")
    rest = S - owned
    print(f"   REMAINDER (glue/other): {th(rest)} thm")
    open('/home/claude/kl/rest_%s.txt' % lab.replace(' ','_'), 'w').write("\n".join(f"{q.names[j]}\t{q.kinds[j]}\t{q.locs[j][0]}:{q.locs[j][1]}-{q.locs[j][2]}" for j in sorted(rest, key=lambda j: q.locs[j])))
