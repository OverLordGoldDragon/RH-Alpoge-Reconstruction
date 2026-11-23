# Final Six Wave 6: dependency map

22 November 2026. Agent 6 of the final six-agent closure wave (PC-6 global records, PC-7 FR-10, final small-leaf sweep). Companion to `Final_Six_Wave_6.pdf`. Lean proof bodies were read as text from `lean.tar.gz`. Nothing was built or run, and no existing file was edited. This is a reconstruction, not a verification.

Route liveness was decided with a reverse-dependency index over all 1,060,824 declaration headers of `src/lean/src/` (token index of bodies). **LIVE** means a reverse path reaches `allChi` (the term of `riemannHypothesis`). **OFF ROUTE** means the whole reverse closure was exhausted without reaching it (every such closure here has at most 23 declarations and was rechecked by text search). **UNDECIDED** means the reverse closure passed the cap.

Path abbreviations under `src/lean/src/`: `TPS/` = `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/`, `DP/` = `Development/AbelianVarietyTheory/Proofs/DivisorProofs/`, `LTD/` = `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/`, `IT/` = `Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/`, `CSN/` = `Formalism/SharpRestriction/CuspSpanNormBounds/`, `STT/` = `Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/`, `IEV/` = `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/`.

Marks: [C] closed, [E] closed modulo named external theorems, [A] assembly read in full, [T] transfer read at top, [R] reduced to named children, [S] statement level, [U] unread, [D] off route.

## Verdict

CLOSED MODULO NAMED EXTERNAL THEOREMS (after the fourth follow-up, section 12). No gap, no circularity, no failed constant, no new engine. Earlier versions of this map said RESIDUAL CHILD REMAINS; section 12 supersedes them. `JoinOut` (CM-period integrality, not on any earlier list) is closed modulo named external theorems after the follow-up of 22 Nov (section 2).

## 0. Route corrections

```
fun0Fit_of_leaves (Divisors/TwistedPlaceChoiceLiesOverPair.lean:345)        [D] closure {fun0Fit_of_leaves, fun0Fit_close, fun0Fit_of_join, hypsE2, everyE2}
  live twin: fun0Fit_of_leaves_alt (TPS/LeafInfinitePlaceBound.lean:83)     same sixteen predicates, renamed
hostEx_of_zeroFreeRegion (GlobalInterpolation/HostExOfPublished.lean:30)    [D] closure {hostEx_.., exists_richRec_.., exists_glob0_.., exists_coreTies_..}
Inh.not_evG_false cluster (AutomorphicMembership/RecExGOfRecAtG.lean:24)   [D] closure of 10; exists_chGoodW [D]
denominators_transport_reflection (DP/CmPeriodStatementOfHyp.lean:56)       [D]; live producer of JoinOut is joinOut_of_five
all_parts_transfer_of_facts, all_parts_transfer_holds, levelAmb_transfer    [D]
levelCompare_statement, passageLat_of                                       [D]
```

## 1. FUN (live chain)

```
allChi <- everyCharacter <- everyCharacter_of_row <- every_character_of_literature_of_vWin
  <- every_character_of_theta_integrals_local_matching
  <- nonempty_hyps_definite_side_of_closed_bound (TPS/SiegelEisensteinSecondTermHypotheses.lean:44)
  <- fourier_coefficient_fit_of_join_alt (TPS/FourierCoefficientFitOfJoin.lean)          [A] unpacks JoinOut
  <- fittedFunction_at_zero_close_alt (TPS/FittedFunctionAtZeroClose.lean:42)            [A]
  <- fun0Fit_of_leaves_alt (TPS/LeafInfinitePlaceBound.lean:83)                          [A]
  <- functional_lower_bound_of_conditions_numeric (IT/FunctionalLowerBoundOfConditionsNumeric.lean:1035)
  <- functional_lower_bound_of_conditions (same file :940, 95 lines)                     [E] slope inequality
       psi_inj (:917), hence_local (:564), ip_first (:826)                                [S] small
       PI.local_global_inclusion'                                                         [S]
       Formalism.AtG.height_h0_index_bound (.../GridSquaresIndexEstimate.lean:280)        [A]
         gridHeightBoundIndexed (:105, first 175 lines)                                   [A] product formula
           grid_squares_index_estimate, partial_nat, grid_ell_bound                       [S]
         grid_function_bound = grid_function_of_lemma_A grid_lemma_A
           (.../FrameHeightOfDualSlope.lean:451, :405)                                    [A]
           Formalism.HN.slope_inequality_mean (HarderNarasimhanProofs/SlopeIneqMean.lean:249)   [E] Bost/Gaudron slope inequality (Layer 3)
           ideal_scaling_holds (ChainSlopeWindows/TruncatedLatticeHolds.lean:525)        [C]
       size_le (:421), size_arith (:243)                                                  [C] checked numerically, max ratio 0.318
```

### Sixteen leaves (+ Scale, Bundle, Exists)

| Predicate | Live producer | Mark |
|---|---|---|
| ScaleCondition | existsIntegralMultiple_holds_alt | [C] |
| DescentHeightCondition | desHLeaf_alt (TPS/DesHLeaf.lean:13) | [C] modulo record fields |
| RankGapBound' | rankGapBound_alt (TPS/RamifiedSumsFifthBound.lean:16, 112 lines, read) | [C] modulo record fields |
| RamifiedSumBound' | ramified_sums_seventh_bound_alt | [T] arithmetic |
| DescentPolynomialCondition | desPol_alt | [T] arithmetic |
| LeafWeightBound | wt_tie_alt | [T] over SizeAt |
| LeafMinimalMass | mm_tie_alt | [T] |
| LeafKernel | leafKernel_of_linK_injK_constK_formula2K | [T] over F3 |
| LeafUniqueMap | oneMap_of_bundle_setAt_kernel_conditions | [T] over F3 |
| LeafFixedPoint | fp_tie_alt | [T] over F2 |
| LeafHeightMapBound | leafHeightMapBound_tie_of_infK | [T] over F2 |
| LeafInfinitePlaceBound | ipb_of_lamLow_alt | [T] over ON (LambdaLowerBound2) |
| LeafUniqueSquareRoot | oneSq_of_log_derivative_bound_thA | [T] over F1, F5 |
| LeafDensity | den_tie_alt | [T] over F1 |
| LeafIntegrality | int_tie_alt (60 lines, read in full) | [T] over F1, F4 |
| ArchimedeanCondition | arch_tie_of_logDeriv_bound | [T] over F4 |
| LeafThetaBound | thb_tie_alt | [T] over F1 |
| BundleCondition | bundle_of_rows_alt | [A] |
| ExistsFunctionIn | ex_of_claims_alt | [T] over F1, F5 |

Log-derivative bound: logDeriv_LFunction_at_one_le_along_family_alt reads the record field `params.logDerivative_le_power` [C].

### Intermediate groups (residual R1)

```
F1 square_top_term_joined_estimates (LTD/SquareTopTermJoinedEstimates.lean:13)        [R] EARLIEST BLOCKER
     completedHeckeL_bounded_in_vertical_strips, fieldDat, lNe_of_functionalEquation,
     heckeLValue_upperBound_permutedWeights_of_FE, ToricExist.torEx, betaConjugate_mean_logAbs_bound_of_transport,
     DenExist.denEx, DenSumPf.denSum, thbSt_of_inputs (85), botSmall_holds, botConst_of_theta_matching,
     bottomPairs_exist_baseTuple, bottomPairsExistEveryTuple_of_cmThetaHypotheses, normBig_of_lNe,
     lValueRatio_lower_bound_gauge, triEx_of_howe_duality_real, bottomTheta_nonvanishing,
     tower_of_theta_matching_lNe, oneSqSt_of_claims' (218)                                [U]
F2 sum_size_finite_away_archimedean_combined                                             [R] 14 producers [U]
F3 joined_local_sum_estimates -> thetaLift_row_properties; injK_of_separates            [R] [U]
F4 NormSum.inp_all (24), intSt_of_forall_inp (32), archSt_of_inp (8)                      [S]
F5 thmA_upper_alt (13), square_ratio_at_point_of_leading_term_alt (27)                   [S]
F6 JoinOut                                                                                section 2
```

## 2. JoinOut, CM-period integrality (follow-up of 22 Nov: CLOSED MODULO NAMED EXTERNAL THEOREMS)

Setting (IsFieldData): E CM, abelian over Q, CM type induced from K = Q(sqrt(-d)), d prime > 4; every CM period is a period of Lambda = O_K, Omega^12 = Delta(Lambda).

```
JoinOut = ToricDenominator /\ Transport /\ TwistedTransport /\ ZetaDenominators /\ Refl
  <- join_out_of_literature <- literature_nonexistence <- published_results_eigen     LIVE
  <- joinOut_of_five (DP/JoinOutOfFive.lean:15) -> joinOut_of_jetInt -> joinOut_of_lat (DP/ToricPeriodZetaOfLatticeValueStatements.lean:21)   [A]

ZetaDenominators <- ZetaDenom.zetaDenominators (DP/PartialZetaDenominatorsCMFieldOfSiegelKlingenDel.lean:146)   [E]
    Siegel-Klingen (rationality), Deligne-Ribet congruence with c = (a): (1 - a^N) zeta_F(C,1-k) in Z_l   inZl_mul_zeta (78) [S]
    m_l(N) by LTE: cmValues_minPadicVal_bound (36) [C]; sum bound dividedPowerValuations_cESum (44) [C] checked N <= 2e5, ratio <= 0.337

ToricDenominator <- ToricDenomRow.toricDenominator (DP/ToricDenominatorOfZetaDenominators.lean:39, 58)   [A]
    classTerm_rep (14), exists_isLatSum (101), exists_isHeckeL_of_hasInf (32), finPart_eq_one          [S]
    LatIntRam <- latIntRam (77, read) ; LatIntUnr <- latIntUnr (83)                                     [A]
      Expansion <- JetExp.expansion_of_jetInt (20): divides by kappa!, pays |kappa|(1+[l=2])           [A]
      DefiningCoordinates.Statement <- DerivAtOrigin.statement (13) <- heckeWeightTwo_of_fe (43)       [S]
      JetInt <- JetIntElliptic.jetInt -> core (DP/CMLatticeDividedPowerJetIntegralityOfHyp.lean:142, 109, read)   [A]
        (uses PartialZetaFunctionalEquation only; SKDR, HilbertClassFieldJ, EllipticMainTheoremCM ignored)
        HilbFam.sz_jet_conj (DP/SzJetConj.lean:24, 35, read)                                          [A]
          jet_conj_expand (35, read): jet = sum_mu rco * (-(s2+wp)/T^2)^{|kappa-mu|} * h_mu, h_mu holomorphic, level N   [C]
          size_values_hfun -> HilbFam.SizeGL.main (16, read) -> sz_hfun_coef (137), TwistSize.main (68),
             weierstrassTorsion_qExpansion_integral (14)                                               [S]
          QFam.sz_value_of_family (22, read) -> QFam.isIntegral_value_div (15, read)                   [C] level-one q-expansion principle
        SzTau.main (DP/ImportsRestLast.lean:23, read)
          JInt.main (31, read): j(tau) algebraic integer via modular polynomial                          [C]
          CMSize.main (DP/DenominatorBoundWeierstrassCmTorsion.lean:30, read)                            [C, tested]
             v_l((s2 + wp(P))/Omega^2) >= -c_l, c_l = 0 (l not | 2d), 1/2 (l = d), 1 or 2 (l = 2), l not | M
             LatTorsVal.main (20) [S]; IsogFormula.main (59) [S]; quasiPeriodConstIsogeny_thm (Masser) [C, tested];
             SzRamified.main (50), ArithThreeInert.main (47) [S]
        HilbertEis.eisExp (40), LipschitzTR.lipschitz (98), iterD_defSum_eq_jet (34), RoadE.passl (76)   [S]

LatAlg  <- latAlg_of_siegelKlingen (143, top read)        [R] q-expansion with rational coefficients + q-expansion principle (Damerell)
LatConj <- LatConjEll.latConj (193, top read)             [R] Galois action on q-expansions (qConj_family), WpFamGL.transport_GL (36, read),
                                                              s2 transport NormSqOfSquareEqNeg.main (38, read in full, via Masser)
Transport <- transport_of (35, read) <- HilbertClassFieldJ, EllipticCM.exists_transports (98, top read, elementary), transportFor_of (60)   [E]
TwistedTransport <- twistedTransport_of_latClaims (15) <- PeriodEx <- periodEx_of_mainTheorem (23, read) <- EllipticMainTheoremCM   [E]
Refl <- refl_of_functionalEquation (11, read) <- refl_square (96) <- HeckeTateFunctionalEquation   [E]
```

External: Siegel-Klingen; Deligne-Ribet (1980); Hecke functional equation (partial zeta, Hecke L); K(j(O_K)) Hilbert class field (Weber, Hasse, Deuring); Shimura main theorem of CM (1971, Thm 5.4). Katz (1978) NOT used. All five proved internally (Layer 3).

Independent checks: Masser's (alpha^2 - d) s2 = sum wp(Q) over ker(alpha), alpha = i sqrt d, d in {7,11,13,17,19,43}, to 400 digits. CMSize.main: (d, M) in {7,11,19,43,67,163} x {2,3,5} (subset) and d = 13 with M = 2, 3; denominators at l not | M only at 2 and d; -1/2 attained at l = d; integral at inert 3 and 5; v_2 >= -1 (d = 13) within the bound -2.

Strength risk of the first version: WITHDRAWN.

## 3. Open0 and ON (residual R3)

```
open_orbit_of_unramified_exponents_alt (TPS/OpenOrbitOfUnramifiedExponents.lean:39)    [A]
  hPA    PrimAt.linkedAt_hPA                                    [C] witness transport
  hDcPtG rowE_dcPt_linked_alt  (LIVE)                           [R] projection/idempotent lemmas
  tie    TieOfLink.hasTie_of_linked                             [R]
  selJ   JoinLinked.selJ_of_bWit                                [R]
  mi     miStarRow_alt_alt (LIVE)                               -> PC-4 (MIstar2)
  hDivG  DivLinked.hDivG_linked_of_mIstar2                      [R]
  hLamP  LamLinked.isotRank_of_wit_alt, rowConditions_at_companion_from_readings,
         finiteTypes_via_full_heckeAlgebra_eigensystems         [R]
  kap    KapLinked.row_kap_of_row_lam_alt_alt (24)              [R]
  good   GoodLinked.row_good_alt_alt                            [R]
  lab    LabLinked.row_lab_of_layer_alt_alt                     [R]
  geo    GeoZeroAt.geometricWeakTies_of_linked_ties (RayField)  [R]
  df     linkedAt_prmR_df_of_cuspRapidDecay                     [R]
ON  ontoX_of_hypotheses_alt_alt (18), lamLow_of_hypotheses_alt_alt (19)   [A] children [U]
```

Correction: the entries are internal packages, not "one named theorem applied to published statements".

## 4. Record inequalities for the FR-12 gap: CLOSED

```
countClauses_closed (Proofs/FlagMeasures/CountClausesClosed.lean:58)  LIVE                [A]
  Closed.large (SmoothDesignExistence/DGamSmooth.lean:38)                                    [C]
  linkThresholds, link_thresholds_spec (CSN/StandingHypothesesHoldFamily.lean:1667, :1671)   [C]
     last slot max(2, 2*C, 8*C_Gamma) with C = c30(cOut).C fixed by the outer constants  =>  2 <= C_l, 2C <= C_l
  sCl = min(CfL, Cw, CDel, CCount, Ch0r, Cgap) (CSN/LeSCSCl.lean:13)                         [C]
  standing_hypotheses_of_bounds -> log_root_discriminant_le (CSN/StandingHypothesesHoldFamily.lean:1110)   [C]
     rd_E <= 2 n x^(eps/100) sqrt(qd), log q, log d <= X^21, C_l <= X = x^(eps/100)  =>  log rd_E <= L / C_l
  countParameterConditions_of_sizeHypotheses -> gap_product_le_of_bounds                    [C] (Wave 4)
```

The value 1.6e15 (C_g + 4) never needs to be checked. Not independent work for Agent 5.

## 5. Nonvacuity on the live route (residual R4)

```
hypotheses_nonempty_of_unramified_exponents_alt (TPS/HypothesesNonemptyOfUnramifiedExponents.lean:41)   [A]
  member_bundles_large_unramified_exponents_alt (TPS/MemberBundlesLargeUnramifiedExponents.lean:34)    [A]
    compatibleSystem_member_hypotheses, compatibleSystem_member_rationalWeights,
    compatibleSystem_weightOne_saturated, member_multiplicatively_closed_alt,
    hyps_e_third_layer_ser_n_of_geometric_galois, member_exists_baseLattice_alt,
    compatibleSystem_weilBlock_ne_alt                                                                 [U]
  window_lower (LIVE), DsP_pos_and_lower (LIVE)                                                       [S]
```

## 6. FR-10 (PC-7)

```
Dict.DualMark.dual_marking (STT/DualHalfLevelMarkingExistsAndMatch.lean:317)                [C] elementary
  exists_form (trace-form duality), cSep_spec (CRT), exists_dual, exists_dual_sub_mem,
  mem_of_dual_mem, mark_eq_of_dual, exists_roots, conj_half                                   [S] in-file, elementary
Dict.MarkLift.exists_lift_marked (STT/ExistsLiftMarked.lean:358)                            [A]
  anFib_lift_ex (142), exists_aut, LevelActionLaws.exists_move (exists_sim, exists_levAut),
  move_fibre, rho_eq                                                                           [S]
  frames_lift_to_cover <- firstFiveLaws <- allSixLaws <- abelianSchemeLaws_all,
     furtherLaws_of_laws, twistBaseChange                                                     [R] residual R5
     candidate boundary: uniformization of PEL moduli and level covers (Shimura; Deligne 1971; Kottwitz 1992 §5; Lan 2013 ch. 1)
series_bound producers (IEV/)                                                                  [R] residual R6
  LevelFourier.smul_mem_trSp (171)       exists K, forall M ...  level independent            [S]
  ConstBound.const_dvd (52)              exists c, forall l2 ... level independent             [S]
  LevelSeries.exists_flip_theta (76), exists_move_denomAt (68), ArchAct.real_act_harm (50),
  clsScal_mem_valRing (127), PinBase.baseCc_of_framePin (89)                                  [U]
Galois-side leaves                                                                              unchanged (cleanup pass)
```

## 7. Small-leaf sweep

| Item | Mark | Note |
|---|---|---|
| CarrierXAll.lean:451 budget | [C] | A0 is chosen as decayThreshold itself in carrierDataBuilt_of_hyp; `polys` checked symbolically (Kst = 5) |
| con_trace g^N to g | [C] | algebraic over F_l and in the maximal ideal, so zero; no condition on l and N |
| five facts of all_parts_transfer_of_facts | [D] | |
| levelCompare_statement, passageLat_of | [D] | |
| isProdCuspChar_good | LIVE (nonvacuity) | [E] Green's classification of GL_r(F_q) characters; see section 10 |
| UniqGap (two declarations) | LIVE (nonvacuity, rowsPos_typeP) | one proposition; reduces to Jiang-Sun-Zhu 2010 + Sun-Zhu 2012 |
| secondCohomologyBound_of_boundaryBound (two) | LIVE (both) | PositivityTheory: Layer 3 step of Jacquet-Shalika rigidity; UpperTheory.V.Pa: patching ultrafilter limit on the vwin_of_row route, outside PC-6/PC-7 |
| exists_coreTies_of_zeroFreeRegion trace | done | no user |
| testRest_bound (SL-1) | LIVE | via topCovolSlim2_use_alt_alt, deep_slim_use |
| admissible_entries_small_chain, datum_exists_coprime (SL-4) | LIVE | unchanged |
| core2, third_identity, stepB_of, lift1, fixBd, pair_count, detFin, alInj | UNDECIDED | names shared across namespaces; unchanged |

## 8. External boundary

| Entry | Change |
|---|---|
| V17 (inputs of hostEx_of_zeroFreeRegion) | Move to "not shown operative". The recorded route is off route. LogDerOne is live as a field of ThetaLocalInputs and discharged internally by LogDerOneProof.logDerOne_holds (Layer 3; partial-fraction formula, Davenport ch. 16). Jutila, PageThm, TZRat, QuadraticHeckeZeroEstimates: every consumer theorem found is off route except the bundles ArithmeticGeometryHyps and PublishedTypesAtPlace (undecided). ExplZeta, ExplChi, ZeroCount, ZFRDirichlet: undecided consumers explicit_formula_used, zeroCount_holds, zFRDirichlet, ZeroFreeHalf.main, HostZeroFree.main, QH.twistK, page_across |
| V18 (psi_thin) | stays; QH.thinH LIVE |
| RayField | stays; explicit argument of live rowFun_at_gridA_alt and geometricWeakTies_of_linked_ties |
| Hermitian slope inequality (Block B) | now the stopping point of the FUN core |
| New (JoinOut) | Siegel-Klingen; Deligne-Ribet; Hecke functional equation; Hilbert class field via j; Shimura main theorem of CM. Katz not used |
| New candidate | uniformization of PEL moduli and level covers, for allSixLaws |

## 9. Smallest residual list (current after the fourth follow-up, section 12)

No residual remains in PC-6 or PC-7. The former residuals and their final status:

| theorem | live consumer | mathematical assertion | mechanism | external boundary | verdict |
|---|---|---|---|---|---|
| R1 SurjectiveOntoX (ontoX_of_hypotheses_alt_alt, TPS/OntoXOfPrints.lean:28) | allRows_of_open0_alt (nonvacuity) | the local index bound IndefData.ON for theta-image lattices at split places, plus the weighted global sum bound | idempotent and Mackey lattice algebra over the level group (local_bound), share bound, place-class depths, explicit absorption (on_core); ten estimate statements | RayField, Green, Bhatt-Scholze, Chebotarev, Clozel, base change, Serre-Tate; FormalTorsion.fhSt to PC-1 | [E] |
| R2 LambdaLowerBound₂ (lamLow_of_hypotheses_alt_alt, TPS/LamLowOfPublished.lean:17) | LeafInfinitePlaceBound of FUN | log λ_σ(p) ≥ lowB = hookPlus − 8 f n_V² log(b·rd·g0·g1·n_V) ≥ l6m for the eigenvalue of θθ* on every isotypic part at every embedding | Rallis inner product formula at the base embedding (AdelC), formal degree via compact dual and hook formula, mass bound; Galois conjugation (conjRatLift5) and complex conjugation elsewhere; p = 0 by scal.abs | CuspRapidDecay, WeilSiegelFormulaUnitary, SiegelEisensteinContinuation, doubling, unramified doubling, Bernstein-Zelevinsky, FormalDegreeCompactDual | [E] |
| R3 LevelSeries.series_bound (IEV/SerIntAtOfSeriesRat.lean:137) | SerStd.untwRatS | l^c θ is an O-combination of rational sections integral at algebraic points, c independent of level | lattice generation, Schrödinger/Fock formulas, valuations (seven producers) | GlobalArtinReciprocity at seriesRatS_and_serInt_of_globalArtin; Weil 1964 | [E] |
| R4 SL-1..SL-4 live copies | see section 12.4 | identities and valuation arguments | see section 12.4 | Turán's second main theorem | [C]/[E]/transferred |

Single earliest blocker: none inside PC-6/PC-7. First item resting on another package: hodgeTate_inclusion_chart via FormalTorsion.fhSt (PC-1).

Does PC-6/PC-7 still block "the live RH route has been reconstructed in ordinary mathematics modulo named external theorems"? No. It still depends on the transfers of section 12.6.

## 10. Second follow-up (22 November 2026): live PC-6/PC-7 interfaces

Legend as above. [T4] = transferred to PC-4 (bottom/anchor theta producers).

### 10.1 Forward live set

Forward closure of riemannHypothesis with namespace/open-aware resolution: 841,665 declarations; second pass with parents and without cross-file matching of top-level helpers (core, key, aux, ...): 840,206. Outside = off route. Inside = live once a single-candidate path is printed and checked in the source.

### 10.2 The three route questions

| Declaration | Status | Path (checked) | Content / classification |
|---|---|---|---|
| GlobalTheory.GapIn.UniqGap | LIVE | allChi > everyCharacter > everyCharacter_of_row > every_character_of_literature_of_vWin > every_character_of_theta_integrals_local_matching > nonempty_hyps_definite_side_of_closed_bound > hypotheses_nonempty_of_unramified_exponents_alt > rowsPos_typeP > bessel_multiplicity_one_large_gap_and_whittaker_bessel | Bessel multiplicity one for U(p,q) discrete series with gap >= 120 n^3; [E] Jiang-Sun-Zhu GAFA 2010 + Sun-Zhu Ann. Math. 2012; archive proof besselMapUniqGap / uniq_of (74) |
| CompanionTheory.Lime.BM.UniqGap | LIVE | same; uniqGap_and_besselOfW > uniqGap_holds | same proposition (uniqGap_of_uniq) |
| PositivityTheory.AdelicQuotientData.secondCohomologyBound_of_boundaryBound | LIVE | every_character_of_literature_of_vWin > published_results_eigen > jacquet_shalika_of_literature > jacquetShalika > jacquetShalikaRigidity > rsPole > rsPole_of_inputs | weighted representation + smooth-vector intertwiner; Layer 3 step of Jacquet-Shalika 1981 |
| UpperTheory.V.Pa.secondCohomologyBound_of_boundaryBound | LIVE | everyCharacter_of_row > vwin_of_row > automorphic_window_of_inputs > ... > modU_of_printsH > pFromAut > V.Pa.norm > V.Pa.core > cohLim | patching: ultrafilter limit of second Selmer classes mod t^m; outside PC-6/PC-7 |
| GlobalTheory.GoodCharProd.isProdCuspChar_good | LIVE | ... > hypotheses_nonempty_of_unramified_exponents_alt > allRows_of_open0_alt > row_rRows_stage0_alt > eventually_small_of_seeEx_primitive > small_along_alt > indefScale_theta_degree > passIn3_at_realT_alt > passIn3_of_rows > goodCharacter_placewise_cuspidal_parabolic_product | [E] Green 1955 (Zelevinsky LNM 869 ch. 9); read in full (34) + irreducible_character_good_idempotent_cuspidal_product (27, top) |

### 10.3 F1 = square_top_term_joined_estimates (LTD/SquareTopTermJoinedEstimates.lean:13)

Hypotheses (all discharged upstream in nonempty_hyps_definite_side_of_closed_bound): HoweDualityReal, ThetaLocalInputs (53 Published fields), HeckeFunctionalEquationAbs (from HeckeTateFunctionalEquation), JoinOut components, ThetaIntegralsAgree, LocalMatching (Final F).

| Output | Producer (unwrapped, lines) | Inputs | Status |
|---|---|---|---|
| FieldDat | fieldDat (10, full) | record | [C] |
| LNe | lNe_of_functionalEquation (11), lNe_square (33), heckeL_ne_zero_int (44), IsHeckeL.ne_zero_nat (full) | Hecke FE, strip bounds, L(1,chi) != 0 | [E] Prop. 5 |
| (strip bounds) | completedLBoundedInStrips (38, full) | partial series | [E] Hecke's continuation, proved internally |
| LBound | lBound_of (77, full) | FE, strips, PL lemma, gridSizes_log_bound | [E] Prop. 6 (Phragmen-Lindelof; weaker than Rademacher convexity) |
| TorEx | torEx (30, full) | toricSum_eq, Transport, LNe | [E] |
| BetaArch | betaArch_of_transport (103, top) | Transport, LBound, sizes (134, top) | [E] |
| DenEx / DenSum | denEx (8) / denSum (127, top) | ZetaDenominators | [E] |
| ThbSt | thbSt_of_inputs (85, top) | ToricDenominator, DenSum, BetaArch | [E] |
| RhoLow | rhoLow_holds + core (110, top) | ToricDenominator | [E] |
| BotSmall | botSmall_holds (9) | record | [C] |
| BotEx / BotExT | botEx_holds (8) / botExT_holds (13) | F4 | transfer over F4 |
| NormBig | normBig_alt (28) | theta_lift_petersson_norm_ratio_formula, big_theta_petersson_norm_ne_zero | [T4] |
| TriEx | triEx_holds_alt (26) | bottom_theta_norm_factorization (139), bottom_theta_lift_ne_zero (33) | [T4] |
| BotNe | bottomTheta_ne_zero_of_innerProduct_formula (53) | NormBig, TriEx | [T4] |
| BotConst | botConst_of_inputs_alt (40) | bottom_constant_ratio_eq_local_factor_ratio, rallis_inner_product_formula_first_occurrence, valuation_proportionalityRatio_le_bottomPairs (F4) | [T4] + F4 |
| Tower | tower_alt_bis (73, full) | five witt_tower_* identities, LNe | algebra [C]; identities [T4] |
| OneSqSt | oneSqSt_of_claims' (218, top) | the above, Refl, F4 | [C] over inputs |

### 10.4 F2, F3, F4, F5

| Group | Finding |
|---|---|
| F2 sum_size_finite_away_archimedean_combined | rowSum_of_hypotheses_alt and finScalK_and_infScalK_of_theta_inputs discard ThetaLocalInputs (explicit sizes, [C] at top); the rest are local-model factorizations over F4 -> [T4] |
| F3 joined_local_sum_estimates | twisted_square_local_matching (64), twisted_theta_integrals_agree (25), weilConvergence_of_siegelSet (SiegelSetUnitary) -> transfer over Final F / [T4] |
| F4 NormSum.inp_all | 22 fields: g1, perm, uni, mu, curve, gal, galEx, t0Ex, use1, alg, conj, nrm, bar, odd3, odd4, rep, model, transl, two, jets, split, eqv. No hypotheses. 21 files, 6,730 lines. RESIDUAL (R1a). Candidates: Shimura 1976 (theta values with CM), Kubert-Lang (units/integrality) |
| F5 thmA_upper_alt (13, full) | ToricRatioConjugates from TwistedTransport (JoinOut), FieldDat, TorEx, record field |L'/L(1)| -> [E] |
| F5 square_ratio_at_point_of_leading_term_alt (27) | bottom_triple_integral_factorization -> [T4] |

### 10.5 Open0 entries (open_orbit_of_unramified_exponents_alt, TPS/OpenOrbitOfUnramifiedExponents.lean:39)

Each entry = LinkedAt p R: for every slot and every built-and-good bundle of the linkage, R holds. Producers are wrappers LinkedAt.of_row (RowE.row ...).

| Entry | Bundle property R | Producer | Row theorem carrying content |
|---|---|---|---|
| hPA | PrimRows3 + TypesSep3 | linkedAt_hPA | [C] (first version) |
| hDcPtG | DcPtG (decomposition point values = period columns) | linkedAt_hDcPtG | rowE_dcPt_linked_alt |
| tie | Nonempty Comparison2 | at_tie_alt | hasTie_of_linked |
| selJ | IndefiniteRealisationJoin exists | at_selJ_alt | selJ_of_bWit |
| mi | MIstar2 (seesaw) | | [T4] |
| hDivG | DivRows3G (sharp/base lattice ties, rational lifts, theta map) | at_hDivG_main_alt | hDivG_linked_of_mIstar2 |
| hLamP | RowsHoldLam3 (isotypic independence and span; eigenvalues = column labels) | at_row_hLamP_alt_alt | isotRank_of_wit_alt, finiteTypes_via_full_heckeAlgebra_eigensystems |
| kap | RowsHoldKap3 (row infinity type = kappa) | row_kap_of_row_lam_alt_alt (24) | from hLamP |
| good | GoodFTAll | row_good_alt_alt (10) | linkedAt_goodFTAll |
| lab | Hida setting + label ties | row_lab_of_layer_alt_alt (4) | row_lab_of_good_alt_alt |
| geo | compatibility point with class-sum pin | geometricWeakTies_of_linked_ties (8) | class_sum_divisor_all_alt |
| df | DefiniteSideCondition | linkedAt_df_of_parameters | DefSide |

### 10.6 Nonvacuity (hypotheses_nonempty_of_unramified_exponents_alt, 21 lines, full)

| Input | Published counterpart | Status |
|---|---|---|
| rowsPos_typeP (UniqGap + BesselOfW) | Jiang-Sun-Zhu 2010; Sun-Zhu 2012 | Layer 3 |
| wuDecayOfGap | Trombi-Varadarajan 1971; Hecht-Schmid 1976 | Layer 3 |
| rowsFinDim_link | Harish-Chandra LNM 62 | Layer 3 |
| litThin (adm6, adm7, adm11) | Montgomery LNM 227 Thm 12.2 (stated exponent 1/4 is weak); Landau-Page; Davenport ch. 14, 16, 17 | Layer 3 |
| rowNGP_of_siegelWeil, rowMainEqP_of_siegelWeil, volumeRatio | convergent Siegel-Weil (published input) | [E] |
| genusMassAt_two | internal (genusMassStd_all) | not reread |
| allRows_of_open0_alt (37), nonempty_hyps_of_allRows_alt (83), final_alt_alt, member_bundles children | assembly | R4 |

## 11. Third follow-up (22 November 2026): F4, Open0/ON, nonvacuity

### 11.1 F4 = NormSum.inp_all (FoundationProofs/CmThetaNormBoundHypothesesSatisfied.lean:29) -> [E]

| Group | Fields | Minimal proposition | Mechanism (producers) | Literature |
|---|---|---|---|---|
| A algebraicity, conjugation | curve, gal, galEx, use1, alg, conj, nrm, bar, g1, perm | Prop. 7: conjugate lattice is delta'c'; torsion transport; rho(s2)=s2(conj); theta coefficients algebraic and conjugation-equivariant; norms | galCurve_holds (38), galStar_holds (48), integral_j_and_algebraic_data (26), cmTheta_taylorCoeff_algebraic_and_conjugate, induced_type | Silverman AT II.2.2, II.4.3; AEC III.8.1; Masser s2 formula. Shimura 1976 related, not used |
| B integrality | model, transl, two, jets, split | Prop. 8: good model; cube; CM laws; jets (<= d^{1/2} at d); split ph ~ 0; translates units | modelEx_holds (87), sigma_add_param (58), frobenius_stickelberger_padic_determinant_formula (24), phAt_mulBy_norm (161), endInt_all (29), jetsPh_of (full), splitZero (full), transl_holds (50), atTwo (37) | AEC IV, VII.5.5; Frobenius-Stickelberger; sigma addition formula; Masser. Mazur-Tate 1991 + Katz 1976 and Kubert-Lang related, not used |
| C Weil rep | uni, mu, odd3, odd4, rep, t0Ex, eqv | Prop. 9 (i)-(vii) | theta_translation_intertwiner_unitary (21), triple_constant (70), vacuum_inert (75), vacuum_scalar (28, full), exists_rep_trivial_at (24, full), exists_point (full), exact_equivariance | Weil 1964; Mumford Tata III; Kudla 1994; weak approximation |

Numerical check (checks/f4_jets.py, d=7, E: y^2+xy=x^3-x^2-2x-1): s2 = 1/4 exactly for the wp-lattice of the short model; jets i=4..22 integral at p=3,5,11,13,17,23,29,37,43; normalized jet2 has |.|_7 = 7^{1/2}; exp(ph(T)) integral through T^14 at split 11,23,29,37,43, fails at inert 3,5,13 (not claimed there).

### 11.2 Open0 -> no internal residual

| Prop | Entries | Mechanism | Verdict |
|---|---|---|---|
| O1 | hPA, hDcPtG, tie, selJ, lab | fields of the witness w.x (rowConditions_at_companion_from_readings, recursion_local_row_condition_alt, tie_of_rpk_alt, join_subspace_real_data_lattice_alt with Schur, ties_of_genPin_goodFTAll') | [C] formal |
| O2 | hLamP, kap | isotypic orthogonality, spherical eigensystems (Schur), liftMat_bij surjectivity, dimension count, settled multiplicity engine (twisted_multiplicity_eq via pseudo-coefficients) | [E] |
| O3 | good | depth-zero LLC, Green, Zelevinsky | [E] |
| O4 | geo | linked_ties_alt over RayField | [E] |
| O5 | hDivG | MIstar2 (PC-4) + base-level complex data + rational pairing law | [E] given PC-4 |
| O6 | df | rowsU_of_colPins_alt (68, top) + memberRows_of_kernelDatum_sizes | [C] mechanism level |

### 11.3 ON -> residual

| Statement | Producer | Inputs | Verdict |
|---|---|---|---|
| LambdaLowerBound₂ | lamLow_closing_alt, lamLow_of_weak, conjRatLift5 (18, top) | Weil-Siegel, Siegel-Weil, doubling, unramified doubling, BZ finiteness, formal degree | RESIDUAL R2 |
| SurjectiveOntoX | ontoX_of_hypotheses_alt_alt (full), ontoX_of_twist_shares_exp_alt | Green cuspidal, Clozel cohomological, l-adic Hecke characters, Chebotarev, CuspU, base change definite unitary, Bhatt-Scholze lattices, LLC (llOf_alt), Casselman-Wallach | RESIDUAL R1 |

### 11.4 Nonvacuity

| Producer | Verdict |
|---|---|
| DsP_pos_and_lower (full) | [C] |
| window_lower (top) | [E] SiegelMassRatioCM |
| recExP_of_recAtG, memberTop_final_contextParameters, classSel (full) | [C] |
| nonempty_hyps_of_allRows_alt (83, full) | [C] assembly |
| allRows_of_open0_alt (37, full) | [C] assembly given Open0 and ON |
| member_bundles children | [E] |
| final_alt_alt (top) | no new mechanism; Selmer engine theoremE_corollaryA_closing_all_data outside PC-6/PC-7 |

## 12. Fourth follow-up (22 November 2026): ON, series_bound, small leaves

Correction: SurjectiveOntoX delivers IndefData.ON (IndefSide.lean:318), a local index bound, not a surjectivity statement. allRows_of_open0_alt turns it into surjectivity onto p.N(C, C_H).

### 12.1 R1 (ON), Proposition 12 of the pdf [E]

- onto_path_alt (TPS/OntoPath.lean:18) [A]: exists_isRec, twistedPlacesBoundChain_twoRunChain, onClauses_with_error_of_splitPart, on_of_onWith_canonical; on_base_atPlaces, on_core_atPlaces → on_core.
- on_core (IT/ExampleSatisfiesConditionsAtFive.lean:603, 270 lines) [C]; local_bound (line 409) [C]: idempotent e_ψ with denominator |U|, Mackey decomposition, scaling costs E·rank + r; share_numeric (n_Z/[P:U] ≤ 3D); depths by place class; local_sum_exact, budget_numeric, absorb_local_conditions_exact with C_E ≥ 4C²+25C+C_b+44.
- Page/geometric/depth: pageSt_alt, geoSt_of_pageSt_alt, leafDepth_all_run [C] given the chart statements.
- AvFSt colength_bound_split_place_chart, UpFSt unramified_companion_chart_characters [T][E]: split formal group law uniformization (Serre-Tate canonical coordinates).
- HTFSt hodgeTate_inclusion_chart [T] → FormalTorsion.fhSt: Lie ⊆ W ⊆ (ζ_p−1)^{-1} Lie, transferred to PC-1 (Fontaine 1982).
- Runs: exists_run_pins (71 lines) [A][C]: TameFinitePart.exists_xiRec, FinalJoin.exists_top_of_core, FinalJoin2.FullExt.exists_full_of_xiRec.
- Rational: twistedClassSums_rational_of_rayClassFields [E] (RayField).
- Maximum: spanOverClasses_of [E] through SeriesRatS (R3).
- Rank: rankLocSt_of_max_geo_runs [C]. Twist: twistSt_of_alt (40 lines) [A][C].
- Share: isWhit_and_eq_embLL_inv_and_halfUnip (48 lines) [T][C], shareSize_bounds.
- Bad places: badWSt_of_greenCuspidal_of_modelSt [E] (Green).
- Exponent: expSt_of_alt, LeviCut.exCut [T][E] (Bhatt-Scholze, Chebotarev, Clozel, base change).
- Reading depth: run completion, share Whittaker vector and Levi cut reconstructed from statements and first steps.

### 12.2 R2 (LambdaLowerBound₂), Proposition 13 of the pdf [E]

- lamLow_of_hypotheses_alt_alt → lamLow_closing_alt → lamLow_of_weak (DP/LiftEigenvalueLowerBoundOfWeakCharacterisation.lean:20) [A].
- Base embedding: liftAdjoint_eigenvalue_lower_bound_base_embedding (scalar_of_lift_ofCore, scalar_on_part_ofCore, lowTop_ofCore) [A]; AdelC via adelC_of_innerProductFormula (AVP/DivisorProofs/AdelCOfInnerProductFormula.lean:249) [A].
  - innerProductFormula_of_hypotheses [T]: CuspRapidDecay, WeilSiegelFormulaUnitary, SiegelEisensteinContinuation.
  - finiteZetaL [T]: BernsteinZelevinskyFiniteness, UnramifiedDoublingGL; finiteZetaC_of_finiteZetaL [T].
  - fockCoefficientC [T] (HarmonicModule from harmonicModule_of [C]).
  - formalDegreeUpperC_of_hypotheses [T]: FormalDegreeCompactDual.
  - massLower_of_stdV [C]; deltaNorm_all [C]; HookPlusLeMainTerm [C].
- Other places over K: rationalLift_lowerBound_off_basePlace, lowForm_six, lower_overK_six, conjRatLift5 [A]; not over K: complex conjugation; p = 0: scal.abs.
- Constants: thetaLift_weightSizes_eventually_along_family, hookLogSum_sub_sizeTerm_le_lowerBound.
- SiegelWeilUnitaryConvergent is an unused argument of adelC_of_siegelWeil_of_doubling_alt.

### 12.3 R3 (series_bound) [E]

- LIVE: GlobalTheory.LevelSeries.series_bound (IEV/SerIntAtOfSeriesRat.lean:137, 104 lines) [A]. Path: … nonempty_hyps_definite_side_of_closed_bound → hypotheses_nonempty_of_unramified_exponents_alt → hyps_e_third_layer_ser_n_of_geometric_galois → exists_hyp_n_of_geometric_galois_compat → seriesRatS_and_serInt_of_globalArtin (GlobalArtinReciprocity) → untwisted_theta_rational_on_good_covers → SerStd.untwRatS → series_bound.
- Producers, all [C]: LevelFourier.smul_mem_trSp (171), LevelSeries.exists_flip_theta (76), LevelSeries.exists_move_denomAt (68), ArchAct.real_act_harm (50), ConstBound.const_dvd (52), clsScal_mem_valRing (127), SerId.exists_forms_of_transSum (54; given the IsDict/FrameTie dictionary of the consumer). None takes a Published hypothesis.
- PinBase.baseCc_of_framePin (named in v1) does not resolve.
- GlobalTheory.KZ.ExpBound.series_bound: q-series tail bound, 54 lines [C]. Formalism.FN.WDiv copy [D].

### 12.4 R4 (small leaves)

| declaration | content | verdict | route |
|---|---|---|---|
| FourierDecayAlt.P.third_identity | EnergyAbsoluteIdentity from the signed identity, polynomial_sign (interlacing), types_interlace, boxes_fit | [C] | CarrierGap via poincareLelong |
| FourierDecayAlt.P.MAx3.F.core2 | matrix identity along cut words | [C] | same |
| FourierDecayAlt.P.GermSumLattices.core2 | lattice character sum (Gauss sum) | [C] | CarrierGap via germ_identity_bis |
| FourierDecayAlt.P.Fr6.core2 | cancel invertible factor | [C] | same |
| L2.Th1.B.Det.core2 | Weierstrass polynomial identity | [C] | F4 jets |
| TuranPowerSumBounds.core2 | Deuring-Heilbronn from Turán power sums (hypothesis hT) | [E] Turán | primes in progressions, Galois side |
| Reformulated.B.DeterminantIdentities.core2 | determinant lifting | [C] | V-window |
| UpperTheory.V.Pr.core2 | valuation comparison | [C] | V-window |
| PI.UnitKronW.stepB_of | Kronecker's theorem | [C] | finite_order_adelic |
| MainNotions.PlaneGram.stepB_of | valuation collapse after Fock projection, given V2 and PROJ from the admitted record | [C] | G-link (Green) |
| Gal.FiniteEtaleModels.stepB_of | assembly of eight Galois-side statements | transferred | Galois side |
| pair_count | cocycle count bound | transferred | patching (UpperTheory.V.Pa.locV) |

Off route: UpperTheory.TorsionCardinalitySetup.Setup.core2, Formalism.DivisionValues stepB_of. Patching: fixBd, detFin, alInj, UpperTheory.V.Pa.lift1.

### 12.5 Dependency paths

- R1/R2: riemannHypothesis → rhOfAll → allChi → everyCharacter → everyCharacter_of_row → every_character_of_literature_of_vWin → every_character_of_theta_integrals_local_matching → nonempty_hyps_definite_side_of_closed_bound → ontoX_and_lamLow_of_unitaryGroupHypotheses' → ontoX_of_hypotheses_alt_alt / lamLow_of_hypotheses_alt_alt.
- R3: section 12.3.
- R4 (PC-6/PC-7 part): every_character_of_literature_of_vWin → hsUse_outright → poincareLelong → lelongLimitAtBranches → branchProperAtPoint → ProperOpenProjectionBranchLocus.proof → CarrierGap.offDiag → CarrierGap.carrierP → lemma_model → induction_imports → third_identity.

### 12.6 Transfer ledger

- PC-4: bottom theta identities (F1, F3), MIstar2 (Open0 O5). Unchanged.
- PC-1: FormalTorsion.fhSt behind HTFSt. New.
- Selmer engine: final_alt_alt. Unchanged.
- Patching route: pair_count, fixBd, detFin, alInj, V.Pa.lift1, Taylor-Wiles secondCohomologyBound. Not touched.
- Galois-side package: FiniteEtaleModels.stepB_of hypotheses; TuranPowerSumBounds.core2. New.
- Multiplicity engine: settled.
- External audit: Rallis 1987, Kudla-Rallis 1994, Ichino 2004, Piatetski-Shapiro-Rallis 1987, Lapid-Rallis 2005, Li 1992, Bernstein-Zelevinsky, Harish-Chandra 1966 (R2); Serre-Tate canonical coordinates (R1); Turán's second main theorem (R4). RayField and Green already on the boundary.

