# E-block (class data, R4-E): status ledger

22 November 2026. Written by Claude for Jimmie Adriazola, for the final internal synthesis. Read-only on the project. Nothing built or run in Lean. No existing file, report, handoff or manuscript edited. The full report is `Final_EBlock.tex` / `.pdf` (16 pages) in this folder.

Sources: `lean.tar.gz` (SHA-256 `9631b4f0…3f49c7fc`, the Kernel Replay value) unpacked to 175,190 files, all matching the Kernel Replay per-file manifest. Supporting reports copied as one bundle `_transfer/eblock_support.tar.gz` (SHA-256 `f1d24484…236cf`). Graph rebuilt with the cleanup scripts: 1,066,087 declarations, 5,943,183 exact edges.

## A. Verdict

**YES.** E1–E5 are closed at the human-proof boundary.

## B. The smallest set of propositions

| | proposition | theorems | heads |
|---|---|---|---|
| M1 | Adelic Weil theta kernel at split places = jet of the classical datum kernel (Prop E), with three lemmas: structure of the half lattices (isotropy, integrality, self-duality), vacuum relations, finite Fourier expansion | 176 | E1 |
| M2 | Transport of the finite datum: each local factor is equivariant under moving the base point and locally constant, so the moved Schwartz–Bruhat datum equals the finite datum at the representative pair | 105 | E1 (E1a and E1c) |
| M3 | Level-pair law: the chart level groups act on the combined theta datum by their characters | 87 | E1 |
| M4 | Characters at determinant roots split into base, class and character-factor parts | 17 | E1 |
| M5 | Fock calculus: creation operators become holomorphic derivatives at 0; the compact groups act on pure tensors by substitution and determinant powers | 47 | E1, E3, E4 |
| M6 | Class points of a definite unitary group: finite double cosets with stabilizer orders, Gross's dictionary (vectors fixed by stabilizers up to the level character), class-sum formulas | 100 | E1, E2, E4, E5 |
| M7 | Branching at the top step: interlacing, equivariant nonzero lowering map, block form | 13 | E2, E4 |
| M8 | Existence of the twist datum (assembly of per-step charts) | 34 | E4 |
| A | assembly in the head bodies | 52 | all |

## C. Per-head table

| head | statement | shared mechanism | external boundary | verdict |
|---|---|---|---|---|
| E1 | kernel class datum satisfies `ClsK.Is` for every tuple, with ρ fixed first: kernel identity, level law, real-point law, class-sum values | M1, M2, M3, M4, M5, M6 | Weil-datum axioms (Weil 1964, Kudla), already on boundary | closed |
| E2 | top class datum satisfies `ClsT.Is`: class reps, invariance, period reading, tail identity | M6, M7 | branching rule (already on boundary) | closed |
| E3 | nonzero jet scales: Fock value at 0 = jet of the reading | M5(a) | none | closed |
| E4 | `realOf` satisfies the real-datum axioms | M8, M7, M5 | branching rule (already on boundary) | closed |
| E5 | level forms are read by class vectors | M6(b) | none | closed |

## D. Residual after the pass

E-block heads: 5 → 0. Remaining heads on the PC4.13 construction: W1, W2, W3 (195), D5, D7, D8, D9 (233 distinct). Kernel-law leaves K-a (Ker.Cd copy), K-b, K-c (243) counted separately and not part of the E-block.

## E. Counts

- Per head (with joint-only material): E1 443, E2 105, E3 35, E4 63, E5 29; sum 675.
- Unique union: 631 (469 block-exclusive + 162 joint-only). 44 theorems serve two heads; none serves three.
- Ledger before: 483 in heads + 102 shared (E1b). The 60 other joint-only theorems (twist-datum existence, chart double cosets) had not been counted.
- After: 0.

## F. Transfer ledger

- To the D-agent: nothing. 25 declarations under D5 and 3 under D8 are joint-only support outside their counted residuals (chart double cosets and level-character continuity, two transport residue lemmas, one top-point lemma). Reconstructed here (M6, M2, M8).
- Upstream inputs outside PC4.13 (not E-block residual): `MovedVac.vac_moved`, `gaussianTwistedRealReading_entire_and_injective`, `gaussianReading_finiteRationalHeisenbergTranslate`, `LatVacSign.heisO_finRat_sign`, `WeilVacChar.vacuum_character`, `OrientedHeis.om_pureTensorO`, `chart_exists`, `ChExM.exists_charts`, `laHyp_eSmooth_true`.
- External boundary: no new row.

## G. Final consequence

The E-block no longer blocks the claim. The claim is still blocked by W1–W3 and D5, D7, D8, D9 (about 428 distinct theorems) and rests on the separately counted kernel-law leaves.

## Where an adversarial pass should start

Proofs reconstructed from statements and dependency trees rather than read line by line: the integrality on the twisted halves (Lemma 1(c), `twO_selfDual`, `halfA_signTrace_isInteger`), the finite Fourier inversion (`four_expand`), the local-constancy moduli of the four transport files, and `reading_stab_inv`, `evz_decomp`, `tailTop_eq_of_pin`, `branching_true_columns`.

## Files

`Final_EBlock.tex/.pdf`, `Final_EBlock_Dependency_Map.md`, `Residual_Heads_After_EBlock.tsv`, `EBlock_Declaration_Classes.tsv` (every declaration of the union with heads, mechanism, set), `EBlock_Shared_Theorems.tsv`, `scripts/` (`eb_*.py`, importing `q.py` of the cleanup scripts).
