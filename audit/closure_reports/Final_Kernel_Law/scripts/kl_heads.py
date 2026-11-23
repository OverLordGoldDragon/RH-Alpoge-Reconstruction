"""kl_heads.py: for each of the 16 residual heads of Final_Internal_Cleanup, the head's exclusive
sub-closure (inside its block's exclusive set), the part owned by the common kernel law (closure of the
law roots of kl_classify.py, components K1-K6 and K8), and what remains."""
import sys; sys.argv = ['q','x','x']
sys.path.insert(0, '/home/claude/scripts')
import q
from collections import deque
exec(open('/home/claude/scripts/kl_classify.py').read().split("heads = [")[0].split("COMP = OrderedDict(")[0])
src = open('/home/claude/scripts/kl_classify.py').read()
COMP = eval("OrderedDict(" + src.split("COMP = OrderedDict(")[1].split("\nheads = [")[0].rstrip().rstrip(")") + ")")
LAWC = ["K1 transport (Heisenberg naturality)","K2 base vector (EqP, chi factor, smoothness)","K3 Heisenberg lattice data (LaHyp)",
        "K4 jet chain rule and weights","K5 scalar bookkeeping (product formula, det laws, Xi characters)","K6 assembly of the step law","K8 diamond invariance (D6 extra)"]
lawroots = [r for c in LAWC for r in ids(COMP[c])]
HEADS = [
 ("X1","bwit_exists_alt",["GlobalTheory.Mem.R3.SelC.square_integrable_columns_of_witnesses"]),
 ("X7","bwit_exists_alt",["GlobalTheory.Mem.Top.Bl.WPt.exists_pinned_spectral_data_compatible","GlobalTheory.Mem.Top.Bl.exists_kernel_spectral_data_at_witnesses"]),
 ("X2 leaf","bwit_exists_alt",["GlobalTheory.T.reFace_zero_part_conventions_chosen_again"]),
 ("D1","colSide_alt",["true_geometry_row_pair_property_alt","true_geometry_row_pair_relation_alt_alt","true_geometry_twist_quadratic_value_alt"]),
 ("D2","colSide_alt",["exists_good","true_geometry_commutation_identity_alt","true_geometry_commutation_property_alt"]),
 ("D3","colSide_alt",["true_geometry_chain_step_value_alt","true_geometry_chain_step_identity_alt","exists_volume_constant_of_true_geometry"]),
 ("D5","colSide_alt",["GlobalTheory.AdForm.twS_ramL"]),
 ("D6","colSide_alt",["GlobalTheory.KRamT.kernel_keeps_ramT"]),
 ("D7","colSide_alt",["GlobalTheory.QVecJoin.step_mid","GlobalTheory.QVecJoin.step_top"]),
 ("D8","colSide_alt",["true_geometry_row_column_entry_alt"]),
 ("D9","colSide_alt",["true_geometry_twist_value_alt"]),
 ("E1","clsPinD_of_famCol_of_trueW",["GlobalTheory.KerTup.kernel_identity_tuple","GlobalTheory.AdForm.LevLaw.lev_law","clsKL_real"]),
 ("E2","clsPinD_of_famCol_of_trueW",["GlobalTheory.AdForm.exists_clsT_of_pinTop"]),
 ("E3","clsPinD_of_famCol_of_trueW",["GlobalTheory.AdForm.JetScales.exists_jetS"]),
 ("E4","clsPinD_of_famCol_of_trueW",["GlobalTheory.AdForm.realOf_is"]),
 ("E5","clsPinD_of_famCol_of_trueW",["GlobalTheory.AdForm.exists_readsG_of_level"]),
]
ALL = set(range(len(q.names)))
blocks = {}
for F in ['bwit_exists_alt','colSide_alt','clsPinD_of_famCol_of_trueW']:
    ex = set(l.split('\t')[0] for l in open('/home/claude/idx/excl_%s.txt' % F))
    blocks[F] = set(i for i, n in enumerate(q.names) if n in ex)
U = J | blocks['bwit_exists_alt'] | blocks['colSide_alt'] | blocks['clsPinD_of_famCol_of_trueW']
LAW = clos(lawroots, U)
print("law closure inside (joint ∪ block-exclusive):", th(LAW), "thm;  in joint-only:", th(LAW - blocks['bwit_exists_alt'] - blocks['colSide_alt'] - blocks['clsPinD_of_famCol_of_trueW']))
rows = []
for lab, F, hs in HEADS:
    E = blocks[F]
    hid = ids(hs)
    S = clos(hid, E)
    L = S & LAW
    rows.append((lab, th(S), th(L), th(S - L)))
    print(f"{lab:8s} exclusive {th(S):5d}  law-owned {th(L):5d}  remaining {th(S-L):5d}")
tot = sum(r[1] for r in rows); rem = sum(r[3] for r in rows)
print("sum over heads (X1 counted once):", tot, "->", rem)
# block totals
for F, E in blocks.items():
    print(F, "block exclusive", th(E), "after law", th(E - LAW))
print("joint exclusive", th(J), "after law", th(J - LAW))

# deduplicated block residual sets before/after
print("\n-- deduplicated residual sets --")
closed_extra = {"X1": ["GlobalTheory.Mem.Col2.TC.RcHyp.hyps_of_isTw"], "D6": ["GlobalTheory.KRamT.kernel_keeps_ramT"]}
keep_leaf = set(clos(ids(["GlobalTheory.Mem.Col2.TC.RcHyp.idxMatNF_of_isTw"]), blocks['bwit_exists_alt']))
for F, labs in [('bwit_exists_alt', ['X1','X7','X2 leaf']), ('colSide_alt', ['D1','D2','D3','D5','D6','D7','D8','D9']), ('clsPinD_of_famCol_of_trueW', ['E1','E2','E3','E4','E5'])]:
    E = blocks[F]
    Rset = set()
    for lab, FF, hs in HEADS:
        if lab in labs: Rset |= clos(ids(hs), E)
    closed = set()
    for k, v in closed_extra.items():
        if k in labs: closed |= clos(ids(v), E)
    closed -= keep_leaf
    print(F, "residual union", th(Rset), "closed by kernel law", th(Rset & closed), "after", th(Rset - closed))
