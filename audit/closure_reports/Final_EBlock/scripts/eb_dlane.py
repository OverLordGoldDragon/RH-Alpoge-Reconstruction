"""eb_dlane.py: overlap of the E-block union with the forward closures of the D-agent's heads D5, D7, D8, D9."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, pickle
g=q.graph("fwd")
P=pickle.load(open('/home/claude/idx/eb_sets.pkl','rb'))
U=set().union(*[set(P[k][1]) for k in ['E1','E2','E3','E4','E5']])
DH={'D5':'GlobalTheory.AdForm.twS_ramL','D7a':'GlobalTheory.QVecJoin.step_mid','D7b':'GlobalTheory.QVecJoin.step_top','D8':'true_geometry_row_column_entry_alt','D9':'true_geometry_twist_value_alt'}
for k,v in DH.items():
    c=q.bfs(g,q.resolve(v)[0])[0]; o=[j for j in U if j in c]
    print(k, q.names[q.resolve(v)[0]], 'overlap with E-block union:', len(o), [q.names[j] for j in o][:5])
import csv
cls={r[0]:r for r in csv.reader(open('/home/claude/eblock/eb_classes.tsv'),delimiter='\t')}
print()
for k in ['D5','D8']:
    c=q.bfs(g,q.resolve(DH[k])[0])[0]
    for j in sorted((j for j in U if j in c), key=lambda j:q.names[j]):
        r=cls[q.names[j]]; print(k, r[1], r[0], r[3], r[4][:3], r[5])
