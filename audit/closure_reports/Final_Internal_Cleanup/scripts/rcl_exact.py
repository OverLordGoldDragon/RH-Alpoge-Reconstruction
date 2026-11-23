import sys; T = sys.argv[1]; CAP = int(sys.argv[2]); sys.argv = ['q','x','x']
import q
g = q.graph("rev")
prev, hit = q.bfs(g, q.resolve(T)[0], {q.ROOT}, CAP)
if hit is not None: print("ROOT REACHED")
print("exact reverse closure", len(prev))
for j in list(prev)[:60]: print("  ", q.names[j], "%s:%d" % q.locs[j][:2])
