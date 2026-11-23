"""gc_upstream.py: for each upstream input used by the PC4.13 blocks, a shortest live path from riemannHypothesis
that avoids the three PC4.13 tops, plus the in-degree of live consumers. Shows the package region it lies in."""
import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
from collections import deque
g=q.graph("fwd"); rv=q.graph("rev"); L=np.load('/home/claude/idx/gc_live.npy')
tops={q.resolve(n)[0] for n in ['Top.Bl.exBL_isLinked_prmR_alt','Fam.colSide_alt','clsPinD_of_famCol_of_trueW']}
UP=['split_pair_generation','GlobalTheory.Mem.TorsionDegree.finrank_torsionField_le','GlobalTheory.Mem.TorsionRam.dvd_discr_torsionField',
'GlobalTheory.Mem.DiscRoot.discField_eq_torsionField','GlobalTheory.T.gaussianTwistedRealReading_entire_and_injective','GlobalTheory.LatVacSign.heisO_finRat_sign',
'GlobalTheory.WeilVacChar.vacuum_character','GlobalTheory.OrientedHeis.om_pureTensorO','GlobalTheory.MovedVac.vac_moved',
'GlobalTheory.T.gaussianReading_finiteRationalHeisenbergTranslate','GlobalTheory.Mem.Col2.ChExM.exists_charts','GlobalTheory.AtG.ramCols_true','GlobalTheory.QNF.nf_iff_matNF','GlobalTheory.T.global_model_power_free']
for n in UP:
    r=[i for i,x in enumerate(q.names) if x==n] or q.resolve(n.rsplit('.',1)[-1]); t=r[0]
    prev={q.ROOT:-1}; dq=deque([q.ROOT]); hit=False
    while dq:
        x=dq.popleft()
        if x==t: hit=True; break
        for y in q.nbrs(g,x):
            y=int(y)
            if y not in prev and y not in tops: prev[y]=x; dq.append(y)
    cons=[int(y) for y in q.nbrs(rv,t) if L[int(y)]]
    p=q.path(prev,t) if hit else []
    print(f"== {q.names[t]}  live={bool(L[t])}  live consumers={len(cons)}  path avoiding PC4.13 tops: {'YES len '+str(len(p)) if hit else 'NO'}")
    if hit: print("   ", " -> ".join(q.names[j].rsplit('.',1)[-1] for j in p[:4]), " ... ", " -> ".join(q.names[j].rsplit('.',1)[-1] for j in p[-7:]))
