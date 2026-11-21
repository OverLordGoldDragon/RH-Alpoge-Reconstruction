# Audit records

This directory contains selected reconstruction and audit records documenting how the dependency structure of the argument was established. It is provenance. The public statement of the current state is [`../RECONSTRUCTION_STATUS.md`](../RECONSTRUCTION_STATUS.md), and the mathematical account is the manuscript [`../RH_Route_Notes.pdf`](../RH_Route_Notes.pdf).

The reports were prepared by Claude (Anthropic) as working reports for Jimmie Adriazola, during a sequence of reconstruction passes on 20 and 21 November 2026. In each pass one or more agents read proofs of the Lean archive as text, wrote them in ordinary mathematics down to classical statements or named published theorems, and recorded what remained unread. No report built or ran the archive, and no report is a kernel check or a verification of the archive.

## Current synthesis

These three files are the most recent audit state, and the public documents at the root of the repository follow them.

| File | Content |
|---|---|
| [`Post_Closure_Synthesis.pdf`](Post_Closure_Synthesis.pdf) | Synthesis after the final closure wave. Status questions (architecture, engines, remaining packages, boundary), risk audit, dependency corrections, and the verdict *reconstruction incomplete, medium internal packages remain* |
| [`Post_Closure_Internal_Residuals.md`](Post_Closure_Internal_Residuals.md) | The seven internal packages PC-1 to PC-7 and the small leaves SL-1 to SL-5, with Lean declarations, files and line numbers, what is closed above each, and its downstream chain |
| [`Post_Closure_Verification_Boundary.md`](Post_Closure_Verification_Boundary.md) | The named published theorems at which the reconstruction stops, priority checks V1 to V20, and the boundary by branch |

## Selected reports

The reports in [`selected_reports/`](selected_reports/) are a small subset of the full audit record, chosen because each documents a major mechanism or an important correction. Earlier reports that were superseded, scratch notes and handoff notes are not included.

| File | What it establishes |
|---|---|
| `01_Gain_Valuation_Mechanism.pdf` | The valuation mechanism behind the formal-group gain at an inert prime, the credit $\alpha p/(p^2-1)$ |
| `02_Loss_LPprime.pdf` | The three engines of `LPprime`, the Hecke nondegeneracy that bounds the loss |
| `03_DeepStR_Mean_Slope_Bound.pdf` | `DeepStR`, the uniform lower bound for mean volume slopes on deep covers |
| `04_DeepStR_Exact_Identity_at_Good_Primes.pdf` | The exact identity at good primes behind the level uniformity of `DeepStR` ($w=\zeta_p-1$, the sandwich, the Frobenius recursion), and the location of PC-1 and PC-2 |
| `05_Theorem_P_and_PuNZ_Order.pdf` | Theorem P and the radial identities, and the resolution of the `PuNZ` question that fixes the order `LinkS → PuNZ → MIstar2 → BesselId → LinkDIV, FrameF` |
| `06_P3core.pdf` | `P3core` and the local structure at reducible points, for the automorphy argument behind `VWin` |
| `07_Theorem_B_Interior.pdf` | The interior of Theorem B, its relay and case exponents |
| `08_Theorem_C_Interior.pdf` | The interior of Theorem C, its eight lemmas and the constant 32 |
| `09_Seesaw_FR10_FR12.pdf` | The seesaw value `valX` and $c_V$, the FR-10 integrality results and the FR-12 counting reductions |
| `10_Final_Authoritative_Synthesis.pdf` | The synthesis before the final closure wave, superseded by `Post_Closure_Synthesis.pdf` and kept for the record of the dependency corrections it introduced |

The selected reports were copied without change and keep their original titles. Their file names here were changed for readability. The mapping to the original report names is in [`../PACKAGE_REPORT.md`](../PACKAGE_REPORT.md).

## How to read them

- Lean names are in `typewriter`, and paths such as `GP/…`, `LLC/…` or `src/lean/src/…` refer to the directory layout of the archive (see [`../SOURCE_MANIFEST.md`](../SOURCE_MANIFEST.md)). Abbreviated prefixes are defined at the start of each report.
- The reports refer to other audit files (wave reports, dependency maps, earlier syntheses) by name. Those files are part of the internal record and are not included here.
- Labels such as AR-xx, FR-xx, PC-x and SL-x are bookkeeping identifiers of the audit. The current ones are PC-1 to PC-7 and SL-1 to SL-5.
- A later report supersedes an earlier one where they differ. In particular, each statement of status in a selected report is superseded by the current synthesis above.
