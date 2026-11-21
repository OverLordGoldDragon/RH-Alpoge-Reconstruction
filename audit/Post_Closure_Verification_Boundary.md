# Post-closure verification boundary

21 November 2026. Companion to `Post_Closure_Synthesis.pdf` and `Post_Closure_Internal_Residuals.md`. Written by the post-closure-wave synthesis agent (Claude). It supersedes `Final_Authoritative_Synthesis/Authoritative_Verification_Boundary.md`, whose entries are all carried forward here, with the additions of the Final Closure Wave marked **(new)**.

This file lists the named published or classical theorems at which the reconstruction stops. Each still needs a fidelity check against the literature. No such check was made in this pass. Internal theorems whose proof body is unread are in `Post_Closure_Internal_Residuals.md`. The two lists are disjoint.

Four cautions.

- The attributions below are the ones the wave agents recorded. Several were written from memory or through secondary sources, and the column "Fidelity" says so where a report did.
- An item marked "proved in the archive" has an internal Lean proof of a statement of published type. Reconstruction stops at the published statement. The archive's own proof is Layer 3, a separate campaign.
- A fidelity check has two directions. The Lean statement must not be stronger than the published theorem, and the published hypotheses must hold where the archive applies it.
- Some inputs enter through `instance : Fact _` declarations (54 in the archive). The top theorem has no instance binders, so each is discharged by a term, but a `Fact` hides the input from the statement that uses it. Locating the term for each instance on the route is part of the campaign (V16).

## What changed since the authoritative boundary

| Change | Source |
|---|---|
| Added V17: the nine analytic inputs of `hostEx_of_zeroFreeRegion` with `RayField`. The nonvacuity route through `HostEx` is live, so these are operative inputs | Final Closure Wave 5, §4.6, §9 |
| Added V18: the prime number theorem for primitive characters in the form of `psi_thin`, with the constant ∫₁^∞ (ψ(u) − u) u⁻² du = −1 − γ | Wave 5, §4.2 |
| Added V19: root exchange for GL_n (Ginzburg–Rallis–Soudry, Ch. 7) and the linear-model seesaw (Kudla), candidate stopping points for PC-4 | Wave 4, §5 |
| Added V20: Raynaud's classification of F-vector space schemes with Fargues's integral Hodge–Tate sequence, a candidate stopping point for `testFacts` (PC-1). Not an input of the archive today | Wave 1, §3.6, §9.4 |
| Added classical statements used by the closure wave: quadratic reciprocity, Dirichlet character theory, Galois theory of Q(ζ_N), quadratic Gauss sums, lifting-the-exponent lemma, Legendre and Kummer formulas, Weierstrass preparation, O[[π]]^Δ = O[[π₀]], Weil's quotient measures, Weil's theta dictionary, PEL level structures, Schmidt and Siegel mean counts, projective lifting and density of lattices in completions, Mazur's Φ_l finiteness, Honda's formal groups (internal) | Waves 2 to 5 |
| Confirmed in place: V8 (Wach record, the stopping point of the relay and of half of `ArcCore`), V12 (`FarguesExact`, `ZarhinStatement`, now the stopping points of PC-1), Fontaine's full faithfulness and exactness of D (`LitFont`, `DDExact`), Bloch–Kato, local Tate duality, local Euler characteristic, Herr, `CM2` | Waves 1 to 5 |
| Clarified: `KillerLev` and `KillerKap` are internal theorems, not clauses of V8 | Wave 2, R-B5 |

## 1. Priority checks

| # | Statement | Why it is a priority | Source |
|---|---|---|---|
| V1 | (C7) = `PNTAPRelW`, primes in progressions with relative error | Derived from Gallagher (Invent. Math. 11, 1970, Theorem 7) at level max(M, e^{√log X}) plus partial summation. Gallagher's paper was not opened; the form was taken from Thorner–Zaman (arXiv:2108.10878, (3.3)–(3.4)) and arXiv:2508.16400, Lemma 7.3. Compare line by line, including the two exceptional-zero windows | Focused Wave 4, §5.3 |
| V2 | `ShortNorm`: primes p = ππ̄, π ≡ 1 (mod M) in Q(√−d), in (X, X(1+h)] | Prime ideal theorem for ray classes in the Landau–Page range (log B ≤ c√log X, exceptional zero in the main term). Used with h = 1, log B ≤ 10 (log Y)^{2/5}, needing Y^{9/10} primes. No longer conditional. Citation from memory (Hecke–Landau; Davenport ch. 20 for Q; Fogels, Lagarias–Montgomery–Odlyzko, Weiss, Thorner–Zaman) | Focused Wave 4, §5.4 |
| V3 | `GdEndAlt` against Skinner–Wiles, Thorne, Allen–Newton–Thorne; `SmallClassNumbers.Bound` against Soulé | Archive's chain gives a polynomial bound in the Vandiver range, far beyond the published one. The test against K₄(Z), K₈(Z) was not run | Report 10 §7; Wave F adv. 5 |
| V4 | Kato's theorem in the range used, with `exists_admissible_hecke_projection_nonvanishing` | The nonvanishing L-value must match Kato's hypotheses | Wave F adv. 6 |
| V5 | `SiegelWeilStd`, `EisBL` | Constant matched by Wave E with Gan–Takeda §7.1; Tamagawa number 2, probability Haar measure and holomorphy at s₀ = (m−n)/2 to confirm | Wave E §7 |
| V6 | two declarations `SiegelWeilUnitaryConvergent` | The doubling form needs its own check. `RowDiag` rests on the Fourier-coefficient form alone | Wave B §12; Focused Wave 2 §5 |
| V7 | published bundles of the covolume branch: `PublishedHodgeBundleTheorems` (28 fields), `HSCore.Quoted` (8), the eleven statements under `deepStR_of_use`, with `GrothendieckDeformation`, `SiegelToroidalIntegral`, `ToroidalForFanKS`, `SemiAbelianLieSeminegative` | Largest published bundle; several fields not unfolded. These are the inputs of `topCovolG_alt_alt` (PC-2) | Report 10 §8; Focused Wave 1 §3.1; Final Closure Wave 1 §8 |
| V8 | Wach and Berger clauses as stated (`p3`, `p4` with rational converse, `p5`, `p9`, `p10`, `SATcore`, `F1`, `F2`, Δ-invariant forms) | Proved in the archive from four propositions. The relay of Theorem B and half of `ArcCore` now stop here. The ring relations of `p9` (π₀(ζ_p − 1) = −p, q = ε q_A) were checked classically by Wave 2 | Wave D adv. 1; Final Closure Wave 2 §2.1, §4 |
| V9 | `LocAb` / `LocCFT`: Σ_v d′_v = [L⁺:Q] | The exponent D₀ of FR-01 cancels exactly. Rank four also rests on this exponent through `b1Ar` | Wave F adv. 1; Focused Wave 4 §4.3 |
| V10 | standard monomial theory in exact integral form; extremal projector constants | Classical in substance, constants unchecked | Report 10, FR-17 |
| V11 | `SlopeBoundSt`: μ_max(Lie) ≤ C_s log(2 + rk + max(−deg, 0)) | Proved internally from `LineOfLargeDegree.Statement` by `slopeBound_and_lemmaS_of_siegel`; printed source not matched (Bost, Graftieaux, Gaudron–Rémond). The one input of C_h of `DeepStR` not made explicit | Focused Wave 1 adv. 6; Final Closure Wave 1 §5 |
| V12 | route-level leaves of `deep_slim_use` | Resolution and principalisation in characteristic zero (Hironaka), an inverse Poincaré–Lelong formula, `HSUse`, `MoriwakiBigStatement`, `FarguesExact` (giving `FarguesHodgeTate` and the element ζ_p − 1), `ZarhinStatement`, `NefRR`. `FarguesHodgeTate` and `ZarhinStatement` are now the stopping points of PC-1 | Focused Wave 1 §3.1; Final Closure Wave 1 §9.4 |
| V13 | Rallis's constant-term formula for theta integrals in the convergent range (Rallis 1984, Kudla–Rallis), with `SiegelSetUnitary` for `WeilConv`, `KDecay` | Behind `GenBig`, `GenAniso`, `GenSmall` of the theta tower | Focused Wave 5 §3 |
| V14 | `CoefWeightedLoc`: ∫ \|⟨w, σ(g)w⟩\| ‖g‖^N dg < ∞, N = 4(2r+k+1)²√(2(r+1)), under `GapBig` | Harish-Chandra and Trombi–Varadarajan type; supplies `Wu_spec` through a `Fact` instance | Focused Wave 5 §3 |
| V15 | Thorne's localized R = T at nice points, n = 3 and n = 4, in the form of `P1core` | Rank four uses `P1core` at every link through `b1Ar`, `b2Ar`, `raw`, `N4` | Focused Wave 4 §4.3 |
| V16 | the 54 `Fact` instances | Locate the term for each instance on the route | Focused Wave 5 §1 |
| **V17 (new)** | the inputs of `GlobalTheory.EX.hostEx_of_zeroFreeRegion` (`GI/HostExOfPublished.lean:30`): `ExplZeta`, `ExplChi` (explicit formulae), `LogDerOne`, `ZeroCount` (zero counting), `ZFRDirichlet` (zero-free region for Dirichlet L-functions), `TZRat`, `PageThm` (Page's theorem), `Jutila` (zero density N(α, Q, T) ≪ (Q²T)^{(2+ε)(1−α)} for α ≥ 4/5), `QuadraticHeckeZeroEstimates`, and `RayField` | The record nonemptiness route through `HostEx` is live (`exists_richRec_of_zeroFreeRegion`, `exists_coreTies_of_zeroFreeRegion`). These were not named on the boundary. Attribution and year of Jutila from memory | Final Closure Wave 5 §4.6, §9 |
| **V18 (new)** | prime number theorem for primitive characters in the form of `psi_thin` (`MSB/PsiThin.lean:385`): \|ψ₀(u, χ)\| ≤ C u (log u + λ)² exp(−c log u/(λ + √log u)) for primitive χ with log N ≤ λ and no real zero in (1 − c₀, 1) | de la Vallée Poussin's zero-free region with the exceptional zero removed by hypothesis, plus the truncated explicit formula. The archive has a Layer 3 proof (`pt_zero_free`, `explicitFormula_closed`, `zerosWindow_closed`, `pt_core`). Closes `QH.thinH`. Source cited from memory (Davenport, ch. 14, 17, 19, 20) | Wave 5 §4.2 |
| **V19 (new)** | root exchange for GL_n over a nonarchimedean local field (Ginzburg–Rallis–Soudry, *The descent map from automorphic representations of GL(n) to classical groups*, 2011, Ch. 7), and the linear model of the Weil representation of GL_a × GL_b with its seesaw (Kudla, *Seesaw dual reductive pairs*, 1984; *Notes on the local theta correspondence*, 1996, §§1–3) | `exchange_isPos` uses root exchange in type and the archive proves it internally (`RootEx`). If the statement matches, the PC-4 leaf `exchange_support` can stop here | Final Closure Wave 4 §2.2, §5 |
| **V20 (new, candidate)** | Raynaud's classification of F-vector space schemes (Raynaud, *Schémas en groupes de type (p, …, p)*, 1974) with Fargues's integral Hodge–Tate sequence | Not an input of the archive: the archive proves the needed lattice facts from `GR.Top.main`. Listed so that the PC-1 specialist can test whether `testFacts` is a statement of published type | Final Closure Wave 1 §3.6, §9.4 |

## 2. The boundary by branch

### Analytic frame and auxiliary primes

| Theorem | Form needed | Fidelity |
|---|---|---|
| Landau; functional equation; (C1) to (C6), (C8) | as in the manuscript | manuscript; (C2), (C4), (C5) not compared |
| Gallagher's prime number theorem (C7) | see V1 | derivation written (Focused Wave 4, Prop. 5); not compared with the original |
| Linnik's theorem (`SmallOne`), via `PrimesRel` (`primesRel_holds`) | least prime ≡ 1 mod M at most M^A; relative form for X ≥ M^{c₂} | Linnik range; not compared |
| Prime ideal theorem for ray classes of Q(√−d) (`ShortNorm`, `NormPrimes`, `LevelPrime`) | see V2 | proved in the archive by an elementary `LFam` convolution (Layer 3); not compared |
| Behrend's construction (`thickFrame2`, `hostThickExists`, `exists_noRel_finset_card_ge`) | sets without relations of small height, constant C = 32 | proved in the manuscript; the key identity of `sphere_rel` checked symbolically (Wave 5) |
| Chebyshev, ψ − ϑ ≪ √X; Dirichlet's theorem | standard | classical |
| **(new)** Analytic inputs of `HostEx` | see V17 | not compared |
| **(new)** Prime number theorem for primitive characters | see V18 | Layer 3; not compared |
| **(new)** ∫₁^∞ (ψ(u) − u) u⁻² du = −1 − γ (behind `g_integral`) | from −ζ′/ζ(s) = s ∫₁^∞ ψ(u) u^{−s−1} du and the Laurent expansion at s = 1 | classical; the archive proves `l21a` |
| **(new)** L(1, χ) ≠ 0 and continuity of L(s, χ) at s = 1 (behind `QH.small_zeros`) | for the finitely many χ of conductor at most 8B; gives an ineffective c₀(B) | Mathlib |
| **(new)** Dirichlet character theory | CRT decomposition, uniqueness of the inducing primitive character, conductor of a product of primitive characters of coprime conductors, quadratic characters of (Z/p)^× | Mathlib and elementary; proved in Wave 5 where needed |
| **(new)** Quadratic reciprocity with both supplements (`boxes_kron_neg`, `qdRows_kron_odd`, `qdRows_kron_two`) | Kronecker symbols at the host moduli | Mathlib; spot-checked (Wave 5) |
| **(new)** Galois theory of Q(ζ_N); quadratic Gauss sums | fixed field of the kernel of the Artin map; √−p ∈ Q(ζ_p) for p ≡ 3 (mod 4) with σ_a √−p = (a/p) √−p | Mathlib; classical |

### Block A, `LPprime`

| Theorem | Form needed | Fidelity |
|---|---|---|
| Standard monomial theory; Pieri, branching, Weyl dimension formula | integral bases compatible with prefix thresholds | see V10 |
| Extremal projector (Asherova–Smirnov–Tolstoy, Zhelobenko); Kummer, Legendre, Mahler; Smith form | as in Final A | proved in the archive; constants unchecked |
| Straightening law (Doubilet–Rota–Stein, De Concini–Eisenbud–Procesi) | for `adm7` | not compared |

### Block B, frame theorem

| Theorem | Form needed | Fidelity |
|---|---|---|
| Harder–Narasimhan theory; slope inequality (Stuhler, Grayson, Bost, Gaudron) | μ_min(φA) ≥ μ_min(A) − h(φ) | hand proof in Report B |

### Block C, `LinkS` and `LinkIRR`, with Theorem P

| Theorem | Form needed | Fidelity |
|---|---|---|
| Quantum minors: column and row expansions, row skew-symmetry, covariance (Molev, *Yangians and Classical Lie Algebras*, ch. 1); Capelli's theorem, centrality of the quantum determinant (ch. 7) | `quantum_minor_border_expansion_first`, `capelli_rho_commute` | used by Focused Wave 2; identities confirmed numerically in nine low-rank configurations. Wave 5 verified symbolically the RLL relation of the Weyl-algebra Lax matrix with Yang's R-matrix and the quantum determinant T(Y+1)ᵀ J T(Y) = J behind `ModelWordsD` |
| Cauchy–Binet; Laplace expansion | `RInvBetaP`, `RInvAlphaP` | classical |
| Multivariate Lagrange interpolation, also with values in L² | Lemma E, `GridConvergence`, `InterpolationCoefficientsInL2` | classical |
| A. A. Markov's inequality ‖q′‖ ≤ (2d²/L)‖q‖ | `markov_inequality_vector` | proved in the archive |
| Cauchy's estimate; Fatou's lemma; dominated convergence; Cauchy–Schwarz | `CauchyTheta`, `FatouStep`, `DomConv`, `PairLimit` | classical; Cauchy bound checked numerically with ratio at most 0.092 |
| Siegel–Weil in Weil's convergent range (Weil; Ichino) | Fourier-coefficient form, 2n < M, used with n = 1 | see V6 |
| Siegel mass formula in ratio form (`SiegelMassRatio`); Siegel mean value theorem | unimodular hermitian lattices; FR-12 (a) hypothesis | in type; not compared |
| **(new)** Mean counts of primitive sublattices over a genus (W. M. Schmidt, Duke Math. J. 35, 1968; C. L. Siegel, Ann. of Math. 46, 1945) | behind `LoopC.GenericMean.main`: genus mean of primitive sublattices of determinant d_e bounded by (d_e/N_T)^{k−1} (eπ/(kv))^{kf} (2k rd_E^{1/2})^f ⋯ | not compared; attribution by Wave 4 |
| Mass-formula leaves of FR-12 (b) (`massDataInputsAll_of`) and the absolutely convergent double-coset unfolding of FR-12 (c) (`KExpansionC_holds`: slab cover, regrouping, neat level, fundamental bridge, Poincaré measure) | as stated | unconditional internal theorems of published type (Layer 3) |
| Schmid's characterisation of discrete series; multiplicity one of the lowest K-type | `FormulaGap`, gap h ≥ 120 n rk^{3/2} | not compared |
| Harish-Chandra: square integrability, formal degree, integrability for large gap, finiteness; Borel–Harish-Chandra; Schur orthogonality | counting theorem; `DiscreteSeriesCover`, `HarishChandraModules`, `StrongApproxSU` | not compared |
| Landherr with Jacobowitz | isometry of hermitian spaces with unimodular lattices | proved in the archive |
| Rank-one class number formula; Tamagawa volume of GL_j | `genLinVolume` | proved in the archive |
| Louboutin; Minkowski | res ≤ (16 log rd)^{[E:Q]}, rd ≥ 3/2 | Wave B: archive form follows |
| Green, characters of GL_r(F_g); Gelfand–Graev multiplicity one; degenerate Whittaker models (Zelevinsky, Gelfand–Kazhdan) | cuspidal parametrisation; `nPos_parInd` | not compared |
| Jiang–Sun–Zhu; Sun–Zhu | uniqueness of Bessel models for real unitary groups | not compared |
| Classical analysis | Fubini, Haar uniqueness, Fourier inversion, Sobolev in dimension two, differentiation under the integral, Poisson summation, Schur test, Hadamard | standard |

### Block D, `VWin`

| Theorem | Form needed | Fidelity |
|---|---|---|
| Galois cohomology (`CohP`, `GC.Hypotheses₂`): local finiteness, local Tate duality, local and global Euler characteristic, Greenberg–Wiles, Poitou–Tate (with H⁰(G_F, W^∨(1)) = 0), tame local structure | cardinality forms; `x1` uses h² + h⁰ + 2d ≤ h¹ | not compared |
| Mazur's presentation lemma (`obs_pres`) | R₀ ≅ Λ[[x₁..x_m]]/(f₁..f_{h²}) from an obstruction theory | proved in the archive |
| **(new)** Noetherian finiteness of cocycle modules under Mazur's Φ_l condition (finitely many open subgroups of index l) | behind `Det.matFg`, `Det.finSub` of `Det.detFin` (FR-01/02) | classical; mechanism read by Wave 5 |
| Krull's height theorem; Nakayama; prime avoidance | `redDim`, `Ch.nice` | classical |
| Grothendieck connectedness (SGA 2, XIII) | `clChain`: chains of minimal primes with dim R/(P+Q) ≥ D when D + b ≤ a | proved in the archive (Layer 3) |
| Local class field theory (`LocCFT`, `LocAb`, `muOf`) | see V9 | not compared |
| Chebotarev density theorem (`cheb_holds`, `Loc.v00`); Brauer–Nesbitt | `chebFam`; `V0ok` in rank three and four | classical |
| Bellaïche–Chenevier generalized matrix algebras | residually multiplicity-free Cayley–Hamilton algebra | Wave F: hypotheses match |
| Taylor–Wiles–Kisin patching | `pmodEx` | proved in the archive through `litN` |
| Hida theory for definite unitary groups (Hida; Geraghty) | 2 ≤ n ≤ 4 | proved in the archive |
| Thorne's localized R = T, clause `P1core` | see V15 | not compared |
| Kato's Euler system; Rubin | see V4 | proved in the archive on the operative branch |
| Adjoint Selmer vanishing (Allen; Newton–Thorne) | `AdjointLiftingTheorem` | proved in the archive |
| Serre, *Algèbre locale*, multiplicities | positivity of the multiplicity symbol | Wave F, by reading `rulePos` |
| Soulé; Dwyer–Friedlander; Borel; Clozel | exponent l^{c(2e)}, c(m) = m(m+5)/2 | archive weaker than Soulé, the safe direction |
| Mazur–Wiles, Rubin; Stickelberger | Kolyvagin system of Gauss sums | not compared |
| Ferrero–Washington | μ = 0 for abelian fields, behind `Bounds` in `x2` | Wave C: field abelian over Q |
| Automorphic induction and cyclic base change (Arthur–Clozel); Labesse; Ramakrishnan's GL₂ × GL₂ → GL₄; Deligne–Serre; Eisenstein series; Gelbart–Jacquet | seeds, descent | not compared |
| Galois representations of RACSDC representations, local–global compatibility, purity (Harris–Taylor, Shin, Chenevier–Harris, Caraiani; Clozel) | clauses `pur`, `aut` | not compared |
| Herbrand-type triviality from an l-unit Bernoulli number | `CorX` | not compared |

### Block E, `LinkN`

| Theorem | Form needed | Fidelity |
|---|---|---|
| Tate 1967 (*p-divisible groups*, §3) | the maximal ideal kills H¹(H_K, O_C); Ax–Sen–Tate O_C^{H_∞} = Ô_{K_∞}; normalized decomposition Ô_{K_∞} = O_{K_m} ⊕ X_m | explicit-constant versions proved in the archive (Layer 3); constants 1 and max(1, ·) derived by Focused Wave 3 |
| Sen 1980; Fontaine 1994 | Hodge–Tate decomposition of de Rham representations; gr^i B_dR^+ ≅ C_p(i) integrally | Layer 3 |
| Tate's filtered invariants (`TateFilteredInvariants`); Fontaine's finiteness and de Rham property (`fontCore`) | Step A of Theorem TB (a) | not compared |
| Bloch–Kato (1990), Corollary 3.8.4 (`BlochKatoLocal`); dual exponential; dimension formula and crystalline extension criterion (fields `adm12`, `adm15` of the Theorem C record) | H¹_f, exp*, `exponent_le` | not compared |
| Local Tate duality; local Euler characteristic (Tate 1962) | `LocalTateDualityK`, `LocalEulerCharK`; hypotheses of both Theorem B and Theorem C producers | not compared |
| Bhatt–Scholze (2023), Theorem 1.2 | prismatic F-crystals for crystalline lattices | not compared |
| Wach (1996); Berger (2004) | Wach lattices, specialization at ζ_{p^n} − 1, sandwich q^{−(M₀+h₀)}; level maps and Hodge filtration (`LevelMapHodgeFiltration`) | see V8. **(new)** Candidate stopping points for PC-3: Berger's membership criterion (C-3, R-B1) and the elementary divisors of φ by Hodge–Tate weights (C-6), in the archive's explicit form |
| Herr (1998); Benois (2000); Berger (2003) | Herr complex, class formula (supplier `local_lemmas_of_literature`), naturality (`HerrClassNaturalExtension`, fields `adm16`, `adm17`), `F2` | proved in the archive |
| Fontaine (1990, 1994) | exactness and strictness of D_cris on crystalline sequences, D_dR = D_cris ⊗ K (`DcrisExactStrict`, `CrysSubQuot`, `DdREqDcris`, field `adm11`); full faithfulness and exactness of D (`LitFont`, `DDExact`), used by `SplitCore` and Theorem C | classical |
| Abhinandan (2023); Du–Liu–Moon–Shimizu (2022) | Wach module as value of the prismatic F-crystal | the archive reproves it |
| **(new)** Lifting-the-exponent lemma for odd p; Legendre's formula; Kummer's theorem on v_l of binomial coefficients; Weierstrass preparation in O[[π]]; O[[π]]^Δ = O[[π₀]] when \|Δ\| is a unit | `partR_coreHval` via `WindowSums.arc_ZpowVal`; `partR_coreHleg`; `PowerSeriesDVRFactorisation`; ring relations of `p9` | classical; proofs written in Waves 2 and 3 |
| Class field theory | characters with prescribed local components | classical |
| CM theory for the Weber function; Shimura, Deligne | `mul_twist_mem_intForms` | not compared |
| Local Langlands for GL_n; Bernstein–Zelevinsky; Moy–Prasad | classification, genericity, depth zero | not compared |

### Block F, covolume

| Theorem | Form needed | Fidelity |
|---|---|---|
| Route leaves of `DeepStR` | see V12 | not compared |
| Layer 3 statements under `DeepStR` | arithmetic intersection system (Gillet–Soulé, Burgos–Kramer–Kühn type), `ResK`, semi-abelian extension, GAGA for sections, quotients by finite flat groups (`QuotientByFiniteFlatStatement`, an input of `FamilyExistsPos`), Zhang's successive minima, arithmetic Hilbert–Samuel upper bounds and multiplicativity, Moret-Bailly's key formula, toroidal compactifications and integral models (`PartI`, `N1ab`, `N1c`), strong approximation, Hirzebruch–Mumford proportionality (`PB.Proportional`), heights of flag varieties (`PB.FlagHeight`), the antisymmetric perturbation lemma, `NumericalSegre`, `Prov.An` | proved in the archive; not compared |
| Bost-type slope bound | see V11 | source not matched |
| Fargues's integral Hodge–Tate sequence; Zarhin's trick | inputs of `familyExistsPos_holds`, `trivFlagOnHodge_of_fargues`, `exists_sandwich_of_hodge_tate_free`; see V12, V20 | not compared |
| Chowla–Selberg; Kronecker limit formula | Re log Ω_K = γ + log(2π/rd_E) − Re L′/L(1, χ_d); \|Re log Ω_K\| bounded | proved in the archive; normalization consistent (Focused Wave 1 §8); the Colmez conjecture is not used |
| Mertens-type bound | Σ_{p≤B} log p/(p−1) ≤ log B + 2.2 (as recorded by the authoritative boundary); the form log B + 3.4 used by `sum_log_div_pred_SB` (excess at most 0.144 for B ≤ 2·10⁶, limit −γ) | elementary, read; checked numerically by Final Closure Wave 1 |
| Kawamata–Viehweg vanishing; other fields of `HSCore.Quoted` | as in the bundle | see V7 |
| Bertini for simple zeros of generic sections over number fields | | not compared |
| Nadel vanishing (`q15`); principalisation (`q16`); Hirzebruch–Mumford (`q7`); Faltings–Chai, Lan; Grothendieck–Messing | fields of `PublishedHodgeBundleTheorems` | see V7 |
| Ray class fields (`p8`) | existence of deep covering levels | classical |
| Product formula; Mahler measure; Hadamard; Schwartz–Zippel; Dedekind's complementary module | effective Hilbert–Samuel | classical |

### Block F, theta side and records

| Theorem | Form needed | Fidelity |
|---|---|---|
| `SiegelWeilStd`; `EisBL` | see V5 | constant matched |
| Rallis's constant-term formula; Kudla–Rallis | see V13 | not compared |
| (GL_a, GL_b) Howe duality on C[M_{b×a}] (`glHoweDuality_holds`) | `howeSpan_unit` behind `KerX` | proved in the archive |
| Multiplicity-one branching U(n+1) ↓ U(n) for interlacing weights (Weyl, Gelfand–Tsetlin) | `mult_one_families` behind `PerX` | proved in the archive |
| Irreducibility of Weyl modules; Schur's lemma; finiteness of the class set of a definite unitary group | `Vn_unit_irreducible`, `equivariantHom_mem_of_stable`, `integral_eq_classSum` | proved in the archive |
| Bernstein–Zelevinsky geometric lemma; Kudla's filtration of the Jacquet module of the Weil representation | `geometricLemmaFiltration` behind `finRam`, `finSplit` | proved in the archive |
| Howe duality (Howe, Waldspurger, Mínguez, Gan–Takeda); unramified Howe duality at inert places | `howeInert` | not compared |
| **(new)** Root exchange; linear-model seesaw | see V19 | not compared |
| **(new)** Haar measure on quotients of unimodular groups and Fubini for products of local groups (A. Weil, *L'intégration dans les groupes topologiques*, ch. II) | behind `CollapseFactor.collapse_factor`, `IterPeel.iterated_integral_product_groups`, `HaarR.quot_int_haar`; Haar pair at Q normalized by vol(K_Q) = 1 | Mathlib measure theory; not compared |
| Rallis inner product formula; doubling method | `AForm`, `BForm`, `LamLow` (FR-14); `nonZeroBottom_of_doubling_integral` | not compared |
| Weighted integrability of discrete-series matrix coefficients | see V14 | not compared |
| Adelic and classical theta dictionary (Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111, 1964) | `thetaKO_transSum_eq_short_series`; **(new)** `thetaKernel_splitPlaces_eq_jet_classicalTheta` behind `kernel_identity_tuple` | read at statement level |
| **(new)** Projective lifting property; density of a global lattice in its completion (strong approximation for A_f-modules) | behind `AdMark.exists_marking` (`exists_lift`, `latG_lattice_and_completion`) | Mathlib `Module.projective_lifting_property`; classical |
| **(new)** Existence of level structures on PEL moduli and lifting through level covers (Kottwitz, J. AMS 5, 1992, §5; Lan, *Arithmetic compactifications of PEL-type Shimura varieties*, 2013, ch. 1) | behind `Dict.MarkLift.exists_lift_marked` (`anFib_lift_ex`, `FramedPointsLiftToLevelCover`, `AllUniformizationLawsHold`) | not compared |
| Hasse's norm theorem (`HasseNormSt`) | `IsUnfEx.exists_isUnf` | classical |
| Orthonormal integral bases of unramified extensions (Serre, *Corps locaux*, I §6); Galois descent of coefficients | `supSet_descent`, `cover_desc_rat` behind `DescIntAt` | classical |
| The thirteen hypotheses of `miStar2_of_allTrue_alt_alt` and `SiegelSetUnitary` | as stated | not compared |
| Tate's thesis; Hecke L nonvanishing at 1 | functional equations | local statements are closed terms |
| Classical measure theory on locally compact groups | Haar uniqueness, Weil's quotient formula, compactness of N(F)\N(A), fundamental domains, Fubini–Tonelli | standard |
| `SiegelMassRatioCM`, `RayField`, `PrincipalIdealSt`, `CMCurveGoodOutsidePrimeSt` | bundle fields behind record nonemptiness; `SiegelMassRatioCM` is used by `window_lower`; `RayField` is part of V17 | not compared |

### Gain side

| Theorem | Form needed | Fidelity |
|---|---|---|
| Global Artin reciprocity, ray class fields, main theorem of CM | `CM2`; good models of CM elliptic curves at l ≥ 5, l ∤ d, behind `inert_theta_admissibility_of_complex_multiplication` and `curveEx_of_cm` (FR-19) | use read |
| **(new)** Honda's theory of formal groups (`CM3`) | an unramified twist of the formal group has logarithm Σ_j x^{l^{2j}}/l^j at inert l | proved internally (`HondaCM3.cm3`); internal, listed for reference |
| Weak approximation; Jacobowitz's classification at unramified and inert primes | `intInert_of` | not compared |
| Chernoff-type binomial tail | `topsBase` | proved in the archive; helper read |
| Duality for finite abelian groups | `Loc.v0e` | classical |

## 3. Not inputs

These are comparisons or internal theorems, and should not be cited as the place where the route stops.

- Skinner–Wiles, Thorne, Allen–Newton–Thorne as a source for residually reducible automorphy lifting. `GdEndAlt`, `SymplecticFourImageDense`, `ThmS6Core_s` are theorems of the archive (see V3).
- The arithmetic Hilbert–Samuel formula `q9`. The explicit inequality `HSAt` is internal and reconstructed, and `DeepStR` does not use it.
- The Capelli identity and the RTT presentation as models for the radial and model-algebra identities. The classical expansions listed in Block C are inputs; the models are not.
- `StatWA0`, the off-route statement whose mechanism the closing synthesis attributed to `coreWA`.
- The Siegel–Walfisz range. None of `ShortNorm`, (C7), `SmallOne` uses it.
- `litN`. Layer 3, unread.
- **(new)** Raynaud's classification, until V20 is settled. The archive does not cite it, so it is the mechanism of `testFacts` and not an input.
- **(new)** `KillerLev`, `KillerKap`. Internal theorems of PC-3, not clauses of the Wach record V8.
- **(new)** `CVEq`. A definition of c_V in `colSide_alt`, not an input.

## 4. Closed in the manuscript, outside both lists

- The analytic frame modulo (C1) to (C8), and `PairEx` from (C1) to (C8). `PairEx` provides the hypothesis `PairGood` of `pairRows`, now closed modulo the classical statements of the analytic block.
- Behrend's construction (Proposition behrend), matched with `hostThickExists` by Wave 5.

## 5. Separate campaigns

- The archive's own Lean proofs of the published theorems (Layer 3), including the explicit-constant versions behind Theorem TB (a) (`cyclotomic_tate_maximalIdeal_kills_first_cohomology`, `tate_decomposition_completed_cyclotomic_integers`, `exists_decompletion_frame_of_lattice`, `exists_hodgeTateBasis_of_crystalline_over_Ks`, `xiGradedPiece_iso_twistedOC`, `xiQuotient_invariants_lift_rationally`, `ses_lattice_trivial_quotient`), the Layer 3 statements under `DeepStR`, the archive's proof of V18 (`pt_zero_free`, `explicitFormula_closed`, `zerosWindow_closed`, `pt_core`), the internal `RootEx` proof of root exchange, and `litN`.
- A kernel replay of the Lean project.
- Refereeing of Sections 7 to 9 of the manuscript, including the corrections listed in Section 9 of `Post_Closure_Synthesis.pdf` and Section 10 of `Final_Authoritative_Synthesis.pdf`.
