# R-2 dependency map (p = 2 integral Hodge–Tate)

Paths: AS = Development/AutomorphicSpectrum, AV = Development/AbelianVarietyTheory, WB = Development/WeilBound.

## Consumer chain (PC-2, Prop. 2.B(ii) at ℓ = 2)

```
or_m1nef                                   AS/Proofs/DivisibilityProofs/GoodTowerM1Nef.lean:19
  FarguesHodgeTate := hG.2.2.2.2.2.2.1     (from Top.Given)
  -> rootModel_nefAt_of_hodgeCpt           AS/Proofs/GeometryProofs/RootLinesWeightBoundOfFree.lean:35   (each ℓ ∈ S_B; 2 ∈ bad by RootTower.two_mem)
     -> trivFlagMod_rootLines_model        AS/Proofs/GeometryProofs/HodgeTateFreeTrivialFlagMod.lean
        -> triv_flag_mod_of_hodge_tate_free_of_root_lines   WB/CoreStatements/HodgeTatePoints/TrivFlagModOfHodgeTateFreeOfRootLines.lean:21
           κ from Famproj.family_proj with IsCp p κ (κ = 4 at p = 2), κ | p² (cp_element_divides_prime_sq)
           chart_sequence: κ·p^{R−2} | p^R, R_ℓ = 4
           PointHT := pointHT_of_fargues_hodge_tate hF
     -> trivflag_nef_fibre  (TrivFlagMod mod p^{R−2} ⇒ mod p ⇒ NefAt p)
```

## PointHT at κ = 4

```
pointHT                                    AS/Proofs/GeometryProofs/PointHTOfFarguesHodgeTate.lean:50
  -> polarised_divisible_group_exists -> TowerPoint.exists_HTPoint   AS/Proofs/AlgebraProofs/PolarisedDivisibleGroupExists.lean:398
     -> dlog_lagrangian                    AS/Proofs/AlgebraProofs/TateMapDualHomBidual.lean:151
          hcoker  <- coker_dlog_killed     AS/Proofs/AlgebraProofs/DvdMulOfGroupLikeVal.lean:416   [report Thm 6; uses IsHTConst, not hF]
          hN      <- (hF ...).2 = FarguesExact clause (ii)                                    [report Prop 11]
          hkey    <- tateMap_dualHom_bidual (λ^D = −λ on Tate modules)
          le_of_finrank (rank count)                                                         [report Prop 12]
     fills HTPoint.κ_mem and HTPoint.lagr  AS/Definitions/CommutativeAlgebra/OmStable.lean
```

## Cokernel bound (clause (i) content), all p

```
coker_dlog_killed
  exists_diag (Smith form over valuation ring, smith_mat)          [F5]
  dvd_mul_of_dvd_dlog (level n)                                    [Lemma 5]
    omegaLevel_surjective, omega_val_eq_zero_iff                   [F3]
    pt_surjective, charElem, dlog_val                              [F1, F2, F4]
    dvd_mul_of_groupLike_val -> dvd_mul_of_groupLike
      isIntegral_inv_smul_of_closed   AV/Proofs/IwasawaDecomposition/IsIntegralOfDivisibleCharacters.lean   [Lemma 4]
      NearlyPrimitive.norm_smul_le_one AV/Proofs/IwasawaDecomposition/NormSmulLeOneOfPrimitiveBoundedPowers.lean:231 [Lemma 3]
        norm_smul_le_one_of_lt (:121), norm_factorial_inv_le (:34)                                       [Lemma 2]
Second proof (not live): hodgeTateCokerSharp  WB/CoreStatements/HodgeTatePoints/Farsharp.lean:103
  (FarsharpA dvd_mul_of_val, FarsharpB mem_of_forall_dvd, smul_mem_of_levels)
  feeds FarguesHodgeTate clause (i) via farguesHodgeTate_of_farguesExact (XXgzFarOfExact.lean:50), v(4) = v(2)^2 ≤ v(2)
```

## Kernel statement (clause (ii)), archive route vs human route

```
Archive:  UpperTheory.Lit.farguesExact
            = farguesExact_of_hodge (WB/.../FarguesExactOfPrismatic.lean:56)
                <- prismaticDieudonneHodge (PrismaticDieudonneHodge.lean:19)   [internal; window/frame proof NOT OPENED]
                <- hodgeTateSandwich_of_prismaticDieudonne, ker_hodgeTateLinear,
                   pDivGroup_omega_finite_free_and_p_sq_mem_dlog_span (p²·ω ⊆ span dlog; p² = 4 at p = 2)
Human:    SW 2013 Prop 5.1.6(iii) (rational exactness, all p)  + saturation lemma B-FHT.1   [report Thm 9, Lemma 10, Prop 11]
```

## External inputs on the human route

| Input | Use | Status |
|---|---|---|
| Scholze–Weinstein, Camb. J. Math. 1 (2013), Prop. 5.1.6(iii) | rational exactness | printed, no p ≠ 2; print check pending (page fetch read) |
| Tate 1967; Messing LNM 264 | F1–F4, freeness of ω | standard |
| Kaplansky 1949 | F5 | standard |
| Legendre | Lemma 2 | standard |
