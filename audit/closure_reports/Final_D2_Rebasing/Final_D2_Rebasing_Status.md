# Final_D2_Rebasing status (22 November 2026)

Continues `Final_Level_Leaves`. Scope: D2's two rebasing steps. Read-only on the project; nothing built or run in Lean.

## Result: D2 closed (94 theorems)
- `PenChart.exists_readsStd_alt` (51 new): ReadsLow → ReadsStd. Match the rational penultimate charts (one per tuple of rational-level classes at the twist primes) with the local orbits on the box quotients (one per local index), using Lemma 9(c) and Prop 3(i) of Final_D123. `dead/live` follows because a nonvanishing datum forces the chart to be good and its cosets to lie in local orbits.
- `Fam.readsOfStd_alt` (43 new): ReadsStd → Reads. Move each penultimate chart point by rational carriers r_P ∈ GL(O_{E,P}) with local image in the last level (density, Lemma 5 of Final_D123), via the transport of Lemma 7 of Final_Level_Leaves. The new ingredient `CplDead.xiCpl1_eq_zero_of_frames`: the coupling term vanishes identically before the move iff after, by periodicity of the rational penultimate finite sums (rational form of Prop 3(iv)).

## Heads
D1 0, D2 94 → 0, D3 0, D5 84, D7 76, D8 46, D9 28. R4-D distinct 327 → 233.
Total distinct residual in heads ≈ 980 → ≈ 890 (plus E1b's 102 shared and K-a..K-c 243, counted separately).

## Next
D5 (84): diamond operators at the level primes on ramified column forms (`ram_iff_scalar_ram` 54, `twTransAct` 17, `twS` assembly).

## Files
`Final_D2_Rebasing.tex/.pdf`, `scripts/d2r_final.py`.
