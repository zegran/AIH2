# Submission package — MANIFEST (updated 2026-06-18 post-remediation)

**Venue:** Energy and AI (Elsevier). **Dataset DOI:** 10.5281/zenodo.20751918 (CC-BY-4.0).

**Status legend:** DONE · PENDING-USER

**Canonical sources:**
- Dataset: `data/curated/aih2_v1.csv` (315 rows, TC={isothermal_bath, self_heating}, 0 uncontrolled)
- Figures: `results/real_v1/figures/` (generated 2026-06-18 from corrected dataset)
- Manuscript LaTeX: `paper/` (main.tex + sections/ + references.bib)
- PDF: CI artifact — GitHub Actions → Build paper PDF → `main-pdf`
- Dataset bundle: `release/zenodo_v1/` → synced to `submission_package/zenodo/`

---

## submission_package/manuscript/  →  JOURNAL (Energy and AI Editorial Manager)

| File | Tag | Status | Note |
|---|---|---|---|
| `main.tex` | JOURNAL | DONE | LaTeX source; `\journal{Energy and AI}`, elsarticle 12pt preprint |
| `sections/introduction.tex` | JOURNAL | DONE | ~650 w; corrected numbers (72%/43%/8%) |
| `sections/related_work.tex` | JOURNAL | DONE | ~750 w |
| `sections/method.tex` | JOURNAL | DONE | ~1,150 w; Tables 1+2; IRR paragraph; 5-procedure QC |
| `sections/results.tex` | JOURNAL | DONE | R²=0.717/0.425/0.081; §3.7 robustness sensitivities |
| `sections/discussion.tex` | JOURNAL | DONE | tab:mireport updated (apparatus first, R²=0.43/0.08) |
| `sections/conclusion.tex` | JOURNAL | DONE | DOI 10.5281/zenodo.20751918 in Data Availability |
| `sections/supplementary.tex` | JOURNAL | DONE | Tables SI-1 (31-study list), SI-2 (perm. importance) |
| `references.bib` | JOURNAL | DONE | 58 entries; Crossref-fetched |
| `figures/fig1_optimism_gap.pdf` | JOURNAL | DONE | Vector; Jun 18 corrected ✅ |
| `figures/fig2_variance_decomposition.pdf` | JOURNAL | DONE | **Vector; Jun 18 corrected (39836 B) ✅** |
| `figures/fig3_particle_size_consistency.pdf` | JOURNAL | DONE | Vector; Jun 18 ✅ |
| `figures/fig4_ea_spread.pdf` | JOURNAL | DONE | Vector; Jun 18 ✅ |
| `figures/fig5_dataset_composition.pdf` | JOURNAL | DONE | Vector; Jun 18 ✅ |
| `figures/fig6_within_study_surface.pdf` | JOURNAL | DONE | Vector; Jun 18 ✅ |
| `figures/fig*.png` | JOURNAL | DONE | 300 dpi raster previews (6 files) |
| `main_review.docx` | JOURNAL | DONE | Pandoc cited DOCX (294 KB); rebuilt 2026-06-18 22:10 on corrected fig2 |
| `main.pdf` | JOURNAL | **PENDING-USER** | Download from CI: GitHub Actions → "Build paper PDF" → artifact `main-pdf` |

---

## submission_package/paperwork/  →  JOURNAL (submission forms)

| File | Tag | Status | Note |
|---|---|---|---|
| `cover_letter.md` | JOURNAL | DONE | Energy and AI; GitHub link removed; 72%/43%/8% numbers |
| `highlights.md` | JOURNAL | DONE | 5 bullets; ≤85 chars (math inflation warns but not hard error) |
| `suggested_reviewers.md` | JOURNAL | **PENDING-USER** | Confirm candidates + COI before submit |
| `ai_disclosure.md` | JOURNAL | **PENDING-USER** | Confirm AI disclosure wording |
| `COMPLIANCE_REPORT.md` | JOURNAL | DONE | All Energy and AI checks PASS |
| `energy_and_ai_checklist.md` | JOURNAL | DONE | Pre-submission checklist; venue locked |
| `highlights.txt` | JOURNAL | DONE | Plain-text copy |

---

## submission_package/zenodo/  →  ZENODO upload (already deposited as DOI 10.5281/zenodo.20751918)

Verified: 0 uncontrolled TC rows; TC={isothermal_bath, self_heating}; CITATION.cff has real DOI.

| File | Tag | Status | Note |
|---|---|---|---|
| `aih2_v1.csv` | ZENODO | DONE | 315 rows; corrected (Trowell+Martínez-Vargas TC; Porciuncula MM) |
| `rate_extraction.csv` | ZENODO | DONE | 76 kinetic rows |
| `data_dictionary.md` | ZENODO | DONE | Corrected TC/MM levels; no uncontrolled |
| `README.md` | ZENODO | DONE | IRR correction history; no GitHub link |
| `LICENSE_CC-BY-4.0.txt` | ZENODO | DONE | |
| `CITATION.cff` | ZENODO | DONE | doi: 10.5281/zenodo.20751918 ✅ |
| `aih2_dataset_v1.zip` | ZENODO | DONE | Bundle of the 6 files above |

---

## submission_package/upload_ready/  →  EM UPLOAD (Editorial Manager)

| File | Tag | Status | Note |
|---|---|---|---|
| `graphical_abstract.pdf` | JOURNAL | DONE | 3.35×3.35 in; shows R² bars for 0.717/0.425/0.081/0.018 |
| `graphical_abstract.png` | JOURNAL | DONE | 300 dpi PNG version |
| `declaration_of_interest.md` | JOURNAL | DONE | Standalone DOI form; "no competing interests" |

---

## Open user gates (3 remaining)

| # | Gate | Status |
|---|---|---|
| 1 | Download main.pdf from CI | PENDING-USER — GitHub Actions → "Build paper PDF" → `main-pdf` artifact |
| 2 | Confirm AI-disclosure wording (`% AUTHOR: confirm` in conclusion.tex) | PENDING-USER |
| 3 | Confirm suggested reviewers + COI, then submit to Energy and AI | PENDING-USER |

---

## Deleted (stale/superseded — removed 2026-06-18)

| Deleted path | Reason |
|---|---|
| `submission_package/dataset/` | Pre-correction data (TC=uncontrolled present); replaced by `zenodo/` |
| `submission_package/zenodo/ZENODO_METADATA.md` | Written for deleted record 10.5281/zenodo.20750297 |
| `submission_package/zenodo/ZENODO_STEPS.md` | Same |
| `release/aih2_dataset_v1/` | Pre-correction bundle; replaced by `release/zenodo_v1/` |
| `release/aih2_dataset_v1.zip` | Same |
| `release/ZENODO_METADATA.md` | Orphaned from deleted record |
| `release/ZENODO_PREVIEW.md` | Same |
| `paper/preview/` | Stale pandoc snapshot (GitHub link, old DOI, pre-correction figs) |
| `temp/` | IRR task JSONs, figure test crops, scratch scripts |
