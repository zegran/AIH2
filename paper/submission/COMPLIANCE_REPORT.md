# Energy and AI compliance report — post-remediation snapshot

Measured from the LaTeX source (`paper/main.tex`, `paper/sections/*.tex`, `references.bib`)
on 2026-06-17 after completing the 7-stage Q1 remediation workflow
(`data/wp1/CLI_EXECUTE_REMEDIATION_ENERGY_AND_AI.md`).

Gate checks run: `tools/lint_paper.py` (structural) + `tools/citation_coverage.py --check`
(data-source attribution) + `tools/compliance_gate.py` (Energy and AI Guide for Authors).

---

## 1. Manuscript counts (current state)

| Metric | Value | Energy and AI limit | Status |
|---|---|---|---|
| Abstract words | ~211 | <=250 | PASS |
| Keywords | 6 | 3-6 | PASS |
| Highlights | 5 bullets | 3-5 | PASS |
| References | 58 | none stated | PASS |
| Figures | 6 (vector PDF) | none stated | PASS |
| Tables | 6 (T1-T6 + tab:mireport + SI-1 + SI-2) | none stated | PASS |

Section word counts (approximate, post-remediation):

| Section | Words | Target |
|---|---|---|
| Introduction | ~650 | 600-700 |
| Related work | ~750 | 700-800 |
| Data and methods | ~1,150 | 1,100-1,200 |
| Results | ~1,600 | 1,500-1,700 |
| Discussion | ~1,000 | 900-1,100 |
| Conclusion | ~300 | 250-350 |
| **Total (body)** | **~5,450** | **>5,000** |

---

## 2. Gate results

| Gate | Tool | Result |
|---|---|---|
| Structural lint (cites/refs/graphics) | `tools/lint_paper.py` | PASS (lint clean) |
| Data-source citation coverage | `tools/citation_coverage.py --check` | PASS (0 missing) |
| Energy and AI compliance | `tools/compliance_gate.py` | PASS (5 non-blocking warnings) |

### Compliance gate detail (all 12 checks)

| Check | Result |
|---|---|
| `\journal{Energy and AI}` in main.tex | PASS |
| Abstract <=250 words (~211) | PASS |
| Keywords 3-6 (count: 6) | PASS |
| Highlights 3-5 bullets (count: 5) | PASS |
| Acknowledgements section present | PASS |
| Declaration of competing interest present | PASS |
| CRediT authorship statement present | PASS |
| Declaration of generative AI present | PASS |
| Data and code availability present | PASS |
| No unresolved \todo{} (except Zenodo placeholder) | WARNING — Zenodo deposit pending |
| elsarticle document class | PASS |
| booktabs loaded | PASS |

### Non-blocking warnings

1. Three highlight bullets exceed 85 chars after LaTeX math-stripping (math tokens counted as
   "MATH"; actual text is within 85 chars in the rendered PDF).
2. Two `\todo{Zenodo DOI}` placeholders — resolved once the Zenodo deposit is minted.

---

## 3. Citation attribution (Tier-A obligation)

All 31 data-source studies cited; 12 domain-context studies cited; total BibTeX entries: 58.
All fetched from Crossref by DOI via `tools/fetch_bibtex.py` — none written from memory.

---

## 4. Structure and declarations

| Item | Present | Where |
|---|---|---|
| Introduction | YES | `introduction.tex` |
| Related work | YES | `related_work.tex` (with `\label{sec:related}`) |
| Data and methods | YES | `method.tex` |
| Results | YES | `results.tex` |
| Discussion | YES | `discussion.tex` |
| Conclusion | YES | `conclusion.tex` |
| Data availability | YES | `conclusion.tex` |
| Acknowledgements / funding | YES | `conclusion.tex` ("received no specific grant") |
| Declaration of competing interest | YES | `conclusion.tex` |
| CRediT authorship | YES | `conclusion.tex` |
| Declaration of generative AI | YES | `conclusion.tex` (author to confirm wording) |
| Supplementary material | YES | `supplementary.tex` (Tables SI-1, SI-2; SI-3, SI-4 in data release) |

---

## 5. Artwork (Elsevier/Energy and AI specs)

| Check | Status |
|---|---|
| Vector PDF, fonts embedded (pdf.fonttype=42) | YES |
| Colorblind-safe (Okabe-Ito), grayscale-legible (shape+colour) | YES |
| >=7 pt fonts; single/double-column sizing | YES |
| No unjustified 3D (one intrinsic-surface panel + 2D companion) | YES |
| All 6 figures referenced; self-contained captions | YES |

---

## 6. Outstanding user gates before submission

1. **Zenodo deposit** — mint DOI → replace `\todo{Zenodo DOI}` in `conclusion.tex` and
   update `submission_package/dataset/CITATION.cff`.
2. **Confirm AI-disclosure wording** — `conclusion.tex` line 32 flagged with `% AUTHOR: confirm`.
3. **Suggested reviewers** — `paper/submission/suggested_reviewers.md` is a template; user confirms.
4. **COI check** — verify no undisclosed conflicts with any suggested reviewer.
5. **Final venue sign-off** — Energy and AI confirmed as primary venue.
6. **Submit** via Elsevier Editorial Manager.

All manuscript content, citations, compliance, and tooling are submission-ready pending the
above user-only gates.
