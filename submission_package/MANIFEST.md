# Submission package — MANIFEST (post-remediation, 2026-06-17)

All manuscript content, citations, compliance, and tooling are submission-ready pending user
gates (Zenodo deposit, AI-disclosure confirmation, reviewer list, venue sign-off).

**Status legend:** DONE · PENDING-USER

---

## Manuscript — sources (canonical in `paper/`)

| Asset | Path | Status | Note |
|---|---|---|---|
| Main LaTeX | `paper/main.tex` | DONE | `\journal{Energy and AI}`, elsarticle preprint 12pt |
| Introduction | `paper/sections/introduction.tex` | DONE | ~650 w; 6 contribution bullets |
| Related work | `paper/sections/related_work.tex` | DONE | ~750 w; regime-organized; `\label{sec:related}` |
| Data and methods | `paper/sections/method.tex` | DONE | ~1,150 w; Tables 1+2; leakage-controlled eval |
| Results | `paper/sections/results.tex` | DONE | ~1,600 w; Tables 3+4; TEST 1 negative control |
| Discussion | `paper/sections/discussion.tex` | DONE | ~1,000 w; named studies; 5 limitation paragraphs |
| Conclusion | `paper/sections/conclusion.tex` | DONE | Acknowledgements, COI, CRediT, gen-AI, data avail |
| Supplementary | `paper/sections/supplementary.tex` | DONE | Tables SI-1 (31-study list), SI-2 (perm. importance) |
| Bibliography | `paper/references.bib` | DONE | 58 entries; 31 Tier-A + 12 Tier-B; Crossref-fetched |
| Figures (vector) | `paper/figures/fig1-fig6.pdf` | DONE | 6 figures, all referenced |

## Manuscript — build

| Asset | Path | Status | Note |
|---|---|---|---|
| CI workflow | `.github/workflows/latex.yml` | DONE | lint -> compliance -> LaTeX compile |
| Structural lint | `tools/lint_paper.py` | DONE | integrates citation_coverage --check |
| Compliance gate | `tools/compliance_gate.py` | DONE | 12 Energy and AI checks; PASS |
| Citation coverage | `tools/citation_coverage.py` | DONE | 31/31 data-source studies cited |
| PDF (authoritative) | — | PENDING-USER | CI build on push; download from Actions artifacts |

## Paperwork (in `paper/submission/`)

| Asset | Status | Note |
|---|---|---|
| `COMPLIANCE_REPORT.md` | DONE | all checks PASS; see outstanding warnings |
| `highlights.txt` | DONE | 5 bullets aligned with main.tex Energy and AI frame |
| `cover_letter.md` | DONE (draft) | date = submission date |
| `suggested_reviewers.md` | PENDING-USER | template; user confirms candidates + COI |
| `ai_disclosure.md` | PENDING-USER | wording in conclusion.tex; author to confirm |
| `IJHE_checklist.md` | OBSOLETE | venue changed to Energy and AI; see COMPLIANCE_REPORT |

## Dataset (Zenodo bundle — `submission_package/dataset/`)

| Asset | Status |
|---|---|
| `aih2_v1.csv` (315 yield rows) | DONE |
| `rate_extraction.csv` (76 kinetic rows) | DONE |
| `data_dictionary.md`, `README.md`, `CITATION.cff` | DONE |
| `LICENSE_CC-BY-4.0.txt`, `aih2_dataset_v1.zip` | DONE |
| Deposit metadata: `release/ZENODO_METADATA.md`, `.zenodo.json` | DONE |
| Zenodo DOI | PENDING-USER — user deposits, then: replace `\todo{Zenodo DOI}` in `conclusion.tex` line 17 and update `CITATION.cff` |

## Tools / gates summary

| Tool | Path | Gate result |
|---|---|---|
| Structural lint + coverage | `tools/lint_paper.py` | PASS (lint clean, 31/31 cited) |
| Energy and AI compliance | `tools/compliance_gate.py` | PASS (12/12 checks) |
| Citation coverage | `tools/citation_coverage.py --check` | PASS (MISSING: 0) |

## Outstanding user gates (consolidated)

1. **Push to GitHub** → CI triggers → confirm PDF builds green (Actions tab).
2. **Zenodo deposit** → insert DOI into `conclusion.tex` + `CITATION.cff`.
3. **Confirm AI-disclosure wording** in `conclusion.tex` (`% AUTHOR: confirm` comment).
4. **Confirm suggested reviewers** + COI check (`paper/submission/suggested_reviewers.md`).
5. **Final venue sign-off** (Energy and AI) + submit via Elsevier Editorial Manager.
