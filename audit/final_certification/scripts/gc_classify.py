"""gc_classify.py: one status for every live declaration (exact-edge graph rooted at riemannHypothesis).
Priority:
 E   EXTERNAL       Published statement definitions, theorems proving a Published statement, and the Layer-3 region
                    (material reachable from the root only through those proofs).
 C   CLOSED         reconstructed by this author: Final_EBlock union, Final_WBlock union (incl. K-a/K-b/K-c),
                    D5/D7/D8/D9/ramBijective_holds joint exclusive set (checked in this certification), and the
                    named upstream inputs reconstructed in the certification report.
 P   CLOSED VIA PRIOR PACKAGE
     P1 declaration-level evidence: kernel-law closure (Final_Kernel_Law), Final_D123 classes, the exclusive sets of
        the three PC4.13 tops (Final_Internal_Cleanup, Final_Level_Leaves, Final_D2_Rebasing, PC-4 R4-A..C);
     P2 package attribution: nearest dominating theorem that a report cites lies below the top of the route
        (depth >= 4 in the dominator tree); the package is the one of that report.
 D   DEFINITION     non-theorem declarations (def/abbrev/structure/class/inductive/instance) not otherwise owned:
                    no propositional content of their own.
 R   RESIDUAL       live theorems not covered above: shared material whose only cited dominators are
                    riemannHypothesis/rhOfAll/allChi/everyCharacter (ownership not evidenced).
Writes Global_Ownership.tsv.gz, Global_Residuals.tsv.gz, counts."""
import sys, pickle, csv, gzip; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
from collections import Counter, deque
OUT='/home/claude/gcert/out/'
L=np.load('/home/claude/idx/gc_live.npy'); lab=np.load('/home/claude/idx/gc_comp.npy'); idom=np.load('/home/claude/idx/gc_cidom.npy'); dep=np.load('/home/claude/idx/gc_cdepth.npy')
named=pickle.load(open('/home/claude/idx/gc_named.pkl','rb')); N={n:i for i,n in enumerate(q.names)}
istheo=lambda i: q.kinds[i] in('theorem','lemma')
live=np.nonzero(L)[0]; n=len(q.names)
status=np.array(['']*n,dtype=object); owner=np.array(['']*n,dtype=object)
def setS(ids,s,o):
    for i in ids:
        i=int(i)
        if L[i] and status[i]=='': status[i]=s; owner[i]=o
# E
l3=pickle.load(open('/home/claude/idx/gc_layer3.pkl','rb'))
setS(l3['pubdefs'],'EXTERNAL','Published statement')
setS(l3['proofs'],'EXTERNAL','proof of a Published statement (Layer 3)')
setS(l3['layer3'],'EXTERNAL','Layer 3: used only to prove Published statements')
# C
for r in csv.reader(open('/home/claude/eblock/eb_classes.tsv'),delimiter='\t'):
    if r[0] in N: setS([N[r[0]]],'CLOSED','Final_EBlock '+r[4][:3].strip())
for r in csv.reader(open('/home/claude/wblock/WBlock_Declaration_Classes.tsv'),delimiter='\t'):
    if r[0] in N: setS([N[r[0]]],'CLOSED','Final_WBlock '+r[4][:3].strip())
dag=pickle.load(open('/home/claude/idx/gc_excl_dagent.pkl','rb'))
setS(dag['__joint__'],'CLOSED','Final_Global_Certification: D5/D7/D8/D9/ramBijective (mechanism check)')
UPST=['split_pair_generation','GlobalTheory.Mem.TorsionDegree.finrank_torsionField_le','GlobalTheory.Mem.DiscRoot.discField_eq_torsionField',
'GlobalTheory.T.gaussianTwistedRealReading_entire_and_injective','GlobalTheory.LatVacSign.heisO_finRat_sign','GlobalTheory.WeilVacChar.vacuum_character',
'GlobalTheory.OrientedHeis.om_pureTensorO','GlobalTheory.MovedVac.vac_moved','GlobalTheory.T.gaussianReading_finiteRationalHeisenbergTranslate',
'GlobalTheory.Mem.Col2.ChExM.exists_charts','GlobalTheory.AtG.ramCols_true','GlobalTheory.QNF.nf_iff_matNF']
setS([N[x] for x in UPST if x in N],'CLOSED','Final_Global_Certification: upstream input reconstructed')
setS([N['GlobalTheory.Mem.TorsionRam.dvd_discr_torsionField']],'EXTERNAL','Neron-Ogg-Shafarevich criterion (new boundary row)')
# P1
P=pickle.load(open('/home/claude/idx/wb_sets.pkl','rb'))
Kleaf=set(pickle.load(open('/home/claude/idx/wb_K.pkl','rb')))
setS([i for i in P['LAW'] if i not in Kleaf],'CLOSED VIA PRIOR PACKAGE','Final_Kernel_Law')
for r in csv.reader(open('/home/claude/eblock/support/Claude_Audit_Core/Final_D123/D123_Declaration_Classes.tsv'),delimiter='\t'):
    if r[0] in N: setS([N[r[0]]],'CLOSED VIA PRIOR PACKAGE','Final_D123 '+r[-1])
for k,o in [('exBL_isLinked_prmR_alt','Final_Internal_Cleanup (record witness X2-X6, Prop. BW)'),('colSide_alt','PC4.13 R4-D: Final_Internal_Cleanup, Final_Level_Leaves, Final_D2_Rebasing, PC-4 R4-A..C'),('clsPinD_of_famCol_of_trueW','Final_EBlock (block top and wrappers)'),('joint','PC4.13 joint material (kernel law / E / W)')]:
    setS([N[l.strip()] for l in open('/home/claude/idx/wb_excl_%s.txt'%k) if l.strip() in N],'CLOSED VIA PRIOR PACKAGE',o)
# P2: nearest cited THEOREM dominator at depth >= 4
C=lab.max()+1; ct=np.full(C,-1,np.int64)
for i in named:
    if istheo(i) and lab[i]>=0 and dep[lab[i]]>=4: ct[lab[i]]=i
near=np.full(C,-1,np.int64)
for c in np.argsort(dep):
    if dep[c]<0: continue
    near[c]=ct[c] if ct[c]>=0 else (near[idom[c]] if idom[c]>=0 else -1)
for i in live:
    if status[i]=='' and istheo(i) and near[lab[i]]>=0:
        j=near[lab[i]]; status[i]='CLOSED VIA PRIOR PACKAGE'; owner[i]='region of '+q.names[j]+' ['+','.join(sorted(named[j]))[:120]+']'
for i in live:
    if status[i]=='' and not istheo(i): status[i]='DEFINITION'; owner[i]='definition/structure (no propositional content)'
for i in live:
    if status[i]=='': status[i]='RESIDUAL'; owner[i]='shared; only cited dominator is the top of the route'
cnt=Counter(status[i] for i in live); print("live",len(live)); print(dict(cnt))
cth=Counter(status[i] for i in live if istheo(i)); print("theorems:",dict(cth))
pickle.dump({'status':status,'owner':owner},open('/home/claude/idx/gc_status.pkl','wb'))
# shortest paths (BFS parents)
ptr,d=q.graph("fwd"); par=np.full(n,-1,np.int64); seen=np.zeros(n,bool); seen[q.ROOT]=True; dq=deque([q.ROOT])
while dq:
    x=dq.popleft()
    for y in d[ptr[x]:ptr[x+1]]:
        if not seen[y]: seen[y]=True; par[y]=x; dq.append(int(y))
np.save('/home/claude/idx/gc_par.npy',par)
def path(i):
    p=[]
    while i!=-1: p.append(q.names[i]); i=par[i]
    return ' > '.join(p[::-1])
with gzip.open(OUT+'Global_Ownership.tsv.gz','wt') as f:
    f.write("declaration\tkind\tfile:line\tstatus\towner_or_evidence\n")
    for i in live: f.write(f"{q.names[i]}\t{q.kinds[i]}\t{q.locs[i][0]}:{q.locs[i][1]}\t{status[i]}\t{owner[i]}\n")
with gzip.open(OUT+'Global_Residuals.tsv.gz','wt') as f:
    f.write("declaration\tkind\tfile:line\tshortest_path_from_riemannHypothesis\n")
    for i in live:
        if status[i]=='RESIDUAL': f.write(f"{q.names[i]}\t{q.kinds[i]}\t{q.locs[i][0]}:{q.locs[i][1]}\t{path(i)}\n")
