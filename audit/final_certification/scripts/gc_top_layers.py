import sys, pickle; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
from collections import deque
C=pickle.load(open('/home/claude/idx/gc_cut.pkl','rb')); H=set(C['H'].tolist()); A=set(C['above'])
named=pickle.load(open('/home/claude/idx/gc_named.pkl','rb'))
ptr,d=q.graph("fwd"); dist={q.ROOT:0}; dq=deque([q.ROOT])
while dq:
    x=dq.popleft()
    if x in H: continue
    for y in d[ptr[x]:ptr[x+1]]:
        y=int(y)
        if y not in dist: dist[y]=dist[x]+1; dq.append(y)
from collections import Counter
print(Counter(dist[i] for i in A).most_common(40))
for k in range(1,6):
    lay=[i for i in A if dist[i]==k]
    print("--- layer",k,len(lay))
    for i in lay[:40]: print("  ",q.names[i], q.locs[i][0])
