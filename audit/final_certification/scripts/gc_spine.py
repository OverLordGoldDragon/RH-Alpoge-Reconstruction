"""gc_spine.py: live declarations reachable from riemannHypothesis without passing THROUGH any report-named
declaration (named nodes are reached but not expanded). These are live and above every named node, so no report
covers them by name. Prints sizes by kind and the largest unnamed spine theorems by their own forward closure."""
import sys, pickle, numpy as np
sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q
from collections import Counter
named=pickle.load(open('/home/claude/idx/gc_named.pkl','rb'))
ptr,d=q.graph("fwd")
seen={q.ROOT}; stack=[q.ROOT]; frontier=set()
while stack:
    x=stack.pop()
    if x in named and x!=q.ROOT: frontier.add(x); continue
    for y in d[ptr[x]:ptr[x+1]]:
        y=int(y)
        if y not in seen: seen.add(y); stack.append(y)
spine=[i for i in seen if i not in named]
k=Counter(q.kinds[i] for i in spine)
print("spine (unnamed, above every named node):",len(spine),dict(k))
print("named frontier nodes:",len(frontier))
pickle.dump({'spine':spine,'frontier':sorted(frontier)},open('/home/claude/idx/gc_spine.pkl','wb'))
th=[i for i in spine if q.kinds[i] in('theorem','lemma')]
for i in sorted(th,key=lambda i:q.names[i])[:400]:
    print("  ",q.names[i],"%s:%d"%q.locs[i][:2])
