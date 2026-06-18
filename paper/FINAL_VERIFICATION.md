# Final Verification — Stage 2 Complete

Date: 2026-06-18

## DOI Inserted

- Zenodo DOI: `10.5281/zenodo.20751918`
- Inserted in: `paper/sections/conclusion.tex` (Data Availability)
- Inserted in: `paper/sections/supplementary.tex` (companion data release line)
- Updated in: `release/zenodo_v1/CITATION.cff` (doi: field)

## Corrected Numbers Propagated Everywhere

| Location | Value | Status |
|---|---|---|
| Abstract (`paper/main.tex`) | ≈72% method / ≈43% apparatus / ≈8% TC | ✅ already in place |
| Highlights (`paper/main.tex`) | ≈72% / apparatus largest ≈43% / TC ≈8% | ✅ already in place |
| Introduction (`paper/sections/introduction.tex`) | ≈72% / apparatus ≈43% / TC ≈8% | ✅ updated this stage |
| Results §3.4 (`paper/sections/results.tex`) | R²=0.717, R²=0.425, R²=0.081 | ✅ already in place |
| Results §3.7 robustness (`paper/sections/results.tex`) | OA-subset / Fisher p values | ✅ already in place |
| Discussion opening (`paper/sections/discussion.tex`) | ≈72% / ≈2% | ✅ already in place |
| Discussion §"Why pooling fails" | apparatus 43%, TC 8% | ✅ updated this stage |
| Discussion `tab:mireport` caption | apparatus largest R²=0.43 | ✅ updated this stage |
| Discussion `tab:mireport` rows | apparatus 0.43 (row 1), TC 0.08 (row 2) | ✅ updated this stage |
| Discussion `tab:mireport` TC level list | removed "uncontrolled" | ✅ updated this stage |
| Discussion §min-reporting-standard text | apparatus listed first, R²=0.43 | ✅ updated this stage |
| Discussion §Limitations associational | apparatus 43%, TC 8% | ✅ already in place |
| Conclusion | ≈72% / apparatus ≈43% / TC ≈8% | ✅ already in place |
| Method §data extraction TC levels | removed "uncontrolled" from level list | ✅ updated this stage |
| Cover letter (`paper/submission/cover_letter.md`) | ≈72% / apparatus ≈43% / TC ≈8% | ✅ updated this stage |

## Unchanged (Correctly Preserved)

- `R²≈0.55` for random-split CV in Introduction, Results, Discussion (optimism-gap number) — CORRECTLY left intact
- `R²=0.018` for regime — CORRECTLY unchanged throughout

## GitHub Link Removed

- `paper/submission/cover_letter.md` — GitHub URL replaced with Zenodo DOI ✅
- No GitHub link remains in any paper source file ✅

## Energy and AI — IJHE References Updated

- `paper/submission/cover_letter.md` — updated to Energy and AI ✅
- `paper/submission/IJHE_checklist.md` — renamed and updated to Energy and AI ✅
- Note: `International Journal of Hydrogen Energy` entries in `references.bib` are CITED PAPERS published in IJHE — these are correct and must not be changed

## Consistency Gate

Run: `uv run python tools/consistency_gate.py`
Result: **PASS** — headline values 0.717 / 0.018 / 0.425 / 0.081 consistent across all text

## All Gates

| Gate | Command | Result |
|---|---|---|
| Structural lint | `uv run python tools/lint_paper.py` | PASS (58/58 cite coverage, 0 hard errors) |
| Compliance | `uv run python tools/compliance_gate.py` | PASS (abstract 250 words, 6 keywords, Energy and AI) |
| Consistency | `uv run python tools/consistency_gate.py` | PASS |

## Zenodo Bundle

- Bundle: `release/zenodo_v1/` (6 files + zip) — corrected dataset (0 uncontrolled TC rows)
- Synced to: `submission_package/zenodo/`
- CITATION.cff: doi = `10.5281/zenodo.20751918` ✅

## DOCX

- `submission_package/manuscript/main_review.docx` — regenerated 2026-06-18 (287 KB, pandoc, 2 harmless `\rm` warnings)

## IRR Documentation

- Method §QC section: blind IRR paragraph; raw κ (sc=0.826, tc=0.429, mm=0.700); 3 corrections; post-correction κ (sc=0.826, tc=1.00, mm=1.00) ✅
- QC Table: row 5 "Independent-agent IRR" ✅
- Limitations: single-author/AI limitation paragraph with IRR finding ✅
- Discussion §Limitations: agent-based IRR caveat ✅

## Definition of Done — SATISFIED

- [x] DOI inserted in all locations
- [x] Corrected numbers propagated to every section + tables (≈72% / apparatus ≈43% / TC ≈8%)
- [x] R²≈0.55 optimism-gap left intact (correct, unchanged by corrections)
- [x] IRR/κ documented in Methods, QC Table, Limitations, Discussion
- [x] Cover-letter GitHub link removed
- [x] IJHE → Energy and AI in cover letter and checklist
- [x] Consistency gate added + PASS
- [x] All gates PASS (lint, compliance, consistency)
- [x] Cited DOCX regenerated (287 KB)
- [x] FINAL_VERIFICATION.md committed + pushed
