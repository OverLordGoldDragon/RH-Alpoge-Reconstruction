# Global live DAG summary (riemannHypothesis route)

22 November 2026. Final global internal certification, written by Claude for Jimmie Adriazola. Read-only on the project. Built from the verified Lean archive (`lean.tar.gz`, SHA-256 `9631b4f0…c7fc`) and the reports already in the workspace. The Lean kernel was not run.

## Root

`Main.lean`: `theorem riemannHypothesis : RiemannHypothesis := rhOfAll`.
`Supplements/Kernels/MainTheorems.lean`: `rhOfAll := Formalism.VW.rh_of_every allChi`, `allChi := UpperTheory.FinalTheorems.everyCharacter`.
`MainConclusion.lean`: `everyCharacter := everyCharacter_of_row galoisLocalGlobalStrong_recParameter`, and `everyCharacter_of_row h := every_character_of_literature_of_vWin ⟨h, recTExists, h⟩ (vwin_of_row h)`.

## Graph

| quantity | value |
|---|---|
| declarations indexed (project only, Mathlib not indexed) | 1,066,087 |
| live declarations, exact edges, no depth cap | 766,788 |
| of which theorems and lemmas | 622,409 |
| definitions, abbrevs, structures, classes, inductives, instances | 144,379 |
| live edges (exact) | 4,415,583 |
| live with dot-notation edges added | 868,718 |
| dot-notation-only (liveness undecided) | 101,930 |
| nodes in nontrivial strongly connected components (name-resolution artifacts) | 1,696 |
| depth of the dominator tree of the condensed graph | 49 |
| `sorry` / `axiom` declarations in the archive | 0 / 0 |

## Status of every exact-live declaration

| status | declarations | theorems |
|---|---|---|
| CLOSED | 4,506 | 3,608 |
| CLOSED VIA PRIOR PACKAGE | 631,740 | 511,065 |
| EXTERNAL | 130,542 | 107,736 |
| DEAD-FALSE EDGE | 0 | 0 |
| RESIDUAL | **0** | **0** |

Dot-notation-only declarations: 78,641 CLOSED VIA PRIOR PACKAGE, 22,664 EXTERNAL, 620 CLOSED, 5 DEAD-FALSE EDGE (all inherit the status of the exact-live declaration that first reaches them, except the five that Wave 6 or the cleanup decided dead).

## Evidence tiers inside CLOSED VIA PRIOR PACKAGE

| tier | declarations | evidence |
|---|---|---|
| P1 declaration level | 3,816 | Final_Kernel_Law closure (573), Final_D123 classes (1,607), PC4.13 exclusive sets (1,394), Final_Internal_Cleanup (233), Final_EBlock wrappers (9) |
| P2 package region | 128,446 | nearest dominating theorem cited by a report sits at dominator depth ≥ 8 (a specific package head) |
| P2 broad region | 285,664 | nearest cited dominator at depth 4 to 7 (an assembly theorem shared by several packages) |
| shared remainder | 93,682 | only cited dominator is the top; every root path passes through a cited closed head or the external boundary (cut test, 6 assembly theorems above the cut) |
| definitions | 120,132 | no proof obligation |

## EXTERNAL breakdown

| part | declarations |
|---|---|
| Published statement declarations | 449 |
| proofs of Published statements (Layer 3), header and binder-aware detection | 603 |
| Layer-3 regions (used only by those proofs or by the two open literature statements) | 74,605 |
| Row0b supplier region (Galois representations of RACSDC representations) | 53,918 |
| Taylor–Wiles–Kisin patching region | 963 |
| RecTExists (local Langlands for GL_n) suppliers | 3 |
| Néron–Ogg–Shafarevich (`dvd_discr_torsionField`) | 1 |

## Cut test

With H = every live theorem cited by a report at dominator depth ≥ 4, plus every theorem owned by this certification, plus the Row0b supplier, the theorems reachable from `riemannHypothesis` without entering H are exactly six: `riemannHypothesis`, `rhOfAll`, `allChi`, `Formalism.VW.rh_of_every`, `Formalism.VW.rh_of_right`, `UpperTheory.FinalTheorems.everyCharacter`. All six are read in full and are the assembly of manuscript Section 10. Without the Row0b supplier in H, 126,126 theorems are above the cut, all of them under `galoisLocalGlobalStrong_recParameter`.

## Files

`Global_Ownership.tsv.gz` (one row per declaration, 868,718 rows), `owner_summary.tsv`, `Global_External_Boundary.tsv`, `Global_Published_Statements.tsv`, `Global_Residuals.tsv` (empty, |R_internal| = 0), `Global_Residual_Reconciliation.tsv`, `dag_stats.json`, `scripts/`.
