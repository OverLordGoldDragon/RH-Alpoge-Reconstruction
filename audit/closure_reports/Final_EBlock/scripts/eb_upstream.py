"""eb_upstream.py: for each upstream input used by the E-block, which exclusive set it lies in
(E, colSide, bwit, joint, or none = live through other routes) and which D-heads reach it."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q
g=q.graph("fwd")
sets={F:set(l.split('\t')[0] for l in open('/home/claude/idx/excl_%s.txt'%F)) for F in ['clsPinD_of_famCol_of_trueW','colSide_alt','bwit_exists_alt','joint']}
UP=['GlobalTheory.MovedVac.vac_moved','GlobalTheory.T.gaussianTwistedRealReading_entire_and_injective','GlobalTheory.WeilVacChar.vacuum_character',
'GlobalTheory.OrientedHeis.om_pureTensorO','GlobalTheory.Mem.Col2.ChExM.exists_charts','GlobalTheory.Mem.Col2.TopBase.topBase_ok',
'GlobalTheory.T.gaussianReading_finiteRationalHeisenbergTranslate','GlobalTheory.Mem.Col2.TC.laHyp_eSmooth_true',
'GlobalTheory.T.entryDatum_transport_badPrime_anyTuple','GlobalTheory.T.exists_tupleChain_adelicData']
DH={'D5':'GlobalTheory.AdForm.twS_ramL','D7a':'GlobalTheory.QVecJoin.step_mid','D7b':'GlobalTheory.QVecJoin.step_top','D8':'true_geometry_row_column_entry_alt','D9':'true_geometry_twist_value_alt'}
cl={k:q.bfs(g,q.resolve(v)[0])[0] for k,v in DH.items()}
for n in UP:
    r=[i for i,x in enumerate(q.names) if x==n] or q.resolve(n)
    if not r: print(n,'NOT FOUND'); continue
    i=r[0]; nm=q.names[i]
    where=[F for F,S in sets.items() if nm in S] or ['none (live via other routes)']
    print(f"{nm.rsplit('.',1)[-1]:52s} set={where}  D-heads reaching: {[k for k,c in cl.items() if i in c]}")
