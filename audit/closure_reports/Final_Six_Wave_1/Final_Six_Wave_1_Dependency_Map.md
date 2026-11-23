# Final Six Wave 1. Dependency map of PC-1 below `FamEx.TestPt.testFacts`

22 November 2026, final version after the global `ck`-interface check. Agent 1 of the final six-agent closure wave (Claude), for Jimmie Adriazola. Companion to `Final_Six_Wave_1.pdf`.

Source read as text from the archive's own `lean.tar.gz` (same 175,187 files and same hashes as `src/lean/src` on the files compared). Nothing was built or run, no existing file was edited. Marks: **[P]** proof body read, **[P top]** top read with children at statement level, **[S]** statement read, **[N]** numerical check run. Line counts are from a use-based closure tool (proof bodies, qualified and opened names, definitions not traversed) and overlap between rows.

Path abbreviations under `src/lean/src/`: `AP/` = `Development/AutomorphicSpectrum/Proofs/AlgebraProofs/`, `GP/` = `Development/AutomorphicSpectrum/Proofs/GeometryProofs/`, `HTP/` = `Development/WeilBound/CoreStatements/HodgeTatePoints/`, `CMF/` = `Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/`, `DL/` = `ReciprocityTheory/DualLattices/`, `DVN/` = `GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers/`.

## Verdict

**CLOSED MODULO NAMED EXTERNAL THEOREMS at the human-proof boundary.**

- Internal residuals of the human proof: none.
- Unexpanded formal implementation packages (listed below, read at their tops, not counted as human-proof residuals): C1, C2, C6, with the small formal leaves C3–C5 and the unchanged C7.
- Remaining task: statement-against-source fidelity checking of the named inputs, first `FarguesHodgeTate` (see the last section).

## Top

`testFacts` [P] (`GP/OrdinaryCurveHodgePrime.lean`, 137 lines). Use-closure 4,142 declarations, 53,167 lines, 849 files. Hypotheses passed in, not in the closure: `FarguesHodgeTate`, `QuotientByFiniteFlatStatement`, `ZarhinStatement`, `HodgeTateDatumStatement` (= `GR.Top.main`), `OrdinaryCurveStatement` (= `ordinaryCurve_of_hodgeTate`).

Conclusion `LieLatticeData.Facts` (`Definitions/CommutativeAlgebra/LieLatticeData.lean`) has six fields.

| Field | Content | Producer | Status |
|---|---|---|---|
| `le_af` | w·O_C^n ⊆ af_τ | `w_mul_forms_le_af` = `Xgn.test_leaf_lattice` (`CMF/TestLeafLattice.lean:235`) | [P top]; child `leaf_abFactor` internal (C5) |
| `im` | im H_τ = ω_τ | `pt_seq_lin` = `Xgn.t_pt_seq_lin` [P] with `htLift` = `Xgn.test_lift_exists` [S] and `ordinary_curve_model_relay` = `Xgn.test_group_point_exists` [P top] | lattice algebra closed; Fargues transport internal (C1) |
| `ker` | ker H_τ = w^(−1) Lie_τ | same | same |
| `dx` | dId_τ(i) = xId_τ(i) | `PtDx.main` [P] (`AP/MemFirstLatticeIff.lean:315`) | **closed** modulo `FlagConcl` |
| `onto` | pr₂ stepGraph_τ(i) = kk_τ(i) | `stepGraph_snd_eq_kk` [P] (`AP/HopfOrderLatticeBase.lean:137`) | **closed** modulo `h3` (Layer 3) |
| `inj` | stepGraph_{φ'τ}(i) ∩ (C×0) = span{c^p : c ∈ xId_τ(i)} | `PtInj.kernel_stepGraph` [P] (`AP/ValMulLeOfCyclicKer.lean:488`) | **closed** modulo `FlagConcl` |

Other children of `testFacts`: `lattice_base_change_larger_ring_holds` = `Xgn.character_data_base_change` [S, elementary]; `arith_variety_prime_global_relay` = `Xgn.test_order_sections` [S] (C5); `arith_variety_model_hodge_relay` = `Xgn.tight_hopf_order_test` [P top] (C2); `arith_variety_prime_hodge_total` = `Xgn.test_character_exists` [P, elementary]; `chartD_th_sqIdeal_mem_and_smul_mem_and_eig_mem_sqIdeal` = `Xgn.teichmuller_test_function` [S] (C5); `abelian_factor_tight_field_action` = `flagConcl_directFactor_of_subquotient` [P]; `quotient_zarhin_hodge_tate_subquotient` = `subquotientStatement_of_quotient_zarhin_hodgeTate` [P].

## Closure sizes by group

| Group | Closure lines | Exclusive lines |
|---|---|---|
| Frobenius layer (`PtDx.main`, `stepGraph_snd_eq_kk`, `kernel_stepGraph`, `flagStatement_holds`, `abelian_factor_tight_field_action`) | 12,454 | 6,795 |
| Subquotient (`quotient_zarhin_hodge_tate_subquotient`) | 7,274 | 1,508 |
| Kernel and image (`ordinary_curve_model_relay`, `htLift`, `pt_seq_lin`) | 40,376 | 26,900 |
| Tightness (`tight_hopf_order_test`) | 8,458 | 0 (inside kernel and image) |
| Test-point data (five producers) | 13,131 | 729 |

## Frobenius layer (closed down to Layer 3 and small leaves)

```
PtDx.main [P]                         dId = xId, from FlagConcl (idealX = idealD = (c))
  PtDx.xId_iff, dId_forward, dId_backward, fund_pow   [P] elementary
stepGraph_snd_eq_kk [P]               onto
  StepOnto.exists_inv_add_sq [P] <- ReciprocityTheory.PGsh.L2.h3 clause (iv)
    mem_sup_of_restrictToSubgroup_mem_sq [P] <- mem_of_restrictToSubgroup_eq_zero [S]   (G -> G/K is a K-torsor)
  avg_mem, avg_smul, eq_on_step [P] elementary (|F^x| unit in O_C)
PtInj.kernel_stepGraph [P]            inj
  val_mul_le_of_cyclic_ker [P] elementary (hasLen_coker_det', hasLen_le_of_surjective)
  step_bound [P]; hopf_order_lattice_base (= onto)
  FlagConcl: c^p = δ c', lengths ∏ v(δ)
flagConcl_directFactor_of_subquotient [P]
  Re.ret_hopf [S], Re.ret_tight [S]  (C4)
  flag_comparison_theorem = flagStatement_holds [P]
    FundGen.main [P]                                  Teichmüller characters
    Rc.step [P top] (exists_quo, exists_res, invres)  rank-one step orders (C3)
    eig_rank_one [P]                                  xIdeal principal
    fundamental_ideal_frobenius_product [P]           c_n^p = δ_n c_{n+1}; Ω_{σ^{p^{n+1}}} = O/δ_n
      Ra.carry [P], Ri.r_decomp [S], fundamental_ideal_frobenius_powers = Pmono.r_mono [P]
        rank_one_sum [P] <- h1 (Cartier duality) [S], Ri.r_dual [S], gauss_value [P] <- gaussCongruence [S]
        Pmono.count [P], prod_digits_sq [P]
    fundamental_ideal_frobenius_valuation [S]         monomial basis; colen^2 = (∏ v(c_n))^{q(p-1)}
    non_fundamental_eigen_le_square_augmentation [S]
    idealX_le_idealD [P]                              Raynaud ideal ⊆ Hodge–Tate ideal
      Rd.a_nonunit_of [P] (adjoin_decomp [P], stable_hopf_order_fundamental_character [S])
      Rd.a_pow [S], hopf_order_ideals_eq_top [S] (C3)
    Rb.flag_D [P top] (aflatT, triang_strong [S])    (C3)
    Rc.flag_colen [P top] <- h3 clause (iii)          (C3)
    Rc.om_split, Rd.flag_om, Rd.gr_partial [S]       (C3)
    stable_hopf_order_fundamental_ideal = Rc.om_split [S]
    Rh.grcount [P]                                     product squeeze using IsTight
```

Mathematics. The rank-one statements are Raynaud, *Schémas en groupes de type (p,…,p)*, Bull. SMF 102 (1974), Théorème 1.4.1, with Cartier duality (δ_n δ'_n = w) and Stickelberger's congruence; the archive proves them by a valuation squeeze through the Cartier dual Hopf order and Gauss sums. `FlagConcl` adds that, for a tight Hopf order whose flag subgroups satisfy `GenAF`, the Raynaud ideals equal the Hodge–Tate ideals and the ω-lengths are the products of v(δ).

**[N]** In Z_q[ζ_p] to precision p^10 for (p, f) ∈ {(3,1), (5,1), (7,1), (3,2)}: v(c) = 1/(p−1) at fundamental characters, monomial law for every m, v(δ_n) = 1, colength duality 2(v cN + v cD) = f q. Carry lemma tested on random periodic sequences. Tightness identities of `IsTight` verified exactly on 120 random rank-one Raynaud schemes. Scripts are in Appendix A of the PDF.

## Kernel and image layer

```
Xgn.t_pt_seq_lin [P]          elementary lattice algebra; needs hh.map h_t = ω and hh.comap h_b = w^(-1) Lie
Xgn.test_lift_exists [S]      exact sequence h_b, h_t and graph descriptions (C5)
Xgn.test_group_point_exists [P top]
  TestGroupPoint.typed [P]    linear algebra over O_C, uses v(p) ≤ v(w)^2 (p ≥ 3)
  TestGroupPoint.point_data [P top]
    TestGroupPoint.reducesAt_pack [P top]   EARLIEST BLOCKER (C1), closure ≈ 28,000
      exists_isParam, exists_coords, exists_levPairing [S]
      reducesAt_of (pointHT_of_fargues_hodge_tate hF) [S]
        HT.Fargues.pointHT [P] -> ordTower <- semiabelian_adic_torsion_one..four [S]
                              -> polarised_divisible_group_exists hF [S]
    chart_matrices [S]
  Sgp.core_pull [S] (uses IsTight), TestGroupPoint.lattices [S], hdual_chart [S], hq_chart [S],
  exists_der [S], pt_af_type_main [S]                                 (C1)
```

`FarguesHodgeTate` (boundary V12) has two clauses: image of the Hodge–Tate map contains κ·ω for v(κ)^(p−1) ≤ v(p), and ker(α ⊗ O_C) is the orthogonal of ker(dlog) under the pairing normalised by `muTate`.

## Hypotheses of the Frobenius layer

| Item | Declaration | Status |
|---|---|---|
| Tightness, abelian factor | `Xgn.tight_hopf_order_test` [P top] → `TightHopfOrder.core` [P top] → `Stight.BadRed.main` [S], `TightHopfOrder.exists_struct` [S], `exists_unif` [S] | internal (C2) |
| `GenAF` | `subquotientStatement_of_quotient_zarhin_hodgeTate` [P] → `tors_pts_finite` [P], `Rf.tors_hopf` [S], `sub_abelianScheme` [S], `Re.ret_hopf` [S] | internal (C4) |
| Hodge–Tate datum | `GR.Top.main` [P top] → `formal_group_chart_family` [S], `hodge_tate_datum_reduce_scalars` [S] | internal, large (C6) |
| Ordinary curve | `GR.ordinaryCurve_of_hodgeTate` [S] | internal (C6) |

## Flag independence (closed)

`ck`, `rootNum` (`DVN/InstFintypeSumElim.lean:249, 259`) use `Classical.choice` of a `FlagModel` and are 0 when none exists. `CommAlg.FlagIndependence.main` [P] = `A_s_flagindep.of_items` [P] from `PairNumberExpansionIndependence.proof`, `HsymmPairFlagIndependence.proof`, `FlagIndependence.proof`, `SymmetricSpanHsymm.proof` [P top]; used through `T.flag_independence` and `flag_model_value_independent` in `ck_rootNum_eq_pairNum_on_flagPair` [P], `SubQuotient.proof`, `ScalarQuotient.proof`, `PairCocycle`.

## `ck`-existence interface on the live route (clean)

Method: token scan of all 1,051,155 declarations for the `NumbersDVR.Bundles` `ck`/`rootNum`, then a whole-source search for every user of every hit and of every statement relay; separately the use-closure of the live `DeepStR` producer `GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use` (contains `testFacts`, `goodOrigin_linked`, `GoodModel.relations`, `TopRel.relations`, `familyExistsPos_holds`).

1. **Closed family.** 43 declarations found by the scan (the two definitions, the local Chern lemmas `Cocycle.main`, `QuotAdd.main`, `SubQuotCk.CkAdd`, `Constants.main`, `ck_rootNum_dual`, `CkLinePow.main`, `LineCk.main`, `CkFlagSum.main`, `CkTransport.main`, `CkPullBirat.main`, `QuotIsoCk.main`, `ck_eq_of_quotEquiv`, `Xgn.t_rootnum_dual`, the relation producers `HodgeTate.main`, `RelH.relH_main`, `RelK.main`, `GoodModel.relations`, `BiratJoin.ckRelations_descend`, the definition `CkRelations`, the bridges `ck_rootNum_eq_pairNum_on_flagPair`, `ChernClassOnFlagPair.proof`, 13 `GlobalTheory.T` relays, `ChernClassOnFlagPair.Statement`, five definitions in `SameGenericSymm.lean`), plus `CkRelations.key`, `main_of`, `main` added by hand. Every user is in the family except one. Same-tail name collisions (`UnivCocycle.main`, `RealPeriodCocycle.main`, `LieHodgeTate.main`, …) checked and excluded.
2. **Single exit.** `TopRel.relations` [P] (`AP/ArithmeticRelationsStatementHolds.lean`) ← `lattice_family_ckRelations` + `uniformizer_model_perm_module_lattice` = `CkRelations.main_of` [P]. `CkRelations.key` [P] requires `IsFlagPair` for the explicit `LocPair` T and proves ck(E,E') = `T.ck` = pairNum(T) and k·rootNum = `laNum`, via `ChernClassOnFlagPair.proof` [P] (`DVN/PTwinCkOnFlagPair.lean:74`, assembled in `ChernFlagPairRootPolynomial.main`): `JoinPointFlagModel.proof` builds F₀ from the flag pair, `Nonempty FlagModel` from F₀, `dif_pos`, then `flag_model_value_independent` / `flag_model_root_independent`. The zero branch cannot reach the exit.
3. **Exported statements use no choice.** `Relations`, `LabelChernComparison`, `BundleChernComparison`, `FlagChernComparison`, `HodgeLatticeFlagBound` are stated with `LocPair.ck` = pairNum on explicit flag data.
4. **Flag pairs supplied on the route.** `model_on_hodge_of_family_pos` [P] (`GP/ModelOnHodgeFromFamily.lean:60–135`): `arith_variety_dedekind_constants` (flag pairs for `labelPair D T s`), `flag_pair_chart_bundle_compat` (dual side, `omPair D T s`), `model_descent_valuation_fibre` (to O'). T is the global flag of `Fl.TwoLevels`, the same T as in `HodgeLatticeFlagBound`.

Verdict of the check: **clean**. The risk recorded in the first version is removed.

## Required checks

- Exactness: all fields of `Facts` are equalities except `le_af`, an inclusion used as a hypothesis. **Confirmed.**
- Level: R = 𝔐.R p enters as precision p^(R−2) in `DualSeq`/`hdual_chart` and through ζ^(p^(R−1)) = ζ_p; w = ζ_p − 1 at every level. **No level-dependent error.**
- Stronger internal version: yes, `FlagStatement` (Raynaud = Hodge–Tate ideals under tightness) and `HodgeTateDatumStatement` (internal integral Hodge–Tate datum for all polarised abelian schemes over O_C).

## Internal residuals of the human proof (none)

None.

## Register of unexpanded formal packages implementing known mathematics

C1, C2, C6 are the packages named in the instruction. C3–C5 are small formal leaves whose mathematics is stated in the report. C7 was not reopened; the Post-Closure Synthesis describes it as standard internal bookkeeping of a known mechanism.

| ID | Declarations | Known mathematics implemented | Downstream | Size | Reading status |
|---|---|---|---|---|---|
| C1 | `TestGroupPoint.reducesAt_pack`, `point_data`, `HT.Fargues.pointHT` children (`polarised_divisible_group_exists`, `semiabelian_adic_torsion_one` to `_four`), `Sgp.core_pull`, `TestGroupPoint.lattices`, `hdual_chart`, `exists_der` | Fargues's integral Hodge–Tate sequence read at level p in chart coordinates | `im`, `ker` | medium (≈27,000 exclusive) | top read |
| C2 | `Stight.BadRed.main`, `TightHopfOrder.exists_struct`, `exists_unif` | uniformisation of a degenerating abelian scheme; v(disc) = \|G\| deg ω, (p−1)·len AFQuot = deg ω | `IsTight`, `IsAbFactor` | medium | top read |
| C6 | `GR.Top.main` (`formal_group_chart_family`, `hodge_tate_datum_reduce_scalars`), `GR.ordinaryCurve_of_hodgeTate` | integral Hodge–Tate datum of a polarised abelian scheme over O_C from its formal group; ordinary elliptic curve | C2, C4, hypotheses of `testFacts` | large | top read |
| C3 | `hopf_order_ideals_eq_top`, `Rb.flag_D` (`aflatT`, `triang_strong`), `Rd.flag_om`, `Rd.gr_partial` (`Rb.fund_ex`, `Rc.subquo`, `Rc.om_step`), `Rc.om_split`, `Rc.flag_colen`, `Rc.step` | length bookkeeping along a flag; étale case | `FlagConcl` | small to medium | statements read |
| C4 | `sub_abelianScheme`, `Re.ret_hopf`, `Re.ret_tight`, `Rf.tors_hopf` | quotient by finite flat subgroup with Zarhin; retracts | `FlagConcl` | small to medium | statements read |
| C5 | `Xgn.test_order_sections`, `Xgn.teichmuller_test_function`, `TestLeafLattice.leaf_abFactor`, `Xgn.test_lift_exists`, `Xgn.character_data_base_change` | test-point Hopf orders, Θ-clauses, `le_af`, exact sequence, base change | all fields | small | statements read |
| C7 | PC-1 parts (b), (c) other than flag independence, (d), (e) | lattice family construction, local Chern calculus, model change, trivial flag | `FamilyExistsPos`, `GoodModel.relations` | medium | as in `Post_Closure_Internal_Residuals.md` |

## Moved to the external boundary (Layer 3: internal proofs of published statements, pending fidelity pass)

| Published statement | Declarations |
|---|---|
| Raynaud 1974, Théorème 1.4.1, with Cartier duality δ_n δ'_n = w (V20, matched in content) | `eig_rank_one`, `Ri.r_decomp`, `Ri.r_dual`, `rank_one_sum`, `Pmono.r_mono`, `fundamental_ideal_frobenius_product`, `fundamental_ideal_frobenius_valuation`, `non_fundamental_eigen_le_square_augmentation` |
| Stickelberger's congruence, v(g(ω^(−1))) = 1/(p−1) | `gauss_value`, `ReciprocityTheory.PGsh.gaussCongruence` |
| Quotients of finite flat group schemes (SGA 3 Exp. V; Raynaud 1967): torsor, cotangent right exactness, discriminant transitivity | `ReciprocityTheory.PGsh.L2.h3` and children, `Rc.exists_quo`, `Rc.invres` |
| Cartier duality of Hopf orders (Tate–Oort 1970 §1) | `ReciprocityTheory.PGsh.L2.h1` |

Unchanged hypotheses: `FarguesHodgeTate`, `FarguesExact`, `ZarhinStatement`, `QuotientByFiniteFlatStatement`.

## Remaining task: statement-against-source fidelity

1. `FarguesHodgeTate` against Fargues, *L'isomorphisme entre les tours de Lubin–Tate et de Drinfeld*, Ch. II, both directions: image ⊇ κ·ω for v(κ)^(p−1) ≤ v(p); ker(α ⊗ O_C) = orthogonal of ker(dlog). Check `PDivGroup`, `hodgeTateLinear`, `dlogLinear`, `muTate` against Fargues's conventions. The 1/(p−1) of the local identity rests on this input.
2. `FarguesExact`, `ZarhinStatement`, `QuotientByFiniteFlatStatement` (V12, Layer 3).
3. Layer 3 matches: Raynaud 1974 Thm 1.4.1 with Cartier duality; Stickelberger's congruence; quotients and Cartier duality of finite flat group schemes.

## Does PC-1 still block "The entire RH proof has been reconstructed in ordinary mathematics modulo named external theorems"?

No, at the human-proof boundary. The formal implementation in C1, C2, C6 (and C3–C5, C7) is listed and was read only at its top; it is not counted as a human-proof residual. The remaining task is the fidelity check above, first `FarguesHodgeTate`. No new engine and no apparent gap.
