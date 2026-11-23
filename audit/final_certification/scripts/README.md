# Scripts of the final global internal certification

Order of execution (indexes in /home/claude/idx built by index_decls.py and build_graph.py from the Final_Internal_Cleanup tools; q.py is their query module):
1. gc_live.py: exact and dot-augmented live closures of riemannHypothesis (no depth cap).
2. gc_named.py: every declaration name cited in the workspace reports, resolved.
3. gc_dom2.py: SCC condensation and dominator tree; gc_attr.py: nearest cited dominator.
4. gc_layer3.py, gc_layer3b.py: Published statements, their proofs (header and binder-aware), Layer-3 regions.
5. gc_excl.py: per-root and joint exclusive sets (used for the D-agent set, the SL leaves and the patching tops).
6. gc_classify.py: first-pass status; gc_cut.py, gc_cut2.py: cut tests; gc_row0b.py: Row0b supplier region.
7. gc_sl.py, gc_sldump.py: SL-1..SL-4 leaves resolved and their statements dumped.
8. gc_final.py: final status of every declaration, Global_Ownership.tsv.gz, owner_summary.tsv.
9. gc_boundary.py: Global_External_Boundary.tsv, Global_Published_Statements.tsv; gc_stats.py: dag_stats.json.
