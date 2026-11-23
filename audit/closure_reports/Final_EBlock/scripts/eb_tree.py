"""eb_tree.py ROOT DEPTH MIN [dom]: tree of the sub-closure of ROOT inside dom
(dom = E (block exclusive), D (E + joint-only), or JO (joint-only part)), children sorted by size."""
import sys; R,DEP,MIN=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]); dom=sys.argv[4] if len(sys.argv)>4 else 'D'
sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q
from collections import deque
g=q.graph("fwd")
def load(F):
    S=set(l.split('\t')[0] for l in open('/home/claude/idx/excl_%s.txt'%F)); return set(i for i,n in enumerate(q.names) if n in S)
E=load('clsPinD_of_famCol_of_trueW'); BW=load('bwit_exists_alt'); CS=load('colSide_alt'); J=load('joint')
JO=J-BW-CS-E
DOM={'E':E,'D':E|JO,'JO':JO,'ALLJ':J|E}[dom]
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
printed=set()
def tag(j): return 'E' if j in E else ('J' if j in JO else ('bw' if j in BW else ('cs' if j in CS else '-')))
def rec(i,d):
    kids=sorted({int(y) for y in q.nbrs(g,i) if int(y) in DOM},key=lambda j:-sub(j))
    for j in kids:
        s=sub(j)
        if s<MIN: continue
        print("  "*d+f"{s:4d} [{tag(j)}] {q.names[j]}  ({q.locs[j][0].rsplit('/',1)[-1]}:{q.locs[j][1]}-{q.locs[j][2]})"+(" (seen)" if j in printed else ""))
        if j in printed or d+1>=DEP: continue
        printed.add(j); rec(j,d+1)
r=q.resolve(R)[0]; print(q.names[r], sub(r)); rec(r,0)
