"""wb_sets.py: W-block head sub-closures.
Block top B = Top.Bl.exBL_isLinked_prmR_alt (the cleanup's unit, which contains bwit_exists_alt).
Domain D = B-exclusive u joint-only (exclusive to the union of B, colSide_alt, clsPinD and to none of them).
Subtracted as already closed: the kernel-law closure (components K1-K6, K8 of kl_classify.py, taken in D),
the E-block union (Final_EBlock), and the D1-D3 union (Final_D123 classes)."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, pickle, csv
from collections import deque, OrderedDict
g=q.graph("fwd")
N={n:i for i,n in enumerate(q.names)}
ld=lambda k: set(N[l.strip()] for l in open('/home/claude/idx/wb_excl_%s.txt'%k) if l.strip())
B=ld('exBL_isLinked_prmR_alt'); BW=ld('bwit_exists_alt'); CS=ld('colSide_alt'); CL=ld('clsPinD_of_famCol_of_trueW'); J=ld('joint')
JO=J-B-CS-CL; D=B|JO
th=lambda S: sum(1 for j in S if q.kinds[j] in('theorem','lemma'))
def clos(ids,dom):
    seen=set(i for i in ids if i in dom)|set(ids); dq=deque(seen)
    while dq:
        x=dq.popleft()
        for y in q.nbrs(g,x):
            y=int(y)
            if y in dom and y not in seen: seen.add(y); dq.append(y)
    return seen
def ids(ns):
    out=[]
    for n in ns:
        r=[N[n]] if n in N else q.resolve(n)
        if r: out.append(r[0])
    return out
src=open('/home/claude/eblock/scripts/kl/kl_classify.py').read()
COMP=eval("OrderedDict("+src.split("COMP = OrderedDict(")[1].split("\nheads = [")[0].rstrip().rstrip(")")+")")
lawroots=[r for c,v in COMP.items() if not c.startswith('K7') for r in ids(v)]
LAW=clos(lawroots,D)-set(r for r in lawroots if r not in D)
EB=set(N[r[0]] for r in csv.reader(open('/home/claude/eblock/eb_classes.tsv'),delimiter='\t') if r[0] in N)
D123=set(N[r[0]] for r in csv.reader(open('/home/claude/eblock/support/Claude_Audit_Core/Final_D123/D123_Declaration_Classes.tsv'),delimiter='\t') if r[0] in N)
# the kernel-law pass also closed the X1 core hyps_of_isTw/chTh_ok_chi by reading it in full, except the
# normal-form leaf idxMatNF_of_isTw, which it moved to W1 (kl_heads.py, closed_extra and keep_leaf)
KLX1=clos(ids(['GlobalTheory.Mem.Col2.TC.RcHyp.hyps_of_isTw']),D)-clos(ids(['GlobalTheory.Mem.Col2.TC.RcHyp.idxMatNF_of_isTw']),D)
# the K-leaves K-a, K-b, K-c were left at statement level by that pass: they are NOT closed
KL=set(pickle.load(open('/home/claude/idx/wb_K.pkl','rb'))) if __import__('os').path.exists('/home/claude/idx/wb_K.pkl') else set()
CLOSED=(LAW|KLX1|EB|D123)-KL
HEADS=OrderedDict([
 ('W1',['GlobalTheory.Mem.R3.SelC.square_integrable_columns_of_witnesses']),
 ('W2',['GlobalTheory.Mem.Top.Bl.WPt.exists_pinned_spectral_data_compatible','GlobalTheory.Mem.Top.Bl.exists_kernel_spectral_data_at_witnesses']),
 ('W3',['GlobalTheory.T.reFace_zero_part_conventions_chosen_again']),
])
print("B-excl",th(B),"bwit-excl",th(BW),"joint-only",th(JO),"D",th(D),"law in D",th(LAW&D),"EB in D",th(EB&D),"D123 in D",th(D123&D))
res={}
for k,v in HEADS.items():
    i=ids(v); S=clos(i,D); R=S-CLOSED
    res[k]=(S,R)
    print(f"   K-leaf part {th(S&KL)}"); print(f"{k}: sub-closure {th(S)} (B-excl {th(S&B)}, joint-only {th(S&JO)}), closed-by-law {th(S&LAW)}, by-EBlock {th(S&EB)}, by-D123 {th(S&D123)}, remaining {th(R)}")
ks=list(HEADS)
print("overlaps of remaining:",[[th(res[a][1]&res[b][1]) for b in ks] for a in ks])
U=set().union(*[res[k][1] for k in ks]); print("unique remaining union",th(U),"sum",sum(th(res[k][1]) for k in ks))
pickle.dump({'res':{k:(sorted(a),sorted(b)) for k,(a,b) in res.items()},'B':sorted(B),'JO':sorted(JO),'LAW':sorted(LAW|KLX1),'EB':sorted(EB),'D123':sorted(D123)},open('/home/claude/idx/wb_sets.pkl','wb'))
