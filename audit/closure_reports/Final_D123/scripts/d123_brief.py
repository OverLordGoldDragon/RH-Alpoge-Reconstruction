"""d123_brief.py NAME...: statement (context stripped), exclusive sub-closure size inside D1∪D2∪D3, membership."""
import sys, re, pickle; args=sys.argv[1:]; sys.argv=['q','x','x']
sys.path.insert(0,'/home/claude/scripts')
import q
from collections import deque
g=q.graph("fwd")
D={k:set(v) for k,v in pickle.load(open('/home/claude/kl/d123.pkl','rb')).items()}
U=D['D1']|D['D2']|D['D3']
th=lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
def clos(i):
    seen={i}; dq=deque([i])
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in U and y not in seen: seen.add(y); dq.append(y)
    return seen
for a in args:
    r=q.resolve(a)
    if not r: print("??",a); continue
    i=r[0]; t=q.text(i)
    body=t.split("\n",1)[1] if "\n" in t else t
    head=body.split(":= by")[0] if ":= by" in body else body.split(":=")[0]
    head=re.sub(r"\s+"," ",head)
    head=re.sub(r"∀ \{B : GlobalTheory\.Mem\.Base\}.*?\{ex : Extra \(I\.rec7 l Z\) L hT Gi Gl Kc Yd cX\}","∀ <ctx>",head)
    head=head.replace("_root_.GlobalTheory.","").replace("(W : MiS.RealPackAlt ex), Fam.AllFamilyConditions W → ∀ (u : B.Word) (a : Fam.GeometricFamily W u), a.Is → a.True →","<W,u,a>")
    print("="*80); print(q.names[i], f"[{q.locs[i][0].rsplit('/',1)[-1]}:{q.locs[i][1]}-{q.locs[i][2]}]", "sub", th(clos(i)), [k for k in D if i in D[k]])
    print(head[:1600])
