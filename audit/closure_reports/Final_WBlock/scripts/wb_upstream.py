"""wb_upstream.py: where the upstream inputs used by W1-W3 sit (W-domain or outside), and whether a D-head reaches them."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, pickle
g=q.graph("fwd"); P=pickle.load(open('/home/claude/idx/wb_sets.pkl','rb')); D=set(P['B'])|set(P['JO'])
names=['split_pair_generation','GlobalTheory.TorsionDegree.finrank_torsionField_le','GlobalTheory.DiscRoot.discField_eq_torsionField','GlobalTheory.TorsionRam.dvd_discr_torsionField',
'GlobalTheory.T.standardAddChar_placeIdempotent_div_prime','GlobalTheory.Mem.CyclotomicFieldContainment.ksQ_eq','GlobalTheory.T.idxT_ok','Formalism.L2.DIV.lvlE_lvlPr_V0E',
'GlobalTheory.AtG.ramCols_true','GlobalTheory.HostDatumExists.exists_hostDatum_alt','Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.J.negOneNorm','GlobalTheory.QNF.nf_iff_matNF','Formalism.L2.Th1.F.discNeZero']
DH={'D5':'GlobalTheory.AdForm.twS_ramL','D7a':'GlobalTheory.QVecJoin.step_mid','D7b':'GlobalTheory.QVecJoin.step_top','D8':'true_geometry_row_column_entry_alt','D9':'true_geometry_twist_value_alt'}
cl={k:set(q.bfs(g,q.resolve(v)[0])[0]) for k,v in DH.items()}
for n in names:
    r=[i for i,x in enumerate(q.names) if x==n] or q.resolve(n.rsplit('.',1)[-1])
    if not r: print(n,'NOT FOUND'); continue
    i=r[0]; print(f"{q.names[i]:70s} {'W-domain' if i in D else 'outside (live elsewhere)'}  D-heads: {[k for k,c in cl.items() if i in c]}")
