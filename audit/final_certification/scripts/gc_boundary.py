"""gc_boundary.py: Global_External_Boundary.tsv (literature boundary, reconciled) and Global_Published_Statements.tsv
(the 449 live Published statement declarations with their live consumer counts)."""
import sys, re, pickle; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
SUP='/home/claude/eblock/support/'; OUT='/home/claude/gcert/out/'
rows=[]
def cells(l): return [c.strip() for c in l.strip().strip('|').split('|')]
# 1. authoritative ledger
txt=open(SUP+'Pre_Synthesis_Audit/Final_External_Fidelity/Authoritative_External_Theorem_Ledger.md').read().split('\n')
sec=None
for l in txt:
    if l.startswith('## 1.'): sec='L'
    elif l.startswith('## 2.'): sec='R'
    elif l.startswith('## 3.'): sec=None
    if sec and l.startswith('|') and not l.startswith('|---') and not l.startswith('| #') and not l.startswith('| id'):
        c=cells(l)
        if sec=='L' and len(c)>=8: rows.append([c[0],c[2][:300],c[3][:200],c[1][:250],c[5],c[7][:200],'Authoritative_External_Theorem_Ledger.md §1'])
        if sec=='R' and len(c)>=4: rows.append([c[0],c[1][:300],'',  '', c[2][:200],c[3][:250],'Authoritative_External_Theorem_Ledger.md §2'])
# 2. post-closure verification boundary (block tables)
blk=None
for l in open(SUP+'Claude_Audit_Core/Post_Closure_Synthesis/Post_Closure_Verification_Boundary.md').read().split('\n'):
    if l.startswith('#'): blk=l.strip('# ').strip()
    if l.startswith('|') and not l.startswith('|---') and not l.startswith('| Theorem') and not l.startswith('| #') and not l.startswith('| ID'):
        c=cells(l)
        if len(c)>=3: rows.append(['PCVB:'+blk[:30],c[0][:300],'',c[1][:250],c[2][:200],'','Post_Closure_Verification_Boundary.md'])
# 3. rows added or rebound by this certification
new=[
['GC-1','Galois representations attached to regular algebraic polarized (conjugate self-dual) cuspidal representations of GL_a over CM fields: continuity, semisimplicity, local-global compatibility away from l, Hodge-Tate weights, crystalline / de Rham / potentially semistable at l with Weil-Deligne compatibility (Row0b, fields away, weights, weights_conj, above.crys, above.nice)','Harris-Taylor 2001; Shin 2011; Chenevier-Harris 2013; Caraiani 2012, 2014; Barnet-Lamb-Gee-Geraghty-Taylor 2014','UpperTheory.GalStar.Row0b, supplied by UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter into UpperTheory.FinalTheorems.everyCharacter_of_row','not compared (PCVB Block D: clauses pur, aut); archive proves it internally through 42,645 exclusive theorems (Layer 3)','EXTERNAL; fidelity mandatory (pre-synthesis E(3)); HIGHEST priority for the literature campaign because the anchor carries the largest uncited region of the route','this certification (anchor binding new)'],
['GC-2','Neron-Ogg-Shafarevich criterion: an elliptic curve over a number field has good reduction at v not dividing m iff E[m] is unramified at v; hence Q(E[12]) is unramified outside 6 Delta','Serre-Tate 1968, Thm 1; Silverman AEC VII.7.1','GlobalTheory.Mem.TorsionRam.dvd_discr_torsionField','not compared; statement read here','EXTERNAL (new row)','this certification Sec. 5.2'],
['GC-3','Taylor-Wiles-Kisin patching and the FR-01/02 patching leaves (detFin, matFg, finSub, lift1, fixBd, pair_count, alInj, secondCohomologyBound_of_boundaryBound, conj_const, testEx)','Taylor-Wiles 1995; Kisin 2009; as cited in PCVB Block D','UpperTheory.V.Pa.pFromAut and children (960 exclusive declarations)','proved in the archive through litN (PCVB); Final_Internal_Cleanup: LIVE AND EXTERNAL (patching row)','EXTERNAL (Layer 3)','PCVB; Final_Internal_Cleanup; this certification'],
['GC-4','Existence of splitting characters / Weil data for unitary dual pairs given a Hecke character of the right parity','Kudla 1994; Harris-Kudla-Sweet 1996','KomExist.exists_compactOpen_alt (proved internally by WeilDatumExistence.weilDatumExists)','from memory in Final_Internal_Cleanup','EXTERNAL (row added by Final_Internal_Cleanup)','Final_Internal_Cleanup_Status.md D'],
['GC-5','Siegel-Weil in Weil convergent range for U(n,n) x U(V) (R-1)','Ichino 2007 (Math. Z. 255); Yamana bridge claimed','GlobalTheory.Published.SiegelWeilUnitaryConvergent (SW-D)','R-1 open in the workspace ledger; claimed CLOSED via a Yamana/Ichino bridge by a report that is not in the workspace','EXTERNAL; claimed closure not verified here','user brief; ledger §2'],
['GC-6','Integral Hodge-Tate at p = 2 with kappa = 4, both clauses (R-2)','Fargues 2008 excludes p = 2','FarguesHodgeTate at p = 2 (PC-2 Prop. 2.B route)','R-2 open in the workspace ledger; claimed CLOSED internally using published input by a report that is not in the workspace','EXTERNAL / internal reconstruction claimed; not verified here','user brief; ledger §2'],
['GC-7','Unramified-outside-S Galois action on 12-torsion and the Kummer theory of Delta^(1/12) (finrank_torsionField_le, discField_eq_torsionField)','classical (Serre, Silverman AEC III.8, Weil pairing)','GlobalTheory.Mem.TorsionDegree.finrank_torsionField_le; GlobalTheory.Mem.DiscRoot.discField_eq_torsionField','reconstructed here; no citation needed','CLOSED (not a boundary item); listed to separate it from GC-2','this certification Sec. 5.2'],
]
for r in new: rows.append(r)
with open(OUT+'Global_External_Boundary.tsv','w') as f:
    f.write("id\tmathematical_requirement\tsource\tlive_anchor\tmatch_or_fidelity\tverdict\tprovenance\n")
    for r in rows: f.write('\t'.join(x.replace('\t',' ').replace('\n',' ') for x in r)+'\n')
print("boundary rows",len(rows))
l3=pickle.load(open('/home/claude/idx/gc_layer3.pkl','rb')); L=np.load('/home/claude/idx/gc_live.npy')
ptr,d=q.graph("rev")
with open(OUT+'Global_Published_Statements.tsv','w') as f:
    f.write("declaration\tkind\tfile:line\tlive_consumers\tproved_in_archive_by\n")
    prf={}
    SRC='/home/claude/lean_src/lean/src/'
    for i in l3['proofs']:
        fl,a,b=q.locs[i]; h=open(SRC+fl,errors='replace').read().split('\n')[a-1]
        m=re.search(r":\s*([^\s:=]+)\s*:=",h)
        if m: prf.setdefault(m.group(1).split('.')[-1],[]).append(q.names[i])
    for i in l3['pubdefs']:
        c=sum(1 for x in d[ptr[i]:ptr[i+1]] if L[x])
        f.write(f"{q.names[i]}\t{q.kinds[i]}\t{q.locs[i][0]}:{q.locs[i][1]}\t{c}\t{'; '.join(prf.get(q.names[i].split('.')[-1],[])[:3])}\n")
