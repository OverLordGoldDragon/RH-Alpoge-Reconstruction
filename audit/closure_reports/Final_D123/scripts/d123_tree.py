"""d123_tree.py NAME [depth]: tree of NAME inside D1∪D2∪D3 minus the twist-dictionary layer; marks calls into T."""
import sys, pickle; NMS=sys.argv[2:]; dep=int(sys.argv[1]); sys.argv=['q','x','x']
sys.path.insert(0,'/home/claude/scripts')
import q
from collections import deque
g=q.graph("fwd")
T=set(pickle.load(open('/home/claude/kl/layerT.pkl','rb')))
D={k:set(v) for k,v in pickle.load(open('/home/claude/kl/d123.pkl','rb')).items()}
U=D['D1']|D['D2']|D['D3']; S=set(pickle.load(open('/home/claude/kl/layerS.pkl','rb')))
R=(T if __import__('os').environ.get('INT') else U-T-S)
th=lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
def clos(i,A):
    seen={i}; dq=deque([i])
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in A and y not in seen: seen.add(y); dq.append(y)
    return seen
def show(i,d):
    kids={int(y) for y in q.nbrs(g,i)}
    tk=[j for j in kids if j in T or j in S]
    if tk: print("  "*d+f"-> T: "+", ".join(sorted(q.names[j].rsplit('.',1)[-1] for j in tk))[:300])
    for j in sorted([j for j in kids if j in R and j!=i],key=lambda j:-th(clos(j,R))):
        s=th(clos(j,R))
        if s<3: continue
        print("  "*d+f"{s:4d} {q.names[j]} [{q.locs[j][0].rsplit('/',1)[-1]}:{q.locs[j][1]}]")
        if d+1<dep: show(j,d+1)
for nm in NMS:
    i=q.resolve(nm)[0]; print('#####',th(clos(i,R)), nm); show(i,0)
