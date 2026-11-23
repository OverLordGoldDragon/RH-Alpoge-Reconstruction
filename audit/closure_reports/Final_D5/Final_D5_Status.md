# Final_D5 status (22 November 2026)

Continues `Final_D2_Rebasing`. Scope: the remaining 84 theorems of D5 (`AdForm.twS_ramL`). Read-only on the project; nothing built or run in Lean.

## Result: D5 closed (181 theorems; 97 already closed with L2, 84 here)
Classical Γ1(p) mechanism, with forms as functions on lattice pairs (lattice + nonzero functional to F_T):
- Lemma R1: a vector is ramified at a pair P iff it is fixed by Stab(P) and its diamond sum Σ_s π(g_s)φ vanishes (vector fixed by Stab(P) = equivariant form on pairs).
- Lemma R2: right-translating a class representative by g_s (g_s·Q = s·Q) lands on the diamond chart point, so the adelic form's value is dilT(s,c)φ(dil(s,c)).
- Lemma R3: vanishing at representatives extends to all points (level components at level places lie in Stab(Q), χ trivial there, Stab(Q) = Stab(sQ)).
- Prop (ramification is local) = `ram_iff_scalar_ram` (54). Prop (Hecke combinations at level places act on column forms) = `twTransAct` (17). Assembly `twS`, `twS_ramL` (13).
- Uses the local fact `ramBijective_holds` (sOp is a finite translation combination and a bijection on ramified vectors), which lies outside all exclusive sets and is not counted.

## Heads
D5 84 → 0; D9 28 → 27 (one shared theorem). R4-D distinct 233 → 149 (D7 76, D8 46, D9 27).
Total distinct residual in heads ≈ 890 → ≈ 800 (plus E1b's 102 shared and K-a..K-c 243, counted separately).

## Files
`Final_D5.tex/.pdf`, `scripts/d5_final.py`.
