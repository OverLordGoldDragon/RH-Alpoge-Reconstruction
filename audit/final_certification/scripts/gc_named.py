"""gc_named.py: every declaration name cited in the staged reports (and the E/W outputs), resolved on the graph.
Tokens: \\lean{...}, `...` code spans. A token resolves to a declaration if it equals a full name or is a unique
dotted suffix of one (suffixes shared by several declarations are kept as 'ambiguous' and resolved to all live matches).
Writes /home/claude/idx/gc_named.pkl: {decl_id: set(report files)}."""
import sys, re, os, glob, pickle, numpy as np
sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q
from collections import defaultdict
L=np.load('/home/claude/idx/gc_live.npy')
full={n:i for i,n in enumerate(q.names)}
suf=defaultdict(list)
for i,n in enumerate(q.names):
    parts=n.split('.')
    for k in range(1,min(len(parts),4)+1):
        suf['.'.join(parts[-k:])].append(i)
files=[f for f in glob.glob('/home/claude/eblock/support/**/*',recursive=True) if f.endswith(('.md','.tex','.tsv'))]
files+=glob.glob('/home/claude/eblock/out/Final_EBlock/*.*')+glob.glob('/home/claude/wblock/out/Final_WBlock/*.*')
files=[f for f in files if f.endswith(('.md','.tex','.tsv'))]
pat=re.compile(r"\\lean\{([^}]*)\}|`([^`\s]{3,200})`")
named=defaultdict(set); amb=0; tok_n=0
for f in files:
    s=open(f,errors='replace').read()
    toks=set()
    for m in pat.finditer(s):
        t=(m.group(1) or m.group(2)).strip().replace('\\_','_')
        t=t.split('(')[0].split(' ')[0].rstrip(',.;:')
        toks.add(t)
    if f.endswith('.tsv'):
        for line in s.split('\n'):
            c=line.split('\t')[0].strip()
            if c and '.' in c: toks.add(c)
    for t in toks:
        tok_n+=1
        if t in full: ids=[full[t]]
        else:
            ids=suf.get(t.lstrip('_root_.'),[])
            if len(ids)>1: amb+=1
            if len(ids)>40: ids=[]
        for i in ids:
            if L[i]: named[i].add(os.path.basename(f))
print("files",len(files),"tokens",tok_n,"ambiguous tokens",amb,"live named declarations",len(named))
pickle.dump(dict(named),open('/home/claude/idx/gc_named.pkl','wb'))
