"""gc_attr.py: for every live declaration, its nearest dominator (on the condensed dominator tree) that contains
a report-cited declaration, and that dominator's depth. Shows how much live material is dominated only by
top-of-route nodes. Writes /home/claude/idx/gc_attr.npy (component id of nearest cited dominator, -1 if none)."""
import sys, pickle; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, numpy as np
from collections import Counter
L=np.load('/home/claude/idx/gc_live.npy'); lab=np.load('/home/claude/idx/gc_comp.npy'); idom=np.load('/home/claude/idx/gc_cidom.npy'); dep=np.load('/home/claude/idx/gc_cdepth.npy')
named=pickle.load(open('/home/claude/idx/gc_named.pkl','rb'))
C=lab.max()+1
cnamed=np.zeros(C,bool)
for i in named: 
    if lab[i]>=0: cnamed[lab[i]]=True
# nearest named strict-or-self dominator per component, processed by depth
near=np.full(C,-1,np.int64)
for c in np.argsort(dep):
    if dep[c]<0: continue
    if cnamed[c]: near[c]=c
    elif idom[c]>=0: near[c]=near[idom[c]]
live=np.nonzero(L)[0]
nd=dep[near[lab[live]]]
h=Counter(int(x) for x in nd)
print("live decls by depth of nearest cited dominator:", dict(sorted(h.items())))
np.save('/home/claude/idx/gc_attr.npy',near)
# route chain: names of cited components at depth <=6
rep={}
for i in named:
    c=lab[i]
    if c>=0 and dep[c]<=6: rep.setdefault(int(dep[c]),set()).add(q.names[i])
for k in sorted(rep): print(k, sorted(rep[k])[:12])
