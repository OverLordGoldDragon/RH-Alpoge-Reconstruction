# Final Six Wave 4 dependency map (PC-4)

22 November 2026. Agent 4 of the six-agent closure wave. Companion to `Final_Six_Wave_4.pdf`. Reconstruction from proof text; nothing in `src/lean` was built or run and no existing file was edited.

Paths under `src/lean/src/`. `DLP/` = `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/`, `TO/` = `.../Proofs/TwistedOperators/`, `TPS/` = `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/`, `LF/` = `Development/AbelianVarietyTheory/Definitions/LatticeFrames/`. Namespace `GlobalTheory` is omitted.

Legend: [R] body read in full, [S] statement read, [C] closed in this wave, [W] stopped at published statement (boundary item), [L] unread internal leaf.

## Verdict

**RESIDUAL CHILD REMAINS.** No gap, no circularity, no new mechanism. One size reclassification: the reference closure of PC-4 is 20,641 theorems in 313,555 lines after sixteen published cuts (22,356 theorems before), dominated by `Fam.colSide_alt` (15,760 theorems). PC-4 is major in size, of known mechanism.

Single earliest blocker: `FlatBFLoc.flatBF_of_laws` (`DLP/FlatMapBesselToFourierJacobiLocalModel.lean:21`), the first unread input of `TriStep.tri`.

## Method of the census

Name index of 1,057,364 declarations in 175,187 files. Reference closure from the 13 roots below, following project names in theorem bodies, resolving `first | exact @Y` redirections, skipping tactic names, recursing through theorems only. Over-approximates through discarded `first` alternatives, under-approximates lemmas reached only through definition bodies.

Roots: `ValFin.valX`, `SeeSawLastValue.valLast`, `SeeSaw.pins_finiteIntegrals`, `Fam.colSide_alt`, `AdForm.clsPinD_of_famCol_of_trueW`, `StepVacForm.main_alt_alt`, `FamChars.weilOK_of_rank_one_gram`, `RowLevel.main_alt_alt`, `MiTop.linkComm_of_laws_alt`, `Core.Mi.colDict_rd_eq_colForm`, `ConjRowRep.exists_contRep`, `MiTop.exists_isShift_of_center_alt`, `SeeSaw.ratio_total_unitRatio_of_parts`.

Self-containment: no root of PC-1, PC-2, PC-3, PC-5, PC-6, PC-7 occurs in the closure.

| closure theorems | lines | declaration |
|---:|---:|---|
| 15,760 | 236,276 | `Fam.colSide_alt` |
| 8,921 | 126,977 | `SeeSaw.pins_finiteIntegrals` |
| 8,610 | 125,913 | `T.true_geometry_family_final_alt` |
| 6,546 | 94,141 | `QLawPf.qLaw_of_pin` |
| 6,304 | 90,262 | `QVal.valQ` |
| 6,227 | 94,722 | `AdForm.clsPinD_of_famCol_of_trueW` |
| 5,905 | 85,331 | `ValOneAt.valOne_all` |
| 5,576 | 79,037 | `TriStep.tri` |
| 4,314 | 59,985 | `ValFin.valX` (laws as hypotheses) |
| 3,369 | 47,204 | `FinPl.flatLaws_all` |
| 2,123 | 29,083 | `SeeSawLastValue.valLast` |
| 2,084 | 29,731 | `StepVacForm.main_alt_alt` |
| 1,538 | 21,794 | `SeeSaw.biAct_all` |
| 633 | 10,702 | `PosOne.comb_eq_sum_cells` |
| 531 | 7,694 | `ConjRowRep.exists_contRep` |
| 460 | 7,003 | `FamChars.weilOK_of_rank_one_gram` |
| 427 | 7,431 | `PosOne.symDbl_existsUnique` |
| 384 | 5,412 | `LocOm.omLoc` |
| 356 | 4,623 | `RowLevel.main_alt_alt` |
| 160 | 1,912 | `Core.Mi.colDict_rd_eq_colForm` |
| 159 | 2,303 | `MiTop.exists_isShift_of_center_alt` |
| 127 | 1,748 | `QuotInt.quotInt_unique_exists` |
| 53 | 641 | `RootEx.Exchange.exchange_isPos` |
| 40 | 582 | `MiTop.linkComm_of_laws_alt` |
| 19 | 224 | `RootEx.ExchangeSupport.exchange_support` |
| 10 | 141 | `SeeSaw.ratio_total_unitRatio_of_parts` |

## Tree below `TriStep.tri`

```
TriStep.tri (DLP/SplitPlaceDoubleStepTrilinearFormProperties.lean:88)          [R][C] assembly
  isBiTheta_add', isBiTheta_zero', isBiTheta_of_prod                            [R][C]
  T.span_schwartzBruhatProduct_eq_top -> LocFlat.CFac.Span.span_prodSB_eq_top   [W14]
  ContractionLocal.exists_normPair, contr_tens                                  [S]
  T.flatMap_besselToFourierJacobi_localModel -> FlatBFLoc.flatBF_of_laws         [L] <- EARLIEST BLOCKER (R4-A)
      inputs: Unf.Flat.flatLaw [L] (R4-B), FinPl.flatLaws_all [L] (R4-B), LocOm.omLoc [R][W1]
  T.flatMap_fourierJacobiToBessel_localModel -> LocMod.flatFB_holds              [L] R4-A
  T.lineContraction_splitPlace_localModel -> ContrLocProof.contrLoc              [L] R4-A
      LocFlat.contrFactor (158)                                                 [L] R4-A
  T.weilCharacter_splitPlace_exists_continuous_nontrivial -> LocChar.weil_char_split   [S] standard local character
  LocMod.GValProof.core_of_bes, hz_link                                         [S]
  T.besselThetaContraction_extendByZero_vacuum_smooth -> ContrComb.contr_comb_main      [L] R4-C
  T.isJointlySmoothBiTheta_twoVarCombination -> FrCombAny.biTheta_biComb         [L] R4-C
  T.doubleThetaLiftValue_bilinear -> TriStep.valK_bilin                          [R][C]
      Lin.per_int, per_add_left, biComb_add, biComb_smul                        [R][C]
      SeeSaw.biAct_all                                                          [L] R4-C
      SeeSawLastValue.contAut_biLift, SeeSmallPf.biLift_sum                     [L] R4-C
      T.besselGroup_quotient_fundamentalDomain_cocompact                        [S] (W8 type)
  T.mem_space_of_typed_automorphic -> TriStep.mem_space_of_typed                 [R][C]
      TriStepMem.eq_one_of_pow_two_pow, SmGL.exists_open_normalised_subgroup_subset   [S]
  TriStep.space, rep, smooth, mem_translate, valK (DLP/MemTranslate.lean)        [R][C]
  T.doubleLiftValue_equivariant_symmetricUnipotent -> TriStep.valK_nEquiv        [R][C]
      per_flagN, LocGrp.mem_flagN_of_mem_N, LocBesChar.psiBes_isLoc             [S]
  T.doubleStepValue_eq_trilinearTensorValue -> TriStep.val_eq_tensorVal          [R][C]
      LocFlat.ContrSum.contr_flat_eq_sum                                        [S]
  T.local_bimodel_translation -> TriStep.valK_gl2                                [L] R4-A
  T.doubleThetaLiftValue_invariant_middleGL -> TriStep.valK_glMid (125)          [L] R4-A
  TriStep.valK_comb (DLP/AconvSingleList.lean:79)                                [L] R4-A
```

## Split-place layer

```
ValOneAt.valOne_all (DLP/SplitPlaceDoubleStepLocalIteratedIntegralProof.lean:56)   [R][C] assembly
  val_translate, sum_rTrans_trc, comb_lin, coe_sum_sub                          [R][C]
  T.splitPlace_doubleStep_trilinearForm_properties = TriStep.tri               [R][C]
  T.splitPlace_local_group_closedEmbedding_integral                             [S]
  T.local_model_weil_operator_trivialAtPlace_isModel                            [S]
  T.doubleStep_local_weil_action_line_characters_cancel                         [L] R4-A
  T.symmetricPositions_doubleIntegral_existsUnique -> PosOne.symDbl_existsUnique [R][C]
      PosOne.bilPos_exUp_exists                                                [R][C]
      PosOne.exists_fj_of_exUp                                                 [R][C]
      T.exists_bilinear_position_middle_vertex                                  [L] R4-A
      T.schwartzBruhat_self_average_heisenberg                                  [L] R4-A
      T.fourierJacobi_target_bilinear_form_integral                             [L] R4-A
      T.exists_linear_isQuotInt_tInt_alt                                        [L] R4-A
      T.schwartzFourierTransformPi_surjective_schwartzBruhat                    [S] Fourier inversion on S(k^n)
      QuotInt.quotInt_unique_exists (TO/QuotientIntegralParabolicUnfolding.lean:259)   [S][W13] checked
  T.symmetricDoubleIntegral_finite_combination                                  [L] R4-A
  T.symmetricDoubleIntegrals_positionOne_eq_cellSum -> PosOne.comb_eq_sum_cells  [L] R4-A
  T.rootExchange_entries_mem_schwartzBruhat                                     [S]

RootEx.Exchange.exchange_isPos (TO/IntegrableOfMemSB.lean:218)                  [R][C]
  integrable_of_mem_SB, avg, avg2, isNEquiv_integral, integral_embX             [R][C]
  rowE_mul_mem, colE_mul_mem, rowE_mul_embX, colE_mul_embX                      [S] block-matrix identities
  SplitWeil.linear_change_of_variables                                          [S] d(mu) = |det m| du
RootEx.ExchangeSupport.exchange_support (TO/RootExchangeSupportAndFourierRelation.lean:203)   [R][C]
  conj_col, conj_row, rowE_add, colE_add, mem_SB_of                             [S]

LocOm.omLoc (DLP/WeilDatumLocalModelFormula.lean:17)                            [R][W1]
  T.localSchrodingerModel_uniq_transport_exists (Stone-von Neumann)             [S]
  T.conj_splitLocalModel_by_supported_pair                                      [S]
  T.weil_vacuum_local_model_integral_matrix_pair                                [S]
  T.exists_scalar_preservesIntegralMatricesSubst, T.linearLaw_localModel_*      [S]
```

## Independent checks

- Modulus of R_p = diag(GL_n,1) N_p on GL_{n+c}: |det|^{c+1-2p}; counted for all c <= 29 (matches the factor in `quotInt_unique_exists`).
- Uniqueness of quotient integrals with a left Haar measure of R_p holds for every p (Bruhat function argument; Bourbaki, Integration VII §2; Bernstein-Zelevinsky 1976 §1.21). The archive's uniqueness clause at non-unimodular positions is correct.
- TriPos exponent ((Q.c+1)+1)/2 - (sigma+1) = 0 under Q.c+2 = 2(sigma+1).
- Root exchange shifts the BilPos exponent by exactly 1 per position.
- W16 forces E/F unramified at every finite place; the host field `𝔟_spec` (relative different = b b̄ with b + b̄ = 1) excludes finite ramification, so the statement is consistent with the record.

## External boundary (stopping points, statements read)

| ID | declaration | published statement |
|---|---|---|
| W1 | `LocOm.omLoc` | linear model of the Weil representation of GL_m x GL_n at a split place (Kudla 1996 §§2-3; Harris-Kudla-Sweet 1996 §1) |
| W2 | `T.exists_weilDatum_powers_unramifiedEtaTilde`, `WeilExist.exists_isWeilDatumO` | global Weil representation of U(S) x U(T) with splitting characters (Weil 1964; Kudla 1994; HKS 1996) |
| W3 | `T.weilDatum_unique_on_thetaFunctions`, `WeilUniq.weilDatum_unique` | Stone-von Neumann uniqueness (Weil 1964) |
| W4 | `T.weilDatum_fixes_vacuum_nonSplitPlace_unramified` | unramified vacuum fixed by the lattice stabilizer (Howe; MVW LNM 1291 Ch. 2) |
| W5 | `T.weilDatum_realPlaces_fockVacuum_character` | Fock vacuum character at real places (Kashiwara-Vergne 1978; Kudla 1996 §4) |
| W6 | `T.thetaDistribution_automorphy_source_group`, `T.thetaDistribution_invariant_rationalTarget` | automorphy of the theta distribution (Weil 1964) |
| W7 | `MultFinite.schurMult` (hypothesis `Published.CuspRapidDecay`) | finite multiplicity on a cocompact quotient (Gelfand-Graev-Piatetski-Shapiro Ch. 1) |
| W8 | `DefiniteQuotient.exists_compact`, `Mem.AnisoQuotient.exists_compact` | compact adelic quotient for anisotropic or definite V (Borel-Harish-Chandra 1962) |
| W9 | `Mem.VolFin.finVol` | finite volume (Borel-Harish-Chandra 1962) |
| W10 | `QNorm.hasseNormSt` | Hasse norm theorem, quadratic case |
| W11 | `IdeleNormChar.existsUnique_isEta` | quadratic character of E/F (class field theory) |
| W12 | `SplitCharTrivial.eq_one_of_rat_of_split`, `T.exists_split_place_half_heisenberg_invariant_form` | strong approximation for SU(V) (Kneser 1966) with det; Heisenberg-invariant functional (Weil 1964) |
| W13 | `QuotInt.quotInt_unique_exists` | quotient integrals of semi-invariant functions (Bourbaki INT VII §2; BZ 1976 §1.21) |
| W14 | `LocFlat.CFac.Span.span_prodSB_eq_top` | S(X x Y) = S(X) ⊗ S(Y) (BZ 1976 §1.22) |
| W15 | `Formalism.GradedWeylDivisibility` entries | standard monomial bases (already V10) |
| W16 | `T.exists_unramifiedHeckeChar_halfExponent_restrict_quadratic` | everywhere unramified Hecke character of E with χ_τ(z) = z/|z| and χ restricted to A_F^× = η; not cut, fidelity item |

Root exchange (V19 first half) is closed internally. Kudla's seesaw (V19 second half) is not cited; the seesaw is R4-C.

## Smallest exact remaining internal residual list

| ID | earliest declaration | content | size |
|---|---|---|---|
| R4-A | `FlatBFLoc.flatBF_of_laws` (`DLP/FlatMapBesselToFourierJacobiLocalModel.lean:21`) with `LocMod.flatFB_holds`, `ContrLocProof.contrLoc`, `LocFlat.contrFactor`, `TriStep.valK_gl2`, `valK_glMid`, `valK_comb`, `T.exists_bilinear_position_middle_vertex`, `T.fourierJacobi_target_bilinear_form_integral`, `T.exists_linear_isQuotInt_tInt_alt`, `T.schwartzBruhat_self_average_heisenberg`, `PosOne.comb_eq_sum_cells`, `T.symmetricDoubleIntegral_finite_combination`, `T.doubleStep_local_weil_action_line_characters_cancel`, `CellQuotInt.isQuotInt_cells`, `QuotIntFJ.quotIntFJ_unique` | local split-place calculus | medium: 1,619 theorems, 24,325 lines |
| R4-B | `FinPl.flatLaws_all` (`DLP/FlatMapsSatisfyFlatLawsFinitePlaces.lean:139`) with `FinPl.Vertex.vertexGlued`, `FinPl.VertexExactCount.vertexExact`, `Unf.Flat.flatLaw`, off-level laws of R-2 | flat-map laws at every finite place | major in size: 3,369 theorems, 47,204 lines |
| R4-C | `SeeSaw.biAct_all` (`DLP/SeeSawWeilBiActionCommutes.lean:17`) with `SeeSawLastValue.contAut_biLift`, `SeeSmallPf.biLift_sum`, `DStepCell.cell_collapse` children, `SeeSawLastValue.valLast` | global seesaw | medium to major: 1,538 and 2,123 theorems |
| R4-D | `T.true_geometry_family_final_alt` and the other `T.true_geometry_*` producers of `Fam.colSide_alt`; `Mem.Col2` charts; `Formalism.L2.Ker.Cd.PairingIndexBounds`; `T.chainKernel_preserves_ramifiedForms_liveCharts` | tuple-family construction and twist-place laws for rescaled tuples | major: 15,760 theorems, 236,276 lines |
| R4-E | `AdForm.clsPinD_of_famCol_of_trueW`; `StepVacForm.main_alt_alt`, `FamChars.weilOK_of_rank_one_gram`, `RowLevel.main_alt_alt`, `MiTop.linkComm_of_laws_alt`; `Core.Mi.colDict_rd_eq_colForm`, `ConjRowRep.exists_contRep`, `MiTop.exists_isShift_of_center_alt` | class data, unit and Weil producers, bottom and anchor | major for clsPinD (6,227), small for the rest (40 to 2,084) |

Retired from the PC-4 list: `nuQ_weil`, `wfr_on` (fields of `Formalism.L2.SG.HidaSetting.HidaSetting`, unused in the PC-4 closure), `SBes.cpt` (field of `Core.Mi.SBes`), `inHH_closed` (off route). The producer of the `HidaSetting` record is a question for the synthesis.

## Proposition package (revision, 22 November 2026)

PC-4 restated as fourteen propositions from the local models to `valX` (Section 8 of the report). Tags: [rec] reconstructed, [asm] assembly read with leaves unread, [stmt] statement read, [ext] boundary.

| # | proposition | declarations | status | external | feeds |
|---|---|---|---|---|---|
| PC4.1 | global Weil data: existence, uniqueness, unramified vacuum, Fock vacuum, theta automorphy | W2-W6 cuts | [ext] | Weil 1964, Kudla 1994, HKS 1996, MVW | all |
| PC4.2 | seesaw bi-action: two Weil actions commute, preserve bi-theta functions, theta lift automorphic | `SeeSaw.biAct_all`, `SeeSawLastValue.contAut_biLift` | [stmt], 1,538 theorems unread | W2, W6, W8 | PC4.7, PC4.14 |
| PC4.3 | linear model at a split place | `LocOm.omLoc` | [rec] | W1 (Stone-von Neumann) | PC4.4, 4.7, 4.11 |
| PC4.4 | flat maps and contraction in the linear model | `FlatBFLoc.flatBF_of_laws`, `LocMod.flatFB_holds`, `ContrLocProof.contrLoc` | [stmt], mechanism inferred from hypotheses | via PC4.3, PC4.5 | PC4.7 |
| PC4.5 | flat laws (convergence, Heisenberg laws, flag equivariance) | `Unf.Flat.flatLaw`, `FinPl.flatLaws_all` | [stmt], 1,156 + 3,369 unread | Schwartz decay | PC4.4, 4.6 |
| PC4.6 | laws at non-twist places: OffLaw, VacLaw, GSupp, GValue, TLaw; level scalars a, 1/a | `SeeSaw.pins_finiteIntegrals` producers | [stmt] | W4 | PC4.14 |
| PC4.7 | trilinear form with TriPos | `TriStep.tri` | [rec] except `valK_gl2`, `valK_glMid`, `valK_comb` | | PC4.11 |
| PC4.8 | quotient integrals of semi-invariant functions | `QuotInt.quotInt_unique_exists` | [rec] as mathematics | W13 | PC4.10, 4.11 |
| PC4.9 | root exchange | `exchange_isPos`, `exchange_support` | [rec], closed | | PC4.10 |
| PC4.10 | symmetric double integral exists uniquely; cell sum with vol_J | `symDbl_existsUnique` [asm]; `comb_eq_sum_cells`, middle vertex, FJ target, tInt, self-average, finite combination [stmt] | about 1,600 theorems unread with PC4.4 | | PC4.11 |
| PC4.11 | split-place double-step identity (ValOne) | `ValOneAt.valOne_all` | [rec] except line-character cancellation | | PC4.12 |
| PC4.12 | all twist places (ValQ) and QLaw, QLast, QFin; c_Q = product of vol_J | `QVal.valQ`, `qLaw_of_pin`, `laws_of_pin_resc` [asm]; induction leaves [stmt] | | Fubini over places | PC4.14 |
| PC4.13 | existence of tuple data; c_V defined by (N6) | `Fam.colSide_alt` and `T.true_geometry_*` | [stmt], 15,760 theorems unread | none | PC4.12, 4.14 |
| PC4.14 | valX: six exact identities | `ValFin.valX` | [rec] (Wave 4) | `collapse_factor` of published type | c_V, LawsX, MIstar2 |

Normalizations: (N1) psi_k of conductor O_k, nu(O_k) = 1 self-dual; (N2) GL(O_k) mass 1, vol(K_Q) = 1; (N3) linear model factors; (N4) modulus |det|^{c+1-2p} of R_p with left Haar quotient integral; (N5) trilinear exponent (c+1)/2 - p, zero at the symmetric position, shifted by 1 per root exchange; (N6) c_V = kappa sc_j sc_{j+1} c_Q c_G c_T.

R4-E (class data, unit, Weil, bottom, anchor) feeds KerX, PerX, RdX and is outside the chain to valX.

**Conceptual status.** No conceptual mechanism is unresolved. The remainder is implementation depth: explicit local computations in known models (PC4.4, 4.5, 4.6, 4.10, 4.12), and one existence claim, PC4.13, that auxiliary tuple data exist simultaneously for the whole family. PC4.13 is the item to read first if PC-4 is reopened.

## Comparison with Slijepčević (arXiv:2611.00812v1, revision of 22 November 2026)

Statement-level comparison with Sections 5-7, 11 and Appendix A of S. Slijepčević, *Outline of Alpöge's proof of the generalised Riemann hypothesis* (21 November 2026). Bracketed numbers are his references.

Placement. His Rallis-type norm and tower identities (Props 7.12, 7.14) and the theta agreement step constants (Prop 7.3, (A2)-(A3)) feed toric functoriality (FUN, Thm 7.6), which the development calls the constant-function fit, i.e. `fun0Fit_of_leaves` (PC-6). They are not on the PC-4 route. PC-4 sits in the family construction (Defs 6.8, 6.16, 6.17, Prop 6.18). Read from the statements of `KerX` and `valX`, PC-4 realizes the column chain (6.1) as iterated theta lifts, which he marks "we understand the definition but not this interpretation".

| PC4 | match in Slijepčević | agreement | his status | boundary / ours |
|---|---|---|---|---|
| 4.1 | §5 Weil rep conventions; Kudla splitting [72], Howe duality [86],[42],[58], [64] | same | cited | legitimate; ours adds Lean locations W2-W6 |
| 4.2 | none (nearest: Def 7.1 configurations) | different identity | absent | ours further |
| 4.3 | linear models at split v1 (Def 7.1, (M3)) | agrees in use | outline | HKS [49]; ours reconstructs omLoc |
| 4.4-4.5 | evaluation maps (Def 7.2): Heisenberg intertwining, translation invariance, vacuum to vacuum | same shape as HeisLaws | definition only | uncited; ours states conclusion and mechanism |
| 4.6 | Prop 7.3 inputs: spherical vectors, coinvariant multiplicity one, unramified Howe duality | same mechanism | outline | MVW [86] for W4 |
| 4.7-4.11 | none | n/a | absent | ours further (4.7, 4.9, 4.11 reconstructed; 4.8 checked) |
| 4.12 | (A2),(A3): step constant C independent of characters | parallel normalization pattern, different objects | not understood | no boundary for (A2),(A3); ours proves the c_V analogue |
| 4.13 | Defs 6.16-6.17 (selection of auxiliary data per member), Prop 6.18 steps 4, 5, 7; (D5) Gauss primes | same kind of claim | theorem stated, proved in outline; forty conditions, openness step, auxiliary choices "not understood" | partial: Chebotarev, short-interval primes [31],[61], Linnik [81]; compatibility conditions uncited |
| 4.14 | none (Props 7.12, 7.14 are PC-6) | different identity | absent | ours further |

PC4.13 producer statements read (`T.exists_quadratic_extension_reads_of_true`, `T.true_geometry_twist_local_data_alt`, `T.true_geometry_quadratic_twist_level_alt`, `T.true_geometry_exists_kernel_alt`, `T.true_geometry_exists_volume_data_alt`, `T.true_geometry_row_pair_relation_alt_alt_alt`): conditional existence under `AllFamilyConditions W`, `a.Is`, `a.True`, giving quadratic-extension readings (twist places), kernel Weil data, volume constants, level law, row-pair constants.

**PC4.13 verdict: partially corroborated but still residual.** Slijepčević confirms that a simultaneous selection for every member is a theorem of the development and names its inputs, but does not state the compatibility conditions or prove the selection, and lists them as not understood. PC4.13 remains the one genuine PC-4 residual; its hypotheses are discharged in the family construction shared with PC-6.

Human-proof verdict unchanged.

## Answer

Does PC-4 still block "The entire RH proof has been reconstructed in ordinary mathematics modulo named external theorems"? **Yes.** The split-place spine is reconstructed and root exchange is closed, but R4-A to R4-E remain internal, about twenty thousand theorems of known mechanism whose bodies have not been read.
