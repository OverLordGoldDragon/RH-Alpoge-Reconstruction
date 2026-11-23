"""exclusive.py NAME...: for each NAME, theorems of its forward closure that are not reachable
from riemannHypothesis once NAME (and the redirect wrappers listed with it) is removed:
the material that only NAME's branch uses. Also the joint exclusive set of all NAMEs."""
import sys; args = sys.argv[1:]; sys.argv = ['q','x','x']
import q
from collections import deque
g = q.graph("fwd")
def reach(start, banned):
    seen = {start}; dq = deque([start])
    while dq:
        x = dq.popleft()
        for y in q.nbrs(g, x):
            y = int(y)
            if y not in seen and y not in banned: seen.add(y); dq.append(y)
    return seen
groups = [a.split(",") for a in args]
allban = set()
res = {}
for grp in groups:
    ids = set(q.resolve(n)[0] for n in grp)
    allban |= ids
    cl = set()
    for i in ids: cl |= reach(i, set())
    live_wo = reach(q.ROOT, ids)
    ex = {j for j in cl if j not in live_wo}
    res[grp[0]] = ex
    th = [j for j in ex if q.kinds[j] in ('theorem','lemma')]
    print(f"{grp[0]}: closure {len(cl)}, exclusive {len(ex)} decls, {len(th)} theorems")
    open('/home/claude/idx/excl_%s.txt' % grp[0].rsplit('.',1)[-1], 'w').write("\n".join(f"{q.names[j]}\t{q.kinds[j]}\t{q.locs[j][0]}:{q.locs[j][1]}-{q.locs[j][2]}" for j in sorted(ex, key=lambda j: q.names[j])))
cl = set()
for grp in groups:
    for n in grp: cl |= reach(q.resolve(n)[0], set())
live_wo = reach(q.ROOT, allban)
ex = {j for j in cl if j not in live_wo}
print("joint exclusive:", len(ex), "decls,", sum(1 for j in ex if q.kinds[j] in ('theorem','lemma')), "theorems")
open('/home/claude/idx/excl_joint.txt', 'w').write("\n".join(f"{q.names[j]}\t{q.kinds[j]}\t{q.locs[j][0]}:{q.locs[j][1]}-{q.locs[j][2]}" for j in sorted(ex, key=lambda j: q.names[j])))
