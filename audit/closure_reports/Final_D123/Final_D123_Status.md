# Final_D123 status (22 November 2026)

Continues `Final_Kernel_Law`. Scope: the tuple-construction heads D1, D2, D3 only. Read-only on the project; nothing built or run in Lean; no existing file edited.

## Answer
**YES, D1, D2 and D3 share one reusable mechanism**: the completion dictionary at a split prime of degree one (Proposition C). Under the matching conditions `AtTwist` (completion, additive character, tame and unramified characters, sign sg with sg^2 = 1), every rational object of the column data at P equals sigma_0 of the corresponding object of a p-adic chain over E_P, up to the sign sg^(v_P(det)·n): levels and characters, double cosets, test functions, volumes, deep finite sums and entries, representative systems.

- twist primes: used by all three heads (406 theorems; D1 281, D2 265, D3 143)
- G-places (standard representatives, symmetric chain): used again by D1 (Proposition C', 150 theorems)

The rest is assembly over places:
- D1: a rational theta datum factors over places; local combinations at disjoint split places multiply it by the local factors (Proposition F)
- D2: a reading is glued from matching local twist data, the representative system of Prop. C(v), and local Schrödinger data (Lemma L, Proposition R)
- D3: the level group is a restricted product; [U^up : U] = product of local indices = weight, so vol(U)·wt = vol(U^up) (Proposition V)

## Counts (theorems)
| | union | D1 | D2 (graph head readsLow) | D3 |
|---|---|---|---|---|
| graph closure | 1,397 | 741 | 453 | 516 |
| closed | 1,181 | 664 | 426 | 388 |
| left (leaves) | 216 | 77 | 27 | 128 |

Mechanism split of the closed set: C-tw 406, C-ty 150, L 130, A 495.

Ledger heads: D1 741 → 77, D2 571 (recount 533) → 99, D3 516 → 128. D7 83 → 76 and D9 43 → 28 collapse in part (those theorems lie inside the D1–D3 union). Counted without repetition, R4-D goes 1,681 → 517 and the total residual ≈ 2,335 → ≈ 1,170. (An earlier draft said ≈ 820; that subtracted shared theorems more than once.)

## Leaves left inside D1–D3
- L1 `Fam.ratDatum_dT_levelPrime_alt` (61): the level-prime datum phiT is rational
- L2 `PenLevPrime.uloc_le_of_std` (101) and L3 `PenLevTyp.uloc_le_alt` (27): one statement, tuple freeness of local penultimate levels where the readings do not twist
- L4 `AdForm.exists_twDat_baseStd` (27): adelic twist datum with standard base points
- D2 rebasing steps outside the graph head: `PenChart.exists_readsStd_alt` (50), `Fam.readsOfStd_alt` (42)

## Next pass
L2+L3 (128; D5 shares 97 theorems with L2), then the D2 rebasing steps (94), then L1 (61).

## Files
- `Final_D123.tex`, `Final_D123.pdf` (16 pages, no overfull boxes)
- `Residual_Heads_After_D123.tsv`
- `D123_Declaration_Classes.tsv` (every declaration of the union, heads and class)
- `scripts/d123_*.py` (import `q.py` of the cleanup scripts)
