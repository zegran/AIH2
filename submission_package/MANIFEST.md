# Submission package — MANIFEST

Single indexed view of every submission asset. **Design:** the canonical source files live in
`paper/` and `release/` (one source of truth); this folder physically holds the *final, stable*
assets (dataset bundle, paperwork) and **indexes** the manuscript sources/outputs by path, because
those will change in the approved Q1 rewrite. At final submission (post-rewrite) the manuscript build
will be materialized here as a flat upload bundle.

**Status legend:** ✅ final · ✏️ draft (will change in the Q1 rewrite) · ⛔ pending-user.

## Manuscript — sources (canonical in `paper/`)
| asset | path | status | note |
|---|---|---|---|
| Main LaTeX | `paper/main.tex` | ✏️ | elsarticle; author = Dogukan Unal |
| Sections | `paper/sections/{introduction,related_work,method,results,discussion,conclusion}.tex` | ✏️ | to be expanded per `REMEDIATION_PLAN.md` |
| Bibliography | `paper/references.bib` | ✏️ | 18 entries → ~46–58 (Tier-A backfill) |
| Figures (vector) | `paper/figures/fig1–fig6.pdf` | ✅ | wired + referenced; 6 figs |

## Manuscript — build outputs
| asset | path | status | note |
|---|---|---|---|
| PDF (authoritative) | `paper/preview/main.pdf` | ✏️ | green CI build; regenerate after rewrite |
| DOCX (review) | `paper/preview/main.docx` | ✏️ | pandoc convenience preview |
| Markdown (review) | `paper/preview/main.md` | ✏️ | pandoc convenience preview |
| CI build | `.github/workflows/latex.yml` | ✅ | compiles `main.pdf` on push |

## Paperwork (copies here in `paperwork/`)
| asset | status | note |
|---|---|---|
| `paperwork/cover_letter.md` | ✏️ | corresponding author filled; `[DATE]` pending |
| `paperwork/highlights.txt` | ✅ | 5 × ≤85 chars |
| `paperwork/suggested_reviewers.md` | ⛔ | template; user confirms candidates + COI |
| `paperwork/IJHE_checklist.md` | ✏️ | author/CRediT/AI done; funding pending |
| `paperwork/ai_disclosure.md` | ⛔ | author to confirm wording |
| `paperwork/COMPLIANCE_REPORT.md` | ✏️ | flags: abstract ≤150, keywords →6, funding |

## Dataset (Zenodo Route-A bundle — copies here in `dataset/`, FINAL)
| asset | status |
|---|---|
| `dataset/aih2_v1.csv` (315 rows) · `dataset/rate_extraction.csv` (76 rows) | ✅ |
| `dataset/data_dictionary.md` · `dataset/README.md` · `dataset/CITATION.cff` | ✅ |
| `dataset/LICENSE_CC-BY-4.0.txt` (verbatim) · `dataset/aih2_dataset_v1.zip` | ✅ |
| Deposit metadata | `release/ZENODO_METADATA.md`, `.zenodo.json` | ✅ |
| Zenodo DOI | — | ⛔ user deposits → DOI into `conclusion.tex` + `CITATION.cff` |

## Q1 remediation plans (canonical in `paper/`)
| asset | path | status |
|---|---|---|
| Root-cause diagnosis | `paper/DIAGNOSIS.md` | ✅ |
| Citation-coverage matrix + target list | `paper/CITATION_COVERAGE.md` | ✅ |
| Section-by-section blueprint | `paper/REMEDIATION_PLAN.md` | ✅ (awaiting approval) |

## Tooling / gates
| tool | path | role |
|---|---|---|
| Structural lint | `tools/lint_paper.py` | cites/refs/graphics/amssymb — clean |
| Citation coverage | `tools/citation_coverage.py` | 28 Tier-A uncited; becomes CI gate post-backfill |
| Counts | `tools/paper_counts.py` | abstract/section words, highlights, refs |

## Outstanding user gates (consolidated)
1. Approve `REMEDIATION_PLAN.md` (then execute the rewrite). 2. Author confirms AI-disclosure wording.
3. Funding statement (or "none"). 4. Zenodo deposit → DOI. 5. Suggested-reviewers list + COI check.
6. Cover-letter date. 7. Final venue sign-off (IJHE primary / Energy and AI floor) + submit.
