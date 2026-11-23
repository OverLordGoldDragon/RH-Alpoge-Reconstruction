"""d123_layers.py: split D1∪D2∪D3 into the twist-place dictionary (closure of every declaration whose
statement assumes AtTwist, plus the localization bridges) and the rest; list the largest remaining roots."""
import sys, re, pickle; sys.argv=['q','x','x']
sys.path.insert(0,'/home/claude/scripts')
import q
from collections import deque
g=q.graph("fwd")
D={k:set(v) for k,v in pickle.load(open('/home/claude/kl/d123.pkl','rb')).items()}
U=D['D1']|D['D2']|D['D3']
th=lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
def clos(roots,A):
    seen=set(r for r in roots if r in A); dq=deque(seen)
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in A and y not in seen: seen.add(y); dq.append(y)
    return seen
roots=[]
for j in U:
    t=q.text(j); head=t.split(":=")[0]
    if re.search(r"AtTwist", head) or q.names[j].startswith("GlobalTheory.VolBridge") or q.names[j].startswith("GlobalTheory.UnipRead") or q.names[j].startswith("GlobalTheory.RankOneMatrix") or q.names[j]=="GlobalTheory.denseGL_completion":
        roots.append(j)
T=clos(roots,U)
print("twist dictionary layer:", th(T), "of", th(U), {k:th(T&v) for k,v in D.items()})
REST=U-T
pickle.dump(sorted(T),open('/home/claude/kl/layerT.pkl','wb'))
for k,v in D.items():
    R=v-T
    called=set()
    for j in R:
        for y in q.nbrs(g,j):
            y=int(y)
            if y in R and y!=j: called.add(y)
    print(f"== {k}: rest {th(R)}")
    def sub(i): return clos([i],R)
    top=[j for j in R if j not in called]
    # print children of top two levels with sizes
    seen=set()
    def show(i,d,D_):
        kids=sorted({int(y) for y in q.nbrs(g,i) if int(y) in R}, key=lambda j:-th(sub(j)))
        for j in kids:
            s=th(sub(j))
            if s<8: continue
            print("  "*d+f"{s:4d} {q.names[j]} [{q.locs[j][0].rsplit('/',1)[-1]}:{q.locs[j][1]}]"+(" (seen)" if j in seen else ""))
            if j in seen or d+1>=D_: continue
            seen.add(j); show(j,d+1,D_)
    for t0 in top: show(t0,0,4)
