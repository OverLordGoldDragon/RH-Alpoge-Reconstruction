import sys, pickle; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q
SRC='/home/claude/lean_src/lean/src/'
out=pickle.load(open('/home/claude/idx/gc_sl.pkl','rb'))
grp=sys.argv[1] if False else None
import os
want=os.environ.get('G')
for (g,t),ids in out.items():
    if want and g!=want: continue
    for i in ids:
        f,a,b=q.locs[i]; lines=open(SRC+f,errors='replace').read().split('\n')
        body=lines[a-1:min(b,a+int(os.environ.get('N','14')))]
        print(f"##### {g} {q.names[i]} [{q.kinds[i]}] {f}:{a}-{b}")
        print('\n'.join(l[:220] for l in body))
