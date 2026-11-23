# Kernel-law pass: dependency map

Exclusive sizes in theorems on the rebuilt exact-edge graph. "block" = exclusive to one of `bwit_exists_alt`, `Fam.colSide_alt`, `AdForm.clsPinD_of_famCol_of_trueW`; "joint" = reached only through the union of the three blocks.

## Proposition A (the kernel law) and its components

```
Prop A(iii) step kernels  ThEquivP (stepT)                         [Formalism.L2.Ker.thEquivP_ofD]
├─ A(ii) induced kernels  Amb.ThIndEq                              [theta_coset_indicator_natural | IndEq.thIndEq_of_vacEq]
│   ├─ Lemma 2 transport  TI.isIsom_RV, TI.alV_RV, TI.imgLat_laV, TI.RV_embH, KS.MM.*_map     (K1)
│   └─ A(i) base vector   Amb.EqLaw  <- Base.EqP clause 1           [Cd.CarC.eqLaw_ambOf_of <- SqG.eqP_car]   (K2, joint 404)
│       ├─ reduction      reduction_of, e3a, e3b (read in full)                         closed (52)
│       ├─ chi factor     character_factor_unitary_action, DetSmul, IsChi              closed (19 incl. wrappers)
│       ├─ (F1) lines     ThZeroSpans, LatAll, QIntAll                                 leaves K-a (105), K-b (41)
│       ├─ (F2) paths     SqP, Tr0L, Tr0R <- tripleFormula [Weil 1964, outside] + split data   leaf K-c (97)
│       ├─ (F3) transport PullIop (Lemma 2)                                            closed
│       └─ (F4) constants J1, J2 <- split_host, J1at_mul, J1at_of_ne
│                         <- UnitaryConstant [Weil 1964, outside], DetCayley, GaussRow <- gaussRow_of, negOneNorm   closed (109)
├─ datum kernels          Amb.ThCEq <- thCEq_of_ind (read in full)                      (K1)
├─ Lemma 4 jets           TE.jetMap_pullD, TE.jetMap_pull, jet_local_rationality        (K4)
├─ Lemma 5 characters     ChiLaw (chiLaw_ambOf*), MuProdLaw <- muProdLaw_of <- md_prod (165, block bwit),
│                         wtLaw_step, jet_in_weight_space_chain, MuDetLaw, UnitInv      (K5)
└─ Heisenberg data        LaHyp <- laHyp_ambOf_top (both copies)                        (K3)

Prop A(iv) decorated form KerDia.Eqv.ent_smul <- th_move <- scal_theta, ana (ThCEq, ChiLaw, EOmega), xiAt_law; opOf_equiv <- opOf_move
```

## Occurrences

```
X1  SelC.square_integrable_columns_of_witnesses (313)
    ├─ TC.RcHyp.hyps_of_isTw (254)
    │   ├─ chTh_ok_chi (246) -> thEquivP_ambOf_tiesD (221) = Prop A(iii)          CLOSED
    │   │   ├─ muProdLaw_of (165)   Lemma 5(b)
    │   │   ├─ thIndEq_ambOf_car (39)  Prop A(ii)
    │   │   └─ thEquivP_stepT_ofD (16) Prop A(iii) assembly
    │   ├─ jetsRat_chi (13), chTh_ok_ambD/stepC_ok_deg (6)                          CLOSED (read in full)
    │   └─ idxMatNF_of_isTw (5) -> twNF_imp_matNF                                  leaf, moves to W1
    └─ column reading (59)                                                         RESIDUAL W1

D6  KRamT.kernel_keeps_ramT (96)
    ├─ entry_dia (89) -> ent_smul (71) = Prop A(iv); ent_dia (9) diamond invariance   CLOSED
    ├─ K_mem_Fi / Kmap_stab (84) -> ent_smul with g = 1                             CLOSED
    └─ sharp_mem_range (6), kmap_mem_valC                                          CLOSED (read in full)

E1  KerTup.kernel_identity_tuple (204) + LevLaw.lev_law (97) + clsKL_real (13)
    ├─ thetaKernel_splitPlaces_eq_jet_classicalTheta (169) = Prop E
    │   └─ reads_datum_eq_thC (160, read in full)
    │       ├─ heisenbergOperator_halfComponent_on_vacuumTranslates (71)           leaf E1a
    │       ├─ finite_fourier_expansion_half_split_places (58)                      leaf E1a
    │       ├─ heisenbergOperator_conjugateHalf_vacuum_eq_semicharacter (32)        leaf E1a
    │       ├─ periodLatticeHalves_reps_finite_index (9), stdChar_..._eq_one (5)   leaf E1a
    │       └─ gaussianReading_finiteRationalHeisenbergTranslate, thetaFourierSum_... (owned outside)
    ├─ movedDatum_eq_finiteDatum_representativePair (102, joint with R4-D)          E1b
    ├─ chainMove_characters_eq_rho_up_to_base (13)                                 E1b
    ├─ pinned input PinX.mv = VacT (moved vacuum; producer MovedVac.vac_moved, outside)
    └─ lev_law (97), clsKL_real (13)                                               E1c
```

## Counts

| set | before | after law |
|---|---|---|
| bundle-witness heads (dedup, recount) | 444 | 195 |
| R4-D heads (dedup, recount / ledger) | 1,537 / 1,743 | 1,441 / 1,647 |
| R4-E heads (dedup, recount / ledger) | 459 / 479 | 459 / 479 |
| joint-only material inside the law | 451 (uncounted) | 243 statement-level leaves (K-a, K-b, K-c) |
| joint exclusive set of the three blocks | 4,555 | 3,798 |
