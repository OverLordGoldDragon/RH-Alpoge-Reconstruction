"""fresh.py TARGET [EXCLUDE...]: closure of TARGET minus the union of closures of every
declaration named in an earlier report (resolved by exact name or unique suffix),
excluding the target's own residual producers listed after it."""
import sys; args = sys.argv[1:]; sys.argv = ['q','x','x']
import q
from collections import defaultdict, deque
target, excl = args[0], set(args[1:])
names = [l.strip() for l in open('/home/claude/idx/report_names.txt') if l.strip()]
last = defaultdict(list)
for i, n in enumerate(q.names): last[n.rsplit('.',1)[-1]].append(i)
full = {n: i for i, n in enumerate(q.names)}
seeds = set()
for n in names:
    if n in full: seeds.add(full[n]); continue
    cand = [i for i in last.get(n.rsplit('.',1)[-1], []) if q.names[i].endswith(n)]
    if len(cand) == 1: seeds.add(cand[0])
g = q.graph("fwd")
tid = q.resolve(target)[0]
tclos, _ = q.bfs(g, tid)
exids = set()
for e in excl:
    exids |= set(q.resolve(e))
seeds = {s for s in seeds if s not in exids and s != tid and s in tclos}
# union closure of seeds, not passing through excluded nodes
seen = set(); dq = deque(seeds); seen |= seeds
while dq:
    x = dq.popleft()
    for y in q.nbrs(g, x):
        y = int(y)
        if y not in seen and y not in exids and y != tid:
            seen.add(y); dq.append(y)
fresh = [j for j in tclos if j not in seen]
th = [j for j in fresh if q.kinds[j] in ('theorem','lemma')]
print("closure", len(tclos), "covered by earlier-report seeds", len(set(tclos) & seen), "fresh", len(fresh), "fresh theorems", len(th))
import collections
c = collections.Counter(q.locs[j][0].rsplit('/',1)[0] for j in th)
for d, n in c.most_common(25): print(f"{n:6d} {d}")
open('/home/claude/idx/fresh_%s.txt' % target.rsplit('.',1)[-1], 'w').write("\n".join(f"{q.names[j]}\t{q.kinds[j]}\t{q.locs[j][0]}:{q.locs[j][1]}" for j in sorted(fresh, key=lambda j: q.names[j])))
