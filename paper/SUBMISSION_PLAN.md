# Submission plan — post-remediation state (2026-06-17)

Status: **manuscript submission-ready** pending 5 user-only gates.

Venue: **Energy and AI** (primary — confirmed in Stage 0 via T_A null / GO-NO-GO binding rule).
Format: full-length research article, open-access, `elsarticle` class.

---

## Gate summary

| Gate | Owner | Status |
|---|---|---|
| Structural lint (cites/refs/labels/graphics) | tools/lint_paper.py | PASS |
| Data-source citation coverage (31/31) | tools/citation_coverage.py | PASS |
| Energy and AI compliance (12 checks) | tools/compliance_gate.py | PASS |
| Word count (>5,000 body words) | — | PASS (~5,450 w) |
| References (>=46) | — | PASS (58 entries) |
| Abstract (<=250 w) | — | PASS (~211 w) |
| Keywords (3-6) | — | PASS (6) |
| Highlights (3-5, <=85 chars) | — | PASS (5 bullets) |
| Acknowledgements / funding statement | — | PASS (added Stage 6) |
| Declarations (COI, CRediT, gen-AI, data avail) | — | PASS (all 4 present) |
| Supplementary material | — | PASS (Tables SI-1, SI-2; SI-3/4 in data release) |
| CI builds PDF | .github/workflows/latex.yml | PENDING (push to trigger) |

---

## Work packages — current state

### WP-CITE — bibliography completion (DONE)
58 BibTeX entries: 31 Tier-A data-source + 12 Tier-B domain-context + 15 other.
All fetched from Crossref by DOI; never written from memory.
Citation coverage: 31/31 data-source studies cited (tools/citation_coverage.py --check passes).

### WP-COMPILE — build the PDF (PENDING USER)
CI workflow `.github/workflows/latex.yml` updated: lint → compliance → LaTeX compile.
**Action required:** push to GitHub main to trigger CI and confirm the PDF builds green.
No local pdflatex available; CI is the build path.

### WP-FRONTMATTER — elsarticle format (DONE)
Author: Dogukan Unal | Affiliation: IPEC, Ankara | ORCID: 0009-0006-5102-8013
Journal: Energy and AI | Class: elsarticle preprint 12pt | Bibliography: elsarticle-num
All frontmatter declarations present. CRediT roles: Conceptualization, Methodology,
Software, Formal analysis, Data curation, Writing.

### WP-CONTENT — Q1 remediation (DONE — 7 stages)
Stage 0: Energy and AI reframe (journal, abstract <=250 w, keywords 6, highlights 5)
Stage 1: Citation backfill (28+12 BibTeX from Crossref, coverage 31/31)
Stage 2: Methods expansion (~1,150 w, Tables 1+2, leakage-controlled eval section)
Stage 3: Results expansion (~1,600 w, Tables 3+4, 14 unreported quantities added)
Stage 4: Related work (~750 w, regime-organized) + Introduction (~650 w, contributions updated)
Stage 5: Discussion (~1,000 w, named studies, round-robin analogues, 5 limitations)
Stage 6: Supplementary (Tables SI-1, SI-2) + compliance gate + declaration of generative AI

### WP-DATA-RELEASE — Zenodo deposit (PENDING USER)
Dataset package ready in `submission_package/dataset/` (315 yield + 76 kinetic rows, CC-BY).
`.zenodo.json` metadata complete. User mints DOI → replace `\todo{Zenodo DOI}` in
`conclusion.tex` (line 17) and update `submission_package/dataset/CITATION.cff`.

### WP-SUBMISSION-PREP — paperwork (MOSTLY DONE, user finalizes)
Cover letter: `paper/submission/cover_letter.md` (date = submission date)
Suggested reviewers: `paper/submission/suggested_reviewers.md` (template; user confirms)
AI disclosure: `conclusion.tex` (user to confirm accuracy of wording)
Checklist: `paper/submission/COMPLIANCE_REPORT.md` (all checks PASS)

---

## Critical path to submit

1. Push → CI turns green (PDF builds) [user]
2. Zenodo deposit → insert DOI into paper [user]
3. Confirm AI-disclosure wording [user]
4. Confirm suggested reviewers + COI check [user]
5. Final venue sign-off + submit via Elsevier Editorial Manager [user]

Items 1-5 are user-only. No further manuscript content changes are required.
