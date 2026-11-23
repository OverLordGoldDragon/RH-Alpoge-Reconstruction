import sys; args = sys.argv[1:]; sys.argv = ['q','x','x']
import q
g = q.graph("fwd")
for a in args:
    ids = q.resolve(a)
    if not ids: print("??", a); continue
    prev, _ = q.bfs(g, ids[0])
    # count only non-Mathlib-like (all are archive) decls; split by kind
    th = sum(1 for j in prev if q.kinds[j] in ("theorem","lemma"))
    print(f"{len(prev):8d} decls ({th:7d} theorems)  {a}")
