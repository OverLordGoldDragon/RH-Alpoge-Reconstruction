# W-block (bundle witness W1–W3): corrected dependency map

22 November 2026. Exact edges on the rebuilt graph (1,066,087 declarations). Block top: `Top.Bl.exBL_isLinked_prmR_alt` (652 exclusive theorems; contains `bwit_exists_alt`, 202). Counts are theorems in the W-domain (block-exclusive + joint-only) after removing material already closed by the kernel law, the E-block and D1–D3. Tags: `[B]` block-exclusive, `[J]` joint-only, `[K]` K-leaf (left at statement level by the kernel-law pass), `(closed)` closed earlier.

```
Top.Bl.exBL_isLinked_prmR_alt
├─ zeta_uniform_of_extension' → ze_u_prm_of_extension_with_law
│   └─ W1  SelC.square_integrable_columns_of_witnesses                    299 = 64 [B] + 235 [K,J]     Q1 + Q2
│       ├─ exists_square_integrable_columns_of_data → exists_rowsKC_colPins_alt → colPins_colK'
│       │   ├─ squareIntegrableColumnsOfKernel → colRecK → colRecC           Q1(i)
│       │   │   ├─ RcHyp.hyps_of_isTw, chTh_ok_chi                         (closed, kernel law)
│       │   │   │   └─ thEquivP_ambOf_tiesD → thIndEq_ambOf_car → SqG.eqP_car
│       │   │   │        ├─ eqP_all → eqP_gen → eqP_of_pair
│       │   │   │        │    ├─ sqSplit_of (K-c)       [K]  ← split_pair_generation (upstream)
│       │   │   │        │    ├─ muOneL_of, muOneR_of (K-c)  [K]  ← signData_of, negOneNorm, tripleFormula (F4-C1)
│       │   │   │        │    └─ rational_integrality_link (K-a) [K] ← hermitian_form_integral_values, delta_nonzero_link
│       │   │   │        └─ SO.stdOK (K-b) [K]
│       │   │   ├─ idxT_ok, of_forall_ix, ker_chi_eq ← chiRec_eq_chi
│       │   ├─ mem_iff_XgE (character idempotents)                          Q1(ii)
│       │   ├─ idxMatNF_of_isTw → twNF_imp_matNF (normal form)              Q1(ii)
│       │   └─ exists_read_fam → exists_read, evC_res_lvl, evRow_res_lvl   Q1(ii)
│       └─ exists_readC_wU_eq_id → face_pt, exists_cpl, jA_row_alt,
│                                  exists_eNu ← nrm_stepZero_eq ← majAt_eq_classSum   Q1(iii)
│
├─ eta_size_recursion_alt → exBL_isLinked_alt → exists_reciprocity_record_compatible
│   └─ WPt.exists_recPinE_alt  (assembly; host datum X4 closed in cleanup)
│       ├─ W2a T.exists_spectral_data_compatible → WPt.exists_pinned_spectral_data_compatible   73 [B]   Q3 (+7 assembly)
│       │   └─ CyclotomicFieldContainment.oTied_of_ksExact (66)
│       │       ├─ exists_smallField_classFieldPieces → SmallFieldPieces.exists_pieces (55)
│       │       │   ├─ isHilbertCF_qb (26) ← hilbert_qb, isRayFieldIn_hilbertField   [GlobalArtinReciprocity, WeberRayFieldSt]
│       │       │   ├─ ray_qb (19) ← natAbs_discr_dvd ← natCast_mem_differentIdeal
│       │       │   ├─ kPsi_qb (11), prime_dvd_discr_iSup_kPsi (5)
│       │       │   └─ upstream: finrank_torsionField_le, dvd_discr_torsionField, discField_eq_torsionField
│       │       └─ ksQ_eq (10)
│       └─ W2b Top.Bl.exists_kernel_spectral_data_at_witnesses               22 [B]   Q4
│           ├─ JointsTrue.joints_of_standard_character (16)
│           │   ├─ psiG_true ← psiG_of_loc ← columnCharacter_reduction_eq_exp
│           │   ├─ isDetLift_local, JointsStd.om_std
│           └─ LowerTie.lowerMap_tieTw_alt
│
└─ local_langlands_prm_reduction_alt → bwit_exists_alt → exists_selected_realization_alt
    → exists_selection_pair_local_langlands_alt → selection_group_ambient_tie
    → column_params_instance_data → twArgs_exists
        └─ W3 T.reFace_zero_part_conventions_chosen_again → reFace_zero_parts   36 [B]   Q5
            ├─ XE_updS_zeroLam ← qp_bot ← part_iff_rows3
            ├─ scal_zeroLam, thmA/thmB/galD_zeroLam, pins_updS, read_updS_keep
```

## Shared material

- No theorem of the residual serves two of W1, W2, W3.
- The K-leaves (235) are shared between W1 and `Fam.colSide_alt` (through the closed D6 kernel law). None is reached by D5, D7, D8, D9.
- The `GlobalArtinReciprocity` input of W2a is also used by the closed host datum X4 and by PC-6.

## False edges

None on the paths above: every edge is a fully qualified call in a proof body (checked in the source text). The two earlier measurements of the bundle block used different tops (`bwit_exists_alt` vs `exBL_isLinked_prmR_alt`); W2 lies only under the latter.

## Counts

| | W1 | W2 | W3 | sum | union |
|---|---|---|---|---|---|
| closure in W-domain | 761 | 95 | 36 | | |
| closed earlier (kernel law) | 462 | 0 | 0 | | |
| residual before this pass | 299 (64 + K 235) | 95 | 36 | 430 | 430 |
| after this pass | 0 | 0 | 0 | 0 | 0 |
