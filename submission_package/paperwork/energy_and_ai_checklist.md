# Energy and AI — Author Checklist (pre-submission)

Source: Elsevier Guide for Authors — Energy and AI
Verified by `tools/compliance_gate.py` (12/12 checks PASS, 2026-06-17)

## Manuscript format

- [x] Journal declared: `\journal{Energy and AI}` in main.tex
- [x] Document class: `elsarticle` (preprint, 12pt)
- [x] Bibliography style: `elsarticle-num`
- [x] booktabs loaded (publication-quality tables)

## Abstract and metadata

- [x] Abstract ≤ 250 words (current: ~211 words)
- [x] Keywords: 3–6 (current: 6)
- [x] Highlights: 3–5 bullets, each ≤ 85 characters (current: 5 bullets — see highlights.md)

## Sections

- [x] Introduction
- [x] Related work (with `\label{sec:related}`)
- [x] Data and methods
- [x] Results
- [x] Discussion
- [x] Conclusion
- [x] Supplementary material (Tables SI-1, SI-2)

## Mandatory declarations

- [x] Acknowledgements / funding statement ("received no specific grant from funding agencies…")
- [x] Declaration of competing interest
- [x] CRediT authorship statement
- [x] Declaration of generative AI and AI-assisted technologies (CONFIRM wording before submit)
- [x] Data and code availability statement

## Figures

- [x] All 6 figures in vector PDF format, fonts embedded
- [x] Colorblind-safe palette (Okabe-Ito); grayscale-legible (shape + color)
- [x] Minimum 7 pt fonts in figures
- [x] All figures cited in text; self-contained captions

## References

- [x] 58 BibTeX entries; 31 Tier-A data-source + 12 Tier-B domain-context
- [x] All data-source studies cited (31/31 — citation_coverage.py PASS)
- [x] All references fetched from Crossref by DOI; none written from memory

## Open gates before submission (user action required)

- [ ] **Zenodo deposit** — mint DOI; replace `\todo{Zenodo DOI}` in conclusion.tex + CITATION.cff
- [ ] **Confirm AI-disclosure wording** — conclusion.tex `% AUTHOR: confirm` comment
- [ ] **Confirm suggested reviewers + COI** — paperwork/suggested_reviewers.md
- [ ] **CI PDF confirmed green** — download main.pdf from GitHub Actions → manuscript/main.pdf
- [ ] **Final venue sign-off** — submit via Elsevier Editorial Manager
