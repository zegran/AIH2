# Submission package — MANIFEST (assembled 2026-06-17)

Assembled per `data/wp1/CLI_ASSEMBLE_UPLOAD_PACKAGE.md`.
**Venue:** Energy and AI (Elsevier). **Dataset:** Zenodo (CC-BY-4.0).

**Status legend:** DONE · PENDING-USER · OBSOLETE

---

## submission_package/manuscript/  →  JOURNAL (Energy and AI Editorial Manager)

| File | Tag | Status | Note |
|---|---|---|---|
| `main.tex` | JOURNAL | DONE | LaTeX source; `\journal{Energy and AI}`, elsarticle 12pt preprint |
| `sections/introduction.tex` | JOURNAL | DONE | ~650 w |
| `sections/related_work.tex` | JOURNAL | DONE | ~750 w; `\label{sec:related}` |
| `sections/method.tex` | JOURNAL | DONE | ~1,150 w; Tables 1+2; pre-registration language fixed (commit 1ce67e3) |
| `sections/results.tex` | JOURNAL | DONE | ~1,600 w; Tables 3+4; TEST 1 negative control |
| `sections/discussion.tex` | JOURNAL | DONE | ~1,000 w; 5 named-study limits |
| `sections/conclusion.tex` | JOURNAL | DONE | Declarations: COI, CRediT, gen-AI, data avail, acknowledgements |
| `sections/supplementary.tex` | JOURNAL | DONE | Tables SI-1 (31-study list), SI-2 (perm. importance) |
| `references.bib` | JOURNAL | DONE | 58 entries; 31 Tier-A + 12 Tier-B; Crossref-fetched |
| `figures/fig1_optimism_gap.pdf` | JOURNAL | DONE | Vector; optimism gap comparison |
| `figures/fig2_variance_decomposition.pdf` | JOURNAL | DONE | Vector; R² variance bars |
| `figures/fig3_particle_size_consistency.pdf` | JOURNAL | DONE | Vector; particle-size slopes |
| `figures/fig4_ea_spread.pdf` | JOURNAL | DONE | Vector; Eₐ by regime |
| `figures/fig5_dataset_composition.pdf` | JOURNAL | DONE | Vector; dataset composition |
| `figures/fig6_within_study_surface.pdf` | JOURNAL | DONE | Vector; within-study surface |
| `figures/fig*.png` | JOURNAL | DONE | 300 dpi raster previews (6 files); for DOCX/Word review |
| `main.docx` | JOURNAL | DONE | Pandoc preview (271 KB); review/track-changes copy; PDF is authoritative |
| `main.pdf` | JOURNAL | **PENDING-USER** | Download from CI: https://github.com/zegran/AIH2/actions → "Build paper PDF" → artifact `main-pdf` (latest green run, commit 1ce67e3) |

> **Note on main.pdf:** `gh` CLI not installed; see `DOWNLOAD_PDF_FROM_CI.txt` in this folder for
> the exact click-path. The DOCX is a convenience preview (pandoc, raster figures, author-year
> citations). The PDF (elsarticle + latexmk, vector figures, numeric citations) is the submission copy.

---

## submission_package/paperwork/  →  JOURNAL (submission forms)

| File | Tag | Status | Note |
|---|---|---|---|
| `cover_letter.md` | JOURNAL | DONE | Date = submission date |
| `highlights.md` | JOURNAL | DONE | 5 bullets, ≤85 chars; Energy and AI format |
| `suggested_reviewers.md` | JOURNAL | **PENDING-USER** | Template; confirm candidates + COI before submit |
| `ai_disclosure.md` | JOURNAL | **PENDING-USER** | Draft wording; confirm accuracy (`% AUTHOR: confirm` in conclusion.tex) |
| `COMPLIANCE_REPORT.md` | JOURNAL | DONE | All 12 Energy and AI checks PASS |
| `energy_and_ai_checklist.md` | JOURNAL | DONE | Full pre-submission checklist; 5 open user gates listed |
| `highlights.txt` | JOURNAL | DONE | Legacy copy; `highlights.md` is canonical |
| `IJHE_checklist.md` | — | OBSOLETE | Former IJHE venue; superseded by `energy_and_ai_checklist.md` |

---

## submission_package/zenodo/  →  ZENODO ONLY (no manuscript, no internal files)

Verified: no manuscript or internal/command-history files in this subfolder.

| File | Tag | Status | Note |
|---|---|---|---|
| `aih2_v1.csv` | ZENODO | DONE | 315 yield rows, 30 columns, provenance-tracked |
| `rate_extraction.csv` | ZENODO | DONE | 76 kinetic rows; Eₐ, rate constants, t80 |
| `data_dictionary.md` | ZENODO | DONE | Column definitions and units |
| `README.md` | ZENODO | DONE | Dataset overview; usage; license |
| `LICENSE_CC-BY-4.0.txt` | ZENODO | DONE | CC-BY-4.0 full text |
| `CITATION.cff` | ZENODO | DONE | Machine-readable citation; **update `doi:` after deposit** |
| `ZENODO_METADATA.md` | ZENODO | DONE | Copy-paste title/description/creators/keywords for Zenodo form |
| `ZENODO_STEPS.md` | ZENODO | DONE | Click-path: login → New Upload → fill form → Publish → update manuscript |
| `aih2_dataset_v1.zip` | ZENODO | DONE | One-shot upload bundle (all dataset files) |
| Zenodo DOI | ZENODO | **PENDING-USER** | Minted after deposit; replace `\todo{Zenodo DOI}` in `conclusion.tex` line 17 + `CITATION.cff` |

---

## dataset/ (legacy)

`submission_package/dataset/` contains the same dataset files as `zenodo/` but without the
Zenodo-specific metadata (`ZENODO_METADATA.md`, `ZENODO_STEPS.md`). It is kept for backward
compatibility. Use `zenodo/` as the canonical Zenodo upload source.

---

## Open user gates (consolidated — 5 items)

| # | Gate | Where | Status |
|---|---|---|---|
| 1 | Download main.pdf from CI (commit 1ce67e3) | Actions → main-pdf artifact → `manuscript/main.pdf` | PENDING-USER |
| 2 | Zenodo deposit → insert DOI into `conclusion.tex` + `CITATION.cff` | ZENODO_STEPS.md | PENDING-USER |
| 3 | Confirm AI-disclosure wording | `conclusion.tex` (`% AUTHOR: confirm`) | PENDING-USER |
| 4 | Confirm suggested reviewers + COI | `paperwork/suggested_reviewers.md` | PENDING-USER |
| 5 | Final venue sign-off + submit | Elsevier Editorial Manager → Energy and AI | PENDING-USER |

All manuscript content, citations, compliance, and tooling are submission-ready pending the above.
