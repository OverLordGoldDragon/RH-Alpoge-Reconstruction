# Orphan and interface pass: status table

22 November 2026. Written by Claude for Jimmie Adriazola, for the final synthesis agent. Read-only pass: no file of the project, the manuscript, the reports or the Lean archive was edited, and nothing was built or run in Lean.

Liveness was decided on a declaration index of the archive (1,066,087 declarations, 175,187 files). The index records each declaration with its namespace and active `open`s and resolves every identifier of its body through those namespaces. A forward search from `riemannHypothesis` gives a candidate live set, and every path quoted here was checked edge by edge against the calling declaration's text. Paths are in `Orphan_Interface_Pass_Dependency_Map.md`.

Status words: **Closed** (reconstructed in ordinary mathematics), **Closed mod X** (reduced to a named external theorem), **Mechanism reconstructed, leaves remain** (statement and mechanism written, internal bodies unread), **Dead**, **Undecided**.

## 1. The five targets

| item | live? | producer | first live consumer | mathematical content | owner | verdict |
|---|---|---|---|---|---|---|
| `GlobalTheory.T.global_model_power_free` | **live**, two consumers | `Rec.exists_isGlobal` from `Top.partI_holds` (hypotheses `SplitFibres`, `N3` of the local systems and domination of the global model); proof `GlobalFib.global_fibPF` | `Conj.hodge_cpt_global_nefness` (to `m2_of_good_tower`, nefness at p ∉ S_B, Prop. 2.B(ii)); `Xgn.numerical_triviality_of_good_reduction` (to `rootFlatOnHodge`, D3, Prop. 2.C) | Proposition A: every geometric fibre of residue characteristic p of the global model is an extension of an abelian variety B by a torus with L ≅ q\*M and K(M) = 0; functions on G^n are constant along the base | PC-2 | **Closed mod X**: `PartI` (toroidal integral models with Faltings–Chai/Lan degeneration data, already on the boundary as a Layer 3 statement). Internal glue (Lemmas A1 to A4) reconstructed |
| PC4.13 family-condition handoff (`AllFamilyConditions W`, `a.Is`, `a.True`) | **live** | bundle level: `Fam.truePack_of_bWit_alt` with `PtRowsAt.good_linked_ptR_of_cuspRapidDecay`, from a `BundleWitness` (`SelAll.bwit_exists_alt`); member level: `GeoExists.exists_geoAll_alt`; index level: `Fam.readsExists_alt` and the `T.true_geometry_*` producers | `Fam.colSide_alt` inside `MiTop.famAllQ_of_allTrue_alt` inside `Fam.miStar2_of_allTrue_alt_alt` | Proposition B: for every linked bundle, the family package satisfies all family conditions; every word has a true member; every index has quadratic-extension readings, with kernel, volume and row-pair data compatible with them | bundle level PC-6 (record cores); member and index level PC-4 (R4-D) | **Handoff reconstructed; no missing clause.** Quantifier order and object identity checked. Bodies remain as R4-D (PC-4) and as the PC-6 record core `bwit_exists_alt` |
| class-data producers of `KerX`, `PerX`, `RdX` (R4-E) | **live** | `AdForm.clsPinD_of_famCol_of_trueW` (= `T.cls_pin_d_of_true_family`) | `SeeSaw.kerX_of_clsPinD`, `perX_of_clsPinD`, `rdX_of_clsPinD` in `Fam.lawsLinks_of_geo_rows_cols_alt` | Proposition C: one real datum ρ for the family (frames, dominant weights, unitary representations of the compact groups) and, for each tuple t, kernel and top class data; the constants of the three laws come from ρ alone | PC-4 | **Mechanism reconstructed, leaves remain** (about 17,000 lines under six producers). Uniformity in t is structural; no hidden dependence on the tuple or the auxiliary places |
| IF-1, points of the covolume bound | **live** | `topCovolG_alt_alt` (PC-2), at points with `RowsTAlt` = `PointConditions'` ∧ `RecTied` | `Fc.Ind.eventual_L3_of_covolume_alt` in `Glob.CovolRow.linked_bundles_l3_of_open_alt` | the consumer applies `L3` exactly at the compatible summand selection, and it establishes `PointConditions'` and `RecTied` there | PC-2 (statement), PC-6 (call) | **Closed** (definitional wiring, checked in source). Settles Slijepčević's open question for this route: (COV) is needed only at compatibly ruled points |
| IF-2, normalisation of (COV) | **live** | `Formalism.DivisionValues.lcv` = (2/[K:ℚ]) log ht | `Formalism.L2.Indef.L3`: lcv(X_W(j), M_j)/D ≤ l3(j) | identical to Slijepčević's (COV) with K = K_S | PC-2 | **Closed** (definitional) |
| IF-3, R4-E without a proposition | live | as for the class data | as for the class data | Proposition C | PC-4 | **Closed as an interface** (Proposition C is now stated); the content is the R4-E row above |
| 54 `Fact` instances (V16) | 150 instances found, see `Fact_Instance_Audit.md` | terms in the instances | implicit, by typeclass resolution | thirteen groups | various, see below | **No instance introduces an unproved hypothesis.** One external theorem missing from the boundary (Bessel non-vanishing, F4c) and three internal propositions previously unowned (F5a to F5c) |

## 2. New items found by this pass

| item | live? | producer | first live consumer | content | owner | verdict |
|---|---|---|---|---|---|---|
| F4c `BesselNVG`, `BesselNVGap` | live | `DS.Lap.TopClosed.besselNVG` | `LitS.PfNVG.besselNVG` (under `ampUnif_holds`); `BesselDiscreteSeries.besselNVGap` (under `wuDecayOfGap`) | existence of Bessel models for discrete series under interlacing | boundary (new V21) | **Closed mod X** once named: local Gan–Gross–Prasad, archimedean, existence half (H. He 2017; Beuzart-Plessis 2020; from memory) |
| F5a `GaugeVolUD` | live | `Pf.GV.gaugeVolU` | `Closed.AprimeInf_holds` | gauge volume of U(k) | PC-6, new group SL-6 | **Mechanism stated, leaf unread**; normalisation consistent by arithmetic |
| F5b `RhsWLim` | live | `RankOneChart.rhsWLim` = `rhsWLim_of_leaves` with seven `T.*` leaves | `Pf.WB.rhsWLim'` (under `JacGauge_holds`) | Jacobian constant of the orbit map at gauge-lattice shifts | PC-6, SL-6 | **Mechanism stated, seven leaves unread** |
| F5c `CoefCapAll` | live | `coefCap_carrierInT_own` | `CarrierT.coefCap_carrierInT` (under `theoremS_leaves_of_carrierG`) | Capelli eigen-equation for carrier coefficients | PC-6, SL-6 | **Mechanism reconstructed** (Capelli identity and Harish-Chandra image, on the boundary); leaves `capelliH_cf_rect`, `gapped_infinitesimal_character` unread |
| `PositivityTheory.Xgn.numerical_triviality_of_good_reduction` | live | consumes `global_model_power_free` | `numTriv_offS`, then `rootFlatOnHodge` | numerical triviality mod p of Hodge lines at good primes | PC-2 (Prop. 2.C) | second consumer of Proposition A; no new content beyond A |

## 3. Undecided liveness inherited from the pre-synthesis audit (§1.1)

| node | result of this pass | owner if live |
|---|---|---|
| `GlobalTheory.GapIn.UniqGap` | **live** (via `bessel_multiplicity_one_large_gap_and_whittaker_bessel`, `rowsPos_typeP`, `hypotheses_nonempty_of_unramified_exponents_alt`) | PC-6 sweep (R8); content is Bessel uniqueness (Jiang–Sun–Zhu, boundary) |
| `CompanionTheory.Lime.BM.UniqGap` | **live** (via `realObj_inInfinityX_jsz`, `rowMainEqP_of_siegelWeil`) | as above |
| `GlobalTheory.GoodCharProd.isProdCuspChar_good` | **live** (via `goodCharacter_placewise_cuspidal_parabolic_product`, `passIn3_of_rows`, `allRows_of_open0_alt`) | PC-6 sweep (R8) |
| `PositivityTheory.AdelicQuotientData.secondCohomologyBound_of_boundaryBound` | **live** (via `rsPole`, `jacquetShalikaRigidity`, `published_results_eigen`) | external: Jacquet–Shalika rigidity, Layer 3 |
| `UpperTheory.V.Pa.secondCohomologyBound_of_boundaryBound` | **undecided**: the only candidate path runs through a local hypothesis named `key`, a false edge | PC-6 sweep (R8) |
| `GlobalTheory.Published.StrongApproxSU` | **live** (as a hypothesis of `UnitaryGroupThirdPlaceHypotheses`, and in `exists_xgeo_alt` for PC4.13) | external, on the boundary |
| `GlobalTheory.ZeroFreeHalf.main` | **live** (via `litThin`, `hypotheses_nonempty_of_unramified_exponents_alt`) | external |
| `GlobalTheory.Mem.An.zeroCount_holds` | **live** (via `explicit_formula_right`, `primesInProgressions_relativeError`, `linnik`) | external (zero counting) |
| `Formalism.ZeroFreeDirichlet.zFRDirichlet` | live through `pt_zero_free` and `psi_thin` (V18), one edge (`thinH` to `thin`) matched by name only | external (V18) |
| `HidaSetting` structures (three) | not reached by the namespace-resolved graph | none needed; PC-4 had found the fields unused |
| `ArithmeticGeometryHyps`, `PublishedTypesAtPlace`, `explicit_formula_used` | not reached by the namespace-resolved graph | external if live |
| `core2`, `third_identity`, `stepB_of`, `lift1`, `fixBd`, `pair_count`, `detFin`, `alInj` | **undecided** (names shared across namespaces, not retested) | PC-6 sweep |

"Not reached" is evidence of deadness, not proof: the graph resolves names through namespaces and `open`s, and it does not follow typeclass resolution or dot notation on local variables.
