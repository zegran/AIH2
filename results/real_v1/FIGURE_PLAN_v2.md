# Figure plan v2 — Q1 re-design (accuracy-first, evidence-based)

Binding standards: Cleveland--McGill encoding accuracy (position/length > area/angle/color);
Weissgerber (show distributions, not bare bars); 3D only when intrinsically 3D + a 2D companion
(Jeong 2024); show uncertainty; Okabe--Ito colorblind-safe + grayscale-legible; Elsevier vector
(PDF+PNG), $\ge$7 pt fonts, single-column $\approx$9 cm / double $\approx$19 cm. Shared style in
`src/analysis/figures/pubstyle.py`. Every value traces to a committed artifact; no synthetic data.

| Fig | Message (one line) | Data source | Encoding + why (rule) | 2D/3D | col | uncertainty |
|---|---|---|---|---|---|---|
| **1** | Random-split predictability collapses under study-grouped CV. | `metrics/cv_metrics.csv` | **Dumbbell / connected-dot** per model (random→grouped $R^2$), zero line. Position+length encode the collapse far better than grouped bars (Cleveland--McGill). | 2D | single | point CV estimates; porc-out shown as a second marker |
| **2** *(headline)* | Methodology explains ~55% of between-study yield variance vs ~2% for physical regime; temperature control dominates. | `aih2_v1.csv` (study-level) + bootstrap | **Cleveland dot plot with 95% bootstrap-CI bars**, rows sorted by $R^2$; regime vs method distinguished by colour **and** marker shape (grayscale-safe). Dot=position, CI=length; avoids bare bars (Weissgerber). | 2D | 1.5 | cluster-bootstrap CI (resample studies) |
| **3** | Within every study that varies particle size, smaller $\Rightarrow$ higher yield (5/5); the "contradiction" is between studies. | `aih2_v1.csv` (5 studies) | **Per-study trajectories**: yield vs $\log$ particle size, one line/study, all sloping down; per-study $\rho$ annotated. Shows the raw data, not a derived bar (Weissgerber). | 2D | single | n/a (raw points); $\rho$ labels |
| **4** | Apparent $E_\mathrm{a}$ does not organize by regime (within-spread $\approx$ between-spread). | `rate_extraction.csv` | **Strip/dot plot per class + median bar + shaded 3.5--102.6 band**; jittered points show the full spread (liquid-metal 8.5--58). Distribution shown, not summarized. | 2D | single | spread visible; median bar |
| **5** | The curated open dataset (315 yield + 76 kinetic rows). | `aih2_v1.csv`, `rate_extraction.csv` | **Horizontal bars** for per-class row counts (counts = length, accurate) + small tier breakdown; data-resource figure. | 2D | single | n/a (counts) |
| **6** *(new, 3D justified)* | Within one study, yield is a smooth monotone surface over (T, alkali conc) — within-study data are clean; the chaos is cross-study. | `aih2_v1.csv` (porciuncula NaOH foil, 4$\times$5 grid) | **2D heatmap/contour (primary) + 3D surface companion.** Intrinsically 3D (response over two continuous predictors) $\Rightarrow$ 3D is *justified* here and only here, always paired with the readable 2D panel. | 2D+3D | double | n/a (single-study factorial) |

## 3D decision (explicit)
Only Fig 6 uses 3D, because it is the one panel whose data are intrinsically a surface
$z=f(x,y)$ over two continuous predictors (porciuncula's within-study temperature$\times$concentration
factorial). It is always shown with a 2D contour companion as the primary readable panel. No other
panel is forced into 3D; no 3D bars/pies/categorical 3D anywhere.

## What changed vs v1
- Fig 1 bars $\to$ dumbbell (encodes the *collapse* directly).
- Fig 2 bars $\to$ dot plot **with bootstrap CIs** (uncertainty now shown; the headline).
- Fig 3 $\rho$-bars $\to$ raw per-study trajectories (show the data).
- Fig 4 kept (already dot-strip) but styled + band + spread annotation.
- Fig 6 added: the legitimate-3D within-study cleanliness contrast (strongest narrative gain).
- All: Okabe--Ito palette, embedded-font vector PDF + 300 dpi PNG, Elsevier sizing, shape+colour
  redundancy for grayscale.

## Build steps
`pubstyle.py` (palette/fonts/sizes/export) $\to$ rewrite `wp5_figures.py` (6 figures) $\to$ regenerate
PDF+PNG $\to$ update `figure-catalog.md` (message/read/so-what + encoding rationale + trace) $\to$
anti-AI captions $\to$ commit+push $\to$ stop for user review (do **not** wire into `.tex` yet).
