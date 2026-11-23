"""gc_excl.py NAME...: for a set of roots, the joint exclusive set on the live exact-edge graph
(theorems reachable from riemannHypothesis only through the roots) and each root's own exclusive set.
Writes /home/claude/idx/gc_excl_<tag>.pkl with tag = first arg of -t (default 'set')."""
import sys
tag='set'
args=sys.argv[1:]
if args and args[0]=='-t': tag=args[1]; args=args[2:]
sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np, pickle
ptr,d=q.graph("fwd")
def reach(starts,ban):
    seen=np.zeros(len(q.names),bool); st=[s for s in starts if s not in ban]
    for s in st: seen[s]=True
    while st:
        x=st.pop()
        for y in d[ptr[x]:ptr[x+1]]:
            if not seen[y] and int(y) not in ban: seen[y]=True; st.append(int(y))
    return seen
th=lambda m: sum(1 for i in np.nonzero(m)[0] if q.kinds[i] in('theorem','lemma'))
ids=[]
for a in args:
    r=[i for i,n in enumerate(q.names) if n==a] or q.resolve(a)
    ids.append(r[0]); 
L=np.load('/home/claude/idx/gc_live.npy')
out={}
for a,i in zip(args,ids):
    cl=reach([i],set()); ex=cl & ~reach([q.ROOT],{i})
    out[q.names[i]]=np.nonzero(ex)[0]
    print(f"{q.names[i]}: live={bool(L[i])} closure {th(cl)} thm, exclusive {th(ex)} thm")
U=reach(ids,set()); J=U & ~reach([q.ROOT],set(ids))
print("joint exclusive:",th(J),"thm,",J.sum(),"decls")
out['__joint__']=np.nonzero(J)[0]
pickle.dump(out,open(f'/home/claude/idx/gc_excl_{tag}.pkl','wb'))
