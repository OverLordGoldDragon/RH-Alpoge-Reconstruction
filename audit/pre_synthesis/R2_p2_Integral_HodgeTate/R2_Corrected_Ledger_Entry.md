# R-2 corrected external-ledger entry (integral Hodge–Tate at p = 2)

22 November 2026. Replaces rows FHT-2 and R-2 of `Pre_Synthesis_Audit/Final_External_Fidelity/Authoritative_External_Theorem_Ledger.md` and the p = 2 row of `Corrected_Source_Map.md`. The full argument is in `R2_p2_Integral_HodgeTate.pdf` in this folder. No existing file was edited.

Archive: `lean.tar.gz`, sha256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`. All 175,190 manifest hashes match.

## Replacement for row FHT-2

| ID | Lean statement | Mathematical content | Source | Match | Bridge | Status |
|---|---|---|---|---|---|---|
| FHT-2 | `FarguesHodgeTate` at p = 2. Clause (i) (v(κ) ≤ v(4)) is **never opened** on any route. The live cokernel bound is `coker_dlog_killed` (sharp, v(κ)^{p−1} ≤ v(p), all p, no external hypothesis), consumed by `dlog_lagrangian` → `exists_HTPoint` → `pointHT` → `PointHT` at κ = 4 (`IsCp`). Clause (ii) = `FarguesExact` is live through `dlog_lagrangian` (line 193 of `TateMapDualHomBidual.lean`). | (i) κ·ω ⊆ im α for \|κ\| ≤ \|2\|, hence for κ = 4. (ii) ker(α_G⊗O) = (ker(α_{G^D}⊗O))^⊥ under the ζ-normalized Weil pairing. Combined at the consumer: ker(α_{G^D}∘λ) is Lagrangian for the alternating form. | (i) none needed. (ii) Scholze–Weinstein, *Moduli of p-divisible groups*, Camb. J. Math. 1 (2013), Prop. 5.1.6(iii) (rational exactness over O_C, no p ≠ 2 hypothesis). | (i) internal, written in full. (ii) MATCH AFTER SHORT BRIDGE | (i) Lemmas 2–5 and Theorem 6 of the report (Legendre, nearly primitive elements, integrality, one level, Smith form). (ii) saturation lemma B-FHT.1 (Lemma 10), Proposition 11 (kernel orthogonality) and Proposition 12 (Lagrangian, rank count) | **Closed internally using published input** |

## Replacement for residual row R-2

| ID | Item | Status | Closes with |
|---|---|---|---|
| R-2 | integral Hodge–Tate at p = 2 on the PC-2 nefness route (and 2.A(ii) and the sandwich at ℓ = 2, which reach the same `PointHT`) | **CLOSED INTERNALLY USING PUBLISHED INPUT.** Closed at the human-proof boundary: YES. | Done. Cokernel bound proved from standard facts (Tate 1967, Messing LNM 264, Kaplansky 1949, Legendre). Kernel statement proved from SW 2013 Prop. 5.1.6(iii) by saturation. |

## Replacement for the p = 2 row of the corrected source map

| Use | Citation | Status |
|---|---|---|
| integral Hodge–Tate, p = 2, clause (i) | none needed. The archive's divided-power argument (report Theorem 6), credited to Alpöge and colleagues | closed |
| integral Hodge–Tate, p = 2, clause (ii) | P. Scholze, J. Weinstein, *Moduli of p-divisible groups*, Camb. J. Math. 1 (2013) 145–237, Prop. 5.1.6(iii), with the saturation lemma B-FHT.1 | closed mod print check |
| integral Hodge–Tate, p odd | Theorem 6 and Prop. 11 of the report cover all p. Fargues, Progr. Math. 262 (2008), Ch. II, Thm II.1.1 stays as printed confirmation | closed |

## Remaining items attached to R-2 (not gaps in the human proof)

1. Prop. 5.1.6(iii) was read through a page fetch of arXiv:1211.6357v2. Check it against the journal version, and check its proof at p = 2 (the paper treats p = 2 in Lemmas 4.2.2 and 4.2.6), with the other literature-verification entries.
2. The internal proof of `Published.PrismaticDieudonneHodge` (window and frame machinery) was not opened. The human route does not use it. Its published model is Anschütz–Le Bras, Forum Math. Pi 11 (2023), Thm 1.4.4 (= 4.6.10) with Rem. 1.4.2.
3. Freeness of ω_G at the PC-2 points comes from `lie_free_finite` in the semi-abelian torsion package, outside R-2.

## Corrections to earlier statements

- Ledger FHT-2 said clause (i) at p = 2 "needs a printed bound c with 2^c \| 4". It needs no printed bound. The archive proves the sharp bound \|κ\| ≤ \|2\| internally, and 4 is a weakening (v(4) = v(2)² ≤ v(2)).
- Ledger FHT-2 and Final External Fidelity §6 treat `FarguesHodgeTate` clause (i) as live. It is not opened anywhere. The live cokernel bound is `coker_dlog_killed`.
- Scholze–Weinstein §4.3 (Prop. 4.3.6) was listed as a candidate source. It does not settle p = 2 independently, because its proof for (C, O_C) is Fargues's Thm II.1.1. The usable SW statement is Prop. 5.1.6(iii).
- The interface item "`dlogLinear` = α_{G^D}, `muTate` = Tate twist" is checked against the definitions in `ToSpanSingletonConstGenInjective.lean` (lines 781, 938, 962, 1035, 1069, 1088). They are the standard objects.
