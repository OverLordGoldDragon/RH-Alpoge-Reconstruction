"""wb_dlane.py: overlap of each W residual (and the K-leaves) with the forward closures of the open D-heads
D5, D7, D8, D9, of colSide_alt and clsPinD (E-block top), and with the E-block union."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, pickle
g=q.graph("fwd"); P=pickle.load(open('/home/claude/idx/wb_sets.pkl','rb'))
K=set(pickle.load(open('/home/claude/idx/wb_K.pkl','rb')))
R={k:set(v[1]) for k,v in P['res'].items()}; R['W1-noK']=R['W1']-K; R['K']=K
th=lambda S: sum(1 for j in S if q.kinds[j] in('theorem','lemma'))
DH={'D5':'GlobalTheory.AdForm.twS_ramL','D7a':'GlobalTheory.QVecJoin.step_mid','D7b':'GlobalTheory.QVecJoin.step_top','D8':'true_geometry_row_column_entry_alt','D9':'true_geometry_twist_value_alt','colSide':'colSide_alt','clsPinD':'clsPinD_of_famCol_of_trueW'}
cl={k:set(q.bfs(g,q.resolve(v)[0])[0]) for k,v in DH.items()}
EB=set(P['EB'])
for k,S in R.items():
    print(f"{k:7s} {th(S):4d} thm |", "  ".join(f"{d}:{th(S&c)}" for d,c in cl.items()), f"| E-block:{th(S&EB)}")
