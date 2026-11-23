# E-block (R4-E): corrected dependency map

22 November 2026. Exact edges on the rebuilt graph (1,066,087 declarations). Counts are theorems inside the class-data exclusive set (E) plus the joint-only part (J, reachable only through the union of the three PC4.13 blocks). Tags: `[E]` block-exclusive, `[J]` joint-only. `(shared Ek)` marks a node also used by head Ek. Mechanisms M1–M8 are the propositions of `Final_EBlock.tex`, Section 4.

```
AdForm.clsPinD_of_famCol_of_trueW                                     block top (read in full)
│  consumers: kerX_of_clsPinD, perX_of_clsPinD, rdX_of_clsPinD  (lawsLinks_of_geo_rows_cols_alt)
│  chooses rho = realOf(u, pk_z W, f.g, s, J) before the tuple index t
│
├─ E3  T.exists_nonzero_jetScale_trueColumns → JetScales.exists_jetS           35 [E]      M5(a)
│      └─ JetRead.pureTensorO_zero_eq_jetP (29) ← aPlus_read (20) ← dRho_read (15); stdPair_world (5)
│
├─ jOf_exists, isTr_unique (translates J; closed, read in full)
│
├─ E4  T.trueColumns_realData_spec → AdForm.realOf_is                          29 [E] + 34 [J]
│      ├─ T.exists_tupleChain_adelicData → AdForm.exists_twDat (33) [J]                 M8
│      │     └─ TupEx.fullStep ← stepCh_all (stepCh_zero 17, stepCh_top 8, stepCh_mid 5), comp (12)
│      ├─ TrueBranch.branching_true_columns (11)                 (shared E2)           M7
│      ├─ EmbTopBlock.isBlock_infM_emb (7)                                             M7
│      └─ T.exists_charExponent_infinity_kernel_shift (3)        (shared E1)           M5
│
├─ E1  T.kernelPart_laws_of_columnPins → KerLaws.clsKL_is                     317 [E] + 126 [J]
│  ├─ E1a KerTup.kernel_identity_tuple (body read in full)
│  │   ├─ KJInf.CoreG.thetaKernel_eq_jet_thC (168) = Prop E                           M1
│  │   │   └─ DatumRead.reads_datum_eq_thC (160)
│  │   │       ├─ HalfHeis.heisO_halfA_eq (70)          Lemma 2 (vacuum relations)
│  │   │       │   ├─ HalfARest.heisO_rest_eq (45)      ← heisO_finRat_sign (upstream), signTrace integer (21)
│  │   │       │   ├─ char_sympl_rest_eq_one (24), CocycleSS.cocycle_trivial (19), alV_mul_self_halfA (17)
│  │   │       ├─ DatumFour.four_expand (57)            Lemma 3 (finite Fourier)
│  │   │       │   └─ HalfSplit.splitHyp_halves (23) ← TwPerSelfDual.twO_selfDual (16)
│  │   │       ├─ ConjHalfHeis.heisO_conjHalf_eq (31)   Lemma 2
│  │   │       ├─ PeriodReps.reps_genuine (9), HalfPairing.char_sympl_halfB (5)   Lemma 1
│  │   │       └─ [upstream] gaussianReading_finiteRationalHeisenbergTranslate, ThetaCosetSum.xiL_eq_kernel
│  │   ├─ T.movedDatum_eq_finiteDatum_representativePair (102) [J]   = E1b              M2
│  │   │   └─ TwMovedVal.moved_datum_val_tw ← TwResid.tw_resid_datum (92)
│  │   │       ├─ TwResid.xiAt_transport_tw (79)   ◆ SHARED with E1c (law_read.transport_base)
│  │   │       │   ├─ lastStep_datum_transport_badPrime (32), beforeLastStep_… (26),
│  │   │       │   ├─ entryDatum_transport_badPrime_anyTuple (23), phiT_tw (13)
│  │   │       └─ CongAtIdem.cong_at_idem (12), exists_rat_half_approx (3)
│  │   ├─ TwDat.chr_moves_eq_rho_base (13)  = E1b                                       M4
│  │   │   └─ DetRootRead.chr_at_detRoot (4)   ◆ SHARED with E1c (MovedLaw.chr_root_eq)
│  │   ├─ KerTup.jetP_cast (5) → fockPolynomialJetValue_eq_jetLinearForm_rescaled           M5
│  │   └─ [pins, upstream] PinX.mv = VacT (MovedVac.vac_moved), laHyp_eSmooth_true
│  ├─ E1c AdForm.LevLaw.lev_law (body read in full)                                    M3
│  │   ├─ LevDat.levDat_law (185) ← RatLaw.law_rat (154) ← XiLaw.xi_law (151)
│  │   │   ├─ ReadLaw.law_read (118) ← transport_base (97) → xiAt_transport_tw ◆ (M2)
│  │   │   │                        └─ MovedLaw.moved_law (19) → chr_root_eq_prod (10) ◆ (M4)
│  │   │   └─ RatApprox.approx (34)
│  │   ├─ SBMove.isSBHalf_actO_lev (26), levels_keep_stdLat (12), LevLaw.omega_eq_smul (3)
│  │   └─ [upstream] gaussianTwistedRealReading_entire_and_injective
│  ├─ E1c KJRealLive.clsKL_real (13)                                                   M5(b)
│  │   └─ KJReal.om_pureTensorO_onb (5) ← [upstream] WeilVacChar.vacuum_character, OrientedHeis.om_pureTensorO
│  └─ ClsKLive.kval (6 [E] + 17 [J])
│      ├─ T.chartLevels_reps_represent_unitaryDoubleCosets (17) [J]  ◆ SHARED with E2     M6
│      └─ KerVal.kernel_classSum (4)                                                   M6
│
├─ E5  T.exists_rowForm_reading_levelForm_lastSpace → AdForm.exists_readsG_of_level   27 [E] + 2 [J]   M6
│      ├─ StabInv.reading_stab_inv (22) ← coset_law_moved (11), eq_smul_of_pair (6)
│      ├─ exists_coefficientVector_reading_realRepresentation_form (3)
│      └─ Mem.ColAd.frL, lT, lT_apply   ◆ SHARED with E2
│
└─ E2  T.exists_lastPeriod_classData_of_lastStep → AdForm.exists_clsT_of_pinTop     85 [E] + 20 [J]
       ├─ TopInv.law_top (58) ← rd_emb_evz (35) ◆ (shared with tailTop) ← evz_decomp (18), emb_mem_chi (14)
       │                     └ rd_right (20) → chartLevels_reps… ◆ (E1)                M6
       ├─ tailTop_eq_of_pin (57) → branching_true_columns ◆ (E4), rd_emb_evz ◆        M6, M7
       ├─ ClassPtReps.isReps_stabOrd_top (10)                                          M6
       └─ TopTranslate.top_translate (10)                                              M6
```

## Shared theorems (44, each used by exactly two heads)

| pair | count | content |
|---|---|---|
| E1, E2 | 19 | chart double-coset reps and continuity of level characters (17, M6); 2 chart-value lemmas |
| E2, E4 | 18 | branching at the top (11, M7); 7 class-point lemmas (M6) |
| E1, E4 | 4 | infinity-type kernel shift (3, M5); `trueColumnSteps_are_standardHermitianPairs` |
| E2, E5 | 3 | frame maps `frL`, `lT`, `lT_apply` (M6) |

Within E1, `xiAt_transport_tw` (79) is reached from both E1a and E1c, and `chr_at_detRoot` from both E1b and E1c.

## False edges

None among the cross-head edges (all are fully qualified names in proof bodies). K-b and K-c are unreachable from the E-heads. K-a is reached only through `laHyp_ambOf_top` (kernel-law K3, closed), in its `GlobalTheoryTheory` copy, which is also live outside PC4.13.

## Counts

| | E1 | E2 | E3 | E4 | E5 | sum | union |
|---|---|---|---|---|---|---|---|
| block-exclusive | 317 | 85 | 35 | 29 | 27 | 493 | 469 |
| with joint-only | 443 | 105 | 35 | 63 | 29 | 675 | 631 |
| after this pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
