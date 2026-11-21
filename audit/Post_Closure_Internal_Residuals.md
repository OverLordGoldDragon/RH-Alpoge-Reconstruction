# Post-closure internal residuals

21 November 2026. Operational form of Section 8 of `Post_Closure_Synthesis.pdf`. Written by the post-closure-wave synthesis agent (Claude).

This file lists the internal packages whose proof bodies have not been reconstructed in ordinary mathematics after the Final Closure Wave. It supersedes `Final_Authoritative_Synthesis/Authoritative_Internal_Residuals.md`. It is a synthesis of reports. Nothing in `src/lean` was opened, built or run in this pass, no existing file was edited, and nothing here is a verification of the archive or a proof of RH. The archive has no `axiom`, `sorry`, `opaque` or `native_decide` (Focused Wave 5), so every entry is a Lean theorem whose proof text has not been read to classical leaves or to a named published theorem. It is not a missing proof.

Sources. The three files of `Final_Authoritative_Synthesis/` and the report and dependency map of each of `Final_Closure_Wave_1` to `Final_Closure_Wave_5`, all read in full. To fix the status of `coreWR` the name was looked up in `Final_6_TheoremE_Adversarial/Final_6_Dependency_Map.md` and `Final_Synthesis/Final_True_Residual_List.md`.

Counting rule. A shared dependency is listed once, at the package that holds it, however many parent theorems it feeds. Two declarations with one mathematics (for example Berger's membership criterion in its Theorem B and Theorem C implementations) are one item with two declarations.

Named published theorems at which the reconstruction stops are in `Post_Closure_Verification_Boundary.md`. The two lists are disjoint.

Paths are under `src/lean/src/`, with the abbreviations of the closure-wave maps: `GP/`, `DP/`, `AP/`, `PC/` (Wave 1); `LLC/`, `RC/`, `QID/`, `IE/`, `FPU` (Waves 2, 3); `DLP/`, `TPS/`, `TO/`, `FM/` (Wave 4); `CB/`, `MSB/`, `GI/`, `HCP/`, `PM/` (Wave 5).

## Count

| | Authoritative synthesis | Now |
|---|---|---|
| Residual entries | 14 (AR-01 to AR-14) | 7 packages (PC-1 to PC-7) and 5 small groups (SL-1 to SL-5) |
| Major engines | 0 | 0 |
| Medium packages | 8 | 6 |
| Small to medium | | 1 (PC-7) |
| Merges | | Theorem B with Theorem C (PC-3); D1 with `FamilyExistsPos` (PC-1); `valX` with class data, unit and Weil producers, bottom and anchor, and the hidden twist chain (PC-4) |
| Splits | | AR-01 into a local package (PC-1) and a global one (PC-2, with AR-03) |

## Summary table

| ID | Package | Earliest blocker | Size | Mechanism | Risk |
|---|---|---|---|---|---|
| PC-1 | local integral Hodge–Tate package at a good prime (FR-15, D1) | `FamEx.TestPt.testFacts` | medium to major | known (Raynaud, Fargues) | moderate |
| PC-2 | global tower and covolume assembly (FR-15, D3, D4, D5, AR-03) | `exists_good_tower`; open constant `SupModel.comp_bound` | medium | known | low to moderate |
| PC-3 | Wach-module calculus below Theorems B and C (FR-08) | Berger level layer: `LevC.secCrit_all` (B), `expCrit_D'` with `frobenius_power_congruence_local` (C) | medium, large in lines | known | low to moderate |
| PC-4 | finite-place harmonic analysis of the seesaw (FR-13) | `GlobalTheory.TriStep.tri` | medium | known | low |
| PC-5 | lattice counting (FR-12) | `count_terms_gramClass_over_sublattice` | medium | known (Siegel, Schmidt) | moderate |
| PC-6 | record construction (FR-16) | sixteen leaves of `FUN` under `fun0Fit_of_leaves` | medium | known at statement level | moderate |
| PC-7 | FR-10 remainder | `Dict.DualMark.dual_marking` | small to medium | known | low to moderate |
| SL-1 | `DeepStR` flag and test leaves, D2 children | `testRest_bound` | small | standard | low |
| SL-2 | rank-four leaves (old AR-11) | residual chains | small | known | low |
| SL-3 | FR-11 frame lemmas, `StepImportsQ` | `core2` | small | known | low |
| SL-4 | FR-18, FR-19, FR-01/02 leaves | FR-18 producers | small | known | low |
| SL-5 | bookkeeping | `UniqGap` | small | known | low |

---

## PC-1. Local integral Hodge–Tate package at a good prime

- **Closed above it (Wave 1).** Bodies of `goodOrigin_linked` (`DP/GoodTowerGlobalConditions.lean:197`), `link_step`, `linked_two_levels`, `power_sum_term_linked_tower`, `power_sum_height_model_change`, `log_mul_degFl_bracket_mul`, `model_on_hodge_of_family_pos`, `TopRel.relations`, `CkTop.ckRelations_of_model`, `GoodModel.relations`, `Constants.main`, `HodgeTate.main`, `RelK.main`, `local_comparison_of_orbits`, `lattice_facts_of_normal`. With w = ζ_p − 1, w^(p−1) = u p and Lie ⊆ W ⊆ w^(−1) Lie: ck(Lie, W) + ck(ω, ω^HT) = h_τ − λ_τ/(p−1) and p^k h_τ = h_{Fr τ} + λ_{Fr τ}, solved uniquely on finite orbits by h_τ = Σ_{n≥0} p^(−k(n+1)) λ_{Fr^(n+1) τ}.
- **(a) Test-point facts. Earliest blocker.** `FamEx.TestPt.testFacts` = `GlobalTheory.T.ordinary_curve_hodge_prime` (`GP/OrdinaryCurveHodgePrime.lean`, 137 lines) with `PtDx.main`, `hodge_kernel_image_lattice`, `ordinary_curve_model_relay`, `abelian_factor_tight_field_action`, `quotient_zarhin_hodge_tate_subquotient`, `arith_variety_prime_global_relay`, `arith_variety_model_hodge_relay`, `arith_variety_prime_hodge_total`, `arith_variety_model_prime_total`, `arith_variety_prime_hodge_estimate`, `chartD_th_sqIdeal_mem_and_smul_mem_and_eig_mem_sqIdeal`, `lattice_base_change_larger_ring_holds`. Content: ker H_τ = (ζ_p − 1)^(−1) Lie_τ, im H_τ = ω_τ, and the Frobenius step on the coordinates of the F-vector space scheme G[p].
- **(b) Construction of the lattice family.** The nine producers of `familyExistsPos_holds` (`GP/FamilyPosOfHodgeTateInputs.lean:62`): `Orbit.orbit_exists` (264), `nonempty_genTors` (376), `PackEx.chartPack_exists` (159), `chartD_fun_clauses` (597), `Over.funfam_holds` (790), `FamLat.lat_main` (229), `Seq.seq_holds` (129), `SeqFam.seqfam_holds` (443), `short_exact_standard_lattice`; `GR.Top.main`; `ordinaryCurve_of_hodgeTate`.
- **(c) Local Chern calculus.** `dvr_bundle_statement_a`, `chart_bundle_extension_intersection`, `same_generic_flag_difference`, `same_generic_bundle_chain`, `scalar_quotient_statement`, `same_generic_linear_equiv`, `line_bundle_chart_generic_comparison`, `chart_bundle_intersection_symmetry`, `dual_bundle_intersection`, `RelH.relH_main` (320), `RelSeq.relSeq` (201), `FamConstr.main` (258), `FamGood1.main` (291), and the flag-independence statements of `StatementsFlagIndependence.lean` (`PairNumberExpansionIndependence`, `HsymmPairFlagIndependence`).
- **(d) Model change.** The nine children of `power_sum_height_model_change`, the eight of `link_step`, `flag_m3_of_local_m3` (`DP/FlagM3FromLocal.lean:94`), `model_descent_integral_closure`, and the twelve statement-level children of `model_on_hodge_of_family_pos`.
- **(e) Trivial flag and sandwich.** `hodge_tate_free_trivial_flag_mod`, `trivFlagMod_of_dvd`, `trivial_flag_at_prime` (children of `trivFlagOnHodge_of_fargues`); the D2 children `exists_sandwich_of_hodge_tate_free`, `tangent_vector_extends_dvr`.
- **Size.** Import closure in `AS/Proofs/` 779 files, 50,664 lines (upper bound).
- **Mechanism.** Raynaud's coordinates for F-vector space schemes with Fargues's integral Hodge–Tate sandwich. Not cited by the archive, so Raynaud is not a boundary input. Implementation of a known mechanism, not an engine.
- **Named mathematics it stops at.** `FarguesExact`/`FarguesHodgeTate`, `ZarhinStatement` (V12), `QuotientByFiniteFlatStatement` (Layer 3).
- **Reclassification option.** If `testFacts` matches Raynaud (1974) with Fargues (V20 of the boundary), part (a) becomes an internal proof of a published statement.
- **Downstream.** `FamilyExistsPos` → `HodgeLatticeFlagBound` → `Prop6` → level uniformity of `DeepStR` → `HeightAt` → `UAt` → `lowAt_of_cover` → `L3` → `LinkDIV`.
- **Source.** Final Closure Wave 1, Sections 2, 3, 4, final report.

## PC-2. Global tower and covolume assembly

- **Closed (Wave 1).** `TwistAutProof.twistAut`, `CmpTied.cmpHodgeTied` (top level); `eigLat_slope` and `slope_eig` modulo two small algebraic children; the arithmetic 250 · 25/2 = 3125 ≤ 4000 of `supConst_size_rows`.
- **D3, unchanged.** `full_intersection_generic_bound`, `cusp_weight_regularisations_tied`, `corrected_weight_regularization`, `testPoly_eq_slX`, `intersection_final_estimate` (`StokesAt`), `cusp_weight_integrable_on_fundamental_set`, `intersection_degree_lower`, `rootFlatOnHodge` with `RF.*` (`NearRecord`, C' = 4).
- **D4 remainder.** `exists_good_tower` (`GP/ExistsGoodRootTower.lean:77`, earliest), `rootTower_proportional_of_unif`, `tower_T1_limit_of_inputs`, `tower_I1_of_reference_linked`, `real_tower_convergence_I2`, `i5_and_i6_of_isGlobal_of_goodOrigin`, `global_model_real_tower_smooth`, the nefness producers (`tower_A1_of_real_tower`, `or_m1nef`, `m2_of_good_tower`, `rootModel_nefFib_zero_one_of_nonneg`, `rt_nefgen`, `effDiff_of_goodOrigin`), `volEq_of_isFullIntersectionSystem`, `propA_of_goodOrigin`, `full_intersection_tower_I8_relation` with `PB.Antisymmetry`; `CmpPair` (`Cmp.PairTop.cmpPair`, `GP/CmpPairOfInputs.lean`, 144), `CmpSt` (`comparison_of_inputs_avoidance`); children of `twistAut` (`twist_iso_nonempty`, `twist_ok_all`, `isReduced_moduli'`) and of `cmpHodgeTied` (six). Constants killed by the cutoff limit; the risk is to existence.
- **D5, unchanged.** `exists_small_basis` (`GP/GenericFrameComponentBound.lean:279`), `modelSmall_mul_mem`, `topGrowth`, `exists_geoRead`, `descent_small`, `htLow`, `strict_weight_growth_bound`, `weight_threshold_limit_coefficients`, `countVol_le_of_le_shift_pow`.
- **Covolume leaves.** The twenty-four producers of `topCovolG_alt_alt` (`.../ThirdPlaceSeries/TopCovolG.lean:39`), `span_thFam` (C = 20000), `exists_cusp_regular_level_determinant`, `SupConstSize.supConst_size` (361 lines) with `SupModel.comp_bound` (**open constant**: log supConst ≤ 250 f² r² L), `adelicProb_mul_volFund`, `valuation_multiplicity_of_consecutive_run_alt`, `rk_le_alt_alt`, `fibreAt_defCase`, `levRing_descent`, `deg_eq_of_local_two_curves`, `hirzebruch_proportionality_toroidal` below its published top, `freeOrbit_projector_eigen`, `SumSlope.le_slope_sq_of_sum`, `FlatLine.DefinitePoint.main`.
- **Downstream.** Tower axioms of `DeepStR`; fields of `topCovolG_alt_alt` other than `HeightAt` → `L3` → `LinkDIV`.
- **Source.** Final Closure Wave 1, Sections 6, 8; authoritative AR-01 D3, D4, D5; AR-03.

## PC-3. Wach-module calculus below Theorems B and C

- **Closed above it.** Wave 2: `Relay2.relayCore_of` (`LLC/RelayGeneralCaseOfAdmissible.lean:1244`) with `coreH` clauses (i) to (iv), `coreTr` clause 2, `SATPcore`, `relay_first`, `tr_trunc_int`; `ArcLCore`; the ring, Λ, π₀Λ, frame-basis and `POfSec` clauses of `ArcCore`; assembly of `SplitCore`; case exponents. Wave 3: the eight lemma bodies, `local_lemmas_of_literature`, `length_bound_of_hypotheses`, `PowerSeriesDVRFactorisation`, `RToolNum`, constant 32, the `big1`/`big2` interface. Earlier waves: `coreWA`, `coreWR`.
- **Shared layer S (counted once).**
  - **S1. Generic lifting fields.** Producers of `ConclusionW`, `ConclusionH`, `ExistsUnitClasses` in `LiftingTheory.local_theory_of_admitted` (`LLC/BaseChangePreservesUnitaryOf.lean:4837`). Fields 5 to 10 of the Theorem C record; source of `coreLiftO` (23, 32, 32) for Theorem B. The one item both theorems consume as the same declaration.
  - **S2. Berger level maps and membership criterion. Earliest common blocker.** Theorem B side (R-B1): `LevC.secCrit_all` (`LLC/SecCritAll.lean:168`), `step_mpr`, `step_mp` (`LLC/InFNcSmul.lean:83`), `CrC.level_zero_membership_of_horizontal`, `CrD.secIn_of_fil`, `fil_of_rep`, `LevE.levETie_of`, `expFrame0_of`, `expNoNeg0_of`, `lev0Mpr_of`, `memCrit_of_free`. Theorem C side (C-3): `expCrit_D'` (`QID/IsAdicCompleteOfLe.lean:60`), `lemK_D`, `expRules_of` (`QID/SmulSDivMem.lean:69`), `ring_condition_uniformizer_polynomial`, `memCrit_of` (`QID/JumpsLetExists.lean:218`), `filDim_of`, `basTool_of`.
  - **S3. Truncation and level expansion.** Theorem B side (R-B2): `ArcF.secOfP` (`LLC/ArcCoordinatesOfMembership.lean:811`), `arcHyp_secOfN` (1015), `arcHyp_nOfSec` (1030), `frame_inv_poly` (729). Theorem C side (C-1): `truncatedSeriesData.tTool2_of` (`LLC/HermFlagUnipotentAnisotropicVectorSubMem.lean:1574`), `tTool1_of`, `tTool2Z_DU`, `Tools.frobenius_power_congruence_local` (`LLC/FrobeniusPowerCongruenceOfAdmitted.lean:713`). The truncation half is the statement of the relay's (R1) to (R3), read in Wave 2; the new half is the level expansion `THor`.
  - **S4. Annihilating polynomials in γ.** Theorem B side (R-B5): `annihilator_levels_unramified_statement` (`LLC/AnnihilatorLevelsUnramifiedStatement.lean`, 576) for `KillerLevCore`, `killer_first_theorem_holds` for `KillerKap` with C = 8. Theorem C side (C-2): `Tools.QToolOpen_of` (`LLC/LocalClauseOfFrobeniusHyps.lean:953`), `lattice_clause_every_situation` (`FPU:1966`), `truncatedSeriesData.gamma_lemma_of_crystalline` (`LLC/EqUniformizerMulOfConstantCoeffZero.lean:324`), `letterConditionGlobal_of_N1used`.
- **Theorem B only.** R-B3 `SplitCore`: `Split2.cutData_of` (`LLC/CancelUnitMulUniformizerPow.lean:433`) with `tauZ_exists`, `lift_avg`, `pp_pull`, `e_tf`; `Split.splitCore_of` (`LLC/SplittingOfExactnessAndData.lean:182`); `splitPolarL_of`; `Split.polarToPoleL_of`. R-B4 `UnivCore`, `UnivNNCore`: `LLC/UniversalGeneralOfRestriction.lean` (2,688 lines: `univFrame_of`, `univLift_of`, `univSec_of`), `universal_general_of_inverse_levels`, `UGen.universal_generators_of_units`, `RatW.ratCore_of`, `InvW.levRat_of`, `invLevCore_fin` (largest single item). R-B6 `RC/` cores: `arc_section_map`, `horizontal_frame_structure`, `arc_filtration_low`, `arc_gamma_lift_at` (`HorFrameCore` existence; substantive, since the case theorems quantify over horizontal frames). R-B7 case bodies and children (`liftDelta`, `exists_phiBridge`, `den_step`, `case2b`, `aI_le`, `N_typeT`, `constants_typeT`, `ArcLengthFourFirst.exists_liftsAt_arcOf_exponent_le`, `liftsAt_of_scaled_power`).
- **Theorem C only.** C-4 `kernel_rank_bound`, `filtration_gap_vanishing`, `gamma_levels_expansion`. C-5 `contentBoundLevel_of` (`QID/SmulSeriesDeltaZero.lean:273`), `pass3`, `pass4`, `fam_exp`, `cmp_of_mem_X`, rank lemmas (`QID/RkMultVNonneg.lean`, `QID/RkFilLevEq.lean`). C-6 `lemmaDN_of_S1E` with `zTool_of`, `adaptBas_of`, `gMem_of`, `detTool_of`, `detAlg_of`; `lemmaDN0_L` (published type, Wach, Berger). C-7 `frobenius_sq_bound_of_local`, `rhoLift_of`. C-8 `cocyclesToWachVectorsBound_of_extTool`, `extData_extTool`, `first_lift_of_uniformizer_clause`, `second_lift_of_hypotheses`. C-9 `TheoremCAdm.admissible_ranks_of_CMDatum` (`IE/LocalLiftingTheoremCHypothesesAdmitted.lean:21`) and five top producers (bookkeeping; fields 11 to 19 on the boundary).
- **Size.** B side at least 10,000 lines by file counts; C-1 alone about 2,300.
- **Mechanism.** Completely known: Theorem E on Wach modules, Berger level maps, truncation, γ-polynomials with LTE, Lagrange interpolation, Newton polygon of lev(p₁), Herr complex.
- **Constants.** 32 at l = 11 (leading 31.108, maximum ratio 0.9718) and σ ≤ 3 Sg for l ≥ 11 (maximum 2.46) confirmed from tool statements; `KillerKap` constant 8 in an unread body.
- **Downstream.** Theorem B (rows C, D with a non-thick letter) and Theorem C (rows C, D, all letters thick) → `LengthBoundAtPlaces` → `LinkN`.
- **Source.** Final Closure Waves 2 and 3.

## PC-4. Finite-place harmonic analysis of the seesaw

- **Closed above it (Wave 4).** `GlobalTheory.ValFin.valX` (`DLP/SeeSawFiniteIntegralsDoubleStepValue.lean:93`): six exact identities, c_V(j) = κ(j,σ) sc_j sc_{j+1} c_Q(j) c_G(j) c_T(j) with c_Q(j) = Π_q (idx_q(j+1) idx_q(j+2))^(−1); the level scalars a and a^(−1) cancel; `CVEq` definitional in `colSide_alt`; c(t)/c(t₀) a root-of-unity ratio; `cell_collapse`, `DStepLev`, `DStepSupp` read; `jOf_exists`, `kernel_identity_tuple`, `exchange_isPos`, `valOne_all`, `innerVal_iter2`, `valQ`, `qLaw_of_pin` read.
- **R-1. Split-place twist layer. Earliest blocker.** `GlobalTheory.TriStep.tri` (`DLP/SplitPlaceDoubleStepTrilinearFormProperties.lean:88`, 145-line file), `PosOne.SymComb.symDbl_comb` (213), `PosOne.comb_eq_sum_cells` (190), `QPl.LineCancel.val_om_loc` (101), `LocModMove.isModel_weil_off` (95), `LocGl.local_group` (256), `RootEx.ExchangeSupport.exchange_support` (`TO/RootExchangeSupportAndFourierRelation.lean`, 240), the children of `symDbl_existsUnique`; induction leaves `QVal.valQr_zero`, `QRed.reduce` (416), `IterPeel.iterated_integral_product_groups` (266), `QVal.Inv.pint_invariant` (392), `QCells.finite_cells` (414), `QValOuter.outer` (144), `QVal.LevCO.isCO_levJ_levB`, `QVal.inner_supp`, `VacAway.vac_comb`, `HaarR.quot_int_haar`; `QLastPf.qLast_of_pin` (194), `QFinMain.qFin_of_pin`.
- **R-2. Off-level and level-place laws (parallel inputs of `valX`).** `FinPl.suppFirst_all`, `FinPl.suppSecond_holds`, `FinPl.FlatVacuum.flatVac`, `ContrComb.contr_comb_main`, `LastVacPf.lastVac`, `gValue_common`, `GSuppAsm.gsupp_of_local`, `LocMod.SuppFirst.gsupp1`, `LocMod.GSuppTwo.gsupp2_std`, `LocOm.omLoc`, `FlatBFLoc.flatBF_of_laws`, `LocMod.flatFB_holds`, `ContrLocProof.contrLoc`, `symCollapse_of_allPositions`, `allPositions_holds`, `lawLevelPrime_all`, `CollapseFactor.collapse_factor` (340, Fubini of published type), `SeeSawRhs.unfolded_eq_kernel_data` (155), `SeeSawLastValue.valLast` (360), `VReal.v_real`, `DisjComb.main`, `VMove.seeSaw_iteratedIntegrand_vacuumForm_base_points_alt`, `FlatIndep.flat_indep`, `HandHom.hand_hom`, the second-variable analogues `LeftSecond`, `DStepOffSnd`, `DStepLev.integ_mul_level`, `DStepSuppSecond`, and `CellLevels.levels`, `FinPl.SetCut.grp_split`, `AdelicSplit.adelic_split`.
- **R-3. Producers of `colSide_alt` (hidden dependency, small).** `readsExists_alt`, `QuadraticExtensionData.dat_exists`, `vol_level_wt_const_alt`, `KomExist.exists_compactOpen_alt`, `FinData.main_alt_alt`, `colOf_readS_alt`, `places_under_alt`, `famOf_eps_mem_alt`, `AdForm.kernels_keep_ramL`, `qLev_of_reads_alt`, `qVec_pinTup_alt`, `famOf_pinTup_combAt_alt`, `chartZero_colOf_alt` (`TPS/`).
- **R-4. Class-data grandchildren.** `pureTensorO_zero_eq_jetP` (399), `stdPair_world`, `AdForm.realOf_is` (`DLP/TrueColumnsRealDataSpec.lean:44`), `AdForm.exists_readsG_of_level`, `lev_law`, `twDat_reps`, `rd_charts`, `clsKL_real`, `kval`, `thetaKernel_splitPlaces_eq_jet_classicalTheta`, `isReps_stabOrd_top`, `law_top`, `top_translate`, `tailTop_eq_of_pin`.
- **R-5. Unit, Weil, bottom, anchor (old AR-07 included).** `exists_ne_zero_scalars_gVec`, `exists_descent_data_chain_alt`, `weil_tuple_root_alt`, `FamChars.weilOK_of_rank_one_gram`, `RowLevel.main_alt_alt` (`TPS/OffLev.lean`), `MiTop.linkComm_of_laws_alt`; `colDict_rd_eq_colForm`, `ConjRowRep.exists_contRep`, `exists_isShift_of_center_alt`; record fields `nuQ_weil`, `wfr_on`, `SBes.cpt`, `inHH_closed`.
- **Size.** About 3,000 lines named in R-1; namespaces of the layer at most 53,166 lines in 391 files.
- **Mechanism.** Linear (Schrödinger) model of the Weil representation of GL_a × GL_b, root exchange, mixed models, Fubini over places.
- **Downstream.** `valX`, c_V, `ClsPinD` → `KerX`, `PerX`, `RdX` → `MIstar2` → `BesselId` → `LinkDIV`, `FrameF`.
- **Source.** Final Closure Wave 4, Sections 2.1 to 2.4, 4.

## PC-5. Lattice counting (FR-12)

- **Closed above it (Wave 4).** `RowCounts.uniform_counts` and `LoopRowBoundsGap.rows_along_family`; the constants c₃, c_H, c_S, c₄ enter only as a family-uniform lower bound on C; `gap_product_le_of_bounds`; `ThmSOwn` low gap.
- **Counting lemmas.** `count_terms_gramClass_over_sublattice` (shared child; **earliest**), `mean_count_primitive_sublattices_over_genus`, `LoopC.PairMean.main` (`FM/OneLeSizeZ.lean:242`), `LoopC.GenericMean.main` (`FM/CntClLeEncardMul.lean:178`), `LoopC.Partner.partners_le` (`FM/OneLeProdReal.lean:190`), `GramHeight.height_bounds` (`FM/EquivIntegral.lean:461`).
- **(g).** `LocModel.clK_core` behind `localModelK_holds` (`.../RankPointCounts/LocModel.lean:1768`); `localModelT_holds` (`DataCut.lean:411`).
- **Counting-engine leaves, untouched since the closing synthesis.** `near_count` (584), `NearUnip`, `unfoldBound` (`IwasawaFormula`, `RadicalCovolume`), `nonzeroFlagBound`, `deep_kernel_bound_of_ptBound`, `absoluteVolume_of_volumeStep`, `oneVectorCc_of_siegelWeil` (428), `siegelMeanCc_of_oneVectorCc`, `volumeStep_of_siegelMean`, `rowsAdd_holds`, `rowsGood_holds`, `etUnip_holds`.
- **Open check.** The level idempotents of the `LinkS` dimension clause against the condition of `NearUnip` (not addressed by Wave 4).
- **Downstream.** `MainTheorem`, `KVIdentity`, row counts of the loop rows, the dimension clause of `LinkS`, `LinkIRR`.
- **Source.** Final Closure Wave 4, Section 2.6; authoritative AR-08.

## PC-6. Record construction (FR-16)

- **Closed above it (Wave 5).** `pairRows`, `realBox`, `AnyGrp`, `QH.thinH` (modulo V18); `qdBig`, `rank_basic_bounds`, `boundedTw`, `isChiField`, `thickFrame2`; assemblies `not_evG_false`, `exists_chGood`, `exists_std_large`. Call-site check of `HostEx` done: live through `hostEx_of_zeroFreeRegion` → `exists_richRec_of_zeroFreeRegion` → `exists_coreTies_of_zeroFreeRegion`.
- **`FUN`. Earliest blocker.** `fun0Fit_of_leaves` with its sixteen leaves (`Development/AbelianVarietyTheory/Definitions/Divisors/TwistedPlaceChoiceLiesOverPair.lean:345`): μ_max(R) ≤ x^(C_H) b − mean_v log κ_v, through denominators of zeta values and toric periods. Feeds `L3`, `LinkDIV`.
- **Record cores.** `stepW_core` (61-line assembly over `AmbEx`, `DivEx`, `ThEx`, `exists_latticeLayer_kernelDatum_trueColumns`), `step_start`, `stepW_builtE`, `exBL_isLinked_prmR`, `level_three_to_four`, `exists_thetaData_trueRowsColumns_allCompatible`, `goodE_of_builtE`.
- **`Open0`, `ON`.** The eleven `Open0` entries other than `mi` (`open_of_hypothesesUE`); the `BigOn` lemmas of `ON`.
- **Nonvacuity leaves (route live).** `exists_chGoodW` (23 lines), `window_lower` (299-line file), `exists_levCh_of_levelPrime` (114), `Inh.g_big`, `DuInt.duStarOf_nat`, `DsP_pos_and_lower` (86); base layer `ev_preX_frame`, `nonempty_fieldDat`, `rayField_le_and_exists_base`, `Inh.exists_fixed`, `BaseEnl.exists_enl`, `lg_colIn`, `exists_sel`, `exists_ambIn_ok`; `Formalism.HC.exists_hostAx`.
- **Gap-supply check (from PC-5).** Trace `hCl3` (C_l ≥ 2C) and `H11` (log rd_E ≤ L/C_l) of the family to their producer; with C = 8·10¹⁴ (C_g + 4) this needs C_l ≥ 1.6·10¹⁵ (C_g + 4), compatibly with the other record conditions.
- **Downstream.** `HostExW`, `CBHyp`, `adm2`, the passage, `DIVinN`; `FUN` → `L3`, `LinkDIV`.
- **Source.** Final Closure Wave 5, Sections 3, 4, 8; Final Closure Wave 4, Section 2.6.

## PC-7. FR-10 remainder

- **Closed above it (Wave 4).** `AdMark.exists_marking` with `exists_lift`; the `series_bound` assembly (`IE/SerIntAtOfSeriesRat.lean:137`) with c = vK + c_f + c_a + c₃ independent of the level.
- **Markings.** `Dict.DualMark.dual_marking` (317-line file; **earliest**), `Dict.MarkLift.exists_lift_marked` (358-line file) with `anFib_lift_ex`.
- **Producers of `series_bound`.** `vacuum_pair_uniform_level_bound`, `exists_centralFlip_thetaTranslate_halfLevel`, `exists_levelSeries_translate_boundedDenominator`, `real_rational_point_acts_harmonic_substitution`, `ConstBound.const_dvd`, `splitSupportedClassScalar_mem_valuationRing`, `baseCc_of_framePin`.
- **Galois-side leaves (unchanged).** `residual_irreducible_of_theorem_three_prime`, `Conclusion42`, `TripFin.triplesGood`, `good_finite_types_all`, `SeriesRat`, `HeckeTransform`, `RatioConj`, `heckeInt`, `heckeReadTie` (classed as published type or `litN` by the cleanup pass).
- **Downstream.** `SerN` → crystalline lattices of Corollary A → `LinkN`.
- **Source.** Final Closure Wave 4, Section 2.5.

## SL-1. `DeepStR` flag and test leaves

`testRest_bound` (444-line file), `hhTestBound_hhFl` (374), `flagHeight_holds`, `hhFl_labelInv`, `antisymPerturbation_holds`; children `rest_sum_primes_bound`, `lie_term_flag_bound`, `factorial_half_power_sum_le`, `flag_degree_weight_formula`, `flag_shift_total_power_sum`, `Small.sum_log_div_pred_le`. D2 children other than the sandwich: `compact_datum_intersection`, `adapted_family_exists_on_eigenspace`, `exists_action`, `LabPt.exists_labVal`, `AbPartConst.lieMult_constant_along_cmType`, `labelled_degree_commensurable_bound`, `labelled_degree_eq_log_index`, `Cusp.torusPartDegree`, `OrthSum.normDegree_rank_iSup`, `cusp_intersection_height`, `cusp_intersection_finite`, `small_points_over_number_field`. Source: Wave 1, Sections 5, 7.

## SL-2. Rank-four leaves (old AR-11, untouched)

Elementary interiors `tan_lowest`, `rank_le_of_lowest`, `eii`, `fibTrdeg`, `fib_gen`, `nicePrimeEx`, `Loc.v0e`, `elts2`, `adj2`; Wave C standard leaves 4, 5, 7, 8, 9, 10 (residual chains, frame and lattice, rank-four Hida children, seed children, count children, host leaves of case V). Source: authoritative AR-11.

## SL-3. FR-11 frame lemmas

`core2`, `Kop_contract`, `DnM_diag`, `part_U`, `part_sum`, `part_alt_alt`, `new_vector_letter_plus`, `c_diagonal`, `frame_module_of_word` (`HCP/IsAdmissibleSplittingCharPairMulTwist.lean`); the eleven fields of `StepImportsQ` other than `third_identity` (measurability, positivity, polynomial dependence on the shift, residue and ratio bounds). `third_identity` reduces to clause (ii) of `ModelWordsD` (closed) and the hypothesis `JEigen`. Source: Wave 5, Section 5.

## SL-4. FR-18, FR-19, FR-01/02

- FR-18: producers of the definitions `FactorialDigitSplitAtRing`, `DerivativeCongruenceAtRing`, `ExtendedModelRank`, `ExtendedKappaBound`, `ExtendedDichotomy`, `adm22`; `stepB_of` (108), `stepC_of` (19), `stepDEF_of` (13), `phi_pair` (30), `lead_bound` (38), `RestCols`, `RestPre`, `RestTCore`, R8 (`PickStep`, `MembStep`, `NumStep`, `MemStep`, `OntoAll`, `IsTrueTheta`, `RestPad`, `SumFacts`, `WalkSharp`); `valuation_window_lower_bound`, `windowMeanAP` below `Top.windowFullAP`. Small to medium.
- FR-19: `admissible_entries_small_chain`, `datum_exists_coprime`, `Cnt.core`.
- FR-01/02: `secondCohomologyBound_of_boundaryBound`, `lift1` (109), `fixBd` (87), `pair_count` (44), `kills` (six declarations), `split_of_ss` below its top, `Det.matFg`, `Det.finSub`, `conj_const`, `testEx`.
- Source: Wave 5, Section 6.

## SL-5. Bookkeeping

- The choice between the two declarations of `UniqGap`.
- The step of `con_trace` from g^N to g when l | N.
- The budget at `.../RootLatticeThresholds/CarrierXAll.lean:451` (hypotheses `hAe`, `hA0`, `hAh`, `hgap`; margin of degree 7.5 against 19 in n).
- The five idempotent and metric facts of `all_parts_transfer_of_facts`; `isProdCuspChar_good`, `levelCompare_statement`, `passageLat_of`.
- The route declaration of `secondCohomologyBound_of_boundaryBound` (two declarations).
- The trace of `exists_coreTies_of_zeroFreeRegion` up to `Main.lean`.

---

## Reconciliation of the authoritative list

| Old | Class | Where the remainder went |
|---|---|---|
| AR-01 D1 | bodies CLOSED; identity REDUCED TO SMALLER INTERNAL CHILDREN | PC-1 |
| AR-01 D2 | `height_comparison_global_model` CLOSED; sandwich children REDUCED; other children REDUCED | PC-1, SL-1 |
| AR-01 D3, D5 | STILL SUBSTANTIVE (unchanged) | PC-2 |
| AR-01 D4 | `TwistAut`, `HodgeComparisonCompatibility` CLOSED; `FamilyExistsPos` merged into D1; tower producers STILL SUBSTANTIVE | PC-1, PC-2 |
| AR-02 | four leaves CLOSED; rest REDUCED | SL-1 |
| AR-03 | `eigLat_slope` CLOSED modulo two small children; rest STILL SUBSTANTIVE | PC-2 |
| AR-04 | relay, `ArcLCore`, half of `ArcCore` CLOSED MODULO NAMED EXTERNAL THEOREMS (V8); rest REDUCED | PC-3 |
| AR-05 | eight bodies and supplier CLOSED to tool hypotheses; tools REDUCED | PC-3 |
| AR-06 | `valX`, c_V, `CVEq`, unit ratio CLOSED; laws and class data REDUCED | PC-4 |
| AR-07 | STILL SUBSTANTIVE (small) | PC-4 (R-5) |
| AR-08 | `uniform_counts` and open check CLOSED; gap supply CLOSED conditional on record constants; rest STILL SUBSTANTIVE | PC-5, PC-6 (check) |
| AR-09 | `exists_marking`, `series_bound` assembly CLOSED; rest REDUCED | PC-7 |
| AR-10 | host size lemmas CLOSED or CLOSED MODULO NAMED EXTERNAL THEOREMS; nine analytic inputs of `HostEx` and `RayField` MOVED TO VERIFICATION BOUNDARY; `FUN`, cores, `Open0`, `ON` STILL SUBSTANTIVE; nonvacuity leaves REDUCED | PC-6 |
| AR-11 | STILL SUBSTANTIVE (small, untouched) | SL-2 |
| AR-12 | `ModelWordsD` CLOSED; `third_identity`, `Xw_eq` REDUCED | SL-3 |
| AR-13 | FR-09 CLOSED; FR-19 trace bounds and three assemblies CLOSED (modulo `CM2`); `detFin`, `alInj` mechanisms CLOSED; rest REDUCED | SL-4 |
| AR-14 | STILL SUBSTANTIVE (untouched) | SL-5 |

## Outside this list on purpose

- The fidelity of every named published statement (`Post_Closure_Verification_Boundary.md`).
- The archive's own Lean proofs of published theorems (Layer 3), including `litN` and the term behind each of the 54 `Fact` instances.
- A kernel replay.
- Refereeing of Sections 7 to 9 of the manuscript.
