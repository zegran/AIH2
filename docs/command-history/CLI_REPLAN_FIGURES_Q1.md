# CLI Command — Re-plan ALL figures from scratch to Q1 standard (ultrathink, evidence-based)

> Paste into Claude Code at the AIH2 repo root. The current 5 figures are not Q1-grade. **Ultrathink
> a complete figure re-plan**, invoking the relevant skills (`results-analysis` for figure
> generation, `writing-anti-ai` for captions, and any publication-plotting skill available). Use the
> embedded research below as the binding standard. Produce a figure PLAN first, then regenerate, then
> stop for user review. Every figure stays deterministic and traceable to committed artifacts. No
> fabricated data; no decorative chart-junk.

---

## A. Research findings (binding standard — derived from the literature + Elsevier specs)

### A1. Perceptual / design evidence (what Q1 reviewers expect)
- **Position & length encode most accurately; area/angle/color encode poorly** (Cleveland–McGill,
  replicated by VanderPlas 2024). Prefer dot/point + length over pies, area bubbles, stacked-angle.
- **Avoid bar graphs for continuous/distributional data; show the distribution** (dot/box/violin,
  individual points, CIs) — Weissgerber 2019.
- **3D for quantitative data REDUCES interpretation accuracy** and "unjustified 3D effects" are a
  recognized deceptive/low-quality pattern (Jeong 2024; VanderPlas 2024; Nguyen 2021). → **3D is
  allowed ONLY when the data is intrinsically 3-dimensional (a genuine response surface over two
  continuous predictors), and ALWAYS paired with a 2D companion (contour/heatmap). NEVER 3D bars,
  3D pies, or 3D for categorical comparisons.**
- **Show uncertainty** (bootstrap/CI bands, error bars) — don't plot point estimates bare.
- General guides to follow: Rougier 2014 (Ten Simple Rules), Midway 2020, Kelleher 2011,
  Franconeri 2021.

### A2. Elsevier/IJHE technical artwork specs (hard requirements)
- **Vector preferred** for line art/plots: export **PDF or EPS with fonts embedded**. Provide a PNG
  preview alongside.
- If raster: ≥**300 dpi** halftone, **500 dpi** combination, **1000 dpi** line art.
- **Sizing:** single-column ≈ 9 cm (≥1063 px @300dpi); double-column ≈ 19 cm (≥2244 px). Design at
  final print size — don't rely on scaling.
- **Fonts:** ≥7 pt printed (≥6 pt sub/superscript), one sans-serif family, consistent across panels.
- **Color:** colorblind-safe palette (e.g., Okabe–Ito / viridis); must remain legible in grayscale;
  never encode meaning by color alone (add shape/label).

## B. Scope (what to re-plan)
- **In scope:** all current figures (fig1–fig5) re-designed from scratch + propose any NEW figure
  that strengthens the narrative; a shared **publication style module** (`src/analysis/figures/
  pubstyle.py`): fonts, sizes, palette, panel layout, vector export.
- **3D — exactly where legitimate.** The strongest (and likely only) genuine 3D candidate: the
  `porciuncula2012` within-study factorial **yield = f(temperature, alkali concentration)** as a
  response **surface** — it visually shows within-study cleanliness vs cross-study chaos. If used,
  pair it with a 2D contour/heatmap companion. Evaluate (ultrathink) whether any other panel is
  *intrinsically* 3D; if not, keep 2D — do not force 3D.
- **Out of scope / forbidden:** decorative 3D, 3D bar/pie, gratuitous gradients/shadows, dual-axis
  tricks, truncated axes without a break marker.

## C. Capacity (toolchain — what is achievable, and limits)
- **matplotlib** produces full Q1-grade **2D vector** (PDF/EPS) output — sufficient for figs 1–5 if
  styled to spec. This is the primary tool.
- **3D:** `matplotlib` `mplot3d` can render a response surface; render at a well-chosen viewing
  angle, high dpi, with a 2D contour companion (a bare 3D mesh reads as amateur). Optionally produce
  an interactive `plotly` HTML **for exploration only** — the print figure must be the static
  vector/high-dpi version.
- All figures must stay **deterministic** (fixed seed, pinned data paths) and **traceable** (every
  value from `data/curated/aih2_v1.csv`, `data/wp1/rate_extraction.csv`,
  `results/real_v1/metrics/*`). No new/synthetic data introduced for visual effect.

## D. Procedure
1. **Ultrathink a figure plan** → write `results/real_v1/FIGURE_PLAN_v2.md`: for each proposed figure
   — message (one sentence), data source, **chosen encoding/chart type + why (cite A1 rule)**,
   2D-vs-3D decision + rationale, panel layout, single/double-column, uncertainty shown. Keep the
   headline (method vs physics variance) as the centerpiece; make encodings accuracy-first.
2. Build `src/analysis/figures/pubstyle.py` (shared style) and rewrite `wp5_figures.py` to use it;
   export each figure as **PDF (vector) + PNG (300+ dpi preview)**.
3. Regenerate all figures; update `results/real_v1/figures/figure-catalog.md` (message/read/so-what
   + the encoding rationale + verification trace).
4. `writing-anti-ai` pass on captions.
5. Commit (`feat(figures): Q1 re-plan — publication style, accuracy-first encodings, justified 3D`)
   and push. **Stop and present the new PNGs + FIGURE_PLAN_v2 for user review** (do not wire into
   the .tex yet — that's a later step once figures are approved).

## E. Definition of done
- `FIGURE_PLAN_v2.md` (with per-figure encoding rationale + 3D justification), `pubstyle.py`,
  regenerated PDF+PNG figures, updated catalog — committed + pushed.
- Every figure: vector export, embedded fonts, colorblind-safe, uncertainty shown, traceable,
  Elsevier-sized. 3D used only on an intrinsically-3D panel with a 2D companion (or not at all).
- Pipeline stops; new figures presented for user review.
