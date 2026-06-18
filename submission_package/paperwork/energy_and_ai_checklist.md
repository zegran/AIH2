# Energy and AI submission checklist

Status: ✅ done · 🟡 CLI-ready, needs user input · ⛔ user gate

## Manuscript
- ✅ Title, abstract (structured: problem / method / result / contribution)
- ✅ Keywords (7)
- 🟡 Highlights — drafted (`highlights.txt` + in `main.tex`); confirm each ≤ 85 chars on final read
- ✅ Sections: Intro, Related work, Data & methods, Results, Discussion, Conclusion
- ✅ Data and code availability statement (Zenodo DOI 10.5281/zenodo.20751918)
- ✅ Declaration of competing interest
- ✅ CRediT authorship contribution statement (Dogukan Unal — all roles)
- ✅ Declaration of generative AI and AI-assisted technologies (flagged `% AUTHOR: confirm`)
- ✅ Author, affiliation, corresponding-author email, ORCID (Dogukan Unal, IPEC; ORCID 0009-0006-5102-8013)
- ⛔ Funding statement — [USER INPUT, if any]

## Figures (Elsevier artwork specs)
- ✅ Vector PDF, fonts embedded (`pdf.fonttype=42`), 300 dpi PNG previews available
- ✅ Colorblind-safe (Okabe–Ito), legible in grayscale (shape+colour redundancy)
- ✅ ≥7 pt fonts; single-/double-column sizing; no unjustified 3D (one intrinsic-surface panel + 2D companion)
- ✅ All 6 figures referenced in text (fig1–fig6); self-contained captions
- ✅ Figures bundled in `paper/figures/` so the source compiles standalone

## References
- ✅ 58 entries, each tier-tagged (full-text- or metadata-verified); zero `\todocite`
- ✅ Every cited key resolves; no uncited entries (structural lint clean)
- 🟡 `das2023fuel`: exact in-sample R² softened to "near-perfect"; confirm against full text if a precise number is wanted (`% NEEDS-FULLTEXT`)
- ✅ `elsarticle-num` bibliography style

## Build / format
- ✅ `elsarticle` class, `[preprint,12pt]`; `\journal{Energy and AI}`
- ✅ Structural lint clean (`tools/lint_paper.py`): cites, refs/labels, graphics, no placeholders
- 🟡 Compile: GitHub Actions workflow added (`.github/workflows/latex.yml`) → download `main.pdf` from the Actions tab; or use Overleaf. (No local TeX in dev env.)

## Declarations & policy
- ✅ Competing-interest declaration present
- ⛔ Funding statement — [USER INPUT, if any]
- ✅ Original work, not under consideration elsewhere (stated in cover letter)
- ✅ Data availability: open dataset at Zenodo 10.5281/zenodo.20751918 (CC-BY-4.0)

## Submission items
- ✅ Cover letter draft (`cover_letter.md`) — updated for Energy and AI
- ✅ Suggested reviewers template (`suggested_reviewers.md`)
- ✅ Highlights file (`highlights.txt`)
- ✅ Venue: Energy and AI (Elsevier)
