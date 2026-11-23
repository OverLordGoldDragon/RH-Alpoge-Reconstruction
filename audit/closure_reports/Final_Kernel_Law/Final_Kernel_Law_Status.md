# Kernel-law pass: status ledger

22 November 2026. Written by Claude for Jimmie Adriazola, for the next cleanup pass and the final synthesis agent. Read-only. Nothing in the project, the manuscript, the earlier reports or the Lean archive was edited. Nothing was built or run in Lean. The full report is `Final_Kernel_Law.tex` / `.pdf` in this folder; the updated residual table is `Residual_Heads_After_Kernel_Law.tsv`.

Sources: `lean.tar.gz` reassembled from its fourteen parts, SHA-256 `9631b4f0…3f49c7fc` (the Kernel Replay value), 175,187 `.lean` files. Reports copied and checked readable: `Final_Internal_Cleanup` (report, status, `Residual_Heads.tsv`, `Liveness_Witness_Paths.md`, scripts), `Final_Six_Wave_6` and `Final_Six_Wave_4` with dependency maps, `Orphan_Interface_Pass` (report, tables, map), `Post_Closure_Synthesis`, `Orphan_Dependency_Audit.md`, `Core_Report_7_Kernel_Law.tex`, the kernel replay report. The cleanup index and graph were rebuilt with the cleanup scripts (1,066,087 declarations; block-exclusive sets reproduced to within one theorem).

## Findings

1. **X1 and D6 are one law; E1 is not.** X1's head `TC.RcHyp.chTh_ok_chi` rests on `ThEquivP` of every step kernel (`Cd.CarC.thEquivP_ambOf_tiesD`). D6's head `KRamT.kernel_keeps_ramT` rests on the same equivariance in decorated-point form (`KerDia.Eqv.ent_smul`) plus diamond invariance. E1's head `KerTup.kernel_identity_tuple` is the identification of the adelic Weil theta kernel at the split places with the jets of the classical theta series with finite data (`thetaKernel_eq_jet_thC`, `reads_datum_eq_thC`), a model comparison.
2. **The shared base-vector law was uncounted.** The covariance of the base theta vector (`Base.EqP`, `eqP_car`) is reached by all three blocks and so was exclusive to none. The union of the three blocks has 451 theorems inside the law that no head counted.

## A. Common kernel proposition (Proposition A of the report)

For a CM field E with CM type Φ, even ranks a, b, self-dual hermitian O_E-lattices N ⊂ E^a, N' ⊂ E^b and γ ∈ U_a(E), γ' ∈ U_b(E), with R(z)_τ = τ(γ') z_τ τ(γ)^{-1} on V = ∏_τ M_{b×a}(ℂ):

- (i) base vector: e(γN, γ'N') = e(N, N') ∘ R^{-1};
- (ii) kernels: θ_{γN,γ'N'}[c, γ'xγ^{-1}] = θ_{N,N'}[c, x] ∘ R^{-1}, and the same for datum kernels θ[Ξ] with Ξ ↦ Ξ ∘ Ad^{-1};
- (iii) step kernels: under the product law for the frame characters (infinity type e) and the weight law n + b/2 − e = detShift(λ), e − a/2 = −detShift(λ'), and K-rationality of the jets, th(γN, γ fr, γ'N', γ' fr', c, γ'xγ^{-1}) = ρ_{λ'}(γ') ∘ th(N, fr, N', fr', c, x) ∘ ρ_λ(γ)^{-1};
- (iv) decorated form: if the ξ-data satisfy the step-character law, ent(gp, g'p') ∘ tr(g) = tr(g') ∘ ent(p, p').

## B. Proof (summary; details in the report, Section 5)

- **Transport (Lemma 2).** R is an isometry of the Fock form, fixes the semicharacter, carries the period and level lattices of (N, N') to those of (γN, γ'N'), and commutes with Heisenberg operators and averaging intertwiners.
- **Base vector (Section 5.2).** e = χ-factor × I∘I(θ_0). Theta spaces of self-dual lattices are lines; path independence on the move triangles and squares (Weil's triple constant is 1 on split triples); transport of intertwiners; the constant of pulling θ_0 by γ is (∏_τ τ(det γ̄))^{b/2} (Lemma 3). Lemma 3: split γ into fixed-point-free factors; Weil's formula gives the constant as (|det A|/det A)·g with A = 1 − δ^{-1} and g a normalized Gauss sum; by rows the constant is ((|a_1|/a_1) g_1)^b; the Cayley determinant gives (|a_1|/a_1)^2 = ∏_τ τ(det γ̄) (dim even); g_1^2 = 1 because −1 is a norm modulo 4|M| (so g_1 is real and of modulus one); b even makes the sign irrelevant. The χ-factor cancels the constant exactly.
- **Kernels.** Naturality of the finite Heisenberg induction under R, and change of the summation variable for datum kernels.
- **Jets (Lemma 4).** Chain rule for the linear substitution z ↦ hzg.
- **Characters (Lemma 5).** χ on norm-one determinant ideals (det ideal of γN is (det γ) times that of N); product formula for the Hecke character of the frames at u = det γ ∈ E^1; weight identity.
- **Mechanism classification.** Covariance of the theta kernel, change of variables, character matching and a finite-level Gauss-sum identity. The Weil representation enters only as Weil's constant of a fixed-point-free unitary on a theta space. No local splitting and no Haar normalization beyond relative indices.
- **Published theorem.** Weil, Acta Math. 111 (1964): the fixed-point-free and triple constants (`UnitaryConstant`, `tripleFormula`), proved in the archive outside the three blocks and already on the boundary (Wave 6, F4, Group C). No new boundary row.

## C. Application table

| occurrence | exact Lean head | common law sufficient? | extra input | verdict |
|---|---|---|---|---|
| X1, kernel laws of the base tuple under `bwit_exists_alt` | `GlobalTheory.Mem.Col2.TC.RcHyp.hyps_of_isTw` / `chTh_ok_chi` via `Cd.CarC.thEquivP_ambOf_tiesD` | yes, for the equivariance conjunct | χ = column character on norm-one ideals (`jetsRat_chi`; det ideals of self-dual lattices are norm one); tuple ties `LawTies`, `MuqTie` (given), which identify `muAt` with `muAtT`; admissibility bookkeeping (`stepC_ok_deg`, `jetAddDeg_of`, read in full). Not part of the law: `idxMatNF_of_isTw` (5 thm) | **Closed** (249 thm); normal-form leaf moves to the column reading |
| D6 | `GlobalTheory.KRamT.kernel_keeps_ramT` | yes, in decorated form (iv) | diamond invariance (`th_dia`, `rho_dia`); weight preservation (`kmap_mem_valC`, `sharp_mem_range`); the averaging argument | **Closed** (96 thm); head disappears |
| E1 | `GlobalTheory.KerTup.kernel_identity_tuple` | no | model comparison (Proposition E): Weil-datum axioms (Kudla, on the boundary), moved vacuum (pinned, `PinX.mv`, producer `MovedVac.vac_moved` outside), finite Fourier expansion and half-component identities at split places, datum transport `movedDatum_eq_finiteDatum_representativePair`, characters `chr_moves_eq_rho_base`, level-pair law `lev_law` | **Residual child remains** (mechanism reconstructed) |

## D. Updated residual list

| ID | content | size (thm) |
|---|---|---|
| W1 | column reading at the base tuple (`colRecC` glue, `chKerC_congr`, `jetK_chi`, `exists_eNu`, rank-one norm-one lattice, step-zero class sum, `exists_read_fam`, DecoFin/EvRow leaves) and the normal-form leaf `idxMatNF_of_isTw`/`twNF_imp_matNF` | 64 |
| W2 | pinned and kernel spectral data (`exists_pinned_spectral_data_compatible`, `exists_kernel_spectral_data_at_witnesses`) | 95 |
| W3 | `reFace_zero_part_conventions_chosen_again` | 30 |
| D1 | row-pair rational-datum identity (`dat_exists` children) | 741 |
| D2 | `exists_good` and the two commutation statements | 571 |
| D3 | volume uniformity | 516 |
| D5 | `AdForm.twS_ramL` | 182 |
| D7 | `QVecJoin.step_mid`, `step_top` | 88 |
| D8 | `true_geometry_row_column_entry_alt` | 61 |
| D9 | `true_geometry_twist_value_alt` | 51 |
| E1a | datum-reading leaves of Proposition E (finite Fourier expansion `four_expand`; half-component vacuum identities `heisO_halfA_eq`, `heisO_conjHalf_eq`; finite-index and character leaves), with jet/parity glue | 191 |
| E1b | datum transport `tw_resid_datum` (102, shared with R4-D, newly counted) and `chr_moves_eq_rho_base` (13) | 13 (+102) |
| E1c | `LevLaw.lev_law`, `clsKL_real` | 103 |
| E2–E5 | last-period class data, jet scale, real data by branching, readings by Schur | 176 |
| K-a | integrality of (√d/2)·H on admissible period lattices (`rational_integrality_link`, `hermitian_form_integral_values`) | 105 (newly counted) |
| K-b | standard theta data `SO.stdOK` | 41 (newly counted) |
| K-c | split data for the move triangles and squares (inside `sqSplit_of`, `muOneL_of`, `muOneR_of`) | 97 (newly counted) |

Heads: 16 → 15 (D6 disappears; X1 shrinks to W1). Residual inside the old heads: about 2,660 → about 2,320 on the ledger (−345, about 13%). Newly counted shared material: 102 (E1b) + 243 (K-a to K-c), all at statement level; 208 further shared theorems of the law are closed by the report.

## E. Final verdict

**NO.** The law is reconstructed and closes X1's kernel core and all of D6, and it settles the shared base-vector covariance. It does not close E1 and does not reach D1, D2, D3, D5 or E2–E5. The residual drops by about 13% and the head count by one.

## Method notes and limits

- Index and graph: the cleanup's own scripts (`index_decls.py`, `build_graph.py`) on the unpacked archive, with the private-declaration list from `rg`. Exact edges only; typeclass resolution not followed; dot edges not used for exclusivity.
- New scripts in `scripts/`: `kl_sub.py`, `kl_classify.py`, `kl_heads.py`, `kl_joint.py`, `kl_where.py`. Paths at their tops assume `/home/claude/idx` and `/home/claude/lean_src`.
- Counts are indicative to within a few theorems. The D2 recount (147) differs from the ledger (571) because the short name `exists_good` resolves to one declaration; ledger values are used in totals.
- Read in full: `hyps_of_isTw`, `chTh_ok_chi`, `jetsRat_chi`, `idxMatNF_of_isTw`, `thEquivP_ambOf_tiesD` (both copies), `thEquivP_ofD`, `thEquivP_stepT_ofD`, `jetMap_pullD`, `theta_coset_indicator_natural`, `thIndEq_of_vacEq`, `thCEq_of_ind`, `ana`, `scal_theta`, `th_move`, `ent_smul`, `opOf_equiv`, `kernel_keeps_ramT` file, `th_dia`, `rho_dia`, `sharp_mem_range`, `kmap_mem_valC`, `reduction_of`, `e3a`, `e3b`, `J1at_of_ne`, `gaussRow_of`, `eqLaw_ambOf`, `chiLaw_ambOf`, `stepC_ok_deg`, `thDistC_ok_deg`, `jetAddDeg_of`, `kernel_identity_tuple`, `reads_datum_eq_thC`, the definitions in `ThDistC.lean`, `ColumnData.lean`, `LateralTheory.lean`, `LocalNewformFunction.lean` (Weil datum, theta-at). Read at the statement: `UnitaryConstant`, `TripleFormula`, `GaussEighth`, `DetCayley`, `mu_one_of_split`, `muOneL_of`, `sqSplit_of`, `hermitian_form_integral_values`, `muProdLaw_of`/`md_prod` (top), the five leaves of E1a, `movedDatum_eq_finiteDatum_representativePair`, `tw_resid_datum`, `chr_moves_eq_rho_base`.
