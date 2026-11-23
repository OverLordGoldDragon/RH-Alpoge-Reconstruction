"""gc_shared.py: characterize live declarations whose nearest report-cited dominator is the top of the route
(depth <= 3, i.e. riemannHypothesis/rhOfAll/allChi/everyCharacter): kinds, top namespaces, Published layer."""
import sys, pickle; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
from collections import Counter
L=np.load('/home/claude/idx/gc_live.npy'); lab=np.load('/home/claude/idx/gc_comp.npy'); dep=np.load('/home/claude/idx/gc_cdepth.npy'); near=np.load('/home/claude/idx/gc_attr.npy')
live=np.nonzero(L)[0]
top=[i for i in live if dep[near[lab[i]]]<=3]
k=Counter(q.kinds[i] for i in top); print("top-dominated:",len(top),dict(k))
ns=Counter('.'.join(q.names[i].split('.')[:2]) for i in top if q.kinds[i] in('theorem','lemma'))
print("top namespaces (theorems):",ns.most_common(25))
pub=[i for i in top if '.Published.' in q.names[i] or q.names[i].startswith('Published.')]
print("Published.* among them:",len(pub))
dirs=Counter('/'.join(q.locs[i][0].split('/')[:2]) for i in top if q.kinds[i] in('theorem','lemma')); print("dirs:",dirs.most_common(15))
pickle.dump(top,open('/home/claude/idx/gc_top.pkl','wb'))
