import sys, pickle; sys.argv=['q','x','x']
sys.path.insert(0,'/home/claude/scripts')
import q
from collections import deque
g=q.graph("fwd")
th=lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
R=lambda n: q.resolve(n)[0]
ex=set(l.split('\t')[0] for l in open('/home/claude/idx/excl_colSide_alt.txt'))
E=set(i for i,n in enumerate(q.names) if n in ex)
C4=set(pickle.load(open('/home/claude/kl/d5_final.pkl','rb'))['C4'])
def clos(roots,A):
    seen=set(r for r in roots if r in A); dq=deque(seen)
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in A and y not in seen: seen.add(y); dq.append(y)
    return seen
H={'D7':['GlobalTheory.QVecJoin.step_mid','GlobalTheory.QVecJoin.step_top'],
   'D8':['GlobalTheory.T.true_geometry_row_column_entry_alt'],
   'D9':['GlobalTheory.T.true_geometry_twist_value_alt']}
S={h:clos([R(n) for n in v],E) for h,v in H.items()}
for h in S: print(h, th(S[h]), "open", th(S[h]-C4))
print("D7&D8",th(S['D7']&S['D8']-C4),"D7&D9",th(S['D7']&S['D9']-C4),"D8&D9",th(S['D8']&S['D9']-C4))
print("union open", th(set().union(*S.values())-C4))
pickle.dump({h:sorted(v) for h,v in S.items()},open('/home/claude/kl/d789.pkl','wb'))
A=set().union(*S.values())-C4
def cl(i):
    seen={i}; dq=deque([i])
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in A and y not in seen: seen.add(y); dq.append(y)
    return seen
seen=set()
def show(i,d):
    s=th(cl(i))
    if s<2 or i in seen or d>7: return
    seen.add(i); print("  "*d+f"{s:3d} {q.names[i]} [{q.locs[i][0].rsplit('/',1)[-1]}:{q.locs[i][1]}]")
    for y in sorted({int(y) for y in q.nbrs(g,i) if int(y) in A and int(y)!=i},key=lambda j:-th(cl(j))): show(y,d+1)
for h,v in H.items():
    print("=====",h)
    for n in v: show(R(n),0)
