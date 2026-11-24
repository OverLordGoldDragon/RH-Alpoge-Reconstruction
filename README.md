# Human-readable reconstruction of the Alpöge/Claude RH argument

The purpose of this repository is to provide a human-readable proof of the Riemann hypothesis. Given how quickly this has all developed, I cannot guarantee that everything in this repository is correct. All priority of the results belongs to Levent and Claude. The current manuscript states precisely each internal step that still lacks a conventional proof and each published input whose exact form still needs verification (see [Current status](#current-status)). I am actively working to complete those proofs and to compress the manuscript so that it reads more clearly. My ultimate hope is that this makes the process of human verification easier for the community.

This repository contains a reconstruction, in conventional mathematical language, of the argument in the Lean archive that Levent Alpöge released on 20 November 2026 together with a four-page note ([Alpöge, *Remark*](https://alpo.ge/remark.pdf)). In that note, Alpöge states his belief that he has, working with Claude, discovered a proof of the Riemann hypothesis, and that the method also gives the generalized Riemann hypothesis for Dirichlet $L$-functions. On 21 November 2026, the Lean and Mathlib communities published a joint statement, endorsed by the Lean FRO and the Mathlib Initiative, certifying that both the statement and the proof of the Riemann hypothesis in Alpöge's Lean library are correct ([Lean community blog, *Lean verification of the Riemann Hypothesis*](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)).

**[Read the manuscript](manuscript/main.pdf)** · 268 pages · revised 24 November 2026. The conventional proof remains conditional. Section 19 begins on page 262.

## Current status

**24 November 2026.** The revision gives the finite-group arguments for the level idempotents in Section 14, distinguishes finiteness from the effective cohomology bound in Section 17, and derives the window needed in Section 18 from the stated Selmer hypothesis.

The current Kimi wave concerns six open assertions in Section 19.1.

| | Assertion under investigation |
| --- | --- |
| N1 | Establish unitary base change with one choice of constituents satisfying the local conditions at every place. |
| N2 | Construct the classical automorphic point and its Galois representation on each required isotypic component, using N1. |
| C1 | Prove the compactly supported Siegel mean with the required measures and deduce the volume and flag bounds. |
| C2 | Prove the discrete-series decay estimates and deduce the far-orbit and deep-kernel bounds. |
| C3 | Bound the near orbits by filtration and combine the estimates with C1 and C2. |
| K1 | Bound the order of the second Galois cohomology group uniformly in the twist, field degree and discriminant. |

Section 19.2 records the other hypotheses still used in the manuscript. I will continue tracing these steps through the archive and checking the published inputs until the argument can be read and verified in full.

## What this repository contains

- **The current manuscript**, [`manuscript/main.pdf`](manuscript/main.pdf) with its LaTeX source in [`manuscript/`](manuscript/). Title: *The Alpöge Proof of the Riemann Hypothesis* (268 pages, 24 November 2026). It is a working document. Section 19 lists the internal statements whose conventional proofs it does not yet give, their dependencies, and the source-verification status of the published theorems it cites.
- **The earlier manuscript**, [`RH_Route_Notes.pdf`](RH_Route_Notes.pdf) with its LaTeX source [`RH_Route_Notes.tex`](RH_Route_Notes.tex). Title: *An End-to-End Reconstruction of the Alpöge–Claude Route to the Riemann Hypothesis* (66 pages, 21 November 2026). It predates the final internal audit and is kept as a historical record.
- **A proof-dependency map**, [`PROOF_DEPENDENCY_MAP.md`](PROOF_DEPENDENCY_MAP.md), giving the argument in mathematical order from the analytic criterion to the conclusion.
- **The dated status reports**, [`STATUS.md`](STATUS.md), with the note of 23 November 2026 on what the audit verdict means, followed by the result of the final internal audit of 22 November 2026, the size of the live dependency graph, the closed blocks and the outstanding external work.
- **A reconstruction-status document**, [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md), the public statement of what was reconstructed and what remained under audit as of 21 November 2026. It is kept as a historical record, and [`STATUS.md`](STATUS.md) supersedes it.
- **An explicit external verification boundary**, [`EXTERNAL_THEOREMS.md`](EXTERNAL_THEOREMS.md), listing the published theorems at which the reconstruction stops, with the state of their comparison against the literature as of 21 November 2026, before the source-fidelity audit began.
- **A source and version manifest**, [`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md), identifying the exact formal archive that was reconstructed.
- **The final internal certification** of 22 November 2026, in [`audit/final_certification/`](audit/final_certification/): the report, the live-graph summary, the residual tables, the full ownership table and the scripts.
- **The reports the certification rests on**, in [`audit/closure_reports/`](audit/closure_reports/) and [`audit/pre_synthesis/`](audit/pre_synthesis/), each with its status file, dependency map and scripts.
- **Selected audit documentation** from 21 November 2026, in [`audit/`](audit/), recording how the dependency structure was established.

## Attribution

The argument, its proof ideas and the formal Lean proof archive originate with **Levent Alpöge and Claude (Anthropic)**. Alpöge's note credits Alpöge with the plan of the proof and with the recognition that Siegel's auxiliary-function argument is Stepanov's argument with multiplicity one, and it credits Claude with the proposal that the chain of theta lifts should have length about $\sqrt{X}$ for a sum over primes of length $X$, and with the automorphic arguments on groups of higher rank. The note thanks in particular David Dohan, Ben Michel, Ralph Furman, Eric Price and Cora Vinther.

This repository concerns a separate piece of work, the **independent reconstruction, organization and audit** of that argument in conventional mathematical language. The manuscript is by **Jimmie Adriazola** (School of Mathematical and Statistical Sciences and Simon A. Levin Mathematical, Computational and Modeling Sciences Center, Arizona State University). As its acknowledgements state, Claude (Anthropic) read the Lean archive, drafted the proofs and ran the computations of the manuscript under the author's direction. The audit reports in [`audit/`](audit/) were prepared by Claude as working reports for the author.

To be clear, reconstruction is not discovery, and nothing in this repository should be read as a claim of authorship of the argument itself.

## Method

The reconstruction works by semantic proof compression with adaptive residual refinement.

1. Identify the formal root theorem, the Lean declaration that proves `riemannHypothesis`.
2. Compute the live dependency graph of that declaration.
3. Partition the graph into mathematical packages.
4. Reconstruct each package as ordinary mathematical propositions, down to classical statements or named published theorems.
5. Keep a residual frontier of the dependencies not yet reconstructed.
6. Refine recursively the dependencies that remain unresolved.
7. Cross-audit dependencies that are shared between packages or lie upstream of several of them.
8. Finish with a global pass that gives an owner and a status to every live declaration.
9. Require the final internal residual set to be empty.

The raw theorem count is not the number of independent mathematical ideas, since one mechanism is usually spread across many Lean theorems. For example, the E-block contained 631 distinct Lean theorems, and they collapsed to eight human propositions.

## Files

| File | What it is |
|---|---|
| [`manuscript/main.pdf`](manuscript/main.pdf) | The current manuscript, 24 November 2026, 268 pages. A working document. Section 19 is the dependency frontier, and every unproved internal step is stated as a numbered hypothesis at its point of use. |
| [`manuscript/`](manuscript/) | LaTeX source of the current manuscript (`main.tex`, `abstract.tex`, the section files `sec*.tex` and `references.bib`). |
| [`RH_Route_Notes.pdf`](RH_Route_Notes.pdf) | The earlier manuscript of 21 November 2026, 66 pages, kept as a historical record. Section 1.3 states the status as of 21 November 2026, Section 11 tabulates the reconstruction boundary component by component, and notes headed *Reconstruction status* mark each package at its point of use. It predates the final internal audit. |
| [`RH_Route_Notes.tex`](RH_Route_Notes.tex) | LaTeX source of the earlier manuscript. It is self-contained (inline bibliography, inline pgfplots coordinates, no external figures). |
| [`references.bib`](references.bib) | BibTeX transcription of the earlier manuscript's bibliography, for reuse. The earlier manuscript does not read it. |
| [`PROOF_DEPENDENCY_MAP.md`](PROOF_DEPENDENCY_MAP.md) | The argument in mathematical order, with the points where the internal packages PC-1 to PC-7 attach. |
| [`STATUS.md`](STATUS.md) | Current status. The note of 23 November 2026 on what the audit verdict means, followed by the status of 22 November 2026: the internal residual verdict, the size of the live graph, the closed blocks, the remaining external-fidelity work, and the difference between reconstruction, formal certification and independent human verification. |
| [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md) | Status as of 21 November 2026: what is reconstructed, the seven internal packages and small leaves then under audit, and what this repository does not claim. Historical record. Its package list predates the final audit and is superseded by [`STATUS.md`](STATUS.md). |
| [`EXTERNAL_THEOREMS.md`](EXTERNAL_THEOREMS.md) | The external verification boundary, with sources and comparison status as of 21 November 2026, before the source-fidelity audit began. |
| [`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md) | The exact archive reconstructed (tarball hash, toolchain, Mathlib revision, final theorem), and the versions of the manuscript and audit synthesis. |
| [`audit/`](audit/) | The final internal certification of 22 November 2026 (`final_certification/`), every closure report it cites (`closure_reports/`), the pre-synthesis, orphan/interface and source-fidelity audits with the R-1 and R-2 reports (`pre_synthesis/`), and the post-closure synthesis and selected reports of 21 November 2026. [`audit/README.md`](audit/README.md) is the index. |
| [`CITATION.cff`](CITATION.cff) | Citation metadata. |
| [`LICENSE`](LICENSE) | Creative Commons Attribution 4.0 International (CC BY 4.0). It covers the manuscript, the documentation and the audit reports in this repository. The Lean archive is not part of this repository and is not covered. |

## Building the manuscripts

The current manuscript is in [`manuscript/`](manuscript/).

```
cd manuscript
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

It needs a standard TeX Live installation with `mathpazo`, `natbib`, `fancyhdr`, `booktabs`, `longtable` and the `wncyr` fonts.

The earlier manuscript builds from the repository root.

```
pdflatex RH_Route_Notes.tex
pdflatex RH_Route_Notes.tex
pdflatex RH_Route_Notes.tex
```

Its preamble needs `newtx`, the TeX Gyre fonts, `pgfplots`, `natbib`, `fancyhdr`, `booktabs` and `longtable`. No BibTeX run is needed.

## How to help

Specific scrutiny is more useful than a request to check the whole proof. The verification boundary has been laid out so that specialists can take one piece each.

- **Specialists in automorphic forms, arithmetic geometry and Galois representations** can take one internal statement of Section 19 of [`manuscript/main.pdf`](manuscript/main.pdf). Section 19.1 gives the six current questions, and Section 19.2 identifies further hypotheses at their places of use. The automorphy statement for residually reducible representations behind the Tate–Shafarevich bound (Section 17) is the step most in need of expert scrutiny.
- **Specialists in a published area** can take rows of [`EXTERNAL_THEOREMS.md`](EXTERNAL_THEOREMS.md). The priority checks V1 to V20 are where a mismatch between the archive's form of a published theorem and the theorem in print would matter most. Useful work includes confirming or correcting a source, and checking both directions, that the archive's statement is not stronger than the published one and that the published hypotheses hold where the archive applies it. The comparison status in that file predates the source-fidelity audit described above, which has since matched, corrected or reclassified some rows, so a row marked `source match pending` there may already have been examined. Independent checks remain useful for every row, since that audit has not yet covered the whole boundary. The largest region not yet checked against its sources is the Galois-representation input from `Row0b` to `galoisLocalGlobalStrong_recParameter` (Harris–Taylor, Shin, Chenevier–Harris, Caraiani).
- **Specialists in the mechanisms of an internal package** can check its reconstruction. [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md), Section 3, describes the packages and their mechanisms, for example local integral $p$-adic Hodge theory and finite flat group schemes (PC-1), arithmetic intersection theory on Shimura varieties (PC-2), Wach modules and $(\varphi,\Gamma)$-modules (PC-3), local theta correspondence and the Weil representation (PC-4), and lattice counting and discrete series (PC-5). Those descriptions predate the final audit. Section 19 of the current manuscript states which internal statements still lack a conventional proof.
- **Analytic number theorists** can check Part I (Sections 2 to 6) of the current manuscript, and Sections 2 and 7 to 9 of the earlier manuscript, which are proved there from classical statements. Section 5 now gives the deduction of (C7) from Gallagher’s theorem and the exceptional-zero bound (C8).
- **Lean users** who want to reproduce the formal check can follow the replay instructions in [`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md), Section 4. The Lean community's [joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) describes how the proof was checked.

Please report findings as GitHub issues, naming the manuscript section, the table row or package ID, and the source you compared against.

## Earlier announcements

> **Status, 23 November 2026, evening. A brief update on the Alpöge RH reconstruction.**
>
> This morning I posted a manuscript and repository status reflecting the result of a global dependency audit: every live internal dependency in the Lean route had been assigned either to a reconstructed mathematical mechanism or to an explicit external boundary. I want to clarify that this was a statement about coverage of the formal route, not a claim that every internal theorem had already been written out as a complete conventional proof.
>
> A referee pass this afternoon pushed the human-proof audit further and found that the list of open statements in the current manuscript is incomplete. The largest newly exposed piece is a $\mathrm{GSp}_4$ argument that had been absorbed into the non-generic cases. The referee also isolated several points that need specialist attention, including `RegDet`, a patching step that moves between different points, and the role of the internal theorem `AdjointLiftingTheorem`. No false statement was identified; the effect of the pass was to make the remaining frontier more precise.
>
> A separate reconciliation of the external boundary also found a substantial number of literature inputs that are used by the route but are not yet represented in the current external-theorem ledger, most of them foundational results in automorphic forms and representation theory. I am therefore treating the present manuscript as a reconstruction in progress rather than a finished conventional proof. The next step is to produce a complete verification map of the remaining internal and external obligations, referee that map, and then work through the resulting finite list systematically.
>
> I am leaving the earlier status material in place so that the chronology of the reconstruction and its corrections remains visible.
>
> **Status, 23 November 2026.** The reconstruction has now reached a 225-page working manuscript, [`manuscript/main.pdf`](manuscript/main.pdf). Reconciling the final dependency audit with the manuscript clarified an important distinction in the status reported here on 22 November. The audit closed the live Lean dependency graph at the level of dependency identification and mathematical packaging. Every live internal dependency had been located, assigned to a reconstructed component, or isolated behind an explicit boundary. The audit did **not** mean that every internal statement on that route had already been written out with a complete conventional proof.
>
> The current manuscript makes that boundary explicit. Its Section 19 lists the internal statements for which a conventional proof is still being reconstructed, together with the published inputs whose exact forms still need source verification. The manuscript therefore does **not yet** constitute a proof of the Riemann hypothesis independent of the Lean development.
>
> I am actively working to complete the original goal of this repository, a human-readable mathematical proof that can be checked from the paper and its cited literature without any appeal to Lean. At the same time I am working to compress the exposition. The increase from 66 pages to 225 pages came from opening the internal packages that the earlier manuscript had summarized and writing out the mathematics they contain.
>
> This is a very large argument, and the reconstruction is developing quickly. Please treat the manuscript as a working document while this process continues. Corrections and specialist scrutiny are extremely welcome.
>
> **Historical status, 22 November 2026.** The statement below gives the conclusion of the final dependency audit as it was understood at that stage. It is kept here unchanged.
>
> **Status, 22 November 2026.** The internal reconstruction phase is complete. A final dependency audit starting from the Lean theorem `riemannHypothesis` finds no unresolved internal mathematical residuals on the live proof route. The exact-edge live subgraph contains 766,788 declarations, including 622,409 theorems. Every live internal mathematical dependency has been reconstructed at the human-proof level, assigned to an already reconstructed package, or transferred to an explicit external theorem boundary. The remaining work is source-fidelity verification of those external inputs and reconciliation of the audit into the human-readable manuscript. Details are in [`STATUS.md`](STATUS.md). The certification report and its tables are in [`audit/final_certification/`](audit/final_certification/), and every report it cites is in [`audit/`](audit/).
>
> This repository does not claim an independent proof of RH by the reconstruction author. The proof being reconstructed is Alpöge's formally verified proof. The manuscript posted here predates the final audit and has not yet been reconciled with it.

### Manuscript status recorded on 23 November 2026

Status as of 23 November 2026. [`STATUS.md`](STATUS.md) gives the details.

The manuscript [`manuscript/main.pdf`](manuscript/main.pdf) proves the Riemann hypothesis from the published theorems it cites and from a finite list of internal statements that it states precisely and does not yet prove. Each such statement appears as a numbered hypothesis at its point of use, and Section 19 collects them with their dependencies. The open internal statements are the following.

- The residual engines of the nondegeneracy of Hecke operators that controls the loss (Section 12).
- The normalization and odd-transfer statements that make the theta lifts a chain datum (Section 11).
- The automorphic inputs for Bessel Poincaré series, namely the kernel expansion, the multiplicity formula, the main-row and loop-row estimates, and the seesaw relation in the theta tower behind the Bessel identity (Section 14).
- The covolume bound with a constant uniform in the level of deep covers, and a few norm and multiplicity statements in the height computation (Section 15).
- The bound for Tate–Shafarevich groups on windows of scales and the congruence bound at the twisted places (Section 17).
- The check that Sections 11 to 17 give the conditions on the chain used in the proof of Theorem A (Section 18).

One finding concerns the strength of these statements. The bound for Tate–Shafarevich groups on windows implies a bound in the direction of Vandiver's conjecture that is stronger than the published bounds of Soulé (1999) and of de la Torre Durán (2026). The Lean development derives it from an automorphy statement for residually reducible Galois representations that lies outside the hypotheses of the published automorphy lifting theorems for residually reducible representations. The manuscript states this step as a hypothesis and does not claim it.

No statement on the route has failed. The Lean development proves each of the statements above, and the Lean and Mathlib communities certified that development on 21 November 2026. The remaining work is to write their proofs as conventional mathematics, to finish the comparison of the cited published theorems with their sources, and to compress the exposition.

## Record of 22 November 2026

The two passages below are the purpose paragraph and the status section of this file as they stood on 22 November 2026. They are kept here unchanged.

The purpose of this repository is to provide a human-readable proof of the Riemann hypothesis. Given how quickly this has all developed, I cannot guarantee that everything in this repository is correct. I am actively working through it and hope that the fact that the manuscript here is currently fewer than 70 pages provides some relief as we collectively process these astonishing results. All priority of the results belongs to Levent and Claude. The architecture of the argument and all of its major mechanisms have been reconstructed, and a final global audit of Alpöge's formal proof has found no unresolved internal residual on the live route. The comparison of the named published theorems with the literature is under way but not finished. The manuscript posted here predates the final audit (see [Current status](#current-status)). I am actively working to clean up the manuscript so that it reads more clearly. My ultimate hope is that this makes the process of human verification easier for the community.

### Current status (22 November 2026)

Status as of 22 November 2026. [`STATUS.md`](STATUS.md) gives the details.

The internal reconstruction phase is complete. The final global audit started from the Lean declaration that proves `riemannHypothesis`, rebuilt the live dependency graph with no depth cap, and gave every live declaration an owner and a status. Its internal residual set is empty. What remains is the source-fidelity check of the external theorem boundary, the reconciliation of the audit into the manuscript, and an independent line-by-line check of the resulting human proof.

The manuscript currently available here predates the final audit and many of the closure and source-fidelity passes before it. A reconciled revision will be prepared in a separate pass. Until then, [`STATUS.md`](STATUS.md) is the current statement, and [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md) and [`EXTERNAL_THEOREMS.md`](EXTERNAL_THEOREMS.md) record the state of 21 November 2026.

In more detail.

- **Architecture: reconstructed.** The route is known end to end, from the analytic criterion for zeros through the arithmetic form of Stepanov's method, the divisibility of theta lifts, the slope and covolume estimates and the automorphic and Galois inputs, to the final explicit-formula argument. The dependency order has no cycle.
- **Major mechanisms: reconstructed.** Each major mechanism of the archive has been written in ordinary mathematics (see [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md), Section 2).
- **Internal packages: closed at the human-proof boundary.** The seven packages PC-1 to PC-7 listed on 21 November, the small leaves, and the blocks isolated by later passes (D1 to D9, E1 to E5, W1 to W3, the kernel leaves K-a to K-c, and `ramBijective_holds`) have all been closed, PC-1 to PC-7 modulo explicit external inputs where they apply. The final pass also found several under-owned upstream items and closed them. [`STATUS.md`](STATUS.md) lists the blocks.
- **Literature verification: under way, not complete.** A dedicated audit now compares the archive's form of each named published theorem with the theorem in print, including hypotheses and normalizations. Its first pass took 26 high-risk inputs. Two match their published statements exactly, five match after a change of notation, and nine match after short bridge lemmas, which the audit writes out. Nine still have at least one unchecked clause, and for one no published source for the exact required statement has yet been found. The rest of the external boundary has not yet been checked statement for statement. Besides confirmations, the pass found corrections to some attributions and to one hypothesis as stated in an earlier human account, and it raised some interface questions. These findings concern the human account. The archive contains no axioms and its final theorem has no hypotheses, so each of these published statements is also proved inside the archive, and a mismatch with print cannot open a gap in the formal proof. Two external questions raised by that audit have since been settled, the doubling form of the Siegel–Weil formula (R-1, through an explicit bridge) and the integral Hodge–Tate input at $p=2$ (R-2). The largest external region identified by the final audit, the existence and local–global compatibility of Galois representations for regular algebraic polarized cuspidal representations over CM fields (from `Row0b` to `galoisLocalGlobalStrong_recParameter`, cited in the manuscript to Harris–Taylor, Shin, Chenevier–Harris and Caraiani), has not yet had a detailed source-fidelity check. The external boundary as a whole has not been verified.
- **Formal verification: done by the Lean and Mathlib communities.** On 21 November 2026, the Lean and Mathlib communities certified that both the statement and the proof of the Riemann hypothesis in Alpöge's Lean library are correct ([joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)). This repository did not build or replay the archive itself. A textual audit of the source (no `axiom`, `sorry`, `admit`, `native_decide`, `opaque` or kernel-disabling option in any of its 175,187 files) is recorded in [`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md).
