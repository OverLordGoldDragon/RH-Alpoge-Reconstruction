"""kl_sub.py EXCLFILE HEAD [HEAD...]: for each HEAD, its sub-closure inside the exclusive set EXCLFILE
(file stem as in excl_<stem>.txt); prints sizes, pairwise overlaps, and writes member lists."""
import sys; args = sys.argv[1:]; sys.argv = ['q','x','x']
import q
from collections import deque
F = args[0]; heads = args[1:]
ex = set(l.split('\t')[0] for l in open('/home/claude/idx/excl_%s.txt' % F))
fid = set(i for i, n in enumerate(q.names) if n in ex)
g = q.graph("fwd")
def sub(i):
    seen = {i}; dq = deque([i])
    while dq:
        x = dq.popleft()
        for y in q.nbrs(g, x):
            y = int(y)
            if y in fid and y not in seen: seen.add(y); dq.append(y)
    return seen
th = lambda S: sum(1 for j in S if q.kinds[j] in ('theorem','lemma'))
subs = {}
for h in heads:
    i = q.resolve(h)[0]; S = sub(i); subs[h] = S
    print(f"{h}: in-excl={i in fid} sub {len(S)} decls {th(S)} thm {sum(q.locs[j][2]-q.locs[j][1]+1 for j in S)} lines")
    open('/home/claude/kl/sub_%s.txt' % h.rsplit('.',1)[-1], 'w').write("\n".join(f"{q.names[j]}\t{q.kinds[j]}\t{q.locs[j][0]}:{q.locs[j][1]}-{q.locs[j][2]}" for j in sorted(S, key=lambda j: q.locs[j])))
ks = list(subs)
for a in range(len(ks)):
    for b in range(a+1, len(ks)):
        print("overlap", ks[a].rsplit('.',1)[-1], ks[b].rsplit('.',1)[-1], th(subs[ks[a]] & subs[ks[b]]))
