# Final Six Wave 2. Dependency map of PC-2 (global tower and covolume)

22 November 2026. Agent 2 of the final six-agent wave (Claude), for Jimmie Adriazola. Companion to `Final_Six_Wave_2.pdf`. Nothing in `src/lean` was built or run, and no existing file was edited. This is a reconstruction map, not a verification of the archive or a proof of RH.

Marks. [P] proof body read in full. [P top] statement and top read, every child named. [S] statement only. [N] constant checked numerically. Paths under `src/lean/src/Development/`: GP = `AutomorphicSpectrum/Proofs/GeometryProofs/`, DvP = `AutomorphicSpectrum/Proofs/DivisibilityProofs/`, AV = `AbelianVarietyTheory/Proofs/DivisorProofs/`, TPS = `AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/`, FC = `WeilBound/CoreStatements/FlagImmersions/`.

## Verdict (third revision, 22 November 2026, after reopening Lemma 8.7)

**RESIDUAL: Proposition D (report §13) at places of non-abelian semi-abelian reduction.** That is the existence, along a complete curve in characteristic p > 2, of the O_E-equivariant de Rham datum (Hodge sequence 0 → L^∨ → H → L → 0 and conjugate sequence 0 → F*L → H → F*L^∨ → 0, with the conjugate inclusion injective on every fibre) for the Lie bundle of the semi-abelian scheme. The eigenflag inequality of Slijepčević's Lemma 8.7 (archive: `CurveSemiAbelianConjecture`, proved by `m2Curve_holds`) is reconstructed with a complete human proof from that datum (§12 below). On the abelian locus the datum is H¹_dR with the Hodge filtration and Katz's conjugate filtration (Katz 1970; Oda 1969). Everything else in PC-2 is closed modulo named external theorems at the human-proof level, and clause (ii) of 2.A depends on PC-1.

Earlier verdicts the same day: RESIDUAL CHILD REMAINS (first pass), CLOSED MODULO NAMED EXTERNAL THEOREMS (§10), RESIDUAL CHILD REMAINS with Lemma 8.7 as the one bespoke residual (§11).

## 1. Bergman / sup-norm constant (CLOSED modulo named external theorem)

```
supConst_size_rows  [P]  log beta <= 4000 (f r Lb)^3,  L = 25/2 Lb,  250*25/2 = 3125 <= 4000  [N]
└─ supConst_size  (AV/SupremumConstantLogBound.lean:288)  [P]  log supConst <= 250 f^2 r^2 L  [N]
   ├─ chart_factor_size [P]   log 8 n!/(pi rho^2)^n <= 3 log 2 + 14 f r^2 L
   ├─ multBd_size [P] + epsLev_bounds [P]   log multBd <= 86 f r^2 L + 8 f^2 r^2 L
   └─ massLev_size [P]   log massLev <= 80 f r^2 L
      ├─ log_classNumber_le_log_abs_discr_div [P]   h <= sqrt(dE)(1+log sqrt(dE))^(2f)
      │  └─ classNumber_le_of_finrank_eq_two_mul [S] (Minkowski bound + ideal count)
      └─ log_size_bounds_class_number_volume [S] (elementary real inequality)

supPet_principal (AV/WeightedFrameSumPositive.lean)  [P]   sup|P|^2 <= supConst * Pet(P)^2
├─ SupModel.comp_bound [P]  (rewrites epsilon)
│  └─ supLoc_component (AV/CuspFormSupNormLePeterssonIntegralComponent.lean:67) [P]
│     ├─ near-max point z0 with pnorm(z0) > sup/2 ; factor 4
│     ├─ maxBound_holds (.../FundamentalDomains/MaxBoundPf.lean) [P]   thick part
│     │  ├─ periodic_schwarz [P]  Schwarz lemma on q-disc ; 2^{w/2 - f w - 1} < 1  [N]
│     │  └─ herm_eq_zero, flowDomainCriterion_holds, m3bNorm_holds, tendsto_zero  [S]
│     ├─ ModeHalfC.orthonormalize [S]
│     ├─ submean_chart (AV/SubMeanValueFlagChartInvariantMeasure.lean:94) [P]   factor 2 n!/(pi rho^2)^n
│     │  ├─ enorm_pow_le_inv_measure_mul_lintegral_ball [P] (sub-mean value, internal)
│     │  ├─ volume_ball_euclideanSpace_complex [S]  vol = pi^n rho^{2n}/n!
│     │  └─ chart_near_one (AV/NormFactorAndDensityNearOneInFlagChart.lean:97) [P]
│     │     │   nfac^2 >= e^{-1/20}, density >= e^{-1/10}, e^{3/20} <= 2  [N]
│     │     └─ dmin_rmul_near_one [S]  (minor perturbation |log d_i| <= 9 r^2 rho)
│     ├─ chart_mult_le (AV/CardGroupElementsChartReturnLe.lean:155) [P]   returns <= multBd
│     │  ├─ maj_le_four [P]
│     │  ├─ exists_short_basis_at [S] (154 lines; Minkowski-type short basis, Bd = (2fr)^4 dE^2/(4 eps))
│     │  ├─ majorant_chart_point_centre_factor_two [S]
│     │  └─ encard_selfDualLattice_bounded_majorant_le [S] (packing count (1+2 sqrt(R/eps))^{2fr})
│     └─ lintegral_chart_le_mul_fundSet [S] (unfolding, 69 lines)
├─ adelicProbability_eq_normalised_fundamentalSets [S]
└─ framed_dictionary_bound = MassLev.mass_components_le [S top]
   ├─ massBound_of_tamagawa (AV/MassBoundOfTamagawaUnitary.lean:15) [P]
   │  ├─ Published.TamagawaSpecialUnitary   ** NEW EXTERNAL: tau(SU) = 1, Prasad volume formula **
   │  ├─ covolume_realSpecialUnitary_eq_flagDomain_mass = SUCovol.covolume_realSU [S]
   │  ├─ unitary_frames_strong_approximation = ClassSum.sum_covolume_le [S]
   │  ├─ equivalence_generated_torus_rel, det_eq_one_unitary_principal_congruence_level_three [S]
   │  └─ volumeConstant_le [S]
   └─ torusBound (AV/NormOneTorusClassNumberBoundProof.lean:14) [P]  torus classes <= h M^{2f}
      └─ normOne_classes_le_classNumber, NormOneMod.normOne_mod, Det.exists_isKM_det_eq [S]
```

## 2. exists_good_tower (top CLOSED; construction lemmas remain)

```
TopTower.exists_good_tower (GP/ExistsGoodRootTower.lean:77) [P]
  hypotheses: Top.Given (from Link.given_of_use / given_of_moriwaki), Out.WeilSt (lawsFieldsSeparately),
              Flat.FlatLineGenerator, Flat.FlatLineGeneratorComponent
├─ Comps.finite_nonempty_maximal (GP/GenericPointsFiniteNonempty.lean:88) [P]  Noetherian + quasi-sober; N1c
├─ bad = primeFactors(2 |disc E| lcm(M,A));  S_B = {p <= B} ∪ bad   [P]
├─ comp_data [P]
│  ├─ isCptGen_of_maximal (GP/IsCptGenResidueFieldGeneric.lean:52) [P]
│  ├─ exists_reference_geometry_same_generic = Ar.exists_refGeo (GP/ExistsReferenceGeometrySameGeneric.lean:172) [P top]
│  │  ├─ exists_coords_for_component = Ar.exists_eigBase            ** EARLIEST BLOCKER ** [S]
│  │  ├─ coords_with_constants_map = Ar.exists_flagStep [S]
│  │  ├─ generic_coords_descend_subfield = Ar.exists_sat_model [S]
│  │  ├─ snc_model_reindexed_coords = SncRefine.isSncModel_refine [S]
│  │  ├─ complex_coords_reindexed = CoordsDown.coordsAt_down [S]
│  │  ├─ embeds_generic_of_char_zero = EmbedsOfTie.embedsGeneric_of_coordTie [S]
│  │  └─ component_generic_char_zero = CharZeroModel.charZero_function_field [S]   (under ResKStatement, V12)
│  ├─ reference_geometry_holomorphic_inverse (10 lines) -> hodge_cpt_flag_xdeg [S]
│  ├─ ExRefEff.exists_eff (51 lines) [P top]: reference_geometry_multihomog_form, nef_polarization,
│  │     lattice_tensor_power_degree, hodge_cpt_birational_arith_var, global_reference_gap_positive
│  └─ RefRoot.refRoot (65 lines) [P top]: same_orbit_of_proportional_coords, lie_model_push_along_map,
│        holomorphic_inverse_chart_value, holomorphic_atlas_coord_compat, ample_of_single_coord_block,
│        algebraic_constants_in_range
└─ level_data [P]
   ├─ ChangeGeo.exists_cover (GP/RootOriginGoodPrimesFinite.lean:49) [P top]: exists_finite_extension_primes,
   │     coords_after_finite_extension, generic_point_factors_open, hodge_comp_comparison_{left,middle,right},
   │     hodge_cpt_label_bases, hodge_cpt_projective_model, smoothGenericFibre_of_dominates
   └─ root_model_on_cover (GP/RootOriginCoordsOverField.lean:38, 186 lines) [P top]: exists_analytic_log_resolution,
         log_resolution_{reindexed,potential_pullback,functorial_holomorphic}, hodge_comp_descent_{first..fifth},
         positive_homogeneous_potential, flat_on_log_resolution_corr, dominating_*, degree_reindexed_coords, ...
```

## 3. D4 axiom producers (wrappers CLOSED; delegated bodies remain)

| producer [P] | delegates to (residual) |
|---|---|
| `i5_and_i6_of_isGlobal_of_goodOrigin` | `RootFieldNumerics.global_model_tower_fifth_condition` (FC, 9 lines) |
| `tower_A1_of_real_tower` | `real_tower_mean_slope_condition` (FC) |
| `or_m1nef` | `HT.rootModel_nefAt_of_hodgeCpt` (under `FarguesHodgeTate`) |
| `m2_of_good_tower` | `Conj.hodge_cpt_global_nefness`; body derives p > 2 and p ∤ d_E from p ∉ S_B |
| `rootModel_nefFib_zero_one_of_nonneg` | `root_model_nef_fibres_base` (FC) |
| `rt_nefgen` | `tower_nef_generic_dominant` (FC, 85 lines) |
| `effDiff_of_goodOrigin` | `global_model_tower_bounds` (FC, 8 lines) |
| `propA_of_goodOrigin` | `real_tower_convergence_I2`, `TowerPropA.propA_of_origin` (with `TwistAut` closed, `CmpPair`) |
| `full_intersection_tower_I8_relation` | `SquareStatements.good_tower_antisymmetry` (with `CmpSt`) |
| `rootTower_proportional_of_unif`, `tower_T1_limit_of_inputs`, `tower_I1_of_reference_linked`, `real_tower_convergence_I2`, `global_model_real_tower_smooth`, `volEq_of_isFullIntersectionSystem`, `Cmp.PairTop.cmpPair`, `comparison_of_inputs_avoidance` | [S], 43 to 65 lines each |

## 4. D5 lattice-point transfer

- `exists_small_basis` [P] CLOSED (rescale a basis).
- `Plug.countVol_le_of_le_shift_pow` [P] CLOSED modulo `term_le_shift`, `tendsto_shift_ratio` (elementary).
- `topGrowth` [P] top CLOSED: growth = vol · flagDeg from `Plug.growth_le_vol_deg` and `uniform_norm_height_count`, under `Pub.NefRR` (V12).
- `descent_small`, `exists_geoRead`, `modelSmall_mul_mem` [P] assemblies over `comp_laws_tower_bound`, `Plug.vs_arch`, `Plug.vs_fin`, `genFrame_exists`, `RdEx.core`, `SmallProd.modelSmall_mul` (residual).
- `htLow`, `strict_weight_growth_bound` (= `Plug.Mult.vs_mult`), `weight_threshold_limit_coefficients` (= `Small.tower_seq`) [S].

## 5. D3 (unchanged, [S])

`full_intersection_generic_bound` (= `Ar.exists_componentData_origin`), `Relay.cusp_weight_regularisations_tied`, `Relay.corrected_weight_regularization`, `testPoly_eq_slX` (86 lines), `intersection_final_estimate` (= `ModelDimension.abelian_cm_stokes_identity`), `cusp_weight_integrable_on_fundamental_set` (= `Cusp.fund_set_mean_cuspW`), `intersection_degree_lower`, `rootFlatOnHodge` (4-line wrapper) with `RF.*`, C' = 4.

## 6. Covolume bound

```
topCovolG_alt_alt (TPS/TopCovolG.lean:39) [P]  -> CovolumeBoundOfX : lcv/D <= mainT + C·unitE eventually
└─ covolX_of_lift_bounds_and_coreLe (TPS/CovolXOfSteps.lean:16) [P]
   └─ lcv_le (AV/CovolumeFromGramAndBounds.lean:39) [P]  loss 12 e^{-x^{ez/7}}(x^A+x^B+C1+C2+1) <= 1 eventually
```

| producer | body (TPS) | lines |
|---|---|---|
| gram | `covering_gram_matrix_of_local_traces_alt` | 4 |
| size | `SizeRows.size_alt_bis` | 1 |
| meas | `MeasRd.covering_measure_reduction_alt` | 10 |
| anchor | `anchor_holds_alt` | 6 |
| deep existence | `DeepExist.exists_deep_covering_level_alt` | 9 |
| deep goodness | `DeepGoodAll.deepGood_alt_alt` | 22 |
| flat degree | `FlatDegProof.flatDeg_alt_alt` | 5 |
| cover degree | `DegProof.covering_degree_eq_alt` [P]: Hirzebruch–Mumford q7, Nadel q15, principalisation q16 | 31 |
| share | `ShareRowsNef.share_alt_alt` | 37 |
| height lower bound | `height_lower_bound_general_alt` | 2 |
| height sums | `ShortRoad.hilbertSamuel_of_component_estimates_alt` | 89 |
| uniform lower bound | `FromComp.u_low_of_cover_hyps` | 9 |
| Σc | `sumC_of_deepGood_alt` | 4 |
| low bound | `LowCover.low_of_cover_hypotheses` | 17 |
| low defect | `DefLow.covering_low_defect_alt` | 30 |
| ring | `RingStep.ring_of_covering_descent_alt` | 41 |
| maps | `DescentMaps.covering_descent_maps_compatible_alt` | 92 |
| rank | `covering_rank_of_descent_steps_alt` | 11 |
| minimal generator | `CovGminTop.covering_gmin_of_gram_deep_size` | 24 |
| flatness | `FlatSplit.flat_alt_alt` | 10 |
| recursion | `liftRecursive_of_gram` | 3 |
| truncation | `covering_cut_of_local_traces_alt` | 4 |
| bad set | `covering_bad_locus_of_descent_steps_alt` | 20 |
| λ-bound | `LamAll.covering_lambda_all_places_alt` | 17 |
| core, rationality | `CoreSlope.coreLe_of_gram_meas_rat_alt`, `covering_rational_of_local_traces_alt` | 9, 4 |

- `CovGmin.span_thFam` (AV/PolynomialCoefficientEmbeddingNormLeOfL1Bound.lean:399) [P]: C = 20000 from `exponent_le` [P][N] (195.5 + 14000 ≤ 20000); residual `Harm.exists_short_harmL_family` [S, 99 lines], `cusp_sub_span_short` [S].
- Other AR-03 leaves [S]: `exists_cusp_regular_level_determinant` (46), `adelicProb_mul_volFund` (70), `valuation_multiplicity_of_consecutive_run_alt` (50), `rk_le_alt_alt` (117), `fibreAt_defCase` (107), `levRing_descent` (85), `deg_eq_of_local_two_curves` (25), `freeOrbit_projector_eigen` (82), `SumSlope.le_slope_sq_of_sum` (58), `hirzebruch_proportionality_toroidal` below its top, `FlatLine.DefinitePoint.main`.

## 7. Signs checked

- `flDefect_vp` = q(v_ℓ(d_E)/[E:Q] − [ℓ = d]); at ℓ = d with different 1/2 it is −q/2 (`flDefect_vp_d`); consistent with `flDefect_vw` = q(ord 𝔡^conj − v(d)) via `flDefect_vw_eq`.
- Cover degree positive (volume and Vandermonde of strictly antidominant weight).
- Bergman constant uses log d_E ≥ 0, rd_E ≥ 1, class number bounded above.
- Prop6 sign: Wave 1, not reopened. CM periods: only via `logOm_bound` (boundary), not met in bodies read.

## 8. External boundary changes

- **Add**: `GlobalTheory.Published.TamagawaSpecialUnitary` (τ(SU) = 1 in Prasad's volume-formula form; Kottwitz 1988, Prasad 1989). Only external input of the Bergman constant.
- Used, already listed: V7 bundles (`PublishedHodgeBundleTheorems` with q7, q15, q16; `HSCore.Quoted`; `GrothendieckDeformation`; `SiegelToroidalIntegral`; `ToroidalForFanKS`; `SemiAbelianLieSeminegative`), V12 (`ResKStatement`, `Pub.NefRR`, `FarguesHodgeTate`), Layer-3 conjuncts of `Top.Given`.
- Not inputs on the paths read: Bergman-kernel asymptotics; Kawamata–Viehweg (field of `HSCore.Quoted`, not met); Moriwaki bigness only via `given_of_moriwaki`.

## 9. First-pass residual list (superseded by §10)

| ID | content | size | mechanism |
|---|---|---|---|
| R2-1 | reference geometry under `exists_refGeo` (`Ar.exists_eigBase` first) | medium | known; **earliest blocker** |
| R2-2 | root-origin construction under `exists_eff`, `refRoot`, `ChangeGeo.exists_cover`, `root_model_on_cover` | medium | known |
| R2-3 | D4 delegated bodies (table of §3), `cmpPair`, `comparison_of_inputs_avoidance` | medium | known; constants killed by B → ∞ |
| R2-4 | D5 children (§4) | medium | known |
| R2-5 | D3 (§5) | medium | known |
| R2-6 | covolume producer bodies (§6) and AR-03 leaves | medium | known |
| R2-7 | Bergman leaves at statement level (§1 [S] entries) | small each | standard |

Single earliest blocker: `GlobalTheory.CompanionTheory.Ar.exists_eigBase` (behind `exists_coords_for_component`, GP/ExistsCoordsForComponentStatement.lean).

Blocking question: yes, PC-2 still blocks "the entire RH proof has been reconstructed in ordinary mathematics modulo named external theorems". No gap, circularity or failed constant was found.

## 10. PC-2 as human-level propositions (revision)

| Prop. | statement | mechanism | named external inputs | downstream | reconstructed | unread formal layer |
|---|---|---|---|---|---|---|
| 2.A tower existence | for every cutoff B and component c, a normal projective model M(B,c) with semi-abelian scheme and O_E-action, Chern-root hermitian lines, smooth generic fibre, B-independent off S_B; full ℓ^4-torsion rational and Hodge–Tate-patched Lie lattices locally free at ℓ ∈ S_B (`R ℓ = 4`, `OmVB`); Mumford-good psh metrics; reference model of flag degree 1, ample | toroidal compactification, snc resolution, O_E-eigenbasis of Lie (`Ar.exists_eigBase`), flag bundle roots, finite extension trivialising ℓ^4-torsion, Hodge–Tate patch, good metrics | PartI, N1ab, N1c (Faltings–Chai, Lan), KeyFormula (Moret-Bailly), ResKStatement (Hironaka), WeilSt, GagaSections, Mumford 1977, FarguesHodgeTate | GoodTowerExistsX → DeepStR | assembly, components, bad set, S_B, meaning of R ℓ = 4 and OmVB | F2-A |
| 2.B qualitative axioms (D4), E/Q abelian, 3q+1 ≤ N | proportionality and equal volumes; nefness on fibres and semipositivity; T1 limit, I1, I2, I5, I6 with tower-dependent O(log B); I8 antisymmetry; PropA Galois invariance | Hirzebruch–Mumford; nefness at ℓ ∈ S_B via Fargues; **nefness at p ∉ S_B via the char-p weighted degree inequality (Slijepčević Lemma 8.7), unread: the one bespoke residual**; continuity of arithmetic intersection, Weyl and Galois actions | PB.Proportional, PB.Antisymmetry, PB.NefPol, PB.Inputs, Prov.HS, Prov.An, FarguesHodgeTate, CmpPair, CmpSt | Steps 1–6 of the tower theorem; constants killed by B → ∞ via exact Prop6 | nine wrappers; ℓ > 2, ℓ ∤ d_E off S_B | F2-B |
| 2.C base settings (D3) | SlopeLower with C_h + C_u/2, C_u = 4; PropF with C' = 4, Λ_B = log(B rd_E) + abs(L'/L(1,χ_d)) | Zhang lower bound on cusp-corrected metric; eigenspace degrees and Chowla–Selberg; Siegel-set bound for cusp weight; flat-degree record plus N/(ℓ−1) and Mertens | ZhangLowerX, logOm_bound, SlopeBoundSt (V11), Prov.An | absolute constant 2C_1 + 17 of DeepStR | tops (Focused 1, Wave 1) | F2-C |
| 2.D transfer (D5) | sl^vol_Z(u) ≥ sl^T_{κZ}(u) − 2 cost_2(B) ‖u‖_1, cost_2 ≤ 60(log B + log rd_E) | nef count ≥ exp(arith. degree); injective trace on products; clearing denominators; countVol shift lemma | HSUse, Prov.HS, Pub.NefRR | top_meanAll → DeepStR | four-step argument, 60, exists_small_basis, countVol lemma, tops | F2-D |
| 2.E sup-norm | sup ‖P‖² ≤ supConst · Pet(P)², log supConst ≤ 250 f² r² L, log β ≤ 4000 (f r L_b)³ | sub-mean value, Schwarz on q-disc, chart returns, unfolding, Tamagawa mass | TamagawaSpecialUnitary (new) | covolume bound | full | F2-E (statement-level standard leaves) |
| 2.F covolume L3 | lcv(M_i)/D ≤ mainT_i + C·unitE with abs(mainT_i − Σ_τ (p−q) a_τ log Ω) ≤ C·unitE | (i) idempotent cut assembly; (ii) top level CM points, Schur functor; (iii) HSAt + ShareAt + DegAt + HeightAt; (iv) flat twist; (v) weight and level descent, theta spanning C = 20000 | PublishedHodgeBundleTheorems (q2, q4, q6–q11, q7, q15, q16, p8), HSCore.Quoted, GrothendieckDeformation, SiegelToroidalIntegral, ToroidalForFanKS, SemiAbelianLieSeminegative, Chowla–Selberg | L3 → LinkDIV | statement, assembly, covering degree, 20000, signs | F2-F |

First-version conclusion (superseded by §11): no bespoke mechanism unresolved. Points for a referee: HSAt via q9; uniformity of C_h, C_u in the level; OmVB at ℓ ∈ S_B through PC-1.

## 11. Comparison with Slijepčević (hexagon:2611.00812v1, Sections 6–8, 11, Appendix A)

| Prop. | his statement | agreement | what he adds | his outline / not understood | we go further |
|---|---|---|---|---|---|
| 2.A tower | Prop. 8.6(1), Def. 8.2–8.3 | yes; adds d ≡ 7 mod 16, O_E/O_E+ unramified (= `Unr` of 2.E), odd level, A = 1; his "normalisation at finitely many primes, not reproduced" = our R ℓ = 4, OmVB | Bierstone–Milman, Włodarczyk, Zarhin, quotients by finite flat subgroups, Mumford uniformisation, AMRT + Lan; no `exists_eigBase` | in outline | yes (assembly, R ℓ = 4 decoded) |
| 2.B D4 | (V1)–(V3), Prop. 8.6(2) | yes; adds E/Q abelian, 3q+1 ≤ p+q, abs(Bad) ≤ 4 abs(Φ)(p+q)² | **Lemma 8.7: char-p weighted degree inequality, threshold 4 abs(T) M ≤ (p−2)g, gives nefness at p ∉ S_B; corrects our Faltings–Chai/Lan attribution**; threshold matches B(u,g) (p − 2 > 4fM/g for p > B) | Lemma 8.7 in outline; "known or new" | yes on wrappers and Prop6; **no** on Lemma 8.7 |
| 2.C D3 | (V5), (V6) with Lg = log(B r) + abs(L) | yes; no constants given | Zhang [138], Gillet–Soulé [44], Moriwaki [91], Yuan [136] | does not see mechanism of (V4)–(V6), dependence on rd and L′/L, or where Zhang enters | yes (Zhang in SlopeLower; C_u = 4, C′ = 4, C_h) |
| 2.D D5 | Prop. 8.5 (mean over components) | yes; level ≤ 15 prime factors; his ar(D) omits the absolute value on Re L′/L (stronger as printed); ours with abs is the supported form | nef Riemann–Roch + birational pull-back/push-forward (matches le_countVol_of_nef) | transport known only through inputs | yes (four-step count, cost 60) |
| 2.E sup-norm | not stated | n/a; his Bergman reference in (Vs) is a different use | Shimura mass formula [113] as second source vs `TamagawaSpecialUnitary`; Kneser [70], Platonov–Rapinchuk [100] for strong approximation; Ohsawa–Takegoshi [98] | n/a | entirely ours |
| 2.F covolume | Thm 8.1, (COV) of Def. 6.16 | shape main + C·unit agrees; his factor 2/[K_S:Q] not reconciled with archive lcv; his (COV) at compatibly ruled points, his open question whether = ruled points (wiring question for PC-6 / synthesis; our 2.F is at RowsTAlt points of CovolumeBoundOfX) | printed sources: Anschütz–Le Bras (q4), Kawamata–Viehweg (q15), Gillet–Soulé/Zhang/Moriwaki (q9), Moret-Bailly/Faltings–Chai (Lie seminegativity), Messing (Grothendieck deformation); no explicit-error HSAt | "some twenty lattice estimates known only through inputs" | yes (main term = anchor-weighted period, five chains, lcv_le, 20000) |

Uniformity: his Prop. 8.5 has absolute C with dependence through rd_E and L′/L, matching 2.C–2.D; he does not explain it, Focused Wave 1 does.

Outcome: five of six propositions confirmed; hypotheses added to 2.B, 2.C; printed sources for several V7 fields (unchecked); one status change, 2.B(ii) nefness at p ∉ S_B is a bespoke characteristic-p lemma (small; plausible mechanism a Verschiebung degree comparison of the kind behind Goldring–Koskivirta partial Hasse invariants, Invent. Math. 217 (2019), a candidate only).

## 12. The characteristic-p eigenflag inequality (Lemma 8.7), reopened

Route (read [P] unless marked):
```
m2_of_good_tower
└─ Conj.hodge_cpt_global_nefness (GP/HodgeCptGlobalNefBound.lean)
   ├─ root_lines_unramified_primes [S]
   └─ rootLineDeRhamModel_holds = Conj.m2Model_holds
      └─ m2Model_of_m2Curve (GP/M2ModelOfCurveBound.lean:166) [P top]
         │   NefThreshold (4f‖μ‖ ≤ (p−2) gap_j) → GapCond (nef_threshold_gap_condition [S]);
         │   curve degree of L_μ = lmuNum (curve_lattice_degree_formula, curve_degree_unique [S]);
         │   function_field_model_exists, function_field_curve_exists, split_characters_unramified [S]
         └─ CurveSemiAbelianConjecture (a proved proposition despite its name) = m2Curve_holds (GP/M2CurveEstablished.lean:60)  == Lemma 8.7
            ├─ lieLat_conjData (GP/CurveLieEigenDegree.lean:114) [P top]  → ConjData (input D)
            │  ├─ curve_family_formal_germ = PositivityTheory.HtPt.Cf.family_ex (WeilBound/CoreStatements/HodgeTatePoints, 299 files) [S]
            │  │   └─ fib_inj ← Cocp.tanpf_inj (CocpMain.lean:85), Ce.geompf_tan (IsPullbackWhisker.lean:1293)   ** earliest non-formal child **
            │  ├─ Conj.Fam.family_conj (AlgebraProofs/FamilyGivesConjugateLieData.lean, 509 lines) [S]
            │  └─ GermLie.germ_lie [S]
            └─ LmuDeg.lmuNum_nonneg_of_conjData (AlgebraProofs/EigenFlagSlopeBound.lean:46) [P]
               ├─ FrobEst.frob_estimate [P]   (p−2)·μ_max ≤ deg L^∨, deg L^∨ ≥ 0
               ├─ ConjEq.subDeg_eig_conj [P] with eq_zero_of_scale [P]   deg L_τ = deg L_τ̄
               ├─ degree_eq_sum_eigen, SubdegMax.subDeg_max, short_exact_sub_degree_bound,
               │  dot_dual_sub_degree_annihilator, sub_degree_mono_injective_hom, subDeg_frob [S, elementary]
               └─ Chain.lmuNum_nonneg with abel_bound (MetricProofs/LmuNumNonneg.lean) [P]
```

Human proof (complete, given D):
1. μ = max deg of a subbundle of L, attained at W0, μ ≥ 0. F*W0 has degree pμ; its image X in H has deg X ≥ pμ. By the Hodge sequence, deg X ≤ deg(X ∩ L^∨) + μ, and deg(Y ⊂ L^∨) = deg L^∨ + deg Y^⊥ ≤ e + μ with e = deg L^∨. So (p−2)μ ≤ e.
2. h(s) = deg H_s = deg L_s − deg L_s̄ (Hodge) and h(u) = p·h(s) for χ_u = χ_s^p (conjugate). Taking s with |h(s)| maximal forces h ≡ 0. So deg L_τ = deg L_τ̄ = a_τ and e = −2 Σ_τ a_τ.
3. Summation by parts gives Σ_τ ≤ g·a_τ + 2Mμ, so Σ ≤ −g·e/2 + 2fMμ ≤ 0, because 4fMμ ≤ (p−2)gμ ≤ g·e.

Constants: p is the Frobenius degree scaling. The −2 comes from the two bounds by μ (the quotient L, and the annihilator in L^∨). 4fM = f places × weight range 2M × the factor 2 from the equal degrees of the τ- and τ̄-eigenbundles. The cutoff B(u,g) gives p − 2 > 4fM/g for p > B. [N] 173,357 admissible random cases gave max Σ = −0.0197; with the gap at 0.3 to 0.6 times the threshold, Σ reached 5.18, so the threshold is necessary.

Mechanism: a Frobenius-pullback degree comparison through the conjugate filtration (Hasse–Witt matrix as F*L → H), plus a Frobenius-twisted eigen-balance and summation by parts. It does not use partial Hasse invariants. HN data enter only through μ_max.

Literature: no published statement of the inequality or of (p−2)μ_max ≤ deg L^∨ was found. Goldring–Koskivirta is not cited (no match found). D on the abelian locus: Katz, Publ. Math. IHÉS 39 (1970), for the conjugate filtration; Oda, Ann. Sci. ÉNS 2 (1969), for H¹_dR and Dieudonné modules; a principal polarisation identifies Lie A^∨ with Lie A.

Residual: D at places of non-abelian semi-abelian reduction (Hodge plus conjugate sequences as subbundles, and fibrewise injectivity of F*L → H). The archive builds it from formal germs in the HodgeTatePoints layer; no matching published statement was found (the expected type is a Faltings–Chai VI canonical extension together with a log-conjugate filtration).
