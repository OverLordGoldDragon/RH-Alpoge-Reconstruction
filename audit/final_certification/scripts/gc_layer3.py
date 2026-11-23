"""gc_layer3.py: live 'Published' statements (Prop definitions in a namespace containing 'Published') and the live
theorems that prove exactly such a statement (source line 'theorem X : <Published statement> :='), plus the
Layer-3 region: theorems reachable from riemannHypothesis only through those proofs (joint exclusive set)."""
import sys, re, pickle; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
L=np.load('/home/claude/idx/gc_live.npy'); SRC='/home/claude/lean_src/lean/src/'
pubdefs=[i for i in np.nonzero(L)[0] if 'Published' in q.names[i] and q.kinds[i] in ('def','abbrev','structure','class')]
short=set(q.names[i].rsplit('.',1)[-1] for i in pubdefs); full=set(q.names[i] for i in pubdefs)
print("live Published statement declarations:",len(pubdefs))
proofs=[]
cache={}
for i in np.nonzero(L)[0]:
    if q.kinds[i] not in('theorem','lemma'): continue
    f,a,b=q.locs[i]
    if f not in cache: cache[f]=open(SRC+f,errors='replace').read().split('\n')
    head=" ".join(cache[f][a-1:min(b,a+2)])
    m=re.search(r"(?:theorem|lemma)\s+\S+\s*:\s*([^\s:=]+)\s*:=",head)
    if m:
        t=m.group(1).lstrip('@').replace('_root_.','')
        if t in full or t.rsplit('.',1)[-1] in short and 'Published' in t or (t in short and 'Published' in head):
            proofs.append(i)
print("live theorems proving a Published statement:",len(proofs))
ptr,d=q.graph("fwd")
def reach(starts,ban):
    seen=np.zeros(len(q.names),bool); st=[s for s in starts if s not in ban]
    for s in st: seen[s]=True
    while st:
        x=st.pop()
        for y in d[ptr[x]:ptr[x+1]]:
            if not seen[y] and int(y) not in ban: seen[y]=True; st.append(int(y))
    return seen
U=reach(proofs,set()); J=U & ~reach([q.ROOT],set(proofs))
th=lambda m: sum(1 for i in np.nonzero(m)[0] if q.kinds[i] in('theorem','lemma'))
print("Layer-3 region (exclusive to published-statement proofs):",th(J),"theorems,",int(J.sum()),"decls")
pickle.dump({'pubdefs':pubdefs,'proofs':proofs,'layer3':np.nonzero(J)[0]},open('/home/claude/idx/gc_layer3.pkl','wb'))
for i in proofs[:15]: print("  ",q.names[i])
