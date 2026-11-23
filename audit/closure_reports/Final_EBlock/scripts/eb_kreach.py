"""eb_kreach.py: reachability (exact edges, full forward closure) of the K-a/K-b/K-c support roots from each E-head and block top,
and whether each root lies in the joint exclusive set J of the three PC4.13 blocks."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q
g=q.graph("fwd")
K=['Formalism.L2.Ker.Cd.IntegralLatticeDensity.rational_integrality_link','Formalism.L2.GlobalTheoryTheory.IntegralLatticeDensity.rational_integrality_link',
'Formalism.L2.Ker.Cd.IntegralLatticeDensity.hermitian_form_integral_values','Formalism.L2.GlobalTheoryTheory.IntegralLatticeDensity.hermitian_form_integral_values',
'Formalism.L2.Ker.Cd.IntegralLatticeDensity.SO.stdOK','Formalism.L2.GlobalTheoryTheory.IntegralLatticeDensity.SO.stdOK',
'Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.SquareSplitPairs.sqSplit_of','Formalism.L2.PairingIndexBounds.Eq.SquareSplitPairs.sqSplit_of',
'Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.Mu.muOneL_of','Formalism.L2.PairingIndexBounds.Eq.Mu.muOneL_of',
'Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.Mu.muOneR_of','Formalism.L2.PairingIndexBounds.Eq.Mu.muOneR_of']
Kid=[q.names.index(k) for k in K]
J=set(l.split('\t')[0] for l in open('/home/claude/idx/excl_joint.txt'))
TOPS={'E1a kernel_identity_tuple':'GlobalTheory.KerTup.kernel_identity_tuple','E1c lev_law':'GlobalTheory.AdForm.LevLaw.lev_law','E1 clsKL_is':'GlobalTheory.KerLaws.clsKL_is',
'E2':'GlobalTheory.AdForm.exists_clsT_of_pinTop','E3':'GlobalTheory.AdForm.JetScales.exists_jetS','E4':'GlobalTheory.AdForm.realOf_is','E5':'GlobalTheory.AdForm.exists_readsG_of_level',
'clsPinD top':'GlobalTheory.AdForm.clsPinD_of_famCol_of_trueW','bwit':'bwit_exists_alt','colSide':'colSide_alt'}
print("roots in J:",[ (k.split('.')[-1], k.split('.')[2], k in J) for k in K])
for lab,n in TOPS.items():
    r=q.resolve(n)[0]; prev,_=q.bfs(g,r)
    print(f"{lab:26s}", ''.join('X' if i in prev else '.' for i in Kid))
