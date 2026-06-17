# Q1 / Elsevier compliance report

Measured from the LaTeX source (`paper/main.tex`, `paper/sections/*.tex`, `references.bib`) on
2026-06-17 via `tools/paper_counts.py`. Journal limits fetched from the live Elsevier Guide for
Authors (GfA) — sources cited inline. Counts are approximate (LaTeX stripping); the word-budget
verdicts hold with margin.

## 1. Manuscript counts (measured)

| Metric | Value | Note |
|---|---|---|
| Abstract words | **≈196** (≈210 incl. inline math) | single paragraph |
| Total words (abstract + body) | **≈2,960** | excl. references/captions; well within any limit |
| Introduction / Related work / Methods | 383 / 243 / 494 | |
| Results / Discussion / Conclusion | 752 / 583 / 305 | |
| Figures | **6** (all vector PDF) | fig1–fig6, all referenced |
| Tables | **1** (minimum-information reporting standard, Discussion) | |
| Display equations | 0 | inline math only |
| References | **18** | all cited, all resolve (lint clean) |
| Highlights | **5**, each ≤85 chars incl. spaces ✓ | 82/—/76/70/≈83 |
| Keywords | **7** | |

## 2. Structure & declarations (present?)

| Item | Present | Where |
|---|---|---|
| Introduction | ✅ | `introduction.tex` |
| Methods / Data | ✅ | `method.tex` ("Data and methods") |
| Results | ✅ | `results.tex` |
| Discussion | ✅ | `discussion.tex` (+ reporting-standard table) |
| Conclusion | ✅ | `conclusion.tex` |
| Data availability statement | ✅ | `conclusion.tex` (Zenodo DOI placeholder) |
| Declaration of competing interest | ✅ | `conclusion.tex` |
| CRediT authorship statement | ✅ | `conclusion.tex` (Dogukan Unal) |
| Generative-AI disclosure | ✅ | `conclusion.tex` (flagged for author confirmation) |
| **Funding statement** | ❌ | **MISSING in manuscript** — both journals require it (state "none" if none) |

## 3. Artwork (Elsevier specs)

| Check | Status |
|---|---|
| Vector PDF, fonts embedded (`pdf.fonttype=42`) | ✅ |
| Colorblind-safe (Okabe–Ito), grayscale-legible (shape+colour) | ✅ |
| ≥7 pt fonts; single/double-column sizing | ✅ |
| No unjustified 3D (one intrinsic-surface panel + 2D companion) | ✅ |
| All 6 figures referenced; self-contained captions | ✅ |
| ≤12 diagrams (IJHE) | ✅ (6) |

## 4. Journal fit — verified against the live Guide for Authors

Sources (fetched June 2026; ScienceDirect blocks direct fetch, values extracted from the live GfA):
- IJHE: <https://www.sciencedirect.com/journal/international-journal-of-hydrogen-energy/publish/guide-for-authors>
- Energy and AI: <https://www.sciencedirect.com/journal/energy-and-ai/publish/guide-for-authors>

| Requirement | IJHE (limit) | our paper | verdict | Energy and AI (limit) | verdict |
|---|---|---|---|---|---|
| Abstract | **≤150 words** | ≈196 | ⚠️ **needs-trim** (cut ~50 words) | ≤250 words | ✅ fit |
| Highlights | required, 3–5, ≤85 chars | 5, all ≤85 | ✅ fit | required, 3–5, ≤85 | ✅ fit |
| Keywords | **max 6** | 7 | ⚠️ **needs-trim** (drop 1) | not specified (≤6 std) | ✅ fit |
| Total length (research paper) | ≤8000 words, ≤12 diagrams | ≈2,960; 6 figs | ✅ fit | not specified | ✅ fit |
| Reference style | numeric (Vancouver-style) | `elsarticle-num` (numeric) | ✅ fit | numeric (name not verbatim-verified) | ✅ likely fit |
| Article type | research / review / short comm (no data/methods type) | research paper | ✅ fit (frame as a hydrogen research contribution) | full / short / perspective / review | ✅ fit (full or perspective) |
| AI disclosure | required (section before references) | present | ✅ | required | ✅ |
| CRediT / Data avail / Competing interest | all required | present | ✅ | all required | ✅ |
| Funding | required (state if none) | **missing** | ⚠️ **missing-item** | required | ⚠️ **missing-item** |

**Honest flags from the GfA fetch:** (a) one search summary claimed IJHE abstract "200 words," but the
live GfA section states **150**; the stricter 150 is used here. (b) Energy and AI's reference style is
auto-formatted via the journal CSL template; the exact name "numbered/Vancouver" was not quoted
verbatim on the page — treated as numeric, name unverified.

## 5. Per-journal verdict

- **IJHE (primary) — FIT with 3 small fixes.** Topically squarely in scope (aluminum–water hydrolysis
  for H₂). Submit as a standard **research paper**. Required before submission: trim abstract to ≤150
  words, drop one keyword (→6), add a funding statement. Framing note: foreground the hydrogen-production
  research contribution (the dataset + the methodological finding), not only the reproducibility critique,
  since IJHE has no methods/data article type.
- **Energy and AI (floor) — FIT only if AI/ML-centric.** Abstract and keywords pass as-is; still add a
  funding statement. The journal explicitly rejects single-aspect (energy-only) papers, so acceptance
  hinges on foregrounding the data-leakage/ML-evaluation methodology as the core contribution. Maps to a
  **full-length** or **Perspective** article; open-access.

## 6. Prioritized fix list before submission

1. **Abstract → ≤150 words** (IJHE). Currently ≈196. *(content edit — left for author review; offer to do it.)*
2. **Keywords → 6** (IJHE). Drop the weakest (e.g. "methodological heterogeneity" overlaps "reproducibility").
3. **Add a funding statement** to the manuscript (both journals) — e.g. "This research received no specific
   grant from funding agencies in the public, commercial, or not-for-profit sectors," if accurate.
4. Confirm the AI-disclosure wording (already flagged in the .tex).
5. Insert the Zenodo DOI once minted (replaces `\todo{Zenodo DOI}`).

Items 1–3 are mechanical and CLI-doable on request; none change the scientific content beyond shortening
the abstract. No fixes were applied in this preview pass (preview-only, per the command).
