# Human-readable reconstruction of the Alpöge/Claude RH argument

This repository contains a reconstruction, in conventional mathematical language, of the argument in the Lean archive that Levent Alpöge released on 20 November 2026 together with a four-page note ([Alpöge, *Remark*](https://alpo.ge/remark.pdf)). In that note, Alpöge states his belief that he has, working with Claude, discovered a proof of the Riemann hypothesis, and that the method also gives the generalized Riemann hypothesis for Dirichlet $L$-functions. On 21 November 2026, the Lean and Mathlib communities published a joint statement, endorsed by the Lean FRO and the Mathlib Initiative, certifying that both the statement and the proof of the Riemann hypothesis in Alpöge's Lean library are correct ([Lean community blog, *Lean verification of the Riemann Hypothesis*](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)).

The purpose of this repository is to provide a human-readable proof of the Riemann hypothesis. Given how quickly this has all developed, I cannot guarantee that everything in this repository is correct. I am actively working through it and hope that the fact that the manuscript here is currently fewer than 70 pages provides some relief as we collectively process these astonishing results. All priority of the results belongs to Levent and Claude. The architecture of the argument and all of its major mechanisms have been reconstructed, and the internal audit has since closed further proof packages modulo named published theorems. The reconstruction is not yet complete. A final audit is checking that every remaining internal dependency has an owner and a closure status, and the comparison of the named published theorems with the literature is under way but not finished. The manuscript posted here predates these latest passes (see [Current status](#current-status)). I am actively working to clean up the manuscript so that it reads more clearly. My ultimate hope is that this makes the process of human verification easier for the community.

## What this repository contains

- **The reconstruction manuscript**, [`RH_Route_Notes.pdf`](RH_Route_Notes.pdf) with its LaTeX source [`RH_Route_Notes.tex`](RH_Route_Notes.tex). Title: *An End-to-End Reconstruction of the Alpöge–Claude Route to the Riemann Hypothesis* (66 pages). This version predates the latest closure and source-fidelity passes.
- **A proof-dependency map**, [`PROOF_DEPENDENCY_MAP.md`](PROOF_DEPENDENCY_MAP.md), giving the argument in mathematical order from the analytic criterion to the conclusion.
- **A reconstruction-status document**, [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md), the public statement of what was reconstructed and what remained under audit as of 21 November 2026. The [Current status](#current-status) section below is more recent.
- **An explicit external verification boundary**, [`EXTERNAL_THEOREMS.md`](EXTERNAL_THEOREMS.md), listing the published theorems at which the reconstruction stops, with the state of their comparison against the literature as of 21 November 2026, before the source-fidelity audit began.
- **A source and version manifest**, [`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md), identifying the exact formal archive that was reconstructed.
- **Selected audit documentation**, in [`audit/`](audit/), recording how the dependency structure was established.

## Attribution

The argument, its proof ideas and the formal Lean proof archive originate with **Levent Alpöge and Claude (Anthropic)**. Alpöge's note credits Alpöge with the plan of the proof and with the recognition that Siegel's auxiliary-function argument is Stepanov's argument with multiplicity one, and it credits Claude with the proposal that the chain of theta lifts should have length about $\sqrt{X}$ for a sum over primes of length $X$, and with the automorphic arguments on groups of higher rank. The note thanks in particular David Dohan, Ben Michel, Ralph Furman, Eric Price and Cora Vinther.

This repository concerns a separate piece of work, the **independent reconstruction, organization and audit** of that argument in conventional mathematical language. The manuscript is by **Jimmie Adriazola** (School of Mathematical and Statistical Sciences and Simon A. Levin Mathematical, Computational and Modeling Sciences Center, Arizona State University). As its acknowledgements state, Claude (Anthropic) read the Lean archive, drafted the proofs and ran the computations of the manuscript under the author's direction. The audit reports in [`audit/`](audit/) were prepared by Claude as working reports for the author.

To be clear, reconstruction is not discovery, and nothing in this repository should be read as a claim of authorship of the argument itself.

## Current status

Status as of 22 November 2026.

In short, the architecture of the argument has been reconstructed end to end, and every major mechanism has been reconstructed in ordinary mathematics. The reconstruction of the internal proof packages has advanced substantially beyond the manuscript posted here, but the project has not yet made the final claim that every live internal dependency is closed. Literature verification of the named published theorems is actively under way and has produced both confirmations and corrections, but it is not complete.

The manuscript currently available here predates the latest closure and source-fidelity passes. The audit reports are ahead of the public manuscript, and those reports are not yet in this repository. A reconciled revision will be prepared after the current orphan/interface and external-source audits are complete. Until then, [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md) and [`EXTERNAL_THEOREMS.md`](EXTERNAL_THEOREMS.md) record the state of 21 November 2026, and where they differ from this section, this section is more recent.

In more detail.

- **Architecture: reconstructed.** The route is known end to end, from the analytic criterion for zeros through the arithmetic form of Stepanov's method, the divisibility of theta lifts, the slope and covolume estimates and the automorphic and Galois inputs, to the final explicit-formula argument. The dependency order has no cycle.
- **Major mechanisms: reconstructed.** Each major mechanism of the archive has been written in ordinary mathematics (see [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md), Section 2).
- **Internal packages: substantially advanced, final audit in progress.** On 21 November the audit listed seven internal packages, PC-1 to PC-7, together with small leaves, whose Lean proofs had not yet been read down to classical statements or named published theorems ([`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md), Section 3). Later passes have closed several of these packages modulo named external theorems. In particular, PC-6 (the global record construction) and PC-7 (the FR-10 remainder) have now been audited to the human-proof boundary with the verdict *closed modulo named external theorems*. Each of their last four residuals was reconstructed, reduced to a named published theorem, or transferred to another package, and no residual remains inside the PC-6/PC-7 assignment. This does not close the project. Some dependencies of PC-6 and PC-7 were transferred to other packages that had already been identified, and a final global orphan/interface audit is now checking that every remaining live internal dependency has an owner and a closure status. Until that audit is finished, this repository does not give a new count of remaining packages.
- **Literature verification: under way, not complete.** A dedicated audit now compares the archive's form of each named published theorem with the theorem in print, including hypotheses and normalizations. Its first pass took 26 high-risk inputs. Two match their published statements exactly, five match after a change of notation, and nine match after short bridge lemmas, which the audit writes out. Nine still have at least one unchecked clause, and for one no published source for the exact required statement has yet been found. The rest of the external boundary has not yet been checked statement for statement. Besides confirmations, the pass found corrections to some attributions and to one hypothesis as stated in an earlier human account, and it raised some interface questions. These findings concern the human account. The archive contains no axioms and its final theorem has no hypotheses, so each of these published statements is also proved inside the archive, and a mismatch with print cannot open a gap in the formal proof. The external boundary as a whole has not been verified.
- **Formal verification: done by the Lean and Mathlib communities.** On 21 November 2026, the Lean and Mathlib communities certified that both the statement and the proof of the Riemann hypothesis in Alpöge's Lean library are correct ([joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)). This repository did not build or replay the archive itself. A textual audit of the source (no `axiom`, `sorry`, `admit`, `native_decide`, `opaque` or kernel-disabling option in any of its 175,187 files) is recorded in [`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md).

## Files

| File | What it is |
|---|---|
| [`RH_Route_Notes.pdf`](RH_Route_Notes.pdf) | The reconstruction manuscript. Section 1.3 states the status as of 21 November 2026, Section 11 tabulates the reconstruction boundary component by component, and notes headed *Reconstruction status* mark each package at its point of use. It predates the latest closure and source-fidelity passes. |
| [`RH_Route_Notes.tex`](RH_Route_Notes.tex) | LaTeX source of the manuscript. It is self-contained (inline bibliography, inline pgfplots coordinates, no external figures). |
| [`references.bib`](references.bib) | BibTeX transcription of the manuscript's bibliography, for reuse. The manuscript does not read it. |
| [`PROOF_DEPENDENCY_MAP.md`](PROOF_DEPENDENCY_MAP.md) | The argument in mathematical order, with the points where the internal packages PC-1 to PC-7 attach. |
| [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md) | Status as of 21 November 2026: what is reconstructed, the seven internal packages and small leaves then under audit, and what this repository does not claim. Its package list predates the latest closure passes and is no longer current. |
| [`EXTERNAL_THEOREMS.md`](EXTERNAL_THEOREMS.md) | The external verification boundary, with sources and comparison status as of 21 November 2026, before the source-fidelity audit began. |
| [`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md) | The exact archive reconstructed (tarball hash, toolchain, Mathlib revision, final theorem), and the versions of the manuscript and audit synthesis. |
| [`audit/`](audit/) | The post-closure audit synthesis of 21 November 2026 and a small set of reports documenting the major mechanisms and the main corrections. The later closure and source-fidelity reports are not yet included. |
| [`CITATION.cff`](CITATION.cff) | Citation metadata. |
| [`LICENSE`](LICENSE) | Creative Commons Attribution 4.0 International (CC BY 4.0). It covers the manuscript, the documentation and the audit reports in this repository. The Lean archive is not part of this repository and is not covered. |

## Building the manuscript

```
pdflatex RH_Route_Notes.tex
pdflatex RH_Route_Notes.tex
pdflatex RH_Route_Notes.tex
```

The preamble needs a standard TeX Live installation with `newtx`, the TeX Gyre fonts, `pgfplots`, `natbib`, `fancyhdr`, `booktabs` and `longtable`. No BibTeX run is needed.

## How to help

Specific scrutiny is more useful than a request to check the whole proof. The verification boundary has been laid out so that specialists can take one piece each.

- **Specialists in a published area** can take rows of [`EXTERNAL_THEOREMS.md`](EXTERNAL_THEOREMS.md). The priority checks V1 to V20 are where a mismatch between the archive's form of a published theorem and the theorem in print would matter most. Useful work includes confirming or correcting a source, and checking both directions, that the archive's statement is not stronger than the published one and that the published hypotheses hold where the archive applies it. The comparison status in that file predates the source-fidelity audit described above, which has since matched, corrected or reclassified some rows, so a row marked `source match pending` there may already have been examined. Independent checks remain useful for every row, since that audit has not yet covered the whole boundary.
- **Specialists in the mechanisms of an internal package** can check its reconstruction. [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md), Section 3, describes the packages and their mechanisms, for example local integral $p$-adic Hodge theory and finite flat group schemes (PC-1), arithmetic intersection theory on Shimura varieties (PC-2), Wach modules and $(\varphi,\Gamma)$-modules (PC-3), local theta correspondence and the Weil representation (PC-4), and lattice counting and discrete series (PC-5). Those descriptions predate the latest closure passes, which have since closed PC-6, PC-7 and several other packages modulo named external theorems, so the earliest unread proof named there may no longer be unread. An independent reading of a reconstructed package is as useful as work on what remains, and the reconciled manuscript will mark which is which.
- **Analytic number theorists** can check Sections 2 and 7 to 9 of the manuscript, which are proved there from classical statements. The quoted forms (C2), (C4), (C5) and the derivation of (C7) from Gallagher's theorem have not been compared with their sources.
- **Lean users** who want to reproduce the formal check can follow the replay instructions in [`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md), Section 4. The Lean community's [joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) describes how the proof was checked.

Please report findings as GitHub issues, naming the manuscript section, the table row or package ID, and the source you compared against.
