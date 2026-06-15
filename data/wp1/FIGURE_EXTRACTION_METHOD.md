# WP1 Phase B — Figure Digitization Method (GUI-free)

*Problem:* much of the usable data (yields, rate curves — including some contradiction
evidence) lives in **figures**, and WebPlotDigitizer is an interactive GUI we can't drive from
the CLI. This documents the GUI-free workflow we adopted instead, with its accuracy envelope and
fallbacks. Researched 2026-06-15 (sources at the end).*

## Method (primary): render → vision

1. **Locate** the figure page via text search of `data/raw/literature/md/<citekey>.md`.
2. **Render** a high-DPI crop of the figure with `tools/render_figure.py`:
   ```
   uv run python tools/render_figure.py <citekey> <page> <x0> <y0> <x1> <y1> --zoom 6
   ```
   (clip fractions isolate the plot+legend; zoom 5–7 gives a readable image)
3. **Read** the PNG (vision): read the y-axis scale, map legend markers to curves, and read each
   curve's **plateau** (= final H2 release in mL/g, which is the yield).
4. **Convert** to the target: `h2_yield_pct = plateau_mL_per_g / 1244 * 100`,
   `value_origin=derived`, `extraction_method=table` (or note `digitized`).
5. **Validate** with `tools/validate_rows.py`; tier the rows (see accuracy below).

## Accuracy envelope (be honest in the dataset)

- **Validated:** on `jayaraman2015` Fig. 4 the read 90 °C plateaus (~1010–1050 mL/g) match the
  text-reported 1010/1030 mL/g → the method reproduces known values to ~±3 %.
- **Reliable for:** axis scales; plateau/yield bands; qualitative direction (e.g. which curve is
  higher); plots with few curves, distinct colors, or clear markers. → tier **B**.
- **Hard case:** dense (≥6) overlapping **black-and-white marker** curves (like jayaraman2015
  Fig. 4) — isolating one specific curve's plateau to ±2 % by eye is unreliable; read the band +
  direction and tier such rows **C**, or use a fallback. Match markers by rendering the legend in
  the same crop.

## Fallbacks for hard plots

- **`plotdigitizer`** (PyPI, CLI): batch digitizer; needs ≥3 axis-calibration pixel points via
  `-p`; works best on single-color curves.
- **LineFormer + ChartDete** (`extract-line-chart-data`): deep-learning automatic line-chart
  extraction; heavier setup, best for clean multi-line charts.
- Last resort: a human runs WebPlotDigitizer and hands back a CSV → we validate + ingest.

## Rules

- Figure-derived rows: `value_origin=derived`, `source_ref="Fig.N"`, tier B (clean) / C (dense).
- Never invent a value that can't be read — record only what the axis + curve support; if a
  specific curve can't be isolated, leave that condition out rather than guess.
- The render PNGs are scratch (`temp/`, gitignored); only the extracted rows are durable.

## Status

Figure extraction is **unblocked** (no GUI needed). The bulk of the 59 studies have readable
plots; dense B&W plots get tier-C rows or a fallback. For `jayaraman2015` the precise 90 °C
values were already text-reported (in the calibration rows); its figure-only 30 µm / low-T values
are the dense-plot hard case and are best obtained via the legend-matched read or `plotdigitizer`.

## Sources (research)
- plotdigitizer (PyPI / dilawar): https://pypi.org/project/plotdigitizer/
- svgdigitizer: https://pypi.org/project/svgdigitizer
- extract-line-chart-data (LineFormer + ChartDete): https://github.com/tdsone/extract-line-chart-data
- Digitize scientific plots with Python: https://www.pantelisliolios.com/digitize-scientific-plots-python/
- WebPlotDigitizer (automeris): https://automeris.io/
