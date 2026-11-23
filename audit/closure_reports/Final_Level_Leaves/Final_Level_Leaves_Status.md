# Final_Level_Leaves status (22 November 2026)

Continues `Final_D123`. Scope: the four leaves L1–L4 left inside D1–D3. Read-only on the project; nothing built or run in Lean.

## Result: all four leaves closed (216 theorems)
- **L2** `PenLevPrime.uloc_le_of_std` (101): at a level prime the local level of any step level structure with base lattice Λ = {x : π_T | x_n} is the group acting trivially on Λ^∨/Λ (last row ≡ e_n mod ϖ at w), whatever its level functional (Lemma "discriminant"). Also closes 97 of D5's 181 theorems (`TwLev'`).
- **L3** `PenLevTyp.uloc_le_alt` (27): at a G-place where neither reading twists, an element supported there is in the level iff it is in the chart level of the base point's G-place cosets; those cosets are y0 + integral vectors for every reading.
- **L1** `Fam.ratDatum_dT_levelPrime_alt` (61): φ_T at base points = product over level-prime split points of indicators of the standard pairs; factorization over places gives the rational datum.
- **L4** `AdForm.exists_twDat_baseStd` (27): rebase the top base point by transport of structure along an adele supported at finitely many places.

## Heads
D1 77 → 0, D3 128 → 0, D2 99 → 94 (rebasing steps), D5 181 → 84. R4-D distinct 517 → 327.
Total distinct residual in heads ≈ 1,170 → ≈ 980 (plus E1b's 102 shared and K-a..K-c 243, counted separately).

## Correction
`Final_D123` first said ≈ 820 after its pass; the correct deduplicated figure is ≈ 1,170 (shared theorems had been subtracted more than once). The copy of `Final_D123` committed to the project has the corrected sentence.

## Next
D2 rebasing steps (94; first is the orbit form of Lemma 9(c) + Prop 3(i), second needs `CplDead.xiCpl1_eq_zero_of_frames`), D5 remainder (84), then D7/D8/D9 and the class data E1–E5.

## Files
`Final_Level_Leaves.tex/.pdf` (9 pages), `Residual_Heads_After_Level_Leaves.tsv`, `scripts/lvl_final.py`.
