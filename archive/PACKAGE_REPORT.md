# Packaging report

Prepared 21 November 2026. This report records how `GitHub_Public_Package/` was assembled from the project folder. No file of the project outside `GitHub_Public_Package/` was edited, moved or deleted. No Lean source was opened for editing, built or run. No mathematical content was changed or added.

## 1. Files included

| Path | Origin | Size |
|---|---|---|
| `README.md` | written for the package | |
| `RH_Route_Notes.tex` | copied unchanged from the project root | 317 KB |
| `RH_Route_Notes.pdf` | copied unchanged from the project root (66 pages) | 753 KB |
| `references.bib` | written for the package, a field-by-field transcription of the manuscript's 43 `\bibitem` entries | |
| `PROOF_DEPENDENCY_MAP.md` | written for the package | |
| `RECONSTRUCTION_STATUS.md` | written for the package | |
| `EXTERNAL_THEOREMS.md` | written for the package | |
| `SOURCE_MANIFEST.md` | written for the package | |
| `CITATION.cff` | written for the package, validated against CFF schema 1.2.0 | |
| `LICENSE` | placeholder (Section 5) | |
| `.gitignore` | written for the package | |
| `PACKAGE_REPORT.md` | this file | |
| `audit/README.md` | written for the package | |
| `audit/Post_Closure_Synthesis.pdf` | copied unchanged | 495 KB |
| `audit/Post_Closure_Internal_Residuals.md` | copied unchanged | 29 KB |
| `audit/Post_Closure_Verification_Boundary.md` | copied unchanged | 31 KB |
| `audit/selected_reports/` | ten report PDFs, copied unchanged and renamed (table below) | 4.6 MB |

Total size about 6 MB in 26 files.

### Selected reports and their original names

| Package name | Original file in `Claude_Audit_Core/` | Reason |
|---|---|---|
| `01_Gain_Valuation_Mechanism.pdf` | `Core_Report_4_Valuation.pdf` | local valuation and gain mechanism |
| `02_Loss_LPprime.pdf` | `Final_A_LPprime/Final_A_LPprime.pdf` | Hecke loss, `LPprime` |
| `03_DeepStR_Mean_Slope_Bound.pdf` | `Focused_Final_Wave_1/Focused_Final_Wave_1.pdf` | `DeepStR` |
| `04_DeepStR_Exact_Identity_at_Good_Primes.pdf` | `Final_Closure_Wave_1/Final_Closure_Wave_1.pdf` | exact identity at good primes, location of PC-1 and PC-2 |
| `05_Theorem_P_and_PuNZ_Order.pdf` | `Focused_Final_Wave_2/Focused_Final_Wave_2.pdf` | Theorem P, and the correction of the `PuNZ` order |
| `06_P3core.pdf` | `Final_5_P3core/Final_5_P3core.pdf` | `P3core` |
| `07_Theorem_B_Interior.pdf` | `Final_Closure_Wave_2/Final_Closure_Wave_2.pdf` | Theorem B |
| `08_Theorem_C_Interior.pdf` | `Final_Closure_Wave_3/Final_Closure_Wave_3.pdf` | Theorem C |
| `09_Seesaw_FR10_FR12.pdf` | `Final_Closure_Wave_4/Final_Closure_Wave_4.pdf` | seesaw, FR-10, FR-12 |
| `10_Final_Authoritative_Synthesis.pdf` | `Final_Authoritative_Synthesis/Final_Authoritative_Synthesis.pdf` | previous authoritative synthesis and its dependency corrections |

Each of these PDFs was checked to be at least as new as its `.tex` source.

## 2. Files intentionally excluded

| Excluded | Reason |
|---|---|
| `lean.tar.gz` and `lean.tar.gz.part01` to `part14` (about 480 MB together), and the extracted `src/lean/` (175,190 files, 1.4 GB) | The formal archive belongs to its authors and is identified by hash in `SOURCE_MANIFEST.md`. Redistributing it is not needed to inspect the reconstruction |
| `Claude_Kernel_Replay/` | Its findings are recorded in `SOURCE_MANIFEST.md`. The report names a machine-specific project path, and the per-file hash list `Source_Manifest_sha256.txt` is about 30 MB (its hash is recorded) |
| `RH_Route_Notes_backup_before_manuscript.*`, `RH_Readers_Guide.*`, `RH_Piece2_Windows.*`, and the backups in `Claude_Audit_Core/` (`RH_Route_Notes_before_*`) | superseded versions of the manuscript |
| `HANDOFF_Next_Agent.md`, `Claude_Audit_Core/HANDOFF_*.md`, `Report8_Working_Notes.md` | internal working instructions for agents |
| `Claude_Audit_Core/Manuscript_End_to_End_Reconciliation.md`, `Manuscript_Reconciliation_2026-11-21.md` | internal edit logs of the manuscript, written to the author |
| All other reports, wave reports and dependency maps in `Claude_Audit_Core/` (Core Reports 1–3 and 5–9, Parallel A–F, Final Waves A–F, Final 1–6, Focused Waves 3–5, Final Closure Wave 5, the FR reports, Final Synthesis, Final Closing Synthesis, `Final_Residual_Dependency_Map.md`, `Full_Reconstruction_Dependency_Map.md`) | superseded by the post-closure synthesis, or historical detail beyond the minimum provenance set |
| `Claude_Audit_Core/Post_Closure_Synthesis/Post_Closure_Synthesis.tex` | the PDF is included as requested; the source is a working document |
| `GPT_Tier2_R3_Audit/`, `Claude_Crosscheck_GPT_Audit/`, `Claude_Core_Reconciliation_After_Report4/7/8/9/` | intermediate cross-check and reconciliation records |
| `_to_delete/`, `untitled folder`, `untitled folder.zip`, `.DS_Store`, `*.aux`, `*.log`, `*.out`, `build.log` | scratch and build files |

## 3. Compilation

**The manuscript compiles self-contained from inside the package.**

- A copy of `GitHub_Public_Package/RH_Route_Notes.tex`, alone in an empty directory, was compiled with three passes of `pdflatex` (TeX Live 2023).
- All three passes exited 0. The log has no errors, no undefined references or citations, and no overfull boxes. The result has 66 pages.
- The extracted text of the result is identical to that of the included `RH_Route_Notes.pdf` (same MD5 of `pdftotext` output), so the included PDF corresponds to the included source.
- The manuscript uses an inline `thebibliography`, inline pgfplots coordinates, and no external figures, style files or data files. No packaging-level fix was needed.
- Required TeX packages are standard (`newtx`, TeX Gyre fonts, `pgfplots`, `natbib`, `fancyhdr`, `booktabs`, `longtable`, `hyperref`, `microtype`, `caption`). The Linux sandbox on the author's machine lacks `newtxtext.sty`, so the check was run in the cloud workspace after installing the Ubuntu packages `texlive-fonts-extra`, `texlive-plain-generic` and `tex-gyre`. The author's own workflow (Overleaf) has these packages.
- The recompiled PDF was not substituted for the included one.

## 4. Release metadata still missing

1. **Canonical public URL of the Lean archive.** The project records the tarball and its SHA-256 but not where it was downloaded from. `SOURCE_MANIFEST.md` says "exact source revision to be inserted before release" at that line.
2. **License.** See Section 5.
3. **Repository URL.** `CITATION.cff` has no `repository-code` or `url` field, because the GitHub repository does not exist yet. Add it after creating the repository.
4. **Optional.** An ORCID for the author in `CITATION.cff`. No DOI or arXiv identifier exists for the manuscript, so none was added.

## 5. Licensing

No license file exists anywhere in the project. `LICENSE` is a placeholder that says **LICENSE TO BE SELECTED BEFORE PUBLIC RELEASE**. The author should choose a license for the manuscript and documentation, and confirm the terms on which the audit report PDFs (working reports prepared by Claude for the author) are distributed. No license was imposed.

## 6. Source revision and hash

- **Found.** SHA-256 of the released tarball, `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`, recomputed during packaging and equal to the value recorded by the kernel-replay attempt of 20 November 2026. The SHA-256 of the per-file manifest, the Lean toolchain, and full revisions of Mathlib and all eight transitive dependencies are recorded.
- **Not applicable.** A Git commit or tag of the archive. It was released as a tarball, not a repository.
- **Not found.** The canonical download URL (Section 4, item 1).

## 7. Machine-specific paths

None remain. A search of every text file in the package for `/Users/`, `Documents/`, the user name, `/sessions/`, `/mnt/` and `/home/` found no match, and the same search over the extracted text of every included PDF found no match. The paths that remain in the audit files (`src/lean/src/…`, `GP/…`, `LLC/…`) refer to the directory layout of the archive and are explained in `audit/README.md`.

## 8. Consistency with the post-closure synthesis

- `README.md`, `RECONSTRUCTION_STATUS.md` and `PROOF_DEPENDENCY_MAP.md` state the status as the post-closure synthesis and Section 1.3 of the manuscript do. Architecture end to end, every major mechanism reconstructed, seven internal packages PC-1 to PC-7 with five small-leaf groups, no gap found, two open constant checks, literature verification separate, no claim of independent verification, and no claim that RH is proved.
- The package list, earliest blockers, mechanisms, sizes and risks in `RECONSTRUCTION_STATUS.md` follow `Post_Closure_Internal_Residuals.md` and the package table in Section 8 of `Post_Closure_Synthesis.pdf`. The remaining packages are called remaining internal audit packages, never gaps.
- The dependency order `LinkS → PuNZ → MIstar2 → BesselId → LinkDIV, FrameF` appears in `PROOF_DEPENDENCY_MAP.md` as in the synthesis and in §1.2 of the manuscript.
- `EXTERNAL_THEOREMS.md` carries V1 to V20 and the boundary by branch from `Post_Closure_Verification_Boundary.md`, with the "not inputs" list and the separate campaigns. Entries whose attribution the audit recorded from memory, or whose source was not opened, are marked `source match pending`. Two items requested for the table need comment. Yamana is not named in the verification boundary and is listed as such. Skinner–Wiles is listed as a comparison and not an input, as the boundary says.
- Discharged mechanisms (the gain, `LPprime`, `HSAt`, `DeepStR` above PC-1 and PC-2, `FrameF`, Theorem P, `P3core`, the relay of Theorem B, the lemmas of Theorem C, the seesaw value, the host) are described as reconstructed, not as black boxes.
- One wording choice to note. The synthesis's verdict line reads "reconstruction incomplete; medium internal packages remain". The public documents state the same content in the agreed public form and do not strengthen it.

## 9. Readiness for `git init`

The folder can be initialized, committed and pushed as it stands. It is about 6 MB, every file is under 1 MB, the `.gitignore` keeps the public PDFs tracked, and all relative links resolve. Before pushing, the author should

1. choose and insert a license (`LICENSE`, and optionally a `license` field in `CITATION.cff`);
2. insert the canonical URL of the Lean archive in `SOURCE_MANIFEST.md`, if one exists;
3. add the repository URL to `CITATION.cff` after creating the repository;
4. read `README.md`, especially the attribution section, and confirm it.

**READY AFTER LISTED METADATA FIXES**
