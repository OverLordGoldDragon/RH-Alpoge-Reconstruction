"""wb_kleaves.py: the kernel-law support leaves K-a, K-b, K-c inside the W-block domain: closures, overlap with W1, and paths."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, pickle
from collections import deque
g=q.graph("fwd"); P=pickle.load(open('/home/claude/idx/wb_sets.pkl','rb'))
B=set(P['B']); JO=set(P['JO']); D=B|JO; W1=set(P['res']['W1'][0])
th=lambda S: sum(1 for j in S if q.kinds[j] in('theorem','lemma'))
def clos(ids,dom):
    seen=set(ids); dq=deque(ids)
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in dom and y not in seen: seen.add(y); dq.append(y)
    return seen
N={n:i for i,n in enumerate(q.names)}
K={'K-a':['rational_integrality_link','hermitian_form_integral_values'],'K-b':['SO.stdOK'],'K-c':['sqSplit_of','muOneL_of','muOneR_of']}
allK=set()
for k,v in K.items():
    roots=[i for i,n in enumerate(q.names) if any(n.endswith('.'+x) for x in v)]
    for r in roots: print(k, q.names[r], 'in D' if r in D else 'outside D', 'in W1' if r in W1 else '')
    S=clos([r for r in roots if r in D],D); allK|=S
    print(f"  {k}: closure in D {th(S)} thm, inside W1 {th(S&W1)}")
print("K union in D",th(allK),"in W1",th(allK&W1))
pickle.dump(sorted(allK),open('/home/claude/idx/wb_K.pkl','wb'))
