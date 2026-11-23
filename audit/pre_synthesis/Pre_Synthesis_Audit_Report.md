# Pre-synthesis audit report

22 November 2026, run from 17:47 to about 18:15 UTC. Written by Claude for Jimmie Adriazola. Nothing in `src/lean` was built or run, no proof body was opened except to decide liveness, and no existing file was edited. Outputs are the five files of this folder; a copy of Zhang's v2 is in `sources/`.

## Executive verdict

**A. Are PC-1 through PC-5 internally closed at the human-proof boundary?**
PC-1, PC-2, PC-3 and PC-5 are, modulo named external theorems. PC-4 is not. Its report's verdict is RESIDUAL CHILD REMAINS. At the human level PC-4 reduces to one existence claim, PC4.13 (tuple data for every member, `Fam.colSide_alt`), which the archive proves conditionally on family hypotheses (`AllFamilyConditions`, `a.Is`, `a.True`) that PC-4 assigns to the record construction. Its class-data producers (R4-E, feeding `KerX`, `PerX`, `RdX`) have no human-level proposition yet. PC-2 is closed with one caveat. It uses the hypothesis `GeomPF` supplied by `global_model_power_free`, which no package owns (C below). PC-5's closure needs `Large` families from PC-6, which Wave 6 supplies.

**B. What remains conditional on PC-6?**
From Wave 6 (16:12 UTC, latest), the groups F1 to F5 of `FUN` below the live `fun0Fit_of_leaves_alt` (earliest `square_top_term_joined_estimates`), the ten `Open0` entries and `ON`, the live nonvacuity producers, and small leaves (R7, R8 route choices, SL-1 to SL-4). From Wave 6's FR-10 scope, `allSixLaws` below `exists_lift_marked` and seven `series_bound` producers. Not in Wave 6 at all, but in PC-6's scope, are the record cores (`stepW_core` and six others) and the PC4.13 hand-off. Closed in Wave 6 are `JoinOut` (modulo Siegel–Klingen, Deligne–Ribet, Hecke, Shimura CM), the record constants, and the FR-12 gap supply.

**C. Are there live orphan dependencies outside PC-1 through PC-6?**
Yes, two.
1. `GlobalTheory.T.global_model_power_free` (principality of the polarization on the abelian part of every semi-abelian fibre). Path: → `hodge_cpt_global_nefness` → `m2_of_good_tower` → tower axioms → `DeepStR` → `L3` → `LinkDIV` → (A3), (A4) → R6 → `riemannHypothesis`.
2. The discharge of the PC4.13 hypotheses. PC-4 hands it to PC-6, and PC-6's register does not contain it. Path: → `T.true_geometry_*` → `Fam.colSide_alt` → `valX` → `MIstar2` → `BesselId` → `LinkDIV` → R6 → `riemannHypothesis`.

Also, PC-7 is not named in the claim and is covered only through Agent 6's assignment, three interface checks have no owner, and the 54 `Fact` instances (V16) are untraced. The claim "if PC-1 to PC-6 close, every internal dependency is closed" is therefore false as stated. `Orphan_Dependency_Audit.md` §6 gives the corrected claim.

**D. Which external theorem matches are fully verified versus still pending?**
None is VERIFIED. Fifteen are PARTIAL. Among them, Fargues's Hodge–Tate theorem is located (Ch. II §1, Thm 1.1), but the article assumes $p\neq2$ while the archive's statement covers $p=2$, and clause (ii) needs a short saturation argument. The Tamagawa input has its discriminant exponent checked, and the unramified hypothesis kills Prasad's outer-form factor, but `locFactor` is unopened. Strong approximation is live in PC-2 and PC-4, and its set $S$ must contain an isotropic place. Zhang's inequality is used in a nef case, while Zhang states it for ample bundles. Nine sources are WRONG SOURCE or off the live route: Katz–Oda, Goldring–Koskivirta, and Faltings–Chai/Lan for Lemma 8.7 (PC-2), Schmidt 1968 and Siegel 1945 (PC-5), Katz 1978 (`JoinOut`), the V17 group, and the old "not an input" label on Raynaud. Everything else is SOURCE NOT YET LOCATED.

**E. Does the comparison with Robin and Siniša reveal any disagreement that changes the proof route?**
No. All three agree on the frame, the inert-prime mechanism, the theta chain, the slope and covolume architecture and the role of the Sha bounds. Four actionable differences are interface or source items. (1) Siniša's (COV) holds at "compatibly ruled points", and our Prop. 2.F holds at `RowsTAlt` points. (2) His factor $2/[K_S:\mathbb Q]$ is unreconciled. (3) The archive constructs its Galois representations itself (Siniša §10), while Robin and we cite the literature, so the fidelity of the clauses `pur`, `aut` is mandatory. (4) A printing difference in his Prop. 8.5. All three texts stop at the same point, the simultaneous selection of auxiliary data (our PC4.13, Siniša's Props 6.18, 6.20, Robin's Prop. 6.3).

**F. If PC-6 closes, is the project ready for final synthesis and manuscript reconciliation?**
Not yet. Six items must be closed or owned first, all small or interface-sized. (i) Give `global_model_power_free` an owner. (ii) Close the PC4.13 hand-off and state R4-E as a proposition. (iii) Report the record cores. (iv) Close PC-7's R5 and R6. (v) Settle the undecided route choices and make the interface checks IF-1 and IF-2. (vi) Reconcile the two manuscript copies (§0 of the patch list). With these done, the synthesis can state "reconstruction complete modulo named external theorems, source fidelity pending", and the 64 patch items of `Stale_Claims_Patch_List.md` can be applied in one pass. The literature-fidelity campaign of Part A is separate and is not a precondition for the synthesis, but no source may be called verified until it is done.

---

## 1. The five kinds of open item, kept apart

| Kind | Examples from this audit | Owner |
|---|---|---|
| 1. Mathematical residual (a proposition with no human proof) | `global_model_power_free`; PC4.13 and its family hypotheses; R4-E as unstated; PC-6 R1, R3, R4 and the record cores; PC-7 R5, R6 | PC-6, PC-4, unowned |
| 2. Formal implementation depth (human proposition stated, Lean body unread) | PC-1 C1–C7; PC-2 F2-A to F2-F; PC-3 about 4,000 lines at skeleton level; PC-4 R4-A to R4-C; PC-5 about 150,000 lines | not a residual by the standard of this audit |
| 3. Source-fidelity check | all of `External_Theorem_Fidelity.md`; priority Fargues at $p=2$, Tamagawa normalization, strong approximation $S$, Zhang nef case, Siegel–Weil V5, V6 | literature campaign |
| 4. Normalization or interface check | IF-1 ruled points; IF-2 the factor $2/[K_S:\mathbb Q]$; `dlogLinear` and `muTate` against Fargues; `locFactor` against Prasad; V16 `Fact` terms | synthesis |
| 5. Dead route | `hostEx_of_zeroFreeRegion` and V17; `fun0Fit_of_leaves`; `Inh.not_evG_false`, `exists_chGoodW`; `denominators_transport_reflection`; `all_parts_transfer_*`; `levelCompare_statement`, `passageLat_of`; Katz–Oda; Schmidt and Siegel mean values | drop from public files |

## 2. Package table at the human-proof boundary

| Package | Report verdict | Human-level status | Residual of kind 1 | Interface dependencies |
|---|---|---|---|---|
| PC-1 local Hodge–Tate | CLOSED MOD. EXT. (Wave 1) | closed | none | feeds PC-2 clause 2.A(ii) |
| PC-2 tower, covolume | CLOSED MOD. EXT. (Wave 2 final §) | closed | none inside; uses `global_model_power_free` (orphan) | IF-1, IF-2 with PC-6 |
| PC-3 Wach layer | CLOSED MOD. EXT. (Wave 3, 7th pass) | closed | none | none |
| PC-4 seesaw | RESIDUAL CHILD REMAINS (Wave 4) | not closed | PC4.13 (conditional existence), R4-E unstated | family hypotheses to PC-6 (not accepted) |
| PC-5 lattice counting | CLOSED MOD. EXT. (Wave 5) | closed | none | `Large` from PC-6 (supplied) |
| PC-6 records | RESIDUAL CHILD REMAINS (Wave 6) | not closed | R1, R3, R4, record cores | PC4.13 hand-off, IF-1 |
| PC-7 FR-10 | in Wave 6 | not closed | R5, R6 | none |

## 3. Things noticed in passing

- `Final_Six_Wave_2_Dependency_Map.md` still carries the superseded verdict "RESIDUAL: Proposition D" and the Katz–Oda description, while the `.tex` final section says CLOSED and that Katz and Oda are not needed. The synthesis should cite the `.tex`.
- `Final_Six_Wave_3` files were rewritten at 17:42 UTC, five minutes before this audit began. If an eighth pass follows, PC-3's row here should be rechecked.
- The 21 November copy of the manuscript at the project root is behind the public and Hexagon copies in five places.
- Zhang's note was first given as hexagonmath.org/2611.00809v1 and then supplied as v2 (PDF of 21 Nov 05:57 EST). v2 was used throughout, and the copy compared is kept under `sources/`.

## 4. Files

| File | Content |
|---|---|
| `External_Theorem_Fidelity.md` | Part A, statement-to-statement fidelity of every named external stopping point, with status |
| `Reconstruction_Concordance.md` | Part B, ours, Zhang (v2) and Slijepčević (v1) by mechanism |
| `Orphan_Dependency_Audit.md` | Part C, live nodes classified, orphans with paths, dead-route material, corrected claim |
| `Stale_Claims_Patch_List.md` | Part D, 64 patch items across the manuscript and the public files |
| `sources/Zhang_2611.00809v2.pdf` | the version of Zhang's note compared |
