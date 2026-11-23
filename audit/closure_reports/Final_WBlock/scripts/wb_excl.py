"""wb_excl.py TOP...: exclusive set of each TOP (theorems of its forward closure that riemannHypothesis
cannot reach once TOP is removed) and the joint exclusive set of all TOPs. Writes /home/claude/idx/wb_excl_<k>.txt."""
import sys; args=sys.argv[1:]; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q
from collections import deque
g=q.graph("fwd")
def reach(s,ban):
    seen={s}; dq=deque([s])
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y not in seen and y not in ban: seen.add(y); dq.append(y)
    return seen
th=lambda S: sum(1 for j in S if q.kinds[j] in('theorem','lemma'))
ids=[q.resolve(a)[0] for a in args]
cls={}
for a,i in zip(args,ids):
    cl=reach(i,set()); cls[a]=cl
    lw_i=reach(q.ROOT,{i}); ex={j for j in cl if j not in lw_i}
    print(f"{q.names[i]}: closure {len(cl)}, exclusive {len(ex)} decls, {th(ex)} thm")
    open('/home/claude/idx/wb_excl_%s.txt'%a.rsplit('.',1)[-1],'w').write("\n".join(q.names[j] for j in ex))
U=set().union(*cls.values()); lw=reach(q.ROOT,set(ids)); J={j for j in U if j not in lw}
print("joint exclusive", len(J), th(J))
open('/home/claude/idx/wb_excl_joint.txt','w').write("\n".join(q.names[j] for j in J))
