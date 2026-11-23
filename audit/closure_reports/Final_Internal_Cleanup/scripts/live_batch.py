import sys; sys.argv=['q','x','x']
import q
ids_all = {}
cands = sys.stdin.read().split()
g = q.graph("fwd")
prev, _ = q.bfs(g, q.ROOT)
print("exact forward live set:", len(prev))
gd = q.graph("fwdd")
prevd, _ = q.bfs(gd, q.ROOT)
print("exact+dot forward live set:", len(prevd))
import pickle
pickle.dump((set(prev), set(prevd)), open('/home/claude/idx/liveset.pkl','wb'))
for c in cands:
    for i in q.resolve(c):
        s = "EXACT-LIVE" if i in prev else ("DOT-LIVE" if i in prevd else "NOT-REACHED")
        print(s, q.names[i], "%s:%d" % q.locs[i][:2])
