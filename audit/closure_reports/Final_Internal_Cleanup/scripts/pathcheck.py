"""pathcheck.py NAME : forward exact path from riemannHypothesis to NAME, every edge explained."""
import sys, subprocess
name = sys.argv[1]
out = subprocess.run(["python3", "q.py", "live", name], capture_output=True, text=True).stdout.strip().split("\n")
nodes = [l.split()[0] for l in out]
if out[0].startswith("NOT"): print(out[0]); sys.exit()
for a, b in zip(nodes, nodes[1:]):
    print(a, "->", b)
    print(subprocess.run(["python3", "why.py", a, b], capture_output=True, text=True).stdout.rstrip())
