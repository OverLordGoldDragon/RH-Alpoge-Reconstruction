"""kl_where.py NAME...: closure size (theorems) and membership in each block's exclusive set and joint exclusive set."""
import sys; args = sys.argv[1:]; sys.argv = ['q','x','x']
import q
g = q.graph("fwd")
sets = {}
for F in ['bwit_exists_alt','colSide_alt','clsPinD_of_famCol_of_trueW','joint']:
    sets[F] = set(l.split('\t')[0] for l in open('/home/claude/idx/excl_%s.txt' % F))
for a in args:
    r = q.resolve(a)
    if not r: print("??", a); continue
    i = r[0]; prev, _ = q.bfs(g, i)
    cl = [j for j in prev if q.kinds[j] in ('theorem','lemma')]
    mem = [F for F in sets if q.names[i] in sets[F]]
    inj = sum(1 for j in cl if q.names[j] in sets['joint'])
    print(f"{q.names[i]}: closure {len(cl)} thm; exclusive-in {mem}; closure∩joint-exclusive {inj}")
