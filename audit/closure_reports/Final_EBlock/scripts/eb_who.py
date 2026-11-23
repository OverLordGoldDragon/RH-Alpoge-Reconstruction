"""eb_who.py NAME: which of the PC4.13 block tops and residual heads reach NAME (exact edges), and a witness path from each block top."""
import sys; T=sys.argv[1]; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q
from collections import deque
g=q.graph("fwd")
t=q.resolve(T)[0]
H={'bwit':'bwit_exists_alt','colSide':'colSide_alt','clsPinD':'clsPinD_of_famCol_of_trueW',
 'D1a':'true_geometry_row_pair_property_alt','D1b':'true_geometry_row_pair_relation_alt_alt','D1c':'true_geometry_twist_quadratic_value_alt',
 'D2a':'GlobalTheory.T.exists_good','D2b':'true_geometry_commutation_identity_alt','D2c':'true_geometry_commutation_property_alt',
 'D3a':'true_geometry_chain_step_value_alt','D3b':'true_geometry_chain_step_identity_alt','D3c':'exists_volume_constant_of_true_geometry',
 'D5':'GlobalTheory.AdForm.twS_ramL','D7a':'GlobalTheory.QVecJoin.step_mid','D7b':'GlobalTheory.QVecJoin.step_top',
 'D8':'true_geometry_row_column_entry_alt','D9':'true_geometry_twist_value_alt',
 'E1':'GlobalTheory.KerLaws.clsKL_is','E2':'GlobalTheory.AdForm.exists_clsT_of_pinTop','E3':'GlobalTheory.AdForm.JetScales.exists_jetS',
 'E4':'GlobalTheory.AdForm.realOf_is','E5':'GlobalTheory.AdForm.exists_readsG_of_level','W1':'GlobalTheory.Mem.R3.SelC.square_integrable_columns_of_witnesses'}
for k,n in H.items():
    r=q.resolve(n)
    if not r: print(k,'unresolved',n); continue
    prev,hit=q.bfs(g,r[0],{t})
    if hit is not None:
        p=q.path(prev,hit); print(f"{k:7s} REACHES ({len(p)} steps): "+" -> ".join(q.names[j].rsplit('.',1)[-1] for j in p[:8])+(' ...' if len(p)>8 else ''))
    else: print(f"{k:7s} no")
