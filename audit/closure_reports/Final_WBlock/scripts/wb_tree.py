"""wb_tree.py ROOT DEPTH MIN [dom]: tree of ROOT's sub-closure in dom.
dom: R = W-domain minus already-closed material (law, E-block, D1-D3) plus the K-leaves (left open by the kernel-law pass);
D = whole W-domain; K = K-leaf closure."""
import sys; R,DEP,MIN=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]); dom=sys.argv[4] if len(sys.argv)>4 else 'R'
sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, pickle
from collections import deque
g=q.graph("fwd"); P=pickle.load(open('/home/claude/idx/wb_sets.pkl','rb'))
B=set(P['B']); JO=set(P['JO']); D=B|JO; K=set(pickle.load(open('/home/claude/idx/wb_K.pkl','rb')))
CLOSED=set(P['LAW'])|set(P['EB'])|set(P['D123'])
DOM={'R':(D-CLOSED)|K,'D':D,'K':K}[dom]
memo={}
def sub(i):
    if i in memo: return memo[i]
    seen={i}; dq=deque([i])
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in DOM and y not in seen: seen.add(y); dq.append(y)
    memo[i]=sum(1 for j in seen if q.kinds[j] in('theorem','lemma')); return memo[i]
def tag(j): return ('K' if j in K else '')+('B' if j in B else ('J' if j in JO else '-'))+('*' if j in CLOSED and j not in K else '')
printed=set()
def rec(i,d):
    kids=sorted({int(y) for y in q.nbrs(g,i) if int(y) in DOM},key=lambda j:-sub(j))
    for j in kids:
        s=sub(j)
        if s<MIN: continue
        print("  "*d+f"{s:4d} [{tag(j)}] {q.names[j]}  ({q.locs[j][0].rsplit('/',1)[-1]}:{q.locs[j][1]}-{q.locs[j][2]})"+(" (seen)" if j in printed else ""))
        if j in printed or d+1>=DEP: continue
        printed.add(j); rec(j,d+1)
r=[i for i,n in enumerate(q.names) if n==R] or q.resolve(R); r=r[0]; print(q.names[r], sub(r)); rec(r,0)
