"""gc_stats.py: numbers for Global_Live_DAG_Summary.md."""
import sys, pickle, json; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
from collections import Counter
I='/home/claude/idx/'
L=np.load(I+'gc_live.npy'); D=np.load(I+'gc_live_dot.npy'); lab=np.load(I+'gc_comp.npy'); dep=np.load(I+'gc_cdepth.npy')
F=pickle.load(open(I+'gc_final.pkl','rb')); st=F['st']; ow=F['ow']
ptr,d=q.graph("fwd")
live=np.nonzero(L)[0]
E=sum(int(L[d[ptr[i]:ptr[i+1]]].sum()) for i in live)
out={'decls_indexed':len(q.names),'live':int(L.sum()),'live_dot':int(D.sum()),'dot_only':int((D&~L).sum()),'live_edges':E,
'kinds':dict(Counter(q.kinds[i] for i in live))}
cs=Counter(lab[i] for i in live); out['components']=len(cs); out['nontrivial_scc_nodes']=sum(c for c in cs.values() if c>1)
out['max_dom_depth']=int(max(dep[lab[i]] for i in live))
out['status']=dict(Counter(st[i] for i in live)); out['status_theorems']=dict(Counter(st[i] for i in live if q.kinds[i] in('theorem','lemma')))
sh=[i for i in live if ow[i].startswith('shared Lean-internal')]
nreg=Counter(ow[i].count(';')+1 for i in sh)
out['shared_remainder']=len(sh); out['shared_by_num_consumer_regions']=dict(nreg)
dirs=Counter(q.locs[i][0].split('/')[0] for i in live); out['top_dirs']=dict(dirs.most_common(12))
# external breakdown
eo=Counter(ow[i].split(':')[0][:60] for i in live if st[i]=='EXTERNAL'); out['external_breakdown']=dict(eo)
co=Counter(ow[i][:40] for i in live if st[i]=='CLOSED'); out['closed_breakdown']=dict(co)
json.dump(out,open('/home/claude/gcert/out/dag_stats.json','w'),indent=1,ensure_ascii=False); print(json.dumps(out,indent=1,ensure_ascii=False))
