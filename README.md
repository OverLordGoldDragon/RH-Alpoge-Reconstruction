# Human-readable reconstruction of the Alpöge/Claude RH argument

This repository contains a reconstruction, in conventional mathematical language, of the argument in the Lean archive that Levent Alpöge released on 20 November 2026 together with a four-page note ([Alpöge, *Remark*](https://alpo.ge/remark.pdf)). In that note Alpöge states his belief that he has, working with Claude, discovered a proof of the Riemann hypothesis, and that the method also gives the generalized Riemann hypothesis for Dirichlet $L$-functions.

This repository does not claim that the Riemann hypothesis is proved. It documents what the formal argument does, how far its proofs have been reconstructed in ordinary mathematics, and what still has to be checked.

## What this repository contains

- **The reconstruction manuscript**, [`RH_Route_Notes.pdf`](RH_Route_Notes.pdf) with its LaTeX source [`RH_Route_Notes.tex`](RH_Route_Notes.tex). Title: *An End-to-End Reconstruction of the Alpöge–Claude Route to the Riemann Hypothesis* (66 pages).
- **A proof-dependency map**, [`PROOF_DEPENDENCY_MAP.md`](PROOF_DEPENDENCY_MAP.md), giving the argument in mathematical order from the analytic criterion to the conclusion.
- **A reconstruction-status document**, [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md), the authoritative public statement of what is reconstructed and what remains under audit.
- **An explicit external verification boundary**, [`EXTERNAL_THEOREMS.md`](EXTERNAL_THEOREMS.md), listing the published theorems at which the reconstruction stops, with the state of their comparison against the literature.
- **A source and version manifest**, [`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md), identifying the exact formal archive that was reconstructed.
- **Selected audit documentation**, in [`audit/`](audit/), recording how the dependency structure was established.

## Attribution

The argument, its proof ideas and the formal Lean proof archive originate with **Levent Alpöge and Claude (Anthropic)**. Alpöge's note credits Alpöge with the plan of the proof and with the recognition that Siegel's auxiliary-function argument is Stepanov's argument with multiplicity one, and it credits Claude with the proposal that the chain of theta lifts should have length about $\sqrt{X}$ for a sum over primes of length $X$, and with the automorphic arguments on groups of higher rank. The note thanks in particular David Dohan, Ben Michel, Ralph Furman, Eric Price and Cora Vinther.

This repository concerns a separate piece of work, the **independent reconstruction, organization and audit** of that argument in conventional mathematical language. The manuscript is by **Jimmie Adriazola** (School of Mathematical and Statistical Sciences and Simon A. Levin Mathematical, Computational and Modeling Sciences Center, Arizona State University). As its acknowledgements state, Claude (Anthropic) read the Lean archive, drafted the proofs and ran the computations of the manuscript under the author's direction. The audit reports in [`audit/`](audit/) were prepared by Claude as working reports for the author.

Reconstruction is not discovery. Nothing in this repository should be read as a claim of authorship of the argument itself.

## Current status

In short, the mathematical architecture of the argument has been reconstructed end to end, and every major mechanism has been reconstructed in ordinary mathematics. A finite set of isolated internal proof packages remains under audit, together with a separate literature-verification boundary. No completed reconstruction pass has identified a mathematical gap, but the present manuscript should not yet be described as an independent verification of every component of the formal proof.

In more detail.

- **Architecture: reconstructed.** The route is known end to end, from the analytic criterion for zeros through the arithmetic form of Stepanov's method, the divisibility of theta lifts, the slope and covolume estimates and the automorphic and Galois inputs, to the final explicit-formula argument. The dependency order has no cycle.
- **Major mechanisms: reconstructed.** Each major mechanism of the archive has been written in ordinary mathematics (see [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md), Section 2).
- **Remaining internal packages: seven, plus small leaves.** Six medium packages and one small-to-medium package remain under audit. Each is a set of Lean theorems whose proofs exist in the archive and whose proof bodies have not yet been read down to classical statements or to named published theorems. For each one the statement, the place of use, the top of the proof and the mechanism are known. Two compatibility checks of constants are open inside these packages.
- **Literature verification: separate and not yet done.** The published theorems that the archive uses form a separate boundary. Each needs a comparison with its source in both directions, and that comparison has not been carried out.
- **Kernel replay: not yet done.** The archive has not been built and replayed in Lean's kernel as part of this work, and the axioms of its final theorem have not been printed. A textual audit of the source (no `axiom`, `sorry`, `admit`, `native_decide`, `opaque` or kernel-disabling option in any of its 175,187 files) is recorded in [`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md). A textual audit is not a kernel check.

## Files

| File | What it is |
|---|---|
| [`RH_Route_Notes.pdf`](RH_Route_Notes.pdf) | The reconstruction manuscript. Section 1.3 states the current status, Section 11 tabulates the reconstruction boundary component by component, and notes headed *Reconstruction status* mark each remaining package at its point of use. |
| [`RH_Route_Notes.tex`](RH_Route_Notes.tex) | LaTeX source of the manuscript. It is self-contained (inline bibliography, inline pgfplots coordinates, no external figures). |
| [`references.bib`](references.bib) | BibTeX transcription of the manuscript's bibliography, for reuse. The manuscript does not read it. |
| [`PROOF_DEPENDENCY_MAP.md`](PROOF_DEPENDENCY_MAP.md) | The argument in mathematical order, with the points where the remaining internal packages attach. |
| [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md) | What is reconstructed, the seven remaining internal packages and small leaves, and what this repository does not claim. |
| [`EXTERNAL_THEOREMS.md`](EXTERNAL_THEOREMS.md) | The external verification boundary, with sources and comparison status. |
| [`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md) | The exact archive reconstructed (tarball hash, toolchain, Mathlib revision, final theorem), and the versions of the manuscript and audit synthesis. |
| [`audit/`](audit/) | The current audit synthesis and a small set of reports documenting the major mechanisms and the main corrections. |
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

- **Specialists in a published area** can take rows of [`EXTERNAL_THEOREMS.md`](EXTERNAL_THEOREMS.md). The priority checks V1 to V20 are where a mismatch between the archive's form of a published theorem and the theorem in print would matter most. Useful work includes confirming or correcting a source, and checking both directions, that the archive's statement is not stronger than the published one and that the published hypotheses hold where the archive applies it. Entries marked `source match pending` most need a literature match.
- **Specialists in the mechanisms of an internal package** can take a package of [`RECONSTRUCTION_STATUS.md`](RECONSTRUCTION_STATUS.md), Section 3. For example, local integral $p$-adic Hodge theory and finite flat group schemes (PC-1), arithmetic intersection theory on Shimura varieties (PC-2), Wach modules and $(\varphi,\Gamma)$-modules (PC-3), local theta correspondence and the Weil representation (PC-4), and lattice counting and discrete series (PC-5). Each package names its earliest unread proof and its expected mechanism.
- **Analytic number theorists** can check Sections 2 and 7 to 9 of the manuscript, which are proved there from classical statements. The quoted forms (C2), (C4), (C5) and the derivation of (C7) from Gallagher's theorem have not been compared with their sources.
- **Lean users with large machines** can attempt the kernel replay described in [`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md), Section 4, and report the output of `#print axioms riemannHypothesis`.

Please report findings as GitHub issues, naming the manuscript section, the table row or package ID, and the source you compared against.
