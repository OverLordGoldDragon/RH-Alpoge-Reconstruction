# Final Six Wave 3 dependency map: the shared Wach-module layer below Theorems B and C (PC-3)

Written 22 November 2026 with `Final_Six_Wave_3.pdf` by Agent 3 (Claude). Continues `Final_Closure_Wave_2_Dependency_Map.md` (Theorem B interior) and `Final_Closure_Wave_3_Dependency_Map.md` (Theorem C interior). The archive was read as text. Nothing in `src/lean` was built or run, no existing file was edited, and this map is not a verification.

Paths under `src/lean/src/`: `LLC/` = `Formalism/SharpRestriction/LevelLetterCocycles/`, `QID/` = `LLC/QuotientImageDivisibility/`, `RC/` = `LLC/RepresentationCongruences/`, `FPU` = `LLC/FrobeniusPowUniformizerFactorisation.lean`.

Statuses: **C** closed (body read to read lemmas or boundary), **CX** closed modulo named external theorem, **S** small leaf (statement read, body unread, mechanism known), **R** residual child (statement read, body unread), **AG** apparent gap (none found). **V8** = Wach record of `Post_Closure_Verification_Boundary.md`. **CMP** = comparison record `CmpOf.tie`.

## 1. Verdict

CLOSED MODULO NAMED EXTERNAL THEOREMS (seventh pass, at the human-proof boundary, with the verification list of §9). Earlier passes recorded RESIDUAL CHILD REMAINS: Shared layer S2, S3 (C-1, R-B2), S4 closed modulo V8, CMP, Fontaine `DdREqDcris`, Mathlib Weierstrass division. B-only cores R-B3, R-B4, R-B6, R-B7 and C-only tools C-2, C-4 to C-8 remain (statement level). No gap, no circularity, no failed constant, no new engine.

Second pass (same session): R-B3 `SplitCore` reconstructed (§8a), and three of the four `UnivCore` sub-cores reconstructed (§8b). They reduce to `KillWinCore`, `SecRestCore` and `UnivGenCore`.

Third pass: `KillWinCore` closed with `RATCore` and `InvLevCore` (§8c).

Fourth pass: `SecRestCore`, `UnivGenCore`, RC cores, principal case-body children, `LevC.sec_unique` closed (§8d). Every Theorem B producer is read down to helper level.

Fifth pass: every remaining Theorem B helper read and closed (§8e). C-2, C-4, `lattice_bounds_of_local`, `fam_exp` closed. Two large implementation subtrees found and packaged as human-level propositions instead of descended: the Theorem B case layer `RC/` (135 files, 25,208 lines, 859 theorems) as Prop RC, and the Theorem C tool region (`QID/` 9,142 lines plus about 7,900 in `LLC/`) as Props C-I, C-II, C-III. Verdict stays RESIDUAL CHILD REMAINS: Theorems B and C are not yet CLOSED MODULO NAMED EXTERNAL THEOREMS at the human-proof boundary.

Sixth pass: Prop RC written as a proof (framework read in full, constants 160, 55, 18 derived, nine cut types with deciding inequalities checked numerically, seven cut bodies at skeleton level). C-I, C-II, C-III written as proofs through five tools read only as statements. Recommendation: mark Theorem B side closed modulo named external theorems (cut bodies as low-risk verification item); Theorem C side open on the five tools.

Seventh pass: the five Theorem C tools close (§8g). No internal blocker of mathematical content. Earliest verification items: `arc_length_one_or_two_case_b` (`RC/ArcLengthOneOrTwoCaseB.lean:28`, B) and `kernel_rank_bound` (`LLC/IdempotentMemInvariantsLetter.lean:893`, C).

## 2. S2, Theorem B side: membership criterion along an arc

```
ArcC.SecCrit  ← LevC.secCrit_all (LLC/SecCritAll.lean:168)                          C   induction on e
  e = 0: secCrit_zero (LLC/SecCritZero.lean:58)                                       C
  e → e+1:
    crt, cop_lamUp (LLC/CoprimeFrobeniusUniformizerPowers.lean:92,119)               C   p^m0 = u0 + u1, u0 ∈ (π0 U²), u1 ∈ (p0^{H+hq})
    step_mp  (LLC/InFNcSmul.lean:83)                                                  C
      u0 part:  SecCrit0 forward (LevelZeroModP)                                      → §3
      u1 part:  exists_smul_pow_eq_sum_of_inFNc (LLC/ExistsSmulPowEqSumOfInFNc.lean:48)  C   P5 clause 2, Δ-average
                arc_down, secOfP', IH, transport, secIn_transport (LLC/SecInTransport.lean:103)  S (48)
                dvO_filLow (LLC/DvOZeroHigh.lean:47)                                   C
                good_sum, good_add, good_of_sec (26), good_of_lpow (11)                S
    step_mpr (LLC/SecCritAll.lean:26)                                                 C
      u0 part:  SecCrit0 converse (LevelZeroModPRefined)                              → §3
      u1 part:  dvO_zero_high (LLC/DvOZeroHigh.lean:67)                               C   fil_high + frame_basis
                mono_lift (LLC/ProdPsUnitE.lean:41)                                    S (77)
                pOfSec', IH, up1 (P5 clause 1), transport                             C
                mem_of_sec_eq (LLC/MemOfSecEq.lean:40)                                 C   piLam_of_sec (S, 40, SATPcore), inN_of_piLam, arc_sat
      saturation: arc_sat (SATcore), arc_up                                           CX (V8)
```

## 3. S2, level zero (SecCrit0)

```
SecCrit0 = LevelZeroModP ∧ LevelZeroModPRefined (LLC/ArcCoordinatesOfLevelZeroParts.lean:21,32)
 forward: lev0MpL_of → CrC.level_zero_membership_of_horizontal (LLC/LevelZeroMembershipOfHorizontal.lean:23)   C
   fil_of_rep (LLC/FrobeniusPowerZeroEqQ.lean:35)                                    C
     lev_qP_X (lev(p0) = t·unit), ExpNoNeg0, ExpFrame0, vanish_of_XU, LevelMapHodgeFiltration (forward)
   CrD.secIn_of_fil (LLC/CoeffAlgMul.lean:33)                                        C
     CrA.adapted (LLC/StageStep.lean:72)                                             C   ← stage_all (S, 15)
     cc_lev_piLamUp (LLC/CrystallineFiltrationAntitone.lean:68)                      C   constant term −p·p^{ΣH} ≠ 0
     DivLevR.divLev_of (LLC/LevLetEMul.lean:194)                                     C   ← step (S), factor theorem at ζ−1
     dvO_filLow                                                                      C
   ExpFrame0, ExpNoNeg0 ← expFrame0_of, expNoNeg0_of (LLC/LevelOneUniformizerCoeffVanish.lean:425,451)   C
     levB_frame, hor_exp (horizontal ⇒ constant level series to order (p−1)M), coeff_lev_q_pow, smulS_congr_shift
   Comparison₂ ← LevE.levETie_of (:501)                                              CX (CMP fields; hneg_of from V8 p4)
 converse: lev0MprL_of → LevM.lev0Mpr_of (LLC/LevelSeriesFirstFactorOrderOne.lean:239)   C
     first_factor_power_isUnit_etale, repVV_iff, qphi_mem (P5), q_unit
     low degrees: expFrame0_of, lev_prod_ps (S, 24), dg_core (S, 40)
     high degrees: fil_low (jump window)
     MemCrit (k = 2H)                                                                → §4
     mem_of_sec_eq                                                                   C
```

## 4. S2, shared: MemCrit (one theorem, two copies)

```
MemCrit (QID/MemCrit.lean:18)
  ← memCrit_of       (QID/JumpsLetExists.lean:218)        used by Theorem C (expCritN_of)
  ← memCrit_of_free  (LLC/ArcCoordinatesFinal.lean:26)    used by Theorem B (memCritL_of → lev0MprL_of)
     identical statements and identical proof bodies                                 C, one item
  proof: jumpsLet_exists, fd_ιDi  (DdREqDcris: Fontaine)                              CX
         P5 clause 3 (converse membership via vanishing ideals vanI)                  CX (V8)
         qroot_prim, shift_exp (lev(Q) = t·unit)                                       C
         mem_vanI_at (QID/JumpsLetExists.lean)                                         C
            WachLatticeFree (letter basis), p3 → rank_le, p4 both directions → hS     CX (V8)
            MC.count_step, MC.indep_of_span (QID/IndepOfSpan.lean:39,90)               C   dimension count H(j) constant
            MC.smulS_sub_cc, MC.dvd_of_dg (:141,154)                                   C   induction peeling t
```

## 5. S2, Theorem C side: ExpCrit

```
expCrit_D' (QID/IsAdicCompleteOfLe.lean:60)                                          C   wrapper: complete_max, isAdicComplete_of_le
  → expCrit_D (QID/LMemMaxOL.lean:31)                                                C   record selection
  → expCrit_of (QID/ExpCritPOf.lean:161)
      expCritN_of (QID/IsExpSmulA.lean:62)                                           C   forward p4; converse memCrit_of + Γ-transport (PtTrans: ptTrans_rec S, levB_Γ)
      expCritP_of (QID/ExpCritPOf.lean)                                              C   BasTool (basTool_of S, 14), phi_exp, indep_phi_cmp (S),
                                                                                         MC.dvd_of_dg (two-step filtration), Wd.dvd_of_dvd_image (S), qp_pow_cancel
  expRules_of (QID/SmulSDivMem.lean:69, 104)                                         S
  lemK_D → lemK_of (QID/SmulSZeroSplit.lean:49, 60)                                  S   (same inputs)
  filDim_of (QID/FilDimOf.lean:18, 12)                                               S
  ring_condition_uniformizer_polynomial (LLC/AnnihilatorGeneralOfRingCondition.lean:75, 13)   S (V8 P9)
```

## 6. S3: truncation and level expansion (C-1), R-B2

```
Tools.frobenius_power_congruence_local (LLC/FrobeniusPowerCongruenceOfAdmitted.lean:713)   C
  → tHor_of (:480)  tool THor                                                        C
      expH (:378)        (γ−1)h = π0^K ν at ζ = 1 ⇒ (χ^k−1) d_k = 0 for 0 < k < (p−1)K
      laurentBounded_zero_of_trivial_twist (p4), levB_γ1 (CMP), levπ₀_dvd, chi_pow_ne_one
      chainζ, stepφ, chain_mul (φ-transport to letter i+j, ζ primitive)
      key_idJ (algebra of z, h, r_y, s_y)
truncatedSeriesData.tTool2_of (LLC/HermFlagUnipotentAnisotropicVectorSubMem.lean:1574)  tool TTool2
  trunc_ex (:1113) ← ser_exists, rs_ex (:1097)                                       C
     rem_exists (:862)  Weierstrass division by π0^M qp^X (wdiv, wuniq)               CX (Mathlib PowerSeries.IsWeierstrassDivision)
     bound1 (j = 1), bound2 (j = 2), num2 (arithmetic), rem_2                          C   σ checked numerically
  b1, gamma_sub_of_frobenius_power, uniq_alt_alt, linear_of_frobenius_power,
  uniformizer_dvd_of_frobenius_power, span_gen, hermFlagUnipotent_anisotropic_vector_sub_mem   S (statements read; pulled back by fp_pull, SATPcore)
  tTool1_of (:178, 7), tTool2Z_DU                                                     S
R-B2:
  secOfP' (LLC/SecOfP.lean:24)                                                        C   Pp_repr, int_of_bd (coreH iv), ArcF.frame_inv_poly, yM_gen
  pOfSec' (:152)                                                                      C
  arcHyp_secOfN, arcHyp_nOfSec (LLC/ArcCoordinatesOfMembership.lean:1015,1030)        C   from SecCrit + secOfP/pOfSec
```

## 7. S4: killer inputs (Theorem B)

```
killer_first_theorem_holds (LLC/KillerSecondTheoremHolds.lean:12)                     C
  → pi_stability_content_clause (LLC/DivisibilityInvariantMulLinear.lean:324)
      killerKap_holds (:185) KillerKap 8                                              C   kappa_bound_logb, kappa_window_bound, arc_KillerVal (LTE)
      killerModL_of ← killer_module_of_pi_stable (Pi0Stable)                          C
annihilator_levels_unramified_statement (LLC/AnnihilatorLevelsUnramifiedStatement.lean:576)   C
  → annihilator_levels_of_grading (LLC/AnnihilatorLevelsOfGrading.lean:16)           C   wrapper
  → KL.killerLevCore_of (LLC/KillerLevCoreOf.lean:486)
      LevGrad ← levGrad_of (:470), aut_core, aut_eq_bs, ode_unique, bs_*              C   γ = (1+X) ↦ (1+X)^χ via binomial series
      KL.step (:283)                                                                  C (first half read; rest bookkeeping)
      KL.levels (:431), psUnitE_of, psCoprime_of, psStable_of                          S
```

## 8. S1: generic lifting record

```
LiftingTheory.local_theory_of_admitted (LLC/BaseChangePreservesUnitaryOf.lean:4837) = local_parts_of_admitted + lifting_all_parts_of_admitted
  ConclusionL  ← lattice_clause_every_situation (FPU:1966) ← lag_coreL (S), assoc_of_v
  ConclusionW  ← wach_statement_of_literature (FPU:4131): coreWX, coreWB, coreWA (C earlier), coreWK1   R (statement level)
  WachAnnihilatorAll ← wach_first_clause_of_literature (FPU:3691)                   R
  WachExponentRecursionAll, WachResultConstant 10 (coreWR, C earlier) ← wach_clauses_of_admitted_inj (FPU:4413)
  ConclusionH  ← gamma_equation_clause_of_uniformizer                                 C (Wave 2)
  ExistsUnitClasses (coreTr) ← truncation_of_uniformizer_clause (FPU:2614)            clauses 1, 2 C (Wave 2); clauses 3, 4 S (rational form of the truncation estimate)
  LiftTheoremAllCases 23 32 32 ← lifting_case_A_of_admitted, lifting_case_B_of_hypotheses   Theorem B route (Wave 2)
```

## 8a. R-B3: SplitCore (second pass)

```
Split.splitCore_of (LLC/SplittingOfExactnessAndData.lean:182)                         C   read in full
  HerrExt (Herr: class of Herr cocycle of a lift)                                     CX
  RelayCore (Wave 2), FirstWachFiltration (ii) uniqueness, (iii) classes, clK_sum (S, 19), clK_congr
  SplitLift ← Split.splitLift_of (:561, assembly, Wave 2) ← CutData
     Split2.cutData_of (LLC/CancelUnitMulUniformizerPow.lean:433)                     C   read in full
        lift_avg (:352)                                                               C   Δ-average
        pull (local): P9 frame, cancel_unit_mul_uniformizer_pow, DDExact (Fontaine), P6 WachSaturationExactness   CX
        Relay2.solData, Relay2.tauZ_exists (:101)                                     C   tr_trunc_int, frobenius_uniformizer_pow_dvd (Wave 2)
        RelayCore in Y, goodZ_map, mkTr, goodZ_comb (S, 28)                           C
        F1 (i) via InFN_φpow (S, 13); ArcCore (closed); Pp_φpow (S, 17); win_ext (S, 10) with coreJumps (Fontaine strictness)
        pp_pull (:367)                                                                C   coreWX (WachLatticeLengthLemma, closed Wave D), e_tf (:314, C), SATPcore
  SplitShape ← splitShapeL_rec → SplitP.splitPolar_of (LLC/SplitPolarLOf.lean:22) + LevC.polarToPole_of_ctx (LLC/PolarToPoleOfCtx.lean:87)
     SplitP.polar_core (LLC/IntAOfNonpol.lean:84)                                     C to helpers (first 120 of ~200 lines read)
        frame_const, repVV_map (S, 39), dv_map (S, 22), secOfP_int (S, 139), LevC.sec_unique (S, 176),
        pull_vec (S, 59; DcrisExactStrict), intA_of_nonpol (C), condPole_of_polar (S, 33)
```

## 8b. R-B4: UnivCore (second pass)

```
universal_general_statement_holds → universal_general_of_level_inverse → universal_general_of_inverse_levels → universal_general_of_window
UnivC.univCore_of = Frame + Sec + Gen + Lift
  UnivFrameCore ← UnivF.univFrame_of (LLC/UniversalGeneralOfRestriction.lean:803)    C   read in full; dimension count |R| ≤ m·ρ
     split (S, 232), frame_change (S, 88), hor_exists, codim_up (S, 19), dim_down (S, 15), mult_le_lowCount (S, 12), DdREqDcris
  UnivLiftCore  ← univLift_of (:1258)                                                C   read in full; ArcCore POfSec/NOfSec/zero clause
     repVV_γ (S, 68), jj_lam (S, 33), lam_γ (PsStable), lam_cancel
  UnivSecCore   ← univSec_of (:1847)                                                 C   read in full
     sec_zero (S, 122), inNL_lam (S, 23)
     SecRestCore ← secRest_of (:2588, assembly)                                      C
        section_restriction_first (:2312, 98), section_restriction_second (:2521, 67), nn_bounds (:2439, 57)   R
        KillWinCore ← KWP.killWinFromCut (LLC/ExistsGammaPi0EqPi0Mul.lean:940, assembly)   C   → §8c
  UnivGenCore   ← UGen.universal_generators_of_units (wrapper) → univGenCore_of_lev → univGenCore_of' (LLC/SingleMemSpan.lean:29, 200)   R
     finLev_of (LLC/EvalZeroXEqUniformizer.lean:128, 73)                              R
```

## 8c. R-B4: KillWinCore (third pass)

```
KillWinCore ← KWP.killWinFromCut (LLC/ExistsGammaPi0EqPi0Mul.lean:940)                C
  exponents per letter: thin (mm G0, dn 0, nnN G0, nnD 0); up b (b+S, 0, 0, b); down b (0, b, b+S, 0)
  raise (:31)  single-level raise via KillerLevCore + KL.inId_aeval (PsStable)        C
  part_b (:514)  P(γ)f ∈ nnDen⁻¹: raise α = −mm → −nnD on [−G0,0) (thin), [−b−S,−b) (up)   C
  part_a (:633)  (γ−1)P(γ)f ∈ π0 nnNum/nnDen: (X−1)P = Π_{0 ∪ JS} fac (xsub_ppo);
                 thin from −G0 over [−G0,G0); up from −(b+S) over [−b−S,−b); down from b over [b,b+S)
                 π0 carried by InIdπ (inIdπ_aeval, exists_gamma_pi0_eq_pi0_mul)        C
  part_c (:835)  down letter: InvLevCore, then induction k → k+1 ≤ b+S:
                 (γ^{p^ℓ} − χ^{kp^ℓ})y and (γ^{p^ℓ} − 1)y in p_s^{k+1}; difference (χ^{kp^ℓ} − 1)y;
                 v((χ^{kp^ℓ}−1)p^ℓ) = 2ℓ+1+v_p(k) (KillerLevCore valuation, ppo_single_eval), div_of_val   C
  RATCore ← RatW.ratCore_of (LLC/LocalInputsFromLiterature.lean:267)                   C
     local_inputs_from_literature (:173, C: elementary identity), loc_π₀ (S, 29),
     crt_prod (S, 17), cop_π₀_ps (S, 19), cop_ps (S, 6), SatW.dvd_of_UPi (Wave 2), psUnitE_of (S, 31)
  InvLevCore ← invLevCore_fin → InvW.invLevCore_L (wrapper) → invLevCore_of_parts → InvW.invLevCore_of (LLC/InvLevCoreOf.lean:45)   C
     evaluation at primitive p^{s+1}-th roots (LevBasics ← levelBasicsOfRingCondition S 50, genUnits S 17)
     invariance under σ(γ), σ(Δ) generating (Z/p^{s+1})^× ⇒ constant (precompConst, C)
     LevRat ← levRat_of (LLC/ExistsDvdPowOfNotIsUnitDvr.lean:63, C) via levRatPf_ev, wdiv_ps (S, 56), poly_eq_zero
     LevDiv ← levDiv_of (S, 50) factor theorem at the roots
  PsStable ← psStable_of (S, 34)
```

## 8d. R-B4 completed, R-B6, R-B7 (fourth pass)

```
SecRestCore ← secRest_of
  section_restriction_first (UniversalGeneralOfRestriction.lean:2312)   C   pole coords bounded by nn_bounds; sec_zero (S, 122); sat_frac (S, 42)
  section_restriction_second (:2521)                                    C   InvNL section bounded by nn_bounds; sat_frac
  nn_bounds (:2439)                                                     C   window ⇒ Fil step above jumps is 0 (filCris_bot S); down letters: Fil^{−η} ⊂ span R ⇒ coord_zero (S)
UnivGenCore ← univGenCore_of' (SingleMemSpan.lean:29)                   C   read in full
  killer_elem (InId0OfMem.lean:137, 139, S partial), lev_const (InvLevAtOf.lean:71, 113, S partial)
  crtLev (S, 19), FinLev ← finLev_of (S, 73, Weierstrass division by π0Λ²), eval_one_dvd_prime_pow (S, 24), sat_l (S, 37), pp_inv (S, 17), psub_of_pi0Lam (S, 8)
  gen_of_killer (GenOfKiller.lean:48)                                   C   Noetherian module lemma over a PID
R-B6
  horizontal_frame_structure, arc_filtration_low (FinrankEqOneOfBijectiveBis.lean:71,155)   C
  arc_gamma_lift_at → arc_gamma_lift (LetterWindowBoundedBelow.lean:39)                      C   assembly over gamma_lift_along_arc (S, 89), section_in_ideal_of_levels (S, 92)
  arc_section_map (SmulPowDifferenceIdentity.lean:153, 184)                                  S   functoriality of frame coordinates (first 30 lines read)
R-B7
  exists_phiBridge (ExistsPhiBridge.lean:147)                           C   A^Δ ≅ O[[X]], X ↦ π0 + p; φ ↦ u(X−p)X^{p−1}
  den_step (ArcLenTwoThickLetters.lean:64) → den_bound (DenBound.lean:12)   C   content estimate PhiData.constant_le_rpow_of_three_le (S; = Wave 3 Lemma 1)
  case2b (DivAddLogbLeEightMulErrorScale.lean:105)                      C   real inequality; checked numerically (check_case2b.py)
  liftsAt_of_scaled_power                                               C
  liftDelta (S, 54), aI_le (S, 74, via coreWR), exists_liftsAt_arcOf_exponent_le (S, 39), N_typeT, constants_typeT (wrappers)
LevC.sec_unique (FrameInvPoly.lean:143)                                 C   relation + indep + frame_inv_poly' with Y^M = π0Λ²ν
```

## 8e. Fifth pass: Theorem B helpers, case layer, Theorem C tools

```
Theorem B helpers (all C, read in full unless marked)
  secOfP_int (LLC/SecOfPInt.lean:24)                          Pp_repr, int_of_bd, frame_inv_poly, yM_gen: integral coordinates
  gamma_lift_along_arc (RC/GammaLiftAlongArc.lean:22)         ArcCore lift/zero clauses, lam_cancel, repVV_gamma, repVV_sub
  section_in_ideal_of_levels (RC/SectionInIdealOfLevels.lean:22)   exists_partition_of_l_pow_levels (C), inId_shift_levels (C)
  polar_core 2nd half, pull_vec, o_inj, repVV_map, dv_map, condPole_of_polar   fil_pull (DcrisExactStrict), int_vec, right_inv
  split (adapted basis over PID), killer_elem, lev_const, sec_zero, frame_change, finLev_of (Weierstrass), repVV_gamma,
    jj_lam, lam_gamma, lam_cancel, sat_frac, sat_l, inId_bound, eval_one_dvd_prime_pow, pp_inv, inNL_lam, jump_ge,
    codim_up, dim_down, coord_zero, filCris_bot, filCris_le, mult_le_lowCount
  arc_section_map (rest), aI_le (tsum_three, Aa_cut_le), liftΔ (Δ-average)
  PhiData.constant_le_rpow_of_three_le                        first part read; binomial expansion + Kummer = Wave 3 Lemma 1
  leaves not read (S): goodZ_comb, clK_sum, Pp_phipow, InFN_phipow, win_ext, crtLev, psub_of_pi0Lam, hor_diff, value0, dvO_zero_hw, adapted

Theorem B case layer (packaged, Prop RC)
  thmB_at (LLC/FrobeniusStatementOfFontaine.lean:119)        C   assembly, arith_big/arith_alt/arith_one, C0 = 320
    exists_liftF_le_sg_of_thick (RC/ExistsLiftFLeSgOfThick.lean:9)   C (§8f)  e0 ≤ 160 Sg
    sum_alt (RC/LogbHBNonneg.lean:386)                       R   e ≤ 55 Sg + 13 S + η bandI, |Z| ≤ 4 [K0:Q_l] m
    sum_one (RC/LogbHBNonneg.lean:408)                       R   e ≤ 18 Sg + 3 R² (S + 1 + log_l(2 h_B)) + 1, |Z| ≤ (R+1)[K0:Q_l] m
      exists_liftsAt_arcOf_exponent_le (C, assembly) → exists_exponent_le_liftsAt_arcOf (skeleton): arc_length_four_denominator,
      saturation_fraction_ring, liftsAt_thick_letter_type, liftsAt_constants_type, le_band_add_errorScale, case2b
  RC/ total: 135 files, 25,208 lines, 859 theorems

Theorem C
  lattice_bounds_of_local (LLC/LatticeBoundsOfThreeParts.lean:504)   C   iter_chain, kerChain_of_pchain, expC_of
    C-I  CocyclesToWachVectorsBound  ← cocyclesToWachVectorsBound_of_extTool (C) ← ExtTool, Step1, Step2      R (Herr)
           extData_extTool (skeleton) ← extDataOne_exists (208, C in §8f)
           Step1 ← first_lift_of_uniformizer_clause (C, wrapper) ← first_lift_of_hypotheses (R)
           Step2 ← second_lift_of_hypotheses (C, wrapper) ← second_lift_at_situation (R)
    C-II WachVectorSubmoduleChainBound ← lattice_bound_three_six_of
           WachVectorLiftingBound ← length_bound_of_hypotheses (QID/LengthBoundOfHypotheses.lean:118, R): MemCrit (C), H2Bound, ContentBoundLevel, LemmaDN, LemmaDN0
           LatticeBoundSix ← frobenius_sq_bound_of_local (skeleton)
    C-III RhoLift ← rhoLift_of (skeleton): TTool2, Herr naturality of clK
  C-2: QToolOpen_of, extJumps_of, rk_jump_of, lag_coreL                C
       gamma_lemma_of_crystalline (C, assembly) → gamma_structure_of (skeleton: q-adic induction, residue −p·res(T_k) = χ^k − 1)
  C-4: filtration_gap_vanishing, gamma_levels_expansion                C;  kernel_rank_bound (skeleton)
  C-5: fam_exp C;  contentBoundLevel_of, pass3, pass4 (skeleton, PChain length counts)
  C-6: detTool_of, zTool_of, adaptBas_of, detAlg_of (skeleton)
  tool region: QID/ 58 files 9,142 lines + about 7,900 lines in LLC/. Tools not named in earlier C lists:
       ExpRing, FTool, DssLet, RToolNum, TTool2Z, GamN, GamA, LemmaDN, LemmaDN0, H2Bound
```

## 8f. Sixth pass: Prop RC and C-I to C-III as proofs

```
Prop RC
  (i)  thmB_at → exists_liftF_le_sg_of_thick (read in full)          C   coreLiftA (S1) exponent ePA ≤ 7.1h/l + 7.1 + 2 log_l(2h) (lift_le, Legendre windows)
                                                                         b < 160 Sg ⇒ ePA ≤ 122.7 Sg (step0)   checked: check_rc_case1.py
  (ii),(iii) sumAltW, sumOneW (read in full)                         C   e = r + 3σ + max κ_c + E1
       r ≤ r_B ≤ 3 Sg      kill_cut ← coreWR at letter c+1, tsum_three
       σ ≤ 3 Sg            TCase truncation constant
       κ_c                 KillerKap: p^κ = y·P(1); kappa_bound_window_sum: ≤ 13S + 3log + 3 (len ≤ 3), ≤ 3R²(S+1+log) (len ≤ R)
       Step A split_sum (SplitCore, ExtYCore)                         C
       Step B arc_length_bound_theorem (skeleton: KillerModCore, UnivGenCore generators → Z_c, LV_galois, rho_uniq)   C
       Step C LiftsAt E1: arc_proposition_alternative, arc_single_type_bound (read in full)
         one direction        r + σ               6 Sg + 1      C
         len2 up, s0 big      r + 3σ              12 Sg + 1     skeleton (unit top coefficient of p_1^y)
         len2 up, else        r + σ + deA         9 Sg + 1 + η bandI   end read; deA_le (Kummer), case1c (checked)
         len2 down, A1 small  lift2a + reduction  9 Sg + 1      skeleton
         len2 down, else      r + σ + de          15 Sg + 1 + η bandI  den_step, case2b (checked)
         len3 up, s2 small    r + σ + s           34 Sg + 1 + η bandI  arc_length_four_denominator, aI_le, le_band_add_errorScale (checked)
         len3 up, else        r + 3σ + 1 + e4     18 Sg + 1     skeleton
         len3 down, s1 small  descent + scale     22 Sg + 1 + η bandI  skeleton
         len3 down, else      s1 + σ              13 Sg + 1     numerics (checked)
       55 = 3 + 9 + 40 + 3 (3 log + 3 ≤ 3 Sg);  18 = 3 + 9 + 6
C-I   extDataOne_exists (C, read in full: Herr data from the extension, μ_i, ν_i);
      first_lift_of_hypotheses (skeleton: kill polynomial ∏(X − c_x), v(c_x) = v_p(x), s1 ≤ B1);
      second_lift_at_situation (skeleton) ← passage_to_quotient (R, **earliest**), TTool2Z
C-II  WachVectorLiftingBound ← length_bound_of_hypotheses (skeleton): fam_exp (C), h2Bound_of_hypotheses (R), pass3, LemmaDN (R, via DetColsE),
        ContentBoundLevel, pass4 (R), MemCrit (C);  LatticeBoundSix ← frobenius_sq_bound_of_local (R)
      e2 + e6 ≤ chain exponent by bound_three_five_add_six_le
C-III rhoLift_of (skeleton): TTool2 in T1 and T2, FTool clauses 3 and 4, naturality of clK
```

## 8g. Seventh pass: the five Theorem C tools

```
passage_to_quotient (LLC/FiltrationQuotientFiniteDimensional.lean:134)   C  read in full
  ExpRules (expansion exists, unique, linear); lemK_of (C, read): γ acts by χ^k ≠ 1 on d_k ⇒ d_k ∈ Fil^{-k}; ExpCrit ⇒ u ∈ N ⟺ d_0 ∈ Fil^0
  filtration_quotient_finiteDimensional (C): dim Fil^{-η}/Fil^0 = #jumps in [−η,0) ≤ m; image f.g. in L^r over PID ⇒ ≤ r generators
h2Bound_of_hypotheses (LLC/IdempotentMemInvariantsLetter.lean:1338)       C  read in full
  gamma_levels_expansion + filtration_gap_vanishing: d_s ∈ Fil^{-η} for 0 < |s| < b_c
  kernel_rank_bound (241, S skeleton): relation p^σ [t^R]lev(P_c) d_0 ≡ Σ [t^R]lev(a_k) φ²(cmp w_k)
  scalar_integrality_relation (139, S skeleton) ← power_series_dvr_factorisation (C, = Wave 3 Lemma 1); integral_coordinate_of_relation (88, S)
  exponent_bound_second (C, arithmetic)
LemmaDN ← lemmaDN_of_detE ← lemmaDN_core (C, read: length coker ≤ v(det)) + detColsE_of
  detAlg_of (end read): v(det Q) = w0 + σ m' − Σ k_j ≤ rS + 2⌊c_D⌋m; DetTool (detTool_of 104, S): det φ = unit·(X+p)^{w0}, w0 = (b+S)r + Σ a mult(a), via P4
  zTool_of (S), adaptBas_of (S), gMem_of (S, 6), deep_bound, sigma_le (C)
pass4 (QID/InIZero.lean:44)                                               C  main part read: basis over PID, ψ4 rank step, MemCrit (mem_of_exp)
frobenius_sq_bound_of_local (QID/FrobeniusSqBoundOfLocal.lean:55)          C  read (assembly)
  frobenius_sq_bound_at (192, S skeleton): LemmaDN at c and c−2 (pchain_DN 74, S), cmp_of_mem_X (C, read), cmp_up (54, S),
     rank step, LemmaGs (C, Wave 3), exists_inI_inPN_pow_smul_sub_map (66, S)
```

## 9. Remaining residual list (body lengths in lines)

| ID | Declarations | Size | Mechanism |
|---|---|---|---|
| RC | proved (§8f). Verification: seven cut bodies at skeleton level (about 1,350 lines), largest `arc_length_one_or_two_case_b` (449) | verification only | inequalities checked |
| C | proved (§8f, §8g). Verification: `kernel_rank_bound` (241), `scalar_integrality_relation` (139), `integral_coordinate_of_relation` (88), `detTool_of` (104), `zTool_of` (60), `adaptBas_of` (210), `gMem_of` (6), `frobenius_sq_bound_at` (192), `pchain_DN` (74), `cmp_up` (54), `exists_inI_inPN_pow_smul_sub_map` (66), `gamma_structure_of`, `contentBoundLevel_of`, `pass3`, `first_lift_of_hypotheses`, `second_lift_at_situation`, `rhoLift_of` (about 2,700 lines) | verification only | known |
| C-9 | `TheoremCAdm.admissible_ranks_of_CMDatum` and five top producers | bookkeeping | |
| B leaves | `goodZ_comb`, `clK_sum`, `Pp_phipow`, `InFN_phipow`, `win_ext`, `crtLev`, `psub_of_pi0Lam`, `hor_diff`, `value0`, `dvO_zero_hw`, `adapted` | small | known |
| SL | `stage_all`, `DivLevR.step`, `secIn_transport`, `mono_lift`, `dg_core`, `lev_prod_ps`, `good_of_sec`, `good_of_lpow`, `piLam_of_sec`, `expRules_of`, `lemK_of`, `basTool_of`, `filDim_of`, `ptTrans_rec`, `gam_of_tie`, `indep_phi_cmp`, `Wd.dvd_of_dvd_image`, seven clause lemmas of `tTool2_of`, `coreTr` clauses 3 and 4, `KL.levels` | small | known |

Discharged in this wave and not to be carried forward: `Split.splitCore_of`, `Split2.cutData_of`, `Relay2.tauZ_exists`, `lift_avg`, `pp_pull`, `e_tf`, `UnivF.univFrame_of`, `univLift_of`, `univSec_of`, `secRest_of`, `KWP.killWinFromCut`, `KWP.part_a`, `part_b`, `part_c`, `raise`, `RatW.ratCore_of`, `local_inputs_from_literature`, `InvW.invLevCore_of`, `levRat_of`, `precompConst`, `LevC.secCrit_all`, `step_mp`, `step_mpr`, `CrC.level_zero_membership_of_horizontal`, `CrD.secIn_of_fil`, `fil_of_rep`, `LevE.levETie_of`, `expFrame0_of`, `expNoNeg0_of`, `lev0Mpr_of`, `memCrit_of_free` (= `memCrit_of`), `expCrit_D'`, `expCrit_of`, `expCritN_of`, `expCritP_of`, `Tools.frobenius_power_congruence_local` (`tHor_of`), the existence clause of `tTool2_of`, `secOfP'`, `pOfSec'`, `arcHyp_secOfN`, `arcHyp_nOfSec`, `killer_first_theorem_holds`, `killerKap_holds`, `annihilator_levels_unramified_statement`, `KL.killerLevCore_of`, `LevGrad`.

## 10. Numerical checks (consistency only, not proofs)

Scripts in the cloud workspace (`check_trunc.py`, `check_trunc_need.py`, `check_killer.py`).

- `TCase` σ: model ring Z_p[[X]], π0 = X, qp = X + p, φ(X) = X(X+p)^{p−1}. Exact test of p^σ φ^j(X)^y ∈ (p^{e(y)}, X^M (X+p)^X) by division by the monic polynomial modulo p^{e(y)−σ}. p ∈ {11, 13}, j = 1 with M ≤ 5, X < 60, y < 25, and j = 2 with M = 1, y < 12: 2,740 cases per prime, 0 failures. Needed exponent ≤ σ − 1 in every case at p = 11.
- `lift_le`, `step0` (check_rc_case1.py): lift_le margin ≥ 0.47; step0 margin ≥ 72 Sg.
- `case1c` (check_rc_leaves.py): 100,148 cases, margins 2.16 and 51.7. `numerics`: witness found in all 2,572 admissible cases.
- `le_band_add_errorScale` (check_band.py): 400,000 adversarial cases, margin ≥ 8.77 Sg.
- `case2b` (RC/DivAddLogbLeEightMulErrorScale.lean:105): 376,008 random admissible cases, first conclusion holds with margin ≥ 2.39; second conclusion holds in all 227 cases where its hypothesis is met (`check_case2b.py`).
- `KillerKap`: 160,000 random cases, l ∈ {5, 7, 11, 13}, h ≤ 10^5, ℓ ≤ 6, ρ ≤ 5, intervals biased to powers of l. Max ratio of the two sides 3.75 (l = 5, ℓ = ρ = 0, G ≈ h), equal to 3(1 + 1/(l − 1)). Constant 8 holds with margin.

## 11. External boundary used by the closed layer

V8 clauses p3, p4 (both directions, `LevelMapHodgeFiltration`), P5 (three clauses), P9 ring relations, `WachLatticeFree`, `wachModuleOverLetters`, `SATcore`, `SATPcore`, `FirstWachFiltration`; CMP fields `levN_eq`, `levB_supp`, `cmp_eq`, `levB_Γ`, `levB_φ`, `lev_φ`, `levB_mem`; Fontaine `DdREqDcris`; Mathlib Weierstrass division; LTE; Legendre. For R-B3 also `DDExact`, `DcrisExactStrict`, `coreJumps` (Fontaine), `HerrExt` (Herr), V8 clause P6 `WachSaturationExactness`. All already on the boundary. Nothing added to `Post_Closure_Verification_Boundary.md`.

## 12. Blocks "entire RH proof reconstructed modulo named external theorems"

No, at the human-proof boundary, subject to the verification list in §9 (about 4,000 lines read at skeleton level, statements and deciding inequalities checked). External boundary unchanged: V8, CMP, `DdREqDcris`, `DcrisExactStrict`, `HerrExt`, Mathlib Weierstrass division.
