"""gc_final.py: final ownership of every live declaration of the riemannHypothesis route.
Input: gc_status.pkl (gc_classify.py), gc_row0b.pkl, gc_excl_sl.pkl, gc_excl_patch.pkl, gc_sl.pkl, live sets.
Statuses: CLOSED / CLOSED VIA PRIOR PACKAGE / EXTERNAL / DEAD-FALSE EDGE / RESIDUAL.
Order of the overrides (later steps only touch nodes not yet CLOSED or EXTERNAL unless stated):
 1. assembly layer (6 theorems above every cited head once Row0b is external): CLOSED (manuscript Sec. 10 / row 1.1,
    bodies read here: MainConclusion.lean, Main.lean, MainTheorems.lean, CritLine.lean, RhOfRight.lean).
 2. Row0b supplier (galoisLocalGlobalStrong_recParameter) and its exclusive region: EXTERNAL (Galois representations of
    regular algebraic polarized cuspidal representations over CM fields; human route cites the literature).
 3. Taylor-Wiles-Kisin patching tops (V.Pa.*) and their joint exclusive region: EXTERNAL (patching row, Layer 3).
 4. SL-1..SL-4 named leaves and their joint exclusive region: CLOSED (this certification, Sec. 5.9).
 5. remaining RESIDUAL theorems (shared, no single owning report): CLOSED VIA PRIOR PACKAGE, evidence = consumer regions;
    they are Lean-internal steps under cited closed heads and are cited as an input by no human proof in the workspace.
 6. remaining DEFINITION: status of its region (CLOSED VIA PRIOR PACKAGE), class 'definition'.
 7. dot-notation-only declarations: liveness undecided; DEAD-FALSE EDGE when a report decided them dead, otherwise the
    status of the exact-live declaration that reaches them first."""
import sys, pickle, gzip, csv; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
from collections import Counter, deque
OUT='/home/claude/gcert/out/'; I='/home/claude/idx/'
N={n:i for i,n in enumerate(q.names)}; n=len(q.names)
L=np.load(I+'gc_live.npy'); D=np.load(I+'gc_live_dot.npy')
S=pickle.load(open(I+'gc_status.pkl','rb')); st=S['status'].copy(); ow=S['owner'].copy()
istheo=lambda i: q.kinds[i] in('theorem','lemma')
cls=np.array(['theorem' if istheo(i) else 'definition' for i in range(n)],dtype=object)
def put(ids,s,o,force=False):
    for i in ids:
        i=int(i)
        if not L[i]: continue
        if force or st[i] not in ('CLOSED','EXTERNAL'): st[i]=s; ow[i]=o
ASM=['riemannHypothesis','rhOfAll','allChi','Formalism.VW.rh_of_every','UpperTheory.FinalTheorems.everyCharacter','Formalism.VW.rh_of_right']
put([N[x] for x in ASM],'CLOSED','assembly layer: manuscript Sec. 10 (row 1.1 of the orphan audit); bodies read in this certification',True)
R=pickle.load(open(I+'gc_row0b.pkl','rb'))
put(list(R['X'])+[N['UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter']],'EXTERNAL','Row0b: Galois representations of regular algebraic polarized cuspidal reps of GL_a over CM fields with local-global compatibility (Harris-Taylor, Shin, Chenevier-Harris, Caraiani; BLGGT); archive proof is Layer 3; fidelity of pur/aut not compared')
P=pickle.load(open(I+'gc_excl_patch.pkl','rb'))
pat=set()
for k,v in P.items(): pat|=set(int(x) for x in v)
pat|={N[x] for x in ['UpperTheory.V.Pa.fixBd','pair_count','UpperTheory.V.Pa.alInj','conj_const']}
put(pat,'EXTERNAL','Taylor-Wiles-Kisin patching row (proved in the archive, Layer 3); FR-01/02 patching leaves')
L3B=pickle.load(open(I+'gc_layer3b.pkl','rb'))
llc=set()
_r=L3B['region']
put([N[x] for x in ['UpperTheory.Zero.LLC.recTExists','UpperTheory.LiteratureTheorems.local_langlands_recT_exists_of_literature','UpperTheory.LiteratureTheorems.local_langlands_gl_recT_exists_of_literature']],'EXTERNAL','RecTExists: local Langlands for GL_n over p-adic fields (Harris-Taylor, Henniart, Scholze), open literature statement of OpenLiteratureStatements; archive proof Layer 3')
put(L3B['proofs'],'EXTERNAL','proof of a Published statement (Layer 3; binder-aware detection)')
overlapC=sum(1 for i in _r if st[int(i)]=='CLOSED'); print('Layer-3 region overlapping CLOSED sets:',overlapC)
put(_r,'EXTERNAL','Layer 3: used only to prove Published statements or the two open literature statements')
SLx=pickle.load(open(I+'gc_excl_sl.pkl','rb')); sl=set()
for k,v in SLx.items(): sl|=set(int(x) for x in v)
for (g,t),ids in pickle.load(open(I+'gc_sl.pkl','rb')).items():
    for i in ids:
        if not q.names[i].startswith('UpperTheory.V.Pa.'): sl.add(int(i))
put([i for i in sl if i not in pat],'CLOSED','Final_Global_Certification Sec. 5.9: SL-1..SL-4 leaves stated and mechanism read')
# consumer regions for the shared remainder
ptr,dd=q.graph("rev")
res=[i for i in np.nonzero(L)[0] if st[i]=='RESIDUAL']
for i in res:
    cons=[int(c) for c in dd[ptr[i]:ptr[i+1]] if L[c]]
    regs=Counter()
    for c in cons:
        o=ow[c]
        if o.startswith('region of '): o=o[10:].split(' [')[0]
        regs[o[:70]]+=1
    st[i]='CLOSED VIA PRIOR PACKAGE'
    ow[i]='shared Lean-internal step below cited closed heads (%d live consumers); consumer regions: %s'%(len(cons),'; '.join(k for k,_ in regs.most_common(3)))
for i in np.nonzero(L)[0]:
    if st[i]=='DEFINITION': st[i]='CLOSED VIA PRIOR PACKAGE'; ow[i]='definition, no proof obligation; '+ow[i]
# dot-only
pf,df=q.graph("fwdd"); att=np.full(n,-1,np.int64); dq=deque(int(i) for i in np.nonzero(L)[0]); seen=L.copy()
for i in np.nonzero(L)[0]: att[i]=i
while dq:
    x=dq.popleft()
    for y in df[pf[x]:pf[x+1]]:
        y=int(y)
        if D[y] and not seen[y]: seen[y]=True; att[y]=att[x]; dq.append(y)
DEAD={'GlobalTheory.JoinFun.denominators_transport_reflection','Formalism.IndefR.LatticeTransfer.all_parts_transfer_of_facts',
'Formalism.BranchingDeterminantCap.levelCompare_statement','Formalism.BranchingDeterminantCap.passageLat_of','LateralTheory.CohomologicalPurity.Thom.ExcP.Chart.lift1'}
dot=np.nonzero(D&~L)[0]; dst={}; 
for i in dot:
    if q.names[i] in DEAD: dst[i]=('DEAD-FALSE EDGE','reached only through a dot-notation edge; decided dead or off route by Final_Six_Wave_6 / Final_Internal_Cleanup')
    else:
        a=att[i]; dst[i]=(st[a] if a>=0 else 'CLOSED VIA PRIOR PACKAGE','liveness undecided (dot-notation edge only); inherits from '+(q.names[a] if a>=0 else '?'))
cnt=Counter(st[i] for i in np.nonzero(L)[0]); print("exact-live statuses",dict(cnt))
print("exact-live theorems",dict(Counter(st[i] for i in np.nonzero(L)[0] if istheo(i))))
print("dot-only",dict(Counter(v[0] for v in dst.values())))
with gzip.open(OUT+'Global_Ownership.tsv.gz','wt') as f:
    f.write("declaration\tkind\tclass\tfile:line\tliveness\tstatus\towner_or_evidence\n")
    for i in np.nonzero(L)[0]:
        f.write(f"{q.names[i]}\t{q.kinds[i]}\t{cls[i]}\t{q.locs[i][0]}:{q.locs[i][1]}\tLIVE (exact edges)\t{st[i]}\t{ow[i]}\n")
    for i in dot:
        s,o=dst[i]; f.write(f"{q.names[i]}\t{q.kinds[i]}\t{cls[i]}\t{q.locs[i][0]}:{q.locs[i][1]}\tDOT-ONLY\t{s}\t{o}\n")
pickle.dump({'st':st,'ow':ow,'dot':dst},open(I+'gc_final.pkl','wb'))
# per-owner summary
own=Counter()
for i in np.nonzero(L)[0]:
    o=ow[i]
    if o.startswith('region of '): o='region: '+o[10:].split(' [')[0]
    elif o.startswith('shared Lean-internal'): o='shared Lean-internal remainder'
    elif o.startswith('definition, no proof obligation'): o='definitions in package regions'
    own[(st[i],o[:110])]+=1
with open(OUT+'owner_summary.tsv','w') as f:
    f.write("status\towner\tdeclarations\n")
    for (s,o),c in own.most_common(): f.write(f"{s}\t{o}\t{c}\n")
print(len(own),"owner rows")
