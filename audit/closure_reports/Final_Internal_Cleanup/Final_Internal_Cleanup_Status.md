# Final internal cleanup: status ledger

22 November 2026. Written by Claude for Jimmie Adriazola, for the final synthesis agent. Read-only pass. Nothing in the project, the manuscript, the earlier reports or the Lean archive was edited. Nothing was built or run in Lean. The full report is `Final_Internal_Cleanup.tex` / `.pdf` in this folder.

Sources copied and checked by SHA-256 against the originals before the work began: `lean.tar.gz` (239,275,554 bytes; equal to the concatenation of the fourteen parts; 175,187 `.lean` files, 1,030,531,854 bytes, identical file count and byte total to `src/lean`), and 137 report and ledger files (`Claude_Audit_Core`, `Pre_Synthesis_Audit` with `Orphan_Interface_Pass`, `Directory_Assessment`, `RH_Route_Notes.tex`, `HANDOFF_Next_Agent.md`, the Zhang and Slijepčević preprints). The checksum of the sorted checksum list agreed on both sides.

## A. Final internal verdict

**YES.** Live internal mathematical residuals remain. They are the three blocks below, all inside the PC4.13 family construction and its record witness. SL-6 is closed and both liveness families are settled.

## B. Exact residual table

Sizes are *exclusive* theorems: theorems of the block's forward closure that no other live branch reaches once the block's root is removed (exact-edge graph, privacy-aware). Material shared with other live branches is owned by those branches and is not counted here.

| theorem/family | live? | owner | mathematical content | mechanism | external boundary | verdict |
|---|---|---|---|---|---|---|
| `SelAll.bwit_exists_alt` with `Top.Bl.exBL_isLinked_prmR_alt` (record witness) | LIVE (path checked edge by edge, §E of report) | PC-6 record core | Proposition BW: eventually in the context, every record-compatible realisation at every weighted point is the realisation of a bundle carrying a witness | assembly of six producers (read in full) plus the host datum; 653 exclusive theorems | GlobalArtinReciprocity, RayField, DiscreteSeries/Harish-Chandra statements (already on boundary) | **RESIDUAL CHILD REMAINS**: X1 base-tuple kernel laws and column reading (`TC.RcHyp.chTh_ok_chi`, `SelC.colRecC`, about 313 thm), X7 pinned spectral data (`WPt.exists_pinned_spectral_data_compatible`, `CyclotomicFieldContainment.oTied_of_ksExact`, 73 thm) and kernel spectral data at witnesses (22 thm), X2 leaf `reFace_zero_part_conventions_chosen_again` (30 thm). Closed in this pass: Hecke parts (108), host datum (19), lower-map ties (13), side and real-input transport (14), placement rescaling (6) |
| R4-D, `Fam.colSide_alt` (PC4.13 tuple construction) | LIVE | PC-4 | Proposition B(ii),(iii): readings, row-pair constants, volume constants, kernel Weil data, column twist data for every tuple, with constants uniform in the tuple | assembly read in full (223 lines); quantifier order checked | Kudla splitting (new boundary row) | **RESIDUAL CHILD REMAINS**: 2,816 exclusive theorems, of which 1,073 (the `laws` field, `seeSawTwistPlaceLaws_of_rootOfUnityRescaling`) are transferred to PC-4 R4-A to R4-C. Remaining 1,743 theorems (28,746 lines) in eight heads: `dat_exists` children (row-pair rational datum), `exists_good` and the two commutation statements under `readsExists_alt`, `chain_step_value`/`chain_step_identity` (volume uniformity), `AdForm.twS_ramL`, `KRamT.kernel_keeps_ramT`, `QVecJoin.step_mid`/`step_top`, `true_geometry_row_column_entry_alt`, `true_geometry_twist_value_alt`. Closed in this pass: kernel Weil data (mod Kudla), finite-combination data, index-level gluing mechanism |
| R4-E, `AdForm.clsPinD_of_famCol_of_trueW` (class data) | LIVE | PC-4 | Proposition C (orphan pass): one real datum for the family, kernel and top class data per tuple, constants depending on the datum alone | mechanism as stated in the orphan pass; heads listed | Schur orthogonality, multiplicity-one branching, class-number finiteness (boundary) | **RESIDUAL CHILD REMAINS**: 479 exclusive theorems in five heads: `KerTup.kernel_identity_tuple` (204), `AdForm.LevLaw.lev_law` (97), `exists_clsT_of_pinTop` (85), `JetScales.exists_jetS` (35), `realOf_is` (29), `exists_readsG_of_level` (27) |
| SL-6a `GaugeVolUD` (`Pf.GV.gaugeVolU`) | LIVE | PC-6 SL-6 | gauge-normalised Haar measure of U(k) has total mass ∏_{i<k}(2π)^{i+1}/i! | Gaussian integral over M_k(ℂ) in QR coordinates gives the QR constant ∏2π^{j}/(j−1)!; exponential chart Jacobian tends to 1; Lebesgue differentiation; factor 2^{k(k−1)/2} between coordinate and Frobenius measures | none (classical analysis) | **CLOSED**; constants checked symbolically for k ≤ 12 |
| SL-6b `RhsWLim` (`RankOneChart.rhsWLim`) | LIVE | PC-6 SL-6 | Haar measure of U(1,k) in double-coset coordinates H_z·m(ζ)·H_{z'} has Jacobian wbConst = 2 vol U(k)² /((TT')^k vol U(k−1) a a') against (|ζ|²−TT')^{k−1} dζ ⊗ μ_W ⊗ μ_{W'} | fibration G→G/H_{z'} = hyperboloid; Gelfand–Leray invariant measure; pushforward of ⟨v,z⟩ is π^k/((k−1)!T^k)(|ζ|²−TT')^{k−1}; sphere fibres are U(k)-orbits | none (classical analysis; Weil's quotient formula is on the boundary) | **CLOSED**; constant derived independently and matched for k ≤ 12 |
| SL-6c `CoefCapAll` (`coefCap_carrierInT_own`) | LIVE | PC-6 SL-6 | Capelli operator acts on the carrier coefficient functions by ∏_s(Y+λ_s) | Capelli operator on matrix coefficients equals the coefficient of the quantum determinant (`capelliH_cf_rect`); the quantum determinant acts by the Harish-Chandra image on a discrete series with lowest K-type λ (`infChar_of_model` with the explicit eigenfunction `PsiM`) | Capelli identity (Molev ch. 7, on boundary); Harish-Chandra's infinitesimal character of discrete series and the lowest-K-type characterisation (Schmid, Vogan) | **CLOSED modulo named external theorems** (transfer) |
| Family 1 `UpperTheory.V.Pa.secondCohomologyBound_of_boundaryBound` | **LIVE** via `pFromAut → raw → coreBC → Pa.core → cohLim` (the earlier path through `norm → core` is a false edge) | patching route | second Selmer bound at every level mod t^m gives a class over K[[t]] | ultrafilter limit over m (compactness) | Taylor–Wiles–Kisin patching row (proved in archive) | **LIVE AND CLOSED** |
| Family 2, 25 declarations named `core2`, `third_identity`, `stepB_of`, `lift1`, `fixBd`, `pair_count`, `detFin`, `alInj` | 23 LIVE, 2 DEAD (§E) | per route | see §E | see §E | Turán (one member), Siegel–Weil and Howe duality (Layer 3) | **resolved**: no member is LIVE AND RESIDUAL |

## C. Newly closed items (statements in the report, §§3–6)

1. Proposition SL6a (gauge volume of U(k)), with proof.
2. Proposition SL6b (Jacobian constant of the double-coset decomposition of U(1,k)), with an independent derivation of the constant.
3. Proposition SL6c (Capelli eigenvalue on carrier coefficients), modulo Capelli and Harish-Chandra.
4. Proposition BW (the statement of `bwit_exists_alt`: hypotheses, object, downstream need, uniformity), and five of its sub-blocks: Hecke parts, host datum, lower-map ties, side and real-input transport, placement rescaling.
5. R4-D kernel Weil data (Proposition KW, modulo the existence of splitting characters), finite combination data, and the gluing mechanism of the index-level readings.
6. Liveness of both families, with one correction to Wave 6 (`TorsionCardinalitySetup.Setup.core2` is live by dot notation) and one correction of a witness path (Family 1).

## D. Transfer ledger

| item | from | to | reason |
|---|---|---|---|
| `laws` field of `colSide_alt` (`seeSawTwistPlaceLaws_of_rootOfUnityRescaling`, 1,073 exclusive theorems: `QLaw`, `QLast`, `QFin`) | R4-D | PC-4 R4-A to R4-C | these are the seesaw twist-place laws; the pre-synthesis audit classes R4-A to R4-C as implementation depth with human propositions stated |
| `KomExist.exists_compactOpen_alt` (kernel Weil data) | R4-D | external boundary (new row) | existence of splitting characters / Weil data for unitary dual pairs given a Hecke character of the right parity (Kudla 1994; Harris–Kudla–Sweet 1996; from memory), proved internally by `WeilDatumExistence.weilDatumExists` |
| SL-6c | PC-6 SL-6 | external boundary | Capelli identity (row exists); add Harish-Chandra's theorem that a discrete series with lowest K-type λ has infinitesimal character λ (with the lowest-K-type characterisation used by `IsDS`) |
| SL-6a, SL-6b | PC-6 SL-6 | closed | classical measure theory and Gaussian integrals |
| `HostDatumExists.exists_hostDatum_alt` | PC-6 record core | external boundary (existing rows) | Hilbert class field as the ray class field of conductor 1 (`GlobalArtinReciprocity`, `RayField`) |
| Family 1 | PC-6 sweep (R8) | patching route | live, closed as an ultrafilter-limit step of patching |
| `TorsionCardinalitySetup.Setup.core2` | "off route" (Wave 6) | Galois side (`FiniteEtaleModels`) | live by `hS.core2` in `lat_main`; content is an elementary counting identity |
| `HoweR.QuadT.core2` | unowned | Howe-duality package (Layer 3) | commutator identity in the Weyl algebra |
| `Rg.Sw.HSt.L3.core2` | unowned | Siegel–Weil package V5 (Layer 3) | vanishing of a singular determinant integral in the holomorphic continuation |
| private `core2` in `DecompU.lean` | unowned | V-window automorphy route | transport of fixed vectors through the automorphic-form dictionary |

## E. Liveness resolution

**Family 1.** `UpperTheory.V.Pa.secondCohomologyBound_of_boundaryBound`: **LIVE AND CLOSED**. Witness path, every edge read:
`riemannHypothesis → rhOfAll → allChi → everyCharacter → everyCharacter_of_row → vwin_of_row → automorphic_window_of_inputs → v_window_of_depth_zero_residual_bc_cm → v_window_of_literal_automorphy_n → v_window_of_automorphy_csd_ss_mono_odd → vwin_of_hypotheses_H_E_alt → Dn.ends0_alt → J.linkedUnlE_holds_alt → HV.Core.modU_of_printsH → Pa.pFromAut → Pa.raw → Pa.coreBC → Pa.core → Pa.cohLim → Pa.secondCohomologyBound_of_boundaryBound`.
`pFromAut` names `UpperTheory.V.Pa.raw` explicitly; `raw := raw_main coreBC`; `coreBC` calls `core l L G0 T n O' r' …` at `CoreBC.lean:49` with no local binder named `core` and no private `core` in that file; `Pa.core` calls `cohLim` at `LiftPt.lean:149`; `cohLim` names the declaration in `CohLim.lean`, namespace `UpperTheory.V.Pa`. The path recorded in Wave 6 (`norm → core`) resolves `core` in `ConjugationDescendsToSubring.lean:229` to `Pa.core`, but that file has a private `core` (line 137) with four explicit arguments, which is the one used. The orphan pass's candidate through a local `key` is also false. The live path above replaces both.

**Family 2.** 25 declarations.

| declaration | status | route of the witness path | content | class |
|---|---|---|---|---|
| `GlobalTheory.HoweR.QuadT.core2` | LIVE | Howe duality (`howeDualityReal_holds`) | Σ_a l_{ai}u_{aj} = Σ_a u_{aj}l_{ai} + δ_{ij}·#ι | LIVE AND CLOSED |
| `UpperTheory.TorsionCardinalitySetup.Setup.core2` | **LIVE** (dot notation `hS.core2`, `TraceIdentityOfTjElement.lean:502`, in `lat_main`, called by `trace_identity_of_tjElement` = `CovMain.trTj_of`, used in `FiniteEtaleModels.stepB`) | Galois side | #{g : K(g), killed by 𝔴} = [Λ : H₀Λ + 𝔴Λ] | LIVE AND CLOSED (corrects Wave 6) |
| `UpperTheory.Reformulated.B.DeterminantIdentities.core2` | LIVE | V-window | determinant lifting (Wave 6) | LIVE AND CLOSED |
| `…PrimesInProgressions.TuranPowerSumBounds.core2` | LIVE | primes in progressions, Galois side | Deuring–Heilbronn from Turán power sums | LIVE AND EXTERNAL (Turán's second main theorem) |
| `Formalism.FourierDecayAlt.P.GermSumLattices.core2` | LIVE | CarrierGap via `germ_identity_bis` | lattice Gauss sum (Wave 6) | LIVE AND CLOSED |
| `Formalism.FourierDecayAlt.P.MAx3.F.core2` | LIVE | CarrierGap | matrix identity along cut words (Wave 6) | LIVE AND CLOSED |
| `UpperTheory.V.Pr.core2` | LIVE | V-window | valuation comparison (Wave 6) | LIVE AND CLOSED |
| private `core2` (`HeckeAlgebras/OrdinaryHeckeCharacters/DecompU.lean:105`) | LIVE (via `decompU`, same file) | V-window, Hida | fixed vectors transported through the automorphic dictionary | LIVE AND CLOSED |
| `PositivityTheory.Rg.Sw.HSt.L3.core2` | LIVE | Siegel–Weil (`siegelWeilStd_k`) | ∫ψ(s)·det(RR*−i(H₀+herm s))^{−m} ds = 0 for m<n and singular test ψ | LIVE AND EXTERNAL (Layer 3 of Siegel–Weil, V5) |
| `Formalism.FourierDecayAlt.P.Fr6.core2` | LIVE | CarrierGap | cancel an invertible factor (Wave 6) | LIVE AND CLOSED |
| `Formalism.L2.Th1.B.Det.core2` | LIVE | F4 jets | Weierstrass polynomial identity (Wave 6) | LIVE AND CLOSED |
| `Formalism.FourierDecayAlt.P.third_identity` | LIVE | CarrierGap | energy identity (Wave 6) | LIVE AND CLOSED |
| `UpperTheory.Gal.FiniteEtaleModels.stepB_of` | LIVE | Galois side | assembly of eight Galois-side statements | LIVE, transferred (Galois side) |
| `PI.UnitKronW.stepB_of` | LIVE | `finite_order_adelic` | Kronecker's theorem | LIVE AND CLOSED |
| `Formalism.DivisionValues.stepB_of` | **DEAD** | exact and dot reverse closure {stepB_of, reduction_second_step, stepB}, exhausted | | DEAD |
| `Formalism.MainNotions.PlaneGram.stepB_of` | LIVE | G-link | valuation collapse after Fock projection | LIVE AND CLOSED |
| `UpperTheory.V.Pa.lift1` | LIVE via `Pa.core → galOut → ctx_out → pres → claim1 → lift1` (the `mkPt` edge is a local `have lift1`, false) | patching | first-order lift | LIVE AND EXTERNAL (patching row) |
| `GlobalTheory.CompanionTheory.CosieveBC.lift1` | LIVE | Hodge–Tate comparison | definition (tensor-product lift) | LIVE AND CLOSED |
| `LateralTheory.CohomologicalPurity.Thom.ExcP.Chart.lift1` | **DEAD** | exact reverse closure 21 declarations, exhausted; no `.lift1` dot use in the archive | | DEAD |
| `GlobalTheory.ThK.Dbl.Inert.lift1` | LIVE | theorem K | definition (inert local lift) | LIVE AND CLOSED |
| `Formalism.MainNotions.ColumnSystems.Pf.lift1` | LIVE | growth bounds | substitution homomorphism (abbrev) | LIVE AND CLOSED |
| `UpperTheory.V.Pa.fixBd` | LIVE via `pFromAut → b1Ar → b1abs → W1_bound_arithmetic_rank_two → h0q → fixBd` | patching | fixed-vector bound | LIVE AND EXTERNAL (patching row) |
| `pair_count` | LIVE via `W1_bound_arithmetic_rank_two → locV → pair_count` | patching | cocycle count bound | LIVE AND EXTERNAL (patching row) |
| `UpperTheory.V.Pa.Det.detFin` | LIVE via `pFromAut → choice → Det.detFin` | patching | determinant over a finite algebra | LIVE AND EXTERNAL (patching row) |
| `UpperTheory.V.Pa.alInj` | LIVE via `Pa.core → … → claim1 → alInj` | patching | injectivity of a conjugation map | LIVE AND EXTERNAL (patching row) |

No member of either family is LIVE AND RESIDUAL. The patching members belong to the package that `Post_Closure_Verification_Boundary.md` lists as "Taylor–Wiles–Kisin patching, proved in the archive through `litN`" and that Final 5 read at statement level.

## F. Final claim consequence

**NO.** The sentence "Every live internal mathematical step on the RH route has been reconstructed in ordinary mathematics or transferred to an explicit external theorem boundary" cannot yet be said. Theorem by theorem:

- `bwit_exists_alt` / `exBL_isLinked_prmR_alt`: statement, hypotheses, object, uniformity and assembly reconstructed; five sub-blocks closed; X1 (base-tuple kernel laws and column reading, about 313 theorems), X7 (pinned and kernel spectral data, about 95 theorems) and the X2 leaf (30 theorems) have mechanisms identified at their heads and unread bodies of genuine identities. Not closed.
- R4-D `colSide_alt`: assembly and quantifiers reconstructed; laws transferred to R4-A–C; kernel Weil data transferred to Kudla; eight heads (1,743 exclusive theorems) remain as stated identities without reconstructed proofs. Not closed.
- R4-E `clsPinD_of_famCol_of_trueW`: Proposition C stands; five heads (479 exclusive theorems) unread. Not closed.
- SL-6a, SL-6b: closed. SL-6c: closed modulo Capelli and Harish-Chandra.
- Family 1, Family 2: settled; none residual.

The surviving set is about 2,700 exclusive theorems in sixteen named heads, all on the PC4.13 family construction and its record witness. A common thread in X1, D6 (`kernel_keeps_ramT`) and E1 (`kernel_identity_tuple`) is the step-kernel theta-equivariance law at specific data, so a single reconstruction of that law at the needed generality would likely discharge three heads at once.

## Method notes and limits

- Index: 1,066,087 declarations. Names resolved through namespaces, the declaration's own name prefix, active `open`s (including `open … in`), `_root_`, trailing projections, and privacy (65,565 private declarations visible only in their own file). Dot notation on local variables is handled as a separate over-approximating edge class. Typeclass resolution is not followed.
- Every LIVE claim above has a printed witness path whose short-name edges were read in the caller's text; two false edges were found and replaced.
- Every DEAD claim has an exhausted reverse closure and a text search for dot-notation uses.
- Exclusive sizes depend on the graph. False edges elsewhere can make material look shared, and missed edges can make it look exclusive, so the counts are indicative. The heads themselves were read at the top.
