# External-theorem fidelity audit (Part A)

22 November 2026. Pre-synthesis audit, written by Claude for Jimmie Adriazola. Companion to `Pre_Synthesis_Audit_Report.md`.

## 0. Scope, inputs and rules

**Inputs read.** The final reports and dependency maps of the six-agent closure wave, as they stood at 17:47 UTC on 22 November 2026 (file times in UTC):

| Package | File | Time | Final verdict in file |
|---|---|---|---|
| PC-1 | `Final_Six_Wave_1/Final_Six_Wave_1_Dependency_Map.md` | 16:55 | CLOSED MODULO NAMED EXTERNAL THEOREMS |
| PC-2 | `Final_Six_Wave_2/Final_Six_Wave_2.tex`, Section "Final report" | 17:34 | CLOSED MODULO NAMED EXTERNAL THEOREMS (the companion `.md` map still carries the superseded verdict RESIDUAL, see Part D) |
| PC-3 | `Final_Six_Wave_3/Final_Six_Wave_3_Dependency_Map.md` | 17:42 | CLOSED MODULO NAMED EXTERNAL THEOREMS (seventh pass) |
| PC-4 | `Final_Six_Wave_4/Final_Six_Wave_4.tex` and map | 17:08 | RESIDUAL CHILD REMAINS (PC4.13 the one human-level residual) |
| PC-5 | `Final_Six_Wave_5/Final_Six_Wave_5_Proposition_Package.tex` | 17:11 | CLOSED MODULO NAMED EXTERNAL THEOREMS at proposition level |
| PC-6, PC-7 | `Final_Six_Wave_6/Final_Six_Wave_6_Dependency_Map.md` | 16:12 | RESIDUAL CHILD REMAINS |

Also read: `Post_Closure_Synthesis/Post_Closure_Verification_Boundary.md` (V1 to V20 and the boundary by branch), and, for statement fidelity, the Lean statements (not proofs) of `FarguesHodgeTate`, `FarguesExact`, `TamagawaSpecialUnitary`, both `SiegelWeilUnitaryConvergent`, `ZhangLowerX.Statement` and `GlobalTheory.T.global_model_power_free`. One published source was opened in this pass, Fargues, *L'isomorphisme entre les tours de Lubin–Tate et de Drinfeld au niveau des points* (arXiv:math/0604063, Chapter II of the Birkhäuser volume, Progress in Math. 262, 2008), Section 1, read through a page fetch.

**Status definitions used below.**

| Status | Meaning in this file |
|---|---|
| VERIFIED | The archive or human-level statement was read, the published statement was opened, and hypotheses, conventions and the direction of implication were checked to match. |
| PARTIAL | The source is identified at the level of a theorem, and at least one hypothesis, normalization or clause was checked. The open items are listed. |
| WRONG SOURCE | The cited source does not supply the statement used, or the citation sits on a route that is not live. |
| SOURCE NOT YET LOCATED | No exact theorem has been located and opened. A name or a book may be known. |

The column **Impl.** says whether the published statement gives the archive's statement exactly (E) or needs an additional argument (A). "Archive" in the column of the user always means the theorem or proposition of our reconstruction that stops at the input.

**Headline.** No external input is VERIFIED. Fifteen are PARTIAL, nine are WRONG SOURCE or not on the live route, and the remainder are SOURCE NOT YET LOCATED. Every "closed" verdict of PC-1 to PC-5 is therefore "closed modulo named external theorems whose source fidelity is pending".

## 1. Items given special attention

### 1.1 Fargues and the integral Hodge–Tate sequence (PC-1, PC-2)

| Field | Content |
|---|---|
| Used by | PC-1: `FamEx.TestPt.testFacts` (fields `im`, `ker` through C1 `TestGroupPoint.reducesAt_pack` and `HT.Fargues.pointHT`). PC-2: nefness at $\ell\in S_B$ in Proposition 2.B (`or_m1nef` through `HT.rootModel_nefAt_of_hodgeCpt`), Proposition 2.A (Hodge–Tate patch of the Lie lattice at $\ell\in S_B$). |
| Archive statement | `FarguesHodgeTate` (two clauses) is derived inside the archive from `FarguesExact` (second clause only). For a $p$-divisible group $G$ over $\mathcal O$, with $\mathcal O$ the $p$-adically complete valuation ring of an algebraically closed $C$ of characteristic zero: (i) if $v(\kappa)^{p-1}\le v(p)$ ($p$ odd) or $v(\kappa)\le v(4)$ ($p=2$), then $\kappa\,\omega_{G^D}\subseteq\operatorname{im}(\alpha_G\otimes\mathcal O)$; (ii) $\ker(\alpha_G\otimes\mathcal O)$ is the orthogonal, under the Weil pairing normalized by a compatible system $\zeta$ of $p$-power roots of unity, of $\ker(\alpha_{G^D}\otimes\mathcal O)$. |
| Published source | Fargues, op. cit., Chapter II, Section 1, Théorème 1.1 (attributed there to an earlier Fargues paper and derived from Théorème A.5 of its appendix). Over a field $K\mid\mathbb Q_p$ complete for a real valuation, the Hodge–Tate sequence of a $p$-divisible group over $\mathcal O_K$ is a complex whose cohomology as a sequence of $\mathcal O_{\widehat{\bar K}}$-modules is killed by $p^{1/(p-1)}$. The article has the standing assumption $p\neq2$. |
| Hypotheses | Match for $p$ odd ($\mathcal O_C$ is the case $K=C$). **Mismatch at $p=2$**: the article assumes $p\neq2$, while the archive's clause (i) is stated for $p=2$ with $\kappa\in4\mathcal O$. The PC-1 route uses $p\ge3$ (Wave 1, "uses $v(p)\le v(w)^2$, $p\ge3$"), so the $p=2$ instance is probably not used on the route. This must be confirmed, or a source for $p=2$ found. |
| Conventions | Clause (i): "cohomology killed by $p^{1/(p-1)}$" gives $\kappa\,\omega\subseteq\operatorname{im}$ for $\lvert\kappa\rvert\le\lvert p\rvert^{1/(p-1)}$, which is the archive's inequality in multiplicative form. Clause (ii) is insensitive to the normalization of the pairing because it asserts only an orthogonal. That `dlogLinear G` is $\alpha_{G^D}$ and that `muTate` is the Tate twist used by Fargues was not checked against the definitions. |
| Implication | (i) E. (ii) A: Théorème 1.1 does not assert integral exactness in the middle. The additional argument is short. Both sides of (ii) are saturated submodules of the free module $T_pG\otimes\mathcal O$ (a kernel of a map to a torsion-free module, and an orthogonal under a perfect pairing), and they have the same span over $C$ because the sequence is exact after inverting $p$. Saturated submodules of a free module over a valuation ring with equal rational spans are equal. |
| Status | **PARTIAL.** Open: $p=2$, identification of `dlogLinear` and `muTate`, write the saturation argument into the PC-1 human proof. |

### 1.2 Raynaud, Stickelberger, finite flat quotients, Cartier duality of Hopf orders (PC-1, Layer 3)

| Input | Used by | Human-level statement | Source | Hyp. | Conv. | Impl. | Status |
|---|---|---|---|---|---|---|---|
| Raynaud's classification of $\mathbb F$-vector space schemes, with Cartier duality $\delta_n\delta'_n=w$ | PC-1 Frobenius layer (`eig_rank_one`, `Ri.r_decomp`, `Ri.r_dual`, `rank_one_sum`, `Pmono.r_mono`, `fundamental_ideal_frobenius_product`, ...) | rank-one Raynaud schemes $\operatorname{Spec}\mathcal O[x_n]/(x_n^p-\delta_nx_{n+1})$ with $\delta_n\delta'_n=w$, $w=\zeta_p-1$ up to unit | Raynaud, *Schémas en groupes de type $(p,\dots,p)$*, Bull. SMF 102 (1974), Théorème 1.4.1 (as recorded by Wave 1, "matched in content") | Raynaud works over a base containing the $(q-1)$-st roots of unity with the constants $w_p$; PC-1 works over $\mathcal O_C$, which satisfies this. Not checked against the text | normalization of $w$ (Raynaud's $w_p$ versus $\zeta_p-1$) not checked | E for the classification; the archive proves it internally | **PARTIAL** (theorem located by number, not opened) |
| Stickelberger's congruence | `gauss_value`, `gaussCongruence` | $v(g(\omega^{-1}))=1/(p-1)$ for the Teichmüller character of $\mathbb F_q$ at a fundamental character | Stickelberger (1890); Washington, *Introduction to Cyclotomic Fields*, Ch. 6 (exact proposition not located) | match in the case used ($q=p^f$, fundamental characters) | sign of exponent of $\omega$ to check | E | **SOURCE NOT YET LOCATED** (exact proposition) |
| Quotients of finite flat group schemes: $G\to G/K$ a $K$-torsor, right exactness of cotangent, transitivity of discriminants | `ReciprocityTheory.PGsh.L2.h3`, `Rc.exists_quo`, `Rc.invres` | as stated | SGA 3, Exp. V (quotients); Raynaud, *Passage au quotient par une relation d'équivalence plate* (1967) | flatness of $K$ over the base to check | none | E | **SOURCE NOT YET LOCATED** (exposé and section) |
| Cartier duality of Hopf orders | `ReciprocityTheory.PGsh.L2.h1` | dual Hopf order of a rank-$p$ group scheme | Tate–Oort, Ann. Sci. ÉNS 3 (1970), §1 | rank $p$, base containing $\mu_{p-1}$ | none | E | **SOURCE NOT YET LOCATED** (theorem number) |
| `ZarhinStatement`, `QuotientByFiniteFlatStatement` | PC-1 hypotheses of `testFacts`; PC-2 2.A | Zarhin's trick over valuation rings; quotient of an abelian scheme by a finite flat subgroup | Zarhin (1977) [Slijepčević ref. 137]; SGA 3 / Raynaud | Zarhin over valuation rings rather than fields to check | none | E | **SOURCE NOT YET LOCATED** |

### 1.3 SGA 3, SGA 7, Mumford biextensions, Cartier isomorphism, Rosenlicht (PC-2, semi-abelian de Rham datum)

These five inputs replace Katz and Oda in the final PC-2 proof of fibrewise injectivity of $F^*\mathcal L\to\mathcal H$ at semi-abelian points (Wave 2, Section "The de Rham datum at points of semi-abelian reduction").

| Input | Human-level statement used | Source | Hyp. | Conv. | Impl. | Status |
|---|---|---|---|---|---|---|
| $[p]=V\circ F$; $V$ an isomorphism on tori | for a commutative group scheme over a field of characteristic $p$; on $\mathbb G_m$, $[p]=F$ | SGA 3, Exp. VII$_A$ (Gabriel), §4 | match (commutative, flat, characteristic $p$) | $\operatorname{Lie}(V)$ as the Hasse–Witt matrix is the archive's `hw`; the identification is the content of Step 1 of the human proof | E | **PARTIAL** (exposé identified; section not opened) |
| Symmetric biextension $\Lambda(L)$ of a cubical $L$ | $\Lambda_y^{\otimes p}\cong\Lambda_{[p]y}$ canonically | SGA 7 I, Exp. VII (Grothendieck), §2; Mumford, *Bi-extensions of formal groups*, Bombay Colloquium 1968 (publ. 1969) | $G_x$ is a semi-abelian variety, $L$ cubical. The cubical structure on $L$ over a semi-abelian (not proper) fibre is extra data; the archive supplies it in the germ data `FB`. Not checked that the archive's `ph1`, `ph2`, `sy` satisfy Grothendieck's axioms | none | E given cubical structure | **PARTIAL** |
| Cartier isomorphism | $\ker(d:\mathcal O\to\Omega^1)=\mathcal O^p$ on a smooth variety over a perfect field | Cartier (1957); Katz, Publ. IHÉS 39 (1970), Thm. 7.2 (from memory) | match (smooth $G_x$ over $k$ algebraically closed) | none | E | **SOURCE NOT YET LOCATED** (exact location not opened) |
| Rosenlicht's theorem | units on a connected algebraic group are constants times characters | Rosenlicht, *Toroidal algebraic groups*, Proc. AMS 12 (1961), Theorem 3 (from memory) | connected, over algebraically closed $k$: match. The human proof applies it to the reduction of a unit of $G_x\otimes k[\varepsilon]/(\varepsilon^2)$, which is legitimate | none | E | **SOURCE NOT YET LOCATED** |
| $\ker\operatorname{Lie}(\varphi_M)=\operatorname{Lie}K(M)$ | for an ample $M$ on an abelian variety $B$ | Mumford, *Abelian Varieties*, §§8, 13 | match | none | E | **SOURCE NOT YET LOCATED** (section) |
| Katz (1970), Oda (1969) | conjugate filtration on $H^1_{\mathrm{dR}}$ | Katz, Publ. IHÉS 39; Oda, Ann. Sci. ÉNS 2 | none | none | none | **WRONG SOURCE.** The archive's $\mathcal H$ is a formal-biextension module, not $H^1_{\mathrm{dR}}$, and the final PC-2 proof does not use either paper (Wave 2, "Published sources"). |
| Goldring–Koskivirta, partial Hasse invariants (Invent. Math. 217, 2019) | candidate source for Lemma 8.7 | none | none | none | none | **WRONG SOURCE** (recorded by Wave 2 as a candidate only; no match; the proof of Lemma 8.7 does not use partial Hasse invariants) |
| Faltings–Chai, Lan, for nefness at $p\notin S_B$ | none | none | none | none | none | **WRONG SOURCE** (Slijepčević's Lemma 8.7 corrected this attribution; the nefness is the internal Lemma 8.7, now proved in Wave 2 §12) |

### 1.4 Tamagawa number, Kottwitz, Prasad (PC-2, Bergman constant)

| Field | Content |
|---|---|
| Used by | PC-2 Proposition 2.E, `massBound_of_tamagawa` → `MassLev.mass_components_le` → `supConst_size` → $\log\beta\le4000(frL_b)^3$ → covolume bound. |
| Archive statement | `GlobalTheory.Published.TamagawaSpecialUnitary`: for a CM field $E$ with $E/E^+$ unramified at every finite place (`Unr E`), a self-dual hermitian lattice $\Lambda$ of rank $r\ge2$, a CM type $\Psi$ and a basis $e$ of $E^+$-linearly independent elements of the Lie lattice, $\sum_j\operatorname{covol}(\Gamma_j\backslash SU(\mathbb R))\cdot\lvert d_{E^+}\rvert^{-(r^2-1)/2}\cdot[\operatorname{span}e:\operatorname{lieLat}]\cdot\prod_v\mathrm{locFactor}_v=1$, with the covolume taken for the Haar measure attached to $e$. |
| Published source | Kottwitz, *Tamagawa numbers*, Ann. of Math. 127 (1988), main theorem ($\tau(G)=1$ for simply connected $G$, which for $SU$ goes back to Weil, *Adeles and Algebraic Groups*); Prasad, *Volumes of S-arithmetic quotients of semi-simple groups*, Publ. Math. IHÉS 69 (1989), Theorem 3.7. |
| Hypotheses | Simply connected: yes ($SU$). Checked here: the exponent $(r^2-1)/2=\dim SU/2$ is Prasad's $D_k^{\dim G/2}$, and Prasad's extra factor $(D_\ell/D_k^{[\ell:k]})^{s/2}$ for the outer form of type ${}^2A_{r-1}$ equals $1$ exactly because `Unr E` gives $D_E=D_{E^+}^2$. This is a consistency check of the statement, not a reading of Prasad. |
| Conventions | Not checked: the definition of `locFactor` (it must be $q_v^{-\dim}\#G(\mathbb F_v)$ or Prasad's $e(P_v)^{-1}$ in the matching normalization), the factor `relIndex`, and the absence of Prasad's archimedean factor $\prod_i m_i!/(2\pi)^{m_i+1}$, which should be absorbed in `tangentHaar` and the real form. |
| Implication | E if the conventions match. |
| Status | **PARTIAL.** Open: open `locFactor`; compare with Prasad 3.7 term by term. |

### 1.5 Shimura's hermitian mass formula (PC-5) and strong approximation (PC-2, PC-4, PC-5)

| Input | Used by | Human-level statement | Source | Hyp. | Conv. | Impl. | Status |
|---|---|---|---|---|---|---|---|
| Hermitian mass formula, ratio form `MaxMass`, `SiegelMassRatio` | PC-5 proposition on masses (`Mass.MaxFormula.main`), genus mean of FR-12(a) | ratio of masses of maximal (unimodular) hermitian lattices in adjacent ranks | Shimura, *Euler Products and Eisenstein Series*, CBMS 93 (1997); Gan–Hanke–Yu, Duke Math. J. 107 (2001); Braun (1940s) | archive uses unimodular lattices over $E/E^+$ unramified; Gan–Hanke–Yu treat maximal lattices in general; to check that the ratio is taken in the same genus normalization | `massRatioRightSide` against Shimura's product of local factors | E (the archive proves it internally by Siegel's induction) | **SOURCE NOT YET LOCATED** (theorem numbers in Shimura and Gan–Hanke–Yu not located) |
| Siegel mean value (1945), Schmidt counts (1968) | earlier boundary for FR-12(a) | none | none | none | none | none | **WRONG SOURCE** (PC-5: "Withdraw from FR-12(a) ... Not used"; the upper bound `PrimMean.main` uses neither) |
| Strong approximation for $SU$ | PC-2 (`unitary_frames_strong_approximation` in the mass bound), PC-4 W12 (`SplitCharTrivial.eq_one_of_rat_of_split`), PC-5 (`StrongApproxSU` recorded as a hypothesis of parents of FR-12, placement not traced) | $SU(V)(F)$ dense in $SU(V)(\mathbb A_F^S)$ | Kneser (1966); Platonov–Rapinchuk, *Algebraic Groups and Number Theory*, Thm. 7.12 | **Live and needs a hypothesis check.** Kneser requires $SU(V)(F_S)$ noncompact. For a definite $V$ (PC-4 works on the definite side) $S$ must contain a finite place where $SU(V)$ is isotropic, for example the split place. PC-4's use is at a split place, which is consistent. PC-2's use is on an indefinite Shimura datum, which is consistent. Neither use was checked against the statement of the Lean hypothesis | none | E under the right $S$ | **PARTIAL** (theorem identified, hypothesis on $S$ named, Lean statements not opened) |
| Weak approximation, Hasse norm theorem, Landherr, Jacobowitz, Witt, Minkowski | PC-5 R5-1 (gluing), PC-4 W10, PC-5 propositions | classical | Landherr (1936); Jacobowitz, Amer. J. Math. 84 (1962) | not checked | none | E | **SOURCE NOT YET LOCATED** (Jacobowitz theorem number) |

### 1.6 Siegel–Weil and Rallis (PC-4, PC-5, PC-6)

| Input | Used by | Archive statement | Source | Hyp. | Conv. | Impl. | Status |
|---|---|---|---|---|---|---|---|
| V6, `SiegelWeilUnitaryConvergent` (Formalism copy) | PC-5 engine: `GaussMean.oneVectorCc_of_siegelWeil`, proposition `vstep` | For a CM extension $E/F$ and a nondegenerate hermitian $J$ of size $M$, for $2n<M$ and nondegenerate $T$, the mean over a fundamental set of the theta sum over $\{X:\ \text{Gram}(X)=T\}$ equals the product of local densities | Weil, Acta Math. 113 (1965); Ichino, Math. Z. 247 (2004); Kudla–Rallis; Harris–Kudla–Sweet, J. AMS 9 (1996) | $2n<M$ implies Weil's convergence condition for unitary groups ($M-r>n$ with Witt index $r\le M/2$). Checked here from the statement. Finite volume is part of the statement (`FinVol`) | the mean is normalized by the measure of the fundamental set, so the Tamagawa number $2$ of $U(V)$ does not enter; the local densities are attached to self-dual measures for $\psi$, to check | E | **PARTIAL** (archive statement read; Weil's condition checked; source not opened) |
| V6, second declaration (doubling form, `GlobalTheory.Published`) | `RowDiag` and the doubling route | Eisenstein value at $s_0$ of the Siegel–Weil section equals the theta mean, for rank $A<B\le2A$ and $A+\operatorname{wittIdx}B<B$ | Ichino (2004); Gan–Takeda; Yamana | the Witt-index condition is Weil's condition; Yamana is not named on the boundary | $s_0$ and the section `swSec` not checked | E | **SOURCE NOT YET LOCATED** |
| V5, `SiegelWeilStd`, `EisBL` | theta tower, records | standard form | Gan–Takeda §7.1 | constant matched by Wave E | Tamagawa number 2, probability Haar measure, holomorphy at $s_0=(m-n)/2$ open | E | **PARTIAL** (as recorded on the boundary) |
| V13, Rallis's constant-term formula | `GenBig`, `GenAniso`, `GenSmall` of the theta tower | constant terms of theta integrals in the convergent range | Rallis, Compositio 51 (1984); Kudla–Rallis | none | none | E | **SOURCE NOT YET LOCATED** |
| Rallis inner product formula; doubling method | `AForm`, `BForm`, `LamLow` (FR-14); PC-6 F1 producers (`lValueRatio_lower_bound_gauge`, `tower_of_theta_matching_lNe`) | Petersson norms of theta lifts by special $L$-values | Rallis (1987); Gan–Qiu–Takeda, Invent. Math. 198 (2014) | Slijepčević could not decide whether his Prop. 7.3 is a consequence of the Rallis formula | none | A | **SOURCE NOT YET LOCATED** |

### 1.7 Arithmetic Hilbert–Samuel and height inequalities (PC-2, PC-6)

| Input | Used by | Archive statement | Source | Hyp. | Conv. | Impl. | Status |
|---|---|---|---|---|---|---|---|
| Zhang's inequality for successive minima, `ZhangLowerX` | PC-2 Proposition 2.C (`SlopeLower`, constant $C_h+C_u/2$) | if every point $W$ of the arithmetic variety $P$ (of arithmetic dimension $n+1$) has $h_A(W)\ge e$, then $(n+1)\,e\,\deg_A(P)\le h_A(P)$, for $A$ relatively semipositive, nef on fibres, conjugation invariant | Zhang, *Positive line bundles on arithmetic varieties*, J. AMS 8 (1995), Thm. 1.10 and Thm. 5.2; Zhang, *Small points and adelic metrics*, J. Algebraic Geom. 4 (1995) | Zhang states it for $L$ ample on the generic fibre with semipositive metric. The archive assumes nefness on fibres and no generic ampleness. The inequality follows from $h(X)\ge\frac{1}{d+1}\sum e_i\cdot(d+1)\deg$ and $e_i\ge\inf_x h(x)\ge e$, but the nef (not ample) case needs a limiting argument | the archive's height is the intersection system `II`; normalization $(n+1)$ versus Zhang's $(d+1)$ with $d=n$ matches | A (nef case) | **PARTIAL** |
| Arithmetic Hilbert–Samuel (Gillet–Soulé, Bismut–Vasserot, Abbes–Bouche, Moriwaki, Yuan) | V12 `HSUse`, `NefRR`, `MoriwakiBigStatement`; PC-2 Proposition 2.D | lower bound of lattice-point counts by arithmetic volume | Gillet–Soulé, Invent. Math. 106 (1991); Moriwaki, J. AMS 22 (2009); Yuan, Invent. Math. 173 (2008), Thm. 2.2 | not checked | none | E | **SOURCE NOT YET LOCATED** |
| `q9`, the arithmetic Hilbert–Samuel formula | none | none | none | none | none | none | not an input (the boundary lists it under "Not inputs"; `HSAt` is internal and reconstructed) |
| Bost / Gaudron slope inequality | PC-6 core of `FUN` (`Formalism.HN.slope_inequality_mean`); `FrameF` | $\mu_{\min}(\varphi A)\ge\mu_{\min}(A)-h(\varphi)$ | Bost, Sém. Bourbaki 795 (1996); Gaudron, Rend. Sem. Mat. Padova 119 (2008) | hand proof in Report B | none | E | **SOURCE NOT YET LOCATED** (theorem number) |
| V11 `SlopeBoundSt` | PC-2 constant $C_h$ of `DeepStR` | $\mu_{\max}(\mathrm{Lie})\le C_s\log(2+\mathrm{rk}+\max(-\deg,0))$ | candidates Bost, Graftieaux, Gaudron–Rémond | none | none | none | **SOURCE NOT YET LOCATED** (manuscript line 804 already says so) |
| Chowla–Selberg | PC-2 2.C (`logOm_bound`), mean period | $\operatorname{Re}\log\Omega_K=\gamma+\log(2\pi/\mathrm{rd}_E)-\operatorname{Re}L'/L(1,\chi_d)$ | Chowla–Selberg, J. reine angew. Math. 227 (1967) | normalization consistent (Focused Wave 1 §8) | none | E | **PARTIAL** |

### 1.8 PC-3 local $p$-adic Hodge theory

| Input | Used by | Source | Status |
|---|---|---|---|
| V8 Wach and Berger clauses (`p3`, `p4` both directions, `P5`, `P9`, `WachLatticeFree`, `SATcore`, `FirstWachFiltration`) | membership criterion, truncation, killer layers | Wach, Bull. SMF 124 (1996); Berger, Ann. Inst. Fourier 54 (2004) | **PARTIAL** (ring relations of `P9` checked classically by Wave 2; no clause compared with Berger's text) |
| `CMP` comparison record | `LevE.levETie_of`, `levB_Γ` | internal record of published type | **SOURCE NOT YET LOCATED** |
| Fontaine: `DdREqDcris`, `DcrisExactStrict`, `DDExact`, `coreJumps` | `MemCrit`, `SplitCore`, `UnivFrame` | Fontaine, Astérisque 223 (1994), Exposés II, III | **SOURCE NOT YET LOCATED** (exposé numbers recalled, not opened) |
| Herr complex, `HerrExt` | `SplitCore`, Theorem C tools C-I | Herr, Bull. SMF 126 (1998) | **SOURCE NOT YET LOCATED** |
| Mathlib Weierstrass division | `rem_exists`, `finLev_of` | Mathlib `PowerSeries.IsWeierstrassDivision` | **PARTIAL** (it is a Mathlib theorem, so its statement is checked by Lean; that it is applied to the right ring was read by Wave 3) |
| LTE, Legendre, Kummer | `KillerKap`, case exponents | classical | **SOURCE NOT YET LOCATED** (textbook) |

### 1.9 PC-4 Weil representation boundary (W1 to W16)

All sixteen are **SOURCE NOT YET LOCATED** at the level of a theorem number, except as follows. W13 (`QuotInt.quotInt_unique_exists`, quotient integrals of semi-invariant functions) is **PARTIAL**: Wave 4 checked the modulus $\lvert\det\rvert^{c+1-2p}$ of $R_p$ for all $c\le29$ against Bourbaki, *Intégration* VII §2 and Bernstein–Zelevinsky (1976) §1.21. W16 (an everywhere unramified Hecke character of $E$ with prescribed infinity type restricting to $\eta$) is a fidelity item in its own right: its existence is not a quoted theorem but a consequence of class field theory under the host condition that $E/F$ is unramified at every finite place, and Wave 4 checked only that the host record forces this. Root exchange (V19 first half) is internal and closed, so it is no longer a boundary item.

### 1.10 PC-5 further inputs

Louboutin's residue bound (**PARTIAL**, "archive form follows", Wave B), Grayson–Stuhler canonical filtrations, Borel–Harish-Chandra reduction theory, Siegel's volume of $GL_j$, Harish-Chandra and Schmid on discrete series (V14 `CoefWeightedLoc` included), Green's parametrization: all **SOURCE NOT YET LOCATED**.

### 1.11 Sources once on the route and now shown not to be live

| Source | Former role | Why not live | Status |
|---|---|---|---|
| V17: explicit formulae, `ZeroCount`, `ZFRDirichlet`, `TZRat`, Page's theorem, Jutila's zero density, `QuadraticHeckeZeroEstimates` | inputs of `hostEx_of_zeroFreeRegion` | Wave 6: `hostEx_of_zeroFreeRegion` is off route, its reverse closure has four declarations; `LogDerOne` is live but discharged internally (`LogDerOneProof.logDerOne_holds`). Consumers `explicit_formula_used`, `zeroCount_holds`, `zFRDirichlet`, `ZeroFreeHalf.main` are UNDECIDED | **WRONG SOURCE** for the live route (move to "not shown operative"; the UNDECIDED consumers must be settled before deletion) |
| Katz, *p-adic interpolation of real analytic Eisenstein series* (1978) | expected source for CM-period integrality | Wave 6: `JoinOut` uses Siegel–Klingen, Deligne–Ribet, Hecke's functional equation, $K(j(\mathcal O_K))$ and Shimura's main theorem of CM, not Katz | **WRONG SOURCE** |
| Schmidt (1968), Siegel (1945) | FR-12(a) mean counts | §1.5 above | **WRONG SOURCE** |
| Katz (1970), Oda (1969) | PC-2 input D | §1.3 above | **WRONG SOURCE** |
| Raynaud (1974) | boundary listed it as "not an input" | now matched in content to the archive's internal Frobenius layer, so it is the published statement at which PC-1 stops (Layer 3) | reclassify from "not an input" to a Layer-3 stopping point (**PARTIAL**, §1.2) |
| Faltings–Chai, Lan (for Lemma 8.7) | nefness at $p\notin S_B$ | §1.3 | **WRONG SOURCE** |

### 1.12 PC-6 inputs (status at Wave 6)

| Input | Used by | Source | Status |
|---|---|---|---|
| Siegel–Klingen rationality; Deligne–Ribet congruence | `ZetaDenom.zetaDenominators` (`JoinOut`) | Siegel (1970), Klingen (1962); Deligne–Ribet, Invent. Math. 59 (1980) | **SOURCE NOT YET LOCATED** (theorem numbers); $\nu_\ell$ sum bound checked numerically by Wave 6 |
| Shimura's main theorem of CM; Hilbert class field via $j$ | `TwistedTransport`, `Transport` | Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions* (1971), Thm. 5.4 | **PARTIAL** (theorem number recorded by Wave 6; Masser's quasi-period identity tested to 400 digits) |
| Hecke functional equation of partial zeta and Hecke $L$ | `Refl` | Hecke; Tate's thesis | **SOURCE NOT YET LOCATED** |
| V18, `psi_thin` | `QH.thinH` (live) | Davenport, ch. 14, 17, 19, 20 (from memory) | **SOURCE NOT YET LOCATED** |
| `RayField` | live argument of `rowFun_at_gridA_alt`, `geometricWeakTies_of_linked_ties` | class field theory | **SOURCE NOT YET LOCATED** |
| PEL uniformization and level covers (candidate) | `allSixLaws` below `exists_lift_marked` (PC-7) | Shimura; Deligne (1971); Kottwitz, J. AMS 5 (1992) §5; Lan (2013) ch. 1 | **SOURCE NOT YET LOCATED** (candidate only) |

## 2. Summary counts

| Status | Count (rows above, deduplicated) |
|---|---|
| VERIFIED | 0 |
| PARTIAL | 15 (Fargues; Raynaud; SGA 3 VII$_A$; SGA 7 VII with Mumford; Tamagawa; strong approximation; Siegel–Weil convergent; V5; Zhang; Chowla–Selberg; V8; Mathlib Weierstrass division; W13; Louboutin; Shimura's main theorem of CM) |
| WRONG SOURCE or not live | 9 (Katz 1970, Oda 1969, Goldring–Koskivirta, Faltings–Chai/Lan for Lemma 8.7, Schmidt 1968, Siegel 1945, Katz 1978, V17 group, and Raynaud's old "not an input" label) |
| SOURCE NOT YET LOCATED | all remaining rows, including all of W1 to W12, W14, W15, the PC-3 Fontaine and Herr inputs, and the PC-5 representation-theoretic inputs |

## 3. What to do next, in order

1. Fargues at $p=2$: confirm no route use of `FarguesHodgeTate` at $p=2$, or find a source. Add the saturation step for clause (ii) to the PC-1 human proof.
2. Open Prasad 3.7 and the Lean definition of `locFactor`; compare term by term.
3. Strong approximation: open the three Lean statements and check that the set $S$ contains a place where $SU$ is isotropic in each use, then trace `StrongApproxSU` in FR-12 (left open by PC-5).
4. Zhang: decide whether the nef case is a published statement (Zhang JAMS 1995 Thm 1.10 is for ample $L$) or needs the limiting argument written.
5. The Siegel–Weil pair V5, V6 and the Rallis inputs, which carry the records and the counting engine.
6. Then the remaining SOURCE NOT YET LOCATED rows, by specialist area.
