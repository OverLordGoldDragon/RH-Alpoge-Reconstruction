# Scripts of the final internal cleanup

Run from any directory; paths at the top of each script point at the unpacked archive
(`/home/claude/lean_src/lean/src`) and the index folder (`/home/claude/idx`). Edit them for another machine.

1. `index_decls.py ROOT OUTPREFIX W NW` writes one TSV per worker: name, kind, file, lines, namespace, opens, identifier tokens.
2. `rg` line for private declarations (in the report, Section 2) writes `private.txt`.
3. `build_graph.py TSV... OUTPREFIX` resolves tokens to declarations (namespaces, own-name prefix, opens, `_root_`, trailing projections, privacy) and writes exact and dot-notation edge arrays.
4. `q.py` (show, find, deps, rdeps, live, closure, rclosure), `why.py A B` (which token of A resolves to B, and whether it is a local binder), `pathcheck.py NAME` (witness path with every edge explained), `liveavoid.py`, `rcl_exact.py`.
5. `live_batch.py`, `closures.py`, `overlap.py`, `exclusive.py`, `excltree.py`, `fresh.py`, `freshtree.py`, `brief.py`, `r4d_split.py` produce the liveness table, closure sizes and the exclusive residual heads.
6. `sl6_constants_check.py` checks the constants of SL-6a and SL-6b (needs sympy and mpmath).
