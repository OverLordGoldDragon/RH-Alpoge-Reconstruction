# W-block (W1–W3) and K-leaves: final W-side status table

22 November 2026. Written by Claude for Jimmie Adriazola, for the global internal sweep. Read-only on the project. Nothing built or run in Lean. No existing file, report, handoff or manuscript edited. Full report: `Final_WBlock.tex` / `.pdf` (11 pages). Same verified archive and graph as `Final_EBlock` (lean.tar.gz SHA-256 `9631b4f0…3f49c7fc`, manifest-checked).

## A. Verdict

**YES.** W1–W3 are closed at the human-proof boundary.

## B. Smallest set of propositions

| | proposition | theorems | heads |
|---|---|---|---|
| Q1 | Column record of the base tuple: record axioms from the kernel law, character-set criterion by central idempotents (Schur orthogonality), twisted normal form = matrix normal form over a DVR, column evaluation onto by the level projectors, step-zero majorant = weighted class sum (polarization) | 64 | W1 |
| Q2 | Integrality and split data of the Fock period lattices: (a) (√d/2)H integral on 𝔞Hom(N,N') by a trace argument, δ ≠ 0; (b) standard theta data; (c) common polarization of the four lattices of a square from a split idempotent mod n, Weil triple constant 1 on move triangles by sign data and −1 a norm mod 4e | 235 | W1 (shared with closed D6) |
| Q3 | Class-field pieces of the small field: Hilbert class field K(j), ray field, torsion field and twelfth root of Δ, compositum of K_Ψ; integers of the small field | 66 (+7 assembly) | W2 |
| Q4 | Joints of the standard character: local standard character at degree-one unramified places, chain character values, determinant lifts | 22 | W2 |
| Q5 | Conventions on zero parts are free: zero eigenspace ⇒ zero part, axioms and readings unchanged | 36 | W3 |

Relation: three separate arguments; one shared support block (Q2) between W1 and D6.

## C. Per-head table

| head | exact mathematical content | shared mechanism | external boundary | verdict |
|---|---|---|---|---|
| W1 | ∃ face data and column reading depending on the kernel entry t only, ∀ tied spectral datum with kernel t, square-integrable columns with compatible characters | Q1, Q2 (with D6), kernel law (closed) | Weil 1964 constants (F4-C1, already on boundary) | closed |
| W2 | (a) a tied spectral datum compatible with each weighted point; (b) its extension to a tied kernel datum with the joints of the standard character | Q3, Q4; host datum X4 (closed) | GlobalArtinReciprocity; WeberRayFieldSt (CM ray class fields) — both already on boundary | closed |
| W3 | re-choosing the face keeps pins, axioms, error identity and readings after resetting the zero-part scalars | Q5 | none | closed |

## D. Residual after the pass

W-block 0, K-leaves 0, E-block 0. Remaining internal heads on PC4.13: D5 (84), D7 (76), D8 (46), D9 (28) — 233 distinct, D-agent.

## E. Counts

- Per head: W1 299 (64 + K-leaves 235: K-a 105, K-b 41 beyond K-a, K-c 89 beyond both), W2 95 (73 + 22), W3 36.
- Unique union: 430 (no theorem in two heads). After: 0.
- Ledger before: W 195, K-leaves 243 counted separately.

## F. Transfer ledger

- To the D-agent: nothing (no W residual or K-leaf reached by D5, D7, D8, D9).
- External boundary: no new row. GlobalArtinReciprocity (PC-6), WeberRayFieldSt (Wave 6 CM rows), Weil 1964 (F4-C1).
- Upstream inputs outside PC4.13, not reopened: split_pair_generation, finrank_torsionField_le, dvd_discr_torsionField, discField_eq_torsionField, lvlE_lvlPr_V0E, AtG.ramCols_true, QNF.nf_iff_matNF, discNeZero.

## G. Final consequence

**NO.** W1–W3 no longer block the claim. With the E-block also closed, the only internal heads left on the PC4.13 construction are D5, D7, D8, D9.

## Adversarial priorities

Q2(c) (common polarization of a square, sign data of the move triangles), the ramification bound in Q3(iii), and the curve-ideal inclusion κ𝔞𝔞̄ ⊂ 𝔡⁻¹ in Q2(a): reconstructed from statements, trees and outer proofs, not line by line.

## Files

`Final_WBlock.tex/.pdf`, `Final_WBlock_Dependency_Map.md`, `Residual_Heads_After_WBlock.tsv`, `WBlock_Declaration_Classes.tsv`, `scripts/` (`wb_*.py`, importing `q.py` of the cleanup scripts).
