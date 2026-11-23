"""kl_joint.py: split the joint-only part of the kernel-law closure into the EqP sub-packages."""
import sys; sys.argv = ['q','x','x']
sys.path.insert(0, '/home/claude/scripts')
exec(open('/home/claude/scripts/kl_heads.py').read().split("rows = []")[0])
JO = LAW - blocks['bwit_exists_alt'] - blocks['colSide_alt'] - blocks['clsPinD_of_famCol_of_trueW']
print("joint-only law material", th(JO))
P = OrderedDict([
 ("hermitian integrality (QInt)", ["Formalism.L2.Ker.Cd.IntegralLatticeDensity.rational_integrality_link","Formalism.L2.Ker.Cd.IntegralLatticeDensity.hermitian_form_integral_values"]),
 ("standard theta data (StdOK)", ["Formalism.L2.Ker.Cd.IntegralLatticeDensity.SO.stdOK"]),
 ("square path independence (SqSplit)", ["Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.SquareSplitPairs.sqSplit_of","Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.Sq.sqP_of"]),
 ("triangle laws mu=1 (MuOneL/R)", ["Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.Mu.left_move_triangles_hold","Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.Mu.right_move_triangles_hold"]),
 ("Weil constants J1,J2 (Cayley, Gauss sum)", ["Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.J.first_constant_of_pullback","Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.J.second_constant_of_pullback"]),
 ("reduction to paths (eqP, e3a, e3b, chi factor)", ["Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.eqP","Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.SqG.eqP_car"]),
 ("chi law, eOmega, eqLaw wrappers", ["Formalism.L2.Ker.Cd.CarC.chiLaw_ambOf_of","Formalism.L2.Ker.Cd.CarC.eOmega_ambOf_of","Formalism.L2.Ker.Cd.CarC.eqLaw_ambOf_of","GlobalTheory.Mem.Col2.ChiFacLaw.chiLaw_ambOf"]),
 ("Heisenberg lattice data (LaHyp)", ["Formalism.L2.Ker.Cd.laHyp_ambOf_top","Formalism.L2.Ker.laHyp_ambOf_top"]),
 ("transport and jets", ["Formalism.L2.Ker.theta_coset_indicator_natural","GlobalTheory.Mem.Col2.IndEq.thIndEq_of_vacEq","GlobalTheory.KerDia.Eqv.thCEq_of_ind","Formalism.L2.Ker.TE.jetMap_pull","GlobalTheory.KerDia.Eqv.opOf_move"]),
])
own = set()
for k, v in P.items():
    C = clos(ids(v), U) & JO
    new = C - own; own |= C
    print(f"  {k}: {th(C)} ({th(new)} new)")
print("  other:", th(JO - own))
