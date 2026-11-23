"""gc_layer3b.py: robust Layer-3 detection.  A live theorem is a proof of a published statement when its declared type,
read from its signature up to ':=', is a declaration in a namespace containing 'Published' (binders allowed), or is one of
the two open literature statements of OpenLiteratureStatements (UpperTheory.One.M.Row / UpperTheory.GalStar.Row0b and
UpperTheory.Zero.LLC.RecTExists).  The Layer-3 region is the joint exclusive set of these proofs, of the Row0b supplier
and of the patching tops."""
import sys, re, pickle; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
I='/home/claude/idx/'; SRC='/home/claude/lean_src/lean/src/'
L=np.load(I+'gc_live.npy'); N={n:i for i,n in enumerate(q.names)}
pubfull=set(q.names[i] for i in pickle.load(open(I+'gc_layer3.pkl','rb'))['pubdefs'])
pubshort=set(x.rsplit('.',1)[-1] for x in pubfull)
OPEN={'Row','Row0b','RecTExists'}
cache={}; proofs=[]; openp=[]
pat=re.compile(r":\s*(?:_root_\.)?([A-Za-z0-9_.'₀-₉]+)\s*:=\s*")
for i in np.nonzero(L)[0]:
    if q.kinds[i] not in('theorem','lemma'): continue
    f,a,b=q.locs[i]
    if f not in cache: cache[f]=open(SRC+f,errors='replace').read().split('\n')
    sig=" ".join(cache[f][a-1:min(b,a+12)])
    k=sig.find(':=')
    if k<0: continue
    m=pat.search(sig[:k+3])
    if not m: continue
    t=m.group(1)
    tail=t.rsplit('.',1)[-1]
    if ('Published' in t and tail in pubshort) or (t in pubfull):
        proofs.append(i)
    elif t in ('UpperTheory.One.M.Row','UpperTheory.Zero.LLC.RecTExists') or (tail in OPEN and ('LLC' in t or 'M.Row' in t or 'GalStar' in t)):
        openp.append(i)
print("proofs of Published statements:",len(proofs),"open-literature suppliers:",len(openp))
for i in openp[:20]: print("   open:",q.names[i])
ptr,d=q.graph("fwd")
def reach(starts,ban):
    seen=np.zeros(len(q.names),bool); st=[s for s in starts if not ban[s]]
    for s in st: seen[s]=True
    while st:
        x=st.pop()
        for y in d[ptr[x]:ptr[x+1]]:
            if not seen[y] and not ban[y]: seen[y]=True; st.append(int(y))
    return seen
P=pickle.load(open(I+'gc_excl_patch.pkl','rb'))
tops=set(proofs)|set(openp)|{N['UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter']}|{N[k] for k in P if k in N and k!='__joint__'}
ban=np.zeros(len(q.names),bool)
for t in tops: ban[t]=True
U=reach(list(tops),np.zeros(len(q.names),bool)); J=U & ~reach([q.ROOT],ban)
th=lambda m: sum(1 for i in np.nonzero(m)[0] if q.kinds[i] in('theorem','lemma'))
print("Layer-3 region (expanded):",th(J),"theorems,",int(J.sum()),"decls")
pickle.dump({'proofs':proofs,'open':openp,'tops':sorted(tops),'region':np.nonzero(J)[0]},open(I+'gc_layer3b.pkl','wb'))
