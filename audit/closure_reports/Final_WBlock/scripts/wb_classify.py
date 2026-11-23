"""wb_classify.py: assign each theorem of the W-block residual union (wb_sets.py) to its mechanism Q1-Q5
(first root closure that contains it, order Q2, Q3, Q4, Q5, Q1) and write WBlock_Declaration_Classes.tsv."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, pickle
from collections import deque, OrderedDict
g=q.graph("fwd"); P=pickle.load(open('/home/claude/idx/wb_sets.pkl','rb'))
K=set(pickle.load(open('/home/claude/idx/wb_K.pkl','rb')))
HS={k:set(v[1]) for k,v in P['res'].items()}; U=set().union(*HS.values())
N={n:i for i,n in enumerate(q.names)}
th=lambda S: sum(1 for j in S if q.kinds[j] in('theorem','lemma'))
def clos(roots):
    ids=[N[r] for r in roots]; seen=set(i for i in ids if i in U); dq=deque(seen)
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in U and y not in seen: seen.add(y); dq.append(y)
    return seen
M=OrderedDict([
 ('Q2 integrality and split data of the Fock period lattices (K-a, K-b, K-c)',None),
 ('Q3 class-field pieces of the small field',['GlobalTheory.Mem.CyclotomicFieldContainment.oTied_of_ksExact']),
 ('Q4 joints of the standard character',['GlobalTheory.Mem.Top.Bl.exists_kernel_spectral_data_at_witnesses']),
 ('Q5 zero-part conventions',['GlobalTheory.T.reFace_zero_part_conventions_chosen_again']),
 ('Q1 column record of the base tuple',['GlobalTheory.Mem.R3.SelC.square_integrable_columns_of_witnesses']),
 ('A  assembly of the record-compatible extension',['GlobalTheory.Mem.Top.Bl.WPt.exists_pinned_spectral_data_compatible']),
])
assign={}
for m,roots in M.items():
    S=(K&U) if roots is None else clos(roots)
    for j in S: assign.setdefault(j,m)
print("union",th(U))
for m in M:
    S={j for j in U if assign.get(j)==m}
    print(f"{th(S):4d}  per-head {[th(S&HS[h]) for h in HS]}  {m}")
print("unassigned",th(U-set(assign)))
E=set(P['B'])
with open('/home/claude/wblock/WBlock_Declaration_Classes.tsv','w') as f:
    f.write("declaration\tkind\tfile:line\thead\tmechanism\tset\n")
    for j in sorted(U,key=lambda j:q.names[j]):
        f.write(f"{q.names[j]}\t{q.kinds[j]}\t{q.locs[j][0]}:{q.locs[j][1]}\t{','.join(h for h in HS if j in HS[h])}\t{assign.get(j,'?')}\t{'B' if j in E else 'J'}\n")
