# Orphan-dependency audit (Part C)

22 November 2026. Pre-synthesis audit, written by Claude for Jimmie Adriazola.

## 0. The claim tested

> "If PC-1 through PC-6 close, then every internal mathematical dependency on the live route to `RiemannHypothesis` is closed."

**Verdict: false as stated.** It becomes true if four things are added, all small or interface-sized.

1. One live proposition is owned by no package: `GlobalTheory.T.global_model_power_free` (§2.1).
2. The discharge of the hypotheses of PC4.13 (`AllFamilyConditions W`, `a.Is`, `a.True`) is handed by PC-4 to PC-6, and PC-6's register does not contain it (§2.2).
3. PC-7 (FR-10) is not named in the claim. It is covered only because Agent 6's assignment included it, and its residuals R5, R6 are open (§1, row 8.6).
4. Three interface checks have no owner (§3).

Separately, the 54 `Fact` instances (V16) have not been traced, so the absence of further orphans behind them cannot be asserted (§4).

**Method.** Package-level route from `riemannHypothesis` (term `allChi`) down, using `PROOF_DEPENDENCY_MAP.md`, `Post_Closure_Internal_Residuals.md`, the six final-wave dependency maps and the reverse-dependency liveness of Wave 6. No proof body was opened. Two Lean statements were opened to decide liveness: `GlobalModelPowerFreeStatement.lean` and the call sites of `global_model_power_free` (found in `HodgeCptGlobalNefBound.lean:17` and `NumericalTrivialityOfGoodReduction.lean:590`).

Classes: **M** reconstructed directly in `RH_Route_Notes`; **PC-n** covered by package n; **X** named external theorem; **ORPHAN**; **IF** interface check with no owner; **U** liveness undecided.

## 1. Live nodes on the route

| # | Live node (mathematics / Lean anchor) | Downstream | Class | Note |
|---|---|---|---|---|
| 1.1 | Final theorem and the deduction from the zero-free half-plane (`riemannHypothesis`, `allChi`, `everyCharacter`) | top | M | §2, §7 |
| 1.2 | Window theorem `engine`, Corollary `corA`, sampled sums | 1.1 | M; X (Landau, functional equations, (C1)–(C8)) | |
| 1.3 | Inert-prime identity, accounting `acct` (A1)–(A7), `step5`, `asm` | 1.2 | M | |
| 1.4 | Auxiliary primes (window pairs) | R5 | M; X (C1)–(C8), Gallagher (V1), Linnik, Landau–Page (V2) | |
| 1.5 | Host field `HostExW` via `supplyChi` (sizes, Artin map, Behrend) | R5, R3 | M; X (V18 `psi_thin`, quadratic reciprocity) | the live nonvacuity of records is not through `HostEx` (row 9.4) |
| 2.1 | Kernel law $\exp(-\Upsilon)U$, `BetaIsG`, `valest`, `SysTw`, `CmpV`, `LinkG`, `LinkMu` | (A2), R1, R2 | M; X (CM theory `CM2`, Honda `CM3` internal) | |
| 2.2 | `LPprime` | (A2) | M; X (V10) | |
| 3.1 | `HSAt` | covolume | M; X (V7 `HSCore.Quoted`) | |
| 3.2 | Height of the chain, `MeanPeriod` | (A4) | M; X (Chowla–Selberg) | |
| 3.3 | `DeepStR` top, descent through the cutoff, exact identity at good primes and its recursion | (A4), `L3` | M | |
| 3.4 | `FamEx.TestPt.testFacts`, `FamilyExistsPos` and parts (b)–(e) | 3.3 | PC-1 | closed modulo X; formal C1–C7 unread |
| 3.5 | Tower existence and axioms (`exists_good_tower`, D3, D4, D5), covolume `topCovolG_alt_alt`, Bergman constant | 3.3, `L3` | PC-2 | closed modulo X |
| 3.6 | Lemma 8.7 (`m2Curve_holds`) and the semi-abelian datum D (`tanpf_inj`) | 3.5 (nefness at $p\notin S_B$) | PC-2 | closed (Wave 2 §§12–13) |
| 3.7 | **`GlobalTheory.T.global_model_power_free`**: the hypothesis `GeomPF`/`FibPF` (fibre an extension of an abelian variety by a torus, $L\cong q^*M$, $K(M)$ trivial) at every centre in characteristic $p$ | 3.6 → 3.5 → 3.3 | **ORPHAN** | §2.1 |
| 3.8 | SL-1, flag and test leaves of `DeepStR` (`testRest_bound` LIVE) | 3.3 | PC-6 (Wave 6 sweep scope) | open (Wave 6 R9) |
| 4.1 | `FrameF` | (A3) | M; X (HN, Bost) | |
| 4.2 | Theorem P, radial identities, `PuNZ` | `LinkS` | M; X (Molev, Capelli) | SL-3 model-algebra leaves in PC-6 sweep scope |
| 4.3 | Pre-trace formula and regions of `LinkS`, `LinkIRR` | `LinkS`, `LinkIRR` | M | |
| 4.4 | FR-12 lattice counting and the counting engine | 4.3 | PC-5 | closed modulo X; needs `Large` families (row 9.2) |
| 5.1 | `valX`, $c_V$, PC4.1–PC4.12, PC4.14 | `MIstar2` | PC-4 | split-place spine reconstructed; R4-A, R4-B, R4-C implementation depth |
| 5.2 | PC4.13, existence of tuple data (`Fam.colSide_alt`, the `T.true_geometry_*` producers, R4-D) | 5.1 | PC-4 | the existence statement is conditional on 5.3 |
| 5.3 | **Discharge of `AllFamilyConditions W`, `a.Is`, `a.True`** in the family construction | 5.2 | **ORPHAN (interface)** | §2.2 |
| 5.4 | R4-E: class data `AdForm.clsPinD_of_famCol_of_trueW` (6,227 theorems), unit, Weil, bottom and anchor producers | `KerX`, `PerX`, `RdX` → `MIstar2`; also `miStarRow_alt_alt` of `Open0` (Wave 6 §3) | PC-4 (scope) | **not stated as a human-level proposition** in the PC-4 package, which covers only the chain to `valX`. If PC-4 is closed through PC4.13 alone, R4-E is dropped silently |
| 5.5 | `BesselId`, `LinkDIV` | (A3), (A4), R2 | M | |
| 6.1 | `VWin`: `P3core`, `GdEndAlt`, `x1`, `red`, `V0ok`, rank four | R4 | M; X (V3, V4 Kato, V15 Thorne, Greenberg–Wiles, Bellaïche–Chenevier, Hida) | |
| 6.2 | SL-2 rank-four leaves, SL-4 FR-01/02, FR-18, FR-19 leaves (`admissible_entries_small_chain`, `datum_exists_coprime` LIVE) | 6.1 | PC-6 (Wave 6 sweep scope) | open (Wave 6 R9) |
| 6.3 | `LinkN` top: torsion bound, `coreWA`, Wach realization | R4 | M; X (Tate, Sen, Fontaine, Wach, Berger, Bloch–Kato) | |
| 6.4 | Theorems B and C, shared Wach layer | 6.3 | PC-3 | closed modulo X; ~4,000 lines at skeleton level |
| 6.5 | FR-10: markings (`dual_marking` closed, `exists_lift_marked` with `allSixLaws`), seven `series_bound` producers | `SerN` → 6.3 | PC-7, **covered by PC-6 only through Agent 6's assignment** | R5, R6 open |
| 7.1 | Records: `FUN` through the live twin `fun0Fit_of_leaves_alt`, groups F1–F5 | `L3`, `LinkDIV` | PC-6 | R1 open; earliest `square_top_term_joined_estimates` |
| 7.2 | `JoinOut` (CM-period integrality) | 7.1 (F6) | PC-6 | closed modulo X |
| 7.3 | `Open0` (ten entries other than `mi`), `ON` | records | PC-6 | R3 open |
| 7.4 | Live nonvacuity producers (`hypotheses_nonempty_of_unramified_exponents_alt`, seven `compatibleSystem_*` producers, `window_lower`, `DsP_pos_and_lower`) | records | PC-6 | R4 open |
| 7.5 | Record cores (`stepW_core`, `step_start`, `stepW_builtE`, `exBL_isLinked_prmR`, `level_three_to_four`, `exists_thetaData_trueRowsColumns_allCompatible`, `goodE_of_builtE`) | records | PC-6 (scope of the Post-Closure listing) | **not mentioned anywhere in Wave 6**, and their liveness was not re-decided after the Wave 6 route corrections |
| 8.1 | Small leaves R7 (`psi_inj`, `hence_local`, `ip_first`, `grid_squares_index_estimate`) | 7.1 | PC-6 | open, elementary |
| 9.1 | Gap supply for FR-12 ($C_l\ge2C$, $\log\mathrm{rd}_E\le L/C_l$) | 4.4 | PC-6 | **closed** (Wave 6 §4) |
| 9.2 | `Large` families with `SizeQD` bounds | 4.4 | PC-6 | **closed** (Wave 6 §4, `Closed.large`) |
| 9.3 | `NearUnip` idempotent check | 4.4 | PC-5 | **closed** (Wave 5) |
| 9.4 | `HostEx` nonvacuity route (`hostEx_of_zeroFreeRegion`, `exists_richRec_…`, `exists_coreTies_…`) | none | dead | §5 |

### 1.1 Undecided liveness

| Node | Owner if live | Status |
|---|---|---|
| `UniqGap` (two declarations), `secondCohomologyBound_of_boundaryBound` (two), `isProdCuspChar_good` | PC-6 sweep (R8) | **U** (reverse closures exceeded 30,000) |
| `core2`, `third_identity`, `stepB_of`, `lift1`, `fixBd`, `pair_count`, `detFin`, `alInj` | PC-6 sweep | **U** (names shared across namespaces) |
| Bundles `ArithmeticGeometryHyps`, `PublishedTypesAtPlace`; consumers `explicit_formula_used`, `zeroCount_holds`, `zFRDirichlet`, `ZeroFreeHalf.main`, `HostZeroFree.m` | X if live | **U** |
| Producer of the `HidaSetting` record (fields `nuQ_weil`, `wfr_on`) | none named | **U**; PC-4 found the fields unused in its closure and left the producer "a question for the synthesis" |
| `StrongApproxSU` in parents of FR-12 | X | live as an external input elsewhere (PC-2, PC-4 W12); its FR-12 consumer was not traced by PC-5 |

## 2. Orphans

### 2.1 `GlobalTheory.T.global_model_power_free`

- **Statement** (`Development/AutomorphicSpectrum/Proofs/GeometryProofs/GlobalModelPowerFreeStatement.lean`). For a CM host, a global model `Ygl` of the moduli at a level good at every prime that dominates the local systems with split fibres and `N3`, the power functions `PowFns` hold and, at every point $z$ of characteristic $p$, `FibPF Ygl.t z`. `FibPF` is `GeomPF` at the centre: the fibre is an extension $0\to T\to G_x\to B\to0$ of an abelian variety by a torus with $L\cong q^*M$ and $K(M)$ trivial. The proof is a redirect to `GlobalTheory.CompanionTheory.Ar.GlobalFib.global_fibPF` (unread).
- **Mathematics.** Principality of the polarization on the abelian part of every semi-abelian fibre of the global model. The expected mechanism is Mumford–Faltings–Chai degeneration data for a principally polarized family, but no report states it.
- **Why orphan.** PC-2's final report uses it as the supply of `GeomPF` in the semi-abelian proof of §13 and says "That supply is outside this reopening". No other package or the Post-Closure list contains it.
- **Path to RH.** `global_model_power_free` → `Conj.hodge_cpt_global_nefness` (`HodgeCptGlobalNefBound.lean:17`) → `m2Model_of_m2Curve` → `m2_of_good_tower` (nefness at $p\notin S_B$, Prop. 2.B(ii)) → tower axioms of `exists_good_tower` → `DeepStR` → `HeightAt` → `UAt` → `lowAt_of_cover` → `L3` → `LinkDIV` → (A3), (A4) → `acct` → R6 → `corA` → `riemannHypothesis`. A second call site is `NumericalTrivialityOfGoodReduction.lean:590`.
- **Size.** Small to medium by the shape of the statement.

### 2.2 The PC-4/PC-6 interface: discharge of PC4.13

- **Statement.** PC4.13 (existence of quadratic-extension readings at twist places, kernel Weil data, volume constants, level law and row-pair constants for every member) is proved by the archive conditionally on `AllFamilyConditions W`, `a.Is` and `a.True`.
- **Hand-off.** PC-4: "Its hypotheses ... are discharged in the family construction, which is shared with PC-6, so the final discharge of PC4.13 belongs to the same campaign as the record construction."
- **Why orphan.** PC-6's report (Wave 6, 16:12 UTC, the latest PC-6 status) does not mention `AllFamilyConditions`, `a.Is`, `a.True`, PC4.13 or the `T.true_geometry_*` producers. Nobody owns the producers of these three hypotheses.
- **Path to RH.** producers of `AllFamilyConditions` → `T.true_geometry_*` → `Fam.colSide_alt` → `QLaw`, `valX` → $c_V$ → `KerX`, `PerX`, `RdX` → `MIstar2` → `BesselId` → `LinkDIV`, `FrameF` → (A3), (A4) → R6 → `riemannHypothesis`.
- **Cross-check.** All three readings stop here (Concordance D2).

## 3. Interface checks with no owner

| # | Check | Raised by | Why it matters |
|---|---|---|---|
| IF-1 | Which points the tied-family construction needs: Slijepčević's "compatibly ruled points" for (COV) and the compatible-point conditions for (FUN), against the `RowsTAlt` points of our Proposition 2.F | PC-2 §11 ("wiring question for PC-6 / synthesis") | the covolume bound must hold where it is used |
| IF-2 | Slijepčević's factor $2/[K_S:\mathbb Q]$ in (COV) against the archive's `lcv`$/D$ | PC-2 §11 | normalization of the main term of `L3` |
| IF-3 | R4-E has no human-level proposition (row 5.4) | this audit | `KerX`, `PerX`, `RdX` and the `mi` entry of `Open0` depend on it |

## 4. What this audit cannot exclude

- **V16, the 54 `Fact` instances.** The top theorem has no instance binders, so each instance is discharged by a term, but the terms on the route have not been located. A term that is a bespoke internal theorem would be an orphan that no dependency map shows.
- **Formal implementation depth.** Each "closed" PC verdict is at the human-proof boundary. The unread formal layers (PC-1 C1–C7, PC-2 F2-A to F2-F, PC-3 skeleton bodies, PC-4 R4-A to R4-C, PC-5 about 150,000 lines) are not orphans by the standard of this audit, because each has a stated proposition and mechanism. They are listed so that nobody reads "closed" as "formally re-verified".

## 5. Dead-route material that older reports treated as live

| Item | Older claim | Current status (source) |
|---|---|---|
| `hostEx_of_zeroFreeRegion` and V17 (nine analytic inputs) | Post-Closure PC-6: "Call-site check of `HostEx` done: live through `hostEx_of_zeroFreeRegion` → `exists_richRec_of_zeroFreeRegion` → `exists_coreTies_of_zeroFreeRegion`"; boundary V17 "operative inputs" | off route; reverse closure of four declarations (Wave 6 §0) |
| `fun0Fit_of_leaves` (`Divisors/TwistedPlaceChoiceLiesOverPair.lean:345`) | named as the `FUN` blocker by Post-Closure, the manuscript and `RECONSTRUCTION_STATUS.md` | off route; the live twin is `fun0Fit_of_leaves_alt` (`TPS/LeafInfinitePlaceBound.lean:83`) with the same sixteen predicates |
| `Inh.not_evG_false` cluster, `exists_chGoodW` | Post-Closure PC-6 "nonvacuity leaves (route live)" | off route (Wave 6 §0) |
| `denominators_transport_reflection` | producer of `JoinOut` | off route; the live producer is `joinOut_of_five` |
| `all_parts_transfer_of_facts`, `all_parts_transfer_holds`, `levelAmb_transfer` | SL-5 bookkeeping | off route |
| `levelCompare_statement`, `passageLat_of` | SL-5 bookkeeping | off route |
| `nuQ_weil`, `wfr_on`, `SBes.cpt`, `inHH_closed` | PC-4 R-5 record fields | unused in the PC-4 closure or off route (Wave 4) |
| Katz–Oda $H^1_{\mathrm{dR}}$ datum for Lemma 8.7 | PC-2 second and third revisions | not used (Wave 2 §13) |
| Schmidt 1968, Siegel 1945 mean value | boundary for FR-12(a) | not used (Wave 5) |
| "Eleven of them apply one published theorem each (`Open0`)" | manuscript §4.7 | the entries are internal packages (Wave 6 §3, "Correction") |

## 6. Corrected claim

> If PC-1 to PC-6 close, PC-7 closes, the hypotheses of PC4.13 and the record cores are owned and closed inside PC-6, `global_model_power_free` is reconstructed, R4-E is stated as a proposition inside PC-4, the interface checks IF-1 and IF-2 are made, and the undecided route choices of §1.1 are settled, then every internal mathematical dependency on the live route to `RiemannHypothesis` that appears in the dependency maps is closed modulo named external theorems. The `Fact` instances (V16) must be traced before the word "every" is justified.
