"""d123_layers2.py: second dictionary layer (split G-places, 'AtType' / symmetric chain), then the rest."""
import sys, re, pickle; sys.argv=['q','x','x']
sys.path.insert(0,'/home/claude/scripts')
import q
from collections import deque, Counter
g=q.graph("fwd")
D={k:set(v) for k,v in pickle.load(open('/home/claude/kl/d123.pkl','rb')).items()}
U=D['D1']|D['D2']|D['D3']
T=set(pickle.load(open('/home/claude/kl/layerT.pkl','rb')))
th=lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
def clos(roots,A):
    seen=set(r for r in roots if r in A); dq=deque(seen)
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in A and y not in seen: seen.add(y); dq.append(y)
    return seen
pref=("GlobalTheory.SymBridge.","GlobalTheory.EntryBridge.","GlobalTheory.UnfoldSum.","GlobalTheory.SymChain.","GlobalTheory.LocMod.SymChainAt.")
roots=[]
for j in U-T:
    head=q.text(j).split(":=")[0]
    if re.search(r"\bAtType\b|IsSymLevel", head) or q.names[j].startswith(pref): roots.append(j)
S=clos(roots,U-T)
print("type-prime dictionary layer:", th(S), {k:th((S)&v) for k,v in D.items()})
pickle.dump(sorted(S),open('/home/claude/kl/layerS.pkl','wb'))
REST=U-T-S
print("rest:", th(REST), {k:th(REST&v) for k,v in D.items()})
c=Counter()
for j in REST:
    if q.kinds[j] in ('theorem','lemma'): c[q.names[j].rsplit('.',1)[0]]+=1
for k,v in c.most_common(45): print(f"{v:4d} {k}")
