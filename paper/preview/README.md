# Manuscript preview pack

Three formats of the manuscript for review. **The PDF is the authoritative typeset version.**

| File | Role | Notes |
|---|---|---|
| `main.pdf` | **Authoritative** | The exact GitHub Actions CI build (Elsevier `elsarticle`, `latexmk`). Faithful typesetting, embedded vector figures, correct math and Turkish characters. |
| `main.docx` | Convenience preview | Pandoc conversion for tracked-changes / Word review. Figures embedded as raster. |
| `main.md` | Convenience preview | Pandoc Markdown; figures reference the `fig*.png` files in this folder. |

The DOCX/MD are **convenience previews only** — LaTeX-specific formatting (the `elsarticle`
frontmatter/author block, some math, citation numbering) may render imperfectly. For anything
definitive, read `main.pdf`. Citations in the DOCX/MD are shown author–year (Pandoc default); the
submitted PDF uses numeric `elsarticle-num` style.

## Provenance
- `main.pdf` — downloaded from the green CI run for the current `main` commit
  (GitHub → Actions → "Build paper PDF" → artifact `main-pdf`). Regenerated on every push to `paper/**`.
- `main.docx` / `main.md` — generated with:
  ```
  pandoc main.tex --citeproc --bibliography=references.bib -o main.docx   # (and -o main.md)
  ```
  run on a copy of the source with figure paths pointed at the 300-dpi PNGs (Word cannot embed PDF
  figures). No content was changed.

## Verified in the preview
Figures appear in place with captions; references resolve to a reference list; Turkish characters
(Çankaya, Türkiye) render correctly in the PDF. See `paper/submission/COMPLIANCE_REPORT.md` for the
counts and journal-fit checks (note: abstract exceeds the IJHE 150-word limit — flagged there).
