"""d123_core.py: the D1, D2, D3 exclusive sub-closures inside colSide_alt, their union, and the shared
core (reached by at least two of them) with its roots and sizes."""
import sys; sys.argv=['q','x','x']
sys.path.insert(0,'/home/claude/scripts')
import q
from collections import deque
g=q.graph("fwd")
ex=set(l.split('\t')[0] for l in open('/home/claude/idx/excl_colSide_alt.txt'))
E=set(i for i,n in enumerate(q.names) if n in ex)
def clos(roots,A):
    seen=set(r for r in roots if r in A); dq=deque(seen)
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in A and y not in seen: seen.add(y); dq.append(y)
    return seen
th=lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
R=lambda n: q.resolve(n)[0]
D={'D1':clos([R('GlobalTheory.Fam.QuadraticExtensionData.dat_exists')],E),
   'D2':clos([R('GlobalTheory.LowJoin.exists_quadratic_extension_readsLow')],E),
   'D3':clos([R('GlobalTheory.Fam.vol_level_wt_const_alt')],E)}
U=D['D1']|D['D2']|D['D3']
print({k:th(v) for k,v in D.items()}, "union", th(U))
cnt={}
for k,v in D.items():
    for j in v: cnt[j]=cnt.get(j,0)+1
S=set(j for j,c in cnt.items() if c>=2)
print("shared by >=2:", th(S), " by all 3:", th(set(j for j,c in cnt.items() if c==3)))
called=set()
for j in S:
    for y in q.nbrs(g,j):
        y=int(y)
        if y in S and y!=j: called.add(y)
roots=[j for j in S if j not in called]
for j in sorted(roots,key=lambda j:-th(clos([j],S))):
    s=th(clos([j],S))
    if s>=3: print(f"{s:4d} {q.names[j]} [{q.locs[j][0].rsplit('/',1)[-1]}:{q.locs[j][1]}] in {[k for k in D if j in D[k]]}")
import pickle; pickle.dump({k:sorted(v) for k,v in D.items()}, open('/home/claude/kl/d123.pkl','wb'))
