import sys; args = sys.argv[1:]; sys.argv = ['q','x','x']
import q
g = q.graph("fwd")
cl = {}
for a in args:
    prev, _ = q.bfs(g, q.resolve(a)[0])
    cl[a] = set(j for j in prev if q.kinds[j] in ('theorem','lemma'))
    print(len(cl[a]), a)
ks = list(cl)
for i in range(len(ks)):
    for j in range(i+1, len(ks)):
        print(len(cl[ks[i]] & cl[ks[j]]), "shared:", ks[i].rsplit('.',1)[-1], ks[j].rsplit('.',1)[-1])
