# R-1 replacement ledger entries (Siegel–Weil, Weil's convergent range)

Source report: `SiegelWeil_R1_Report.tex` / `.pdf` (this folder), 22 Nov 2026.
Inputs: `lean.tar.gz` sha256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc` (matches Kernel Replay), `Final_External_Fidelity`, Final Six Wave 4 and 6, Final Internal Cleanup.
No project file was edited. These rows replace the rows named below when the next synthesis consolidates the ledger.

## 1. Replacement for the SW-D row of `Authoritative_External_Theorem_Ledger.md` (§1)

| id | Lean name and liveness | exact statement used | source | theorem number | verdict | bridge | status |
|---|---|---|---|---|---|---|---|
| SW-D | `GlobalTheory.Published.SiegelWeilUnitaryConvergent` (doubled form), live on `miStar2_of_allTrue_alt_alt` → `ontoAll_of_hecke_alt` → `heckeForm_of_doubling'` → `globalForm_of_siegelWeil'` → `siegelWeil_fockDoubledPair_of_weil_and_ichino` (= `Core.Rk.IP.siegelWeilAll_of_hypotheses`, which uses it exactly for n < m ≤ 2n with n + r < m). **Discharged inside the archive**: `siegel_weil_unitary_convergent_of_literature O := UpperTheory.Lit.Sw47.convergent` (ignores `O`) `:= sw_doubled_of_std PositivityTheory.SiegelWeilCoefficients.field`; `field : SiegelWeilUnitarySchrodinger` is a closed theorem (Kudla–Rallis-type Fourier-coefficient proof, not read here) | SW-S: for U(n,n) × U(V), E/F CM, dim V = m, n < m ≤ 2n, n + r(V) < m, ψ nontrivial on 𝔸_F/F, χ Hecke with χ\|𝔸_F^× = η^m, φ Fock-polynomial at ∞ (any Cartan involution of V) and Schwartz–Bruhat at finite places, f_φ(g,s) = \|a(g)\|^{s−s₀} ω(g)φ(0), s₀ = (m−n)/2: θ(g,·,φ) integrable on [U(V)]; E(g,s,φ) absolutely convergent and P(F)-invariant section for Re s > n/2; continuation holomorphic at s₀ with E(g,s₀,φ) = ⨍_{[U(V)]} θ(g,h,φ) dh (probability measure, κ = 1). SW-D (live) is SW-S transported to U(W ⊕ −W) | S. Yamana, *The Siegel–Weil formula for unitary groups*, Pacific J. Math. 264 (2013) 235–256, doi:10.2140/pjm.2013.264.235 (opened, MSP PDF); original for δ = 1: A. Ichino, *On the Siegel–Weil formula for unitary groups*, Math. Z. 255 (2007) 721–729, doi:10.1007/s00209-006-0045-8 (not opened, paywall) | Yamana **Theorem 2**, case δ = 1, m − r > n, κ = 1 (pp. 236–237; proof of this case §4, p. 247). Ichino **Theorem 1.1** (number from C. Li, IHES notes, Thm. 2.3.1; not checked against print) | **MATCH AFTER EXPLICIT BRIDGE** | B-SW.1 Cartan involution (U(V)(ℝ)-conjugacy, proved); B-SW.2 `HolValueAt` = holomorphic value of the meromorphic continuation (proved); B-SW.3 κ·vol([H],dh) = 1 is forced (positivity argument, proved) and Yamana's implicit dh is the probability measure (pinned by Li's Tamagawa normalization κ = ½, τ(U(V)) = 2, and Xiong's vol = 1 normalization); B-SW.4 side clauses from Weil 1965 n° 51 Prop. 8 and Godement; B-SW.5 doubled → Schrödinger (= `sw_doubled_of_std`, assembly read in full, seven classical steps, sub-lemma proofs not read) | **Closed.** Bibliographic residue only: Ichino's Thm 1.1 and Weil's Prop. 8 numbers are via secondary citation |

## 2. Replacement for the R-1 row of §2 ("Smallest unresolved external residual list")

| id | statement | status | what closes it |
|---|---|---|---|
| R-1 | Siegel–Weil in Weil's convergent range for U(n,n) × U(V), n < m ≤ 2n, n + r(V) < m, Fock-polynomial φ, value at s₀ = (m−n)/2, probability measure, κ = 1 | **CLOSED (MATCH AFTER EXPLICIT BRIDGE)**: Yamana, Pacific J. Math. 264 (2013), Theorem 2, δ = 1 (statement inspected), crediting Ichino, Math. Z. 255 (2007), Theorem 1.1; bridges B-SW.1–B-SW.5 in `Pre_Synthesis_Audit/SiegelWeil_R1/`. The archive also proves the Schrödinger form internally (`SiegelWeilCoefficients.field`) | nothing mathematical. Optional bibliographic check: open Ichino 2007 and confirm Theorem 1.1's wording and measure; open Weil 1965 n° 51 |

Delete R-1 from the list of live unresolved external residuals. Answer F of the ledger should then cite R-2 and R-3 as the remaining reasons for NO.

## 3. Replacements for `Corrected_Source_Map.md`

| claim | cite | status |
|---|---|---|
| Siegel–Weil, Weil's convergent range, n < m ≤ 2n, n + r < m | S. Yamana, *The Siegel–Weil formula for unitary groups*, Pacific J. Math. 264 (2013), 235–256, Theorem 2 (case δ = 1); A. Ichino, *On the Siegel–Weil formula for unitary groups*, Math. Z. 255 (2007), 721–729, Theorem 1.1 | **verified** (Yamana statement inspected; Ichino number via Li's notes) |
| Siegel–Weil, m > 2n | A. Weil, Acta Math. 113 (1965), 1–87 (Théorème 5 per Li's notes) | as before |
| Convergence of the theta integral for r = 0 or m − r > n | A. Weil, Acta Math. 113 (1965), n° 51, Prop. 8, p. 75 (as cited by Xiong, arXiv:1806.02049, Prop. 5.1) | number via secondary citation |

Withdraw the line in the "not the source" table that lists Yamana, Pacific J. Math. 264 (2013) as "skew-field case, not Weil's convergent range for d = 1". Yamana's Theorem 2 is stated for every δ ≥ 1, including δ = 1, and covers m − r > n.

## 4. Smallest missing theorem

None. R-1 needs no further mathematical input.
