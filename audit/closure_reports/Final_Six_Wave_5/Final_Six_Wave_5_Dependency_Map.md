# Final Six Wave 5: dependency map (PC-5, FR-12 lattice counting)

22 November 2026. Agent 5. Companion to `Final_Six_Wave_5.pdf`. Reconstruction from proof text, not a verification. Nothing in `src/lean` was built or run, `RH_Route_Notes.tex` was not touched, and no existing file was edited.

Legend. `[R]` proof body read. `[S]` statement read. `[A]` assembly. `[C]` closed. `[E]` stops at named external mathematics. `[N]` new lines from the declaration-level trace (upper bound, theorem and lemma bodies only, counting only what earlier rows did not already contain). Paths are under `src/lean/src/`. `FM/` = `Development/AbelianVarietyTheory/Proofs/FlagMeasures/`. `FUL/` = `Formalism/FlagUnipotentLattices/`. `SHF` = `Formalism/SharpRestriction/CuspSpanNormBounds/StandingHypothesesHoldFamily.lean`.

## Verdict

**RESIDUAL CHILD REMAINS.** Earliest blocker `count_terms_gramClass_over_sublattice` CLOSED. No gap, circularity or failed constant. PC-5 is major in volume (union about 11,000 theorems, 200,000 lines), not medium. Single earliest blocker now: `GlobalTheory.LoopC.RowGlue.main` (`FM/SplitRowLatticeMiddleIffGluedLattice.lean`).

## Closed: count_terms_gramClass_over_sublattice   [C]  [N 518 thm, 9,211 l]

```
T.count_terms_gramClass_over_sublattice (FM/CountTermsGramClassOverSublatticeStatement.lean:9)
= LoopC.TermsOver.main (FM/CountTermsGramClassOverSublattice.lean, 267)            [R][A] C0 = max(C1, 1, 2|CT|)
  zequiv_trans / zequiv_symm / frSet_congr                                          [R] unitriangular group
  NT_sq_le, frB_le                                                                  [R] exponents checked numerically
  LoopC.Base.main (FM/StandardBaseFlagComplementIntegralLattice.lean, 320)          [R] L0 integral PD, [L0#:L0]=T^[E:Q], det L0 = NT
    perp_lattice, exists_rep (UnimodQuot.exists_lattice_rep)                         [R] unimodular duality on saturated sublattice
    DefiniteQuotient.posDef_of_signature (DivisorProofs/ExistsBoundUnitary.lean:44) [S] signature (p,0) => PD
  LoopC.DetCard.main (FM/DefiniteLatticeDiscriminantModuleCardDetSq.lean, 112)      [R] [M#:M]=det^2, det P = det M [M:P]
    Mass.DiscOrder.main (FM/HermitianLatticeDiscriminantOrderNeZeroUnimodula.lean)  [R] index via covering pairs
    Mass.DetAgree.genIdxH_eq_idxN (FM/IsLatticeLatIn.lean)                          [S]
  LoopC.GramSize.main (FM/ExistsGramRepresentativeSizeLeHHSq.lean, 519)             [R] QOK with Q = HHZ^2; C0 = 2|CT|+3
    uses standing field log rd_E <= L/C_l (only rd_E <= b)                          [R]
    stab_cell (FM/GramUnipotentStabilizerBruhatCellConjRoot.lean, 321)              [S]
  LoopC.FrCount.main (FM/FrameTermCountSublatticeBound.lean, 237)                   [R][A]
    RowSplit.main (FM/ExistsFrameFixingIsometrySplitRowLattice.lean, 540)           [S] frame-fixing isometry to split lattice
    FrameMove.exists_exact_frame (FM/ExistsExactGramFrameInTermClass.lean, 515)     [S] exact Gram representative in class
    FrEx.cntCl_ExSet_le (FM/CardExactGramIntegralFrameClassesLe.lean, 216)          [R] count <= #lifts * max fixed-lift count
      Lifts.main (FM/ExistsSublatticeLiftsModuloFixingUnipotent.lean, 424)          [R] (NT^2 Q)^rS lift classes
        FunIdx.funIdx (FM/LinearFormsBoundedRepresentatives.lean, 127)              [S] Hom(M0,O)/h(L0,.) has NT^2 classes
        homRestrictIndex (FUL/.../MeasurePreservingPiCompProd.lean:422)              [S][E-type] Ext over Dedekind domain
      FixedLift.card_frames_le (FM/CardIntegralFramesFixedLiftLe.lean, 544)         [R] fixB = 9^{sf}(De^2 NT^2 Q)^{s+s rS} Q^{2 rS^2}
        PerpDisc.main (FM/PerpendicularRankIdealBound.lean, 261)                    [R] ideal I, N I <= De^2 NT^2
        WMem.main (FM/FixedFramesPerpendicularVectors.lean, 269)                    [S] T h(y,y) = G for cofactor sum y
        DefinitePacking.dualPack (FM/OneLeNormMulAbsNormSq.lean:142)                [R]
          box_count_alt (FUL/MinkowskiFactorialBounds/SchurAverage.lean:146)       [R] 9^{s|iota|} max(1, prod B^2/nu)^s, checked
        exists_reps_cofVec_orth_mod_rowSpace (FM/MinorSmulEqRowSpaceOfCofVecOrth.lean:117) [S]
        FrameDiff.frame_diff (FM/FramesSameGramDifferBySkewSolution.lean, 168)      [S] skew solution x^H Y + Y^H x = 0
        xClasses (FM/XClassesDenom.lean:80), Centre (FM/CentralMap...lean)           [S] <= Q^{2 rS^2} classes
        EichlerUnip.eichler_mem_unipotent (FM/IntegralOfUnimodular.lean)            [S] Eichler transvections
  library leaves: kernelRowSpace, cofVecAdjugate, omegaNorm, class_number_upper_bound (FUL/)  [S][E-type] Cramer, adjugate, Minkowski
```

## FR-12(a) counting lemmas

```
LoopC.PairMean.main (FM/OneLeSizeZ.lean:242)                                       [R][A]  [N 618 thm, 9,153 l]
  count_terms (closed); loop_count_exponent_bound (FM/LoopCountExponentBound.lean)  [S]
  hypothesis H1 : congruence_at_split_frobenius_holds  <- mean_count
  T.rowLattices_mean_eq_genus_mean = MeanGenus.mean_rows_eq_mean_genus (FM/RowLatticesMeanEqGenusMean.lean:891)  [R]
    rows_sum (798)                                                                  [R] fibration, (T-1)^f cancels
    T.row_lattices_same_middle_conjugate_unipotent = LoopC.rowsLift                [S] R5-1
    T.rowBaseLattices_mem_same_hermitianGenus = LoopC.RowsGenus.main               [S] R5-1
    T.card_middleLattices_over_genus_lattice = LoopC.GluingNum.gluingNum           [S] R5-1  count (T-1)^f
      shared: LoopC.RowGlue.main (FM/SplitRowLatticeMiddleIffGluedLattice.lean)    [S] EARLIEST BLOCKER
        exists_isom_of_isUnimodularAt (FM/ExistsIsometryOfUnimodularLatticesAtPlace.lean:229)  [S]
        exists_coprime_scaled_isometry (UnitaryExistence/ExistsCoprimeScaledIsometrySameSignature.lean:231) [S]
        Hasse norm theorem, quadratic case (AdelicLatticeProofs/HasseNormTheoremQuadraticExtension.lean) [L] internal
        UnRep.WeakApprox.core (AdelicLatticeProofs/UnitaryGroupWeakApproximationAtPrimes.lean) [L] internal
  small children: TraceFormPos..., PairIsometryUnique..., EncardSublatticesBoundedDetLeSum, LatticeSeen..., CntPrimLatticeImage..., OrthTransversal..., ExistsCommonSublatticeSmallDet, LiftedFlagLatticeChainSpans, IsPairMove..., PairLatticeLe..., XLamLeSmul..., MemOfPerpPerp   [L] about 4k lines

LoopC.GenericMean.main (FM/CntClLeEncardMul.lean:178)                              [R][A]  [N 58 thm, 1,661 l]
  count_terms; hypothesis hP <- mean_count
  T.classNumber_rootDisc_factor_le_HHZ (FM/ClassNumberRootDiscFactorLeHHZ.lean)     [R] via class_number_upper_bound
  exponent_divisor_sum_le, IdxNOneMulAbsNorm, NormPowLeCardFlagQuotient              [L] R5-4

LoopC.Partner.partners_le (FM/OneLeProdReal.lean:190)                              [R][A]  [N 171 thm, 3,033 l]
  count_terms; ExistsPartnerLift, FockGram.HermDualOf                              [L] R5-4

GramHeight.height_bounds (FM/EquivIntegral.lean:461)                               [R]     [N 28 thm, 775 l]
  constant 2N+7, N >= |CT|+|Cg|+1; uses log rd_E <= L/C_l as rd_E <= b
  T.exists_zEquiv_gram_bounded_minors = ReducedGram.exists_reduced (FM/ExistsZEquivGramBoundedMinors.lean:99) [S] R5-4

T.mean_count_primitive_sublattices_over_genus = Mass.PrimMeanRow.main (FM/MeanCountPrimitiveSublatticesOverGenus.lean:143)  [R]  [N 1,942 thm, 38,219 l]
  num_mid, num_top                                                                  [R] C >= 16, C >= 1/c0; uses log rd_E <= L/c0
  Mass.PrimMean.main (FM/PrimitiveSublatticeMeanCountBound.lean:139)                [R] upper bound; NO Siegel mean value, NO Schmidt
    few_orbits_subspaces_hermitian_lattice_discriminant                             [S] R5-3
    witt_extension_totally_definite_hermitian                                       [S] R5-3
    orbitStabilizerMass_subspace_cyclicDiscriminant_le                              [S] R5-3
    mass_integralLattices_discriminantOrder_le (hyp MaxMass)                        [S] R5-3
  T.maximalHermitianLattice_massRatio : MaxMass = Mass.MaxFormula.main (FM/MaximalHermitianLatticeMassRatio.lean)  [R] R5-2
    massConst_all, siegelMassRatio_of_LI (Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/SiegelMassRatioOfLI.lean) [R]
      massConst_succ (MassConstSucc.lean:99)                                        [R] Siegel rank induction by ball counts
      liStat (LiStatOf.lean:24), binary_hermitian_represents (FM/BinaryHermitianRepresents.lean)  [S] internal
      Fact HermRepUnram discharged by GlobalTheory.hermRepUnram (FM/HermRepUnram.lean) [R]
    [E-candidate] Siegel-Braun mass formula; Shimura; Gan-Hanke-Yu (Duke 107, 2001)
  T.exists_orthonormalLattice_of_unimodular_landherr = Mass.exists_orthoLattice_of_unimodular [S] internal Landherr
  T.mass_rowLattice_orthogonal_split_prime = Mass.RowPerpMass.main                  [S] R5-3
  Mass.StdMass.main, Mass.CyclicGenus.main, Mass.PrimCount.main, Mass.OrbMono.main  [S] R5-3
```

## FR-12(g)

```
localModelK_holds (Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/LocModel.lean:1768)  [R] call of clK_core
  LocModel.clK_core (1589)                                                          [S] Kr = a a prod_p [cl] d d K_p   [N 423 thm, 6,727 l]  R5-5
localModelT_holds (.../DataCut.lean:411)                                            [S] vanishing on joined top index  [N 15 thm, 229 l]  R5-5
```

## Counting-engine leaves

```
GaussMean.oneVectorCc_of_siegelWeil (FM/OneVectorCcOfSiegelWeil.lean:379)         [R] SiegelWeilUnitaryConvergent -> OneVectorCc  [C][E V6]
OneVectorMean.siegelMeanCc_of_oneVectorCc (FM/SiegelMeanCcOfOneVectorCc.lean:279) [S] OneVectorCc -> SiegelMeanCc   [N 12,587]  R5-6
GaussMean.Step.volumeStep_of_siegelMean (FM/EnnrealVolumeRatioStepCancel.lean:77)  [S] SiegelMean -> VolumeStep    [N 12,133]  R5-6
FlagMeas.AbsVol.absoluteVolume_of_volumeStep (FM/HermAbsoluteVolumeBound...lean:37) [S] VolumeStep -> AbsoluteVolume [N 4,632]  R5-6
NonzeroFlag.nonzeroFlagBound (FM/NonzeroFlagProbabilityBound...lean:84)            [S] VolumeStep -> NonzeroFlagBound [N 32,427] R5-6
FlagUnfold.unfoldBound (FM/IsotropicFlagUnfoldingBound.lean:213)                   [S] unconditional; contained in the above  R5-6
DeepKernel.deep_kernel_bound_of_ptBound (FM/DeepPointKernelBoundOfPointwiseBound.lean:22) [S] PtBound -> DeepKernelBound [N 36,913] R5-6
NearCount.near_count (FM/PowLePowRatio.lean:479)                                   [S] #nearSet <= prod (1 + 12 delta/lambda) [N 10,796] R5-6
rowsAdd_holds / rowsGood_holds / etUnip_holds (Formalism/.../RootLatticeThresholds/AllRows*.lean) [S] hyps RowsFinDim, GapHyp [N 2,106 / 17,001 / 1,711] R5-6
```

## NearUnip check   [C]

```
Dec.NearUnip (Development/AbelianVarietyTheory/Statements/CuspFrameWeights/ConvolutionSmoothL2.lean:136)
= NearElement.near_unipotent (FM/ConjPowOfMulEqOne.lean:93)                        [R] tr G^j = n via radical (g0) and 3n < g0
  call site near_terms_one_type (FM/NearTermsModeratePointsOneTypeBound.lean:116)  [R]
    CountHyp (Development/AbelianVarietyTheory/Definitions/SemilocalFrames/LayerProd.lean:108): g0 prime, 4n < g0, splits completely
    isRadical_span_of_ncard_primesOver                                              [S] split prime => radical
  CountHyp producer: count_parameters_of_hyp (SHF:424), 4r < g0 from H12           [R]
```

## Record inequalities and constants

```
gap_const (Development/AbelianVarietyTheory/Definitions/SemilocalFrames/LamXEquivariant.lean:31)  16 (10^6)^2 (4*11+6) = 8e14   [R] checked
unbundled count C0 = max 0 (8e14 (A+4)) (FM/UnitaryAutomorphicCountingUnbundled.lean:43)          [R]
count_parameters_of_hyp (SHF:424): hyp hCl3 2C <= C_l; field H11 log rd_E <= L/C_l                 [R]
  gap_product_le_of_bounds (SHF:297)                                                               [R]
hCl3 supply: countOwn_of_rowsPEv / linkS_of_thmSPEv (Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/LinkSFinal.lean:22,57)
  <- linkS_concreteEv <- link_thresholds_spec (SHF:1671), linkThresholds (SHF:1667)                [R]
     sCl = min(CfL, Cw, CDel, CCount, Ch0r, Cgap) (.../LeSCSCl.lean:13); Large forces each >= max(2, 2C, 8 CGam)
H11 supply: log_root_discriminant_le (SHF:1110) via standing_hypotheses_hold_family (SHF:1602)    [R] checked numerically
  => C_l >= 2C >= 1.6e15 (Cg+4) when C >= 8e14 (A+4), A >= 2 Cg >= Cg >= 0
  Remaining condition belongs to PC-6: families in the class are Large with SizeQD bounds.
```

## Boundary changes proposed

- Keep V6 (Siegel-Weil, convergent range) as the stopping point of the engine chain.
- Propose: hermitian mass formula (`MaxMass`, `SiegelMassRatio`) as a named stopping point after a statement match. Proved internally, so a reclassification option.
- Optional for R5-1: Jacobowitz 1962, Landherr 1936, weak approximation.
- Withdraw from FR-12(a): Schmidt 1968 and Siegel 1945 mean value. Not used.

## Remaining internal residuals

| ID | Declaration | Size | Mechanism |
|---|---|---|---|
| R5-1 | `LoopC.RowGlue.main`, `rowsLift`, `RowsGenus.main`, `GluingNum.gluingNum` | medium (~9k) | gluing, local isometry, weak approximation |
| R5-2 | `Mass.MaxFormula.main`, `massConst_all`, `liStat` | major in lines (25k to 35k) | Siegel mass formula; reclassifiable |
| R5-3 | children of `PrimMean.main`, `StdMass`, `CyclicGenus`, `RowPerpMass`, `PrimCount` | medium | Witt, orbit counts, mass monotonicity |
| R5-4 | `ExistsPartnerLift`, `IdxNOneMulAbsNorm`, `ExponentDivisorSumLe`, `NormPowLeCardFlagQuotient`, `ExistsZEquivGramBoundedMinors` | small (~4k) | elementary |
| R5-5 | `LocModel.clK_core`, `localModelT_holds` | medium (6.7k), small | tensor factorization |
| R5-6 | engine chain (`siegelMeanCc`, `volumeStep`, `absoluteVolume`, `nonzeroFlagBound`, `unfoldBound`, `deep_kernel_bound`, `near_count`, `rows*`) | major (~130k) | volume induction on flag strata |

## Method note

Sizes come from a declaration-level tracer written for this wave: index of 1,050,950 declarations and 143,379 namespace lines over 175,187 Lean files; each theorem body is tokenized and identifiers resolved against the transitive import closure of its file. Short-name collisions make it over-inclusive, so the counts are upper bounds. File-level import closures are much larger and misleading (the gluing subtree imports abelian scheme laws it does not use).
