# Status

22 November 2026. This file is the current statement of the reconstruction state. It supersedes [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md) of 21 November 2026, which is kept as a historical record.

The proof being reconstructed is Alpöge's formally verified proof. This repository does not claim an independent proof of RH by the reconstruction author.

## 1. Current phase

The internal reconstruction phase is complete. The next phases are

1. the source-fidelity check of the external theorem boundary,
2. the reconciliation of the audit into the manuscript [`RH_Route_Notes.pdf`](RH_Route_Notes.pdf), which predates the final audit,
3. an independent line-by-line check of the resulting human proof.

## 2. Internal residual verdict

The final global internal certification pass started from the Lean declaration that proves `riemannHypothesis` and rebuilt the live dependency graph with no depth cap. It gave every live declaration one of four classes.

| Class | Declarations |
|---|---:|
| Closed | 4,506 |
| Closed via prior package | 631,740 |
| External | 130,542 |
| Residual | 0 |
| **Exact-edge live graph** | **766,788** |

The internal residual set is empty, `|R_internal| = 0`. Every live internal mathematical dependency has been reconstructed at the human-proof level, assigned to an already reconstructed package, or transferred to an explicit external theorem boundary.

## 3. The live graph

- The exact-edge live graph has 766,788 declarations, of which 622,409 are theorems.
- The archive has no `sorry` and no `axiom` declarations.
- Qualification on the graph extraction. About 102,000 further declarations are reached through dot-notation dependency edges. Their ownership is inherited from the declarations that reach them. They produce no internal residual, but the extraction method for these edges has not yet been documented in full.
- Evidence tiers. About 3,800 declarations are closed by a report that names them. About 379,000 are classed by region, since they lie under a package head that a report closed, and no report names them individually. Section 3 of the certification report states this inference.
- The certification did not run the Lean kernel.

## 4. Closed blocks

| Block | Status |
|---|---|
| PC-1 to PC-7 | closed internally, modulo explicit external inputs where they apply |
| D1 to D9 | closed |
| E1 to E5 | closed |
| W1 to W3 | closed |
| K-a, K-b, K-c | closed |
| `ramBijective_holds` | closed internally |
| R-1, doubling Siegel–Weil formula | closed after an explicit bridge |
| R-2, integral Hodge–Tate input at $p=2$ | closed internally, using Scholze–Weinstein (2013), Prop. 5.1.6(iii) |

The final pass also found items that were under-owned or lay upstream of several packages, and closed them. These are `split_pair_generation`, `ramBijective_holds`, the K-support leaves, `HidaSetting`, the small leaves SL-1 to SL-4, and the torsion-field inputs they need.

## 5. Remaining external-fidelity work

The source-fidelity check of the external theorem boundary is not complete.

- The largest external region identified by the final audit runs from `Row0b` to `galoisLocalGlobalStrong_recParameter`. It supplies the existence and local–global compatibility of Galois representations for regular algebraic polarized cuspidal representations over CM fields. The manuscript cites Harris–Taylor, Shin, Chenevier–Harris and Caraiani for it. This region has not yet had a detailed source-fidelity check.
- The certification added two external rows, the Taylor–Wiles–Kisin patching region and the Néron–Ogg–Shafarevich criterion (used by `dvd_discr_torsionField`). The full list of external declarations is [`audit/final_certification/Global_External_Boundary.tsv`](audit/final_certification/Global_External_Boundary.tsv).
- The rest of the boundary is listed in [`EXTERNAL_THEOREMS.md`](EXTERNAL_THEOREMS.md) as of 21 November 2026. The source-fidelity audit since then has matched, corrected or reclassified part of it, and has not covered all of it.

## 6. Reconstruction, formal certification and human verification

These are three different things.

| | What it is | State |
|---|---|---|
| Reconstruction | A human-readable account of the live internal route of Alpöge's formal proof, with a dependency audit. This is the work of this repository. | Internal phase complete. External fidelity and manuscript reconciliation outstanding. |
| Formal certification | A check of the Lean statement and proof. | Done by the Lean and Mathlib communities, joint statement of 21 November 2026 ([link](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)). This repository did not build or replay the archive. |
| Independent human verification | A line-by-line check of the human proof by mathematicians independent of the reconstruction. | Not done. |

## 7. Documents

- The manuscript [`RH_Route_Notes.pdf`](RH_Route_Notes.pdf) predates the final audit. Its Section 1.3 and Section 11 describe the state of 21 November 2026, when internal packages were still under audit.
- The final certification is in [`audit/final_certification/`](audit/final_certification/). [`Global_Residual_Reconciliation.tsv`](audit/final_certification/Global_Residual_Reconciliation.tsv) names, for each former residual, the report that closed it. Those reports are in [`audit/closure_reports/`](audit/closure_reports/) and [`audit/pre_synthesis/`](audit/pre_synthesis/).
- [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md), [`EXTERNAL_THEOREMS.md`](EXTERNAL_THEOREMS.md), [`PROOF_DEPENDENCY_MAP.md`](PROOF_DEPENDENCY_MAP.md) and the files in [`audit/`](audit/) are kept as records of the reconstruction and its corrections. Where they differ from this file, this file is more recent.
