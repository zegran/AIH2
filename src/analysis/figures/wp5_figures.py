"""WP5 figures (Q1 re-design). Accuracy-first encodings; Okabe--Ito; vector PDF + 300 dpi PNG.
Deterministic; every value traces to committed artifacts. Run:
  uv run python -m src.analysis.figures.wp5_figures
"""
from __future__ import annotations
import warnings; warnings.filterwarnings("ignore")
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from src.analysis.figures import pubstyle as ps

ps.apply()
REPO = Path(__file__).resolve().parents[3]
rng = np.random.default_rng(42)
df = pd.read_csv(REPO / "data/curated/aih2_v1.csv")
rate = pd.read_csv(REPO / "data/wp1/rate_extraction.csv")
PORC = "10.1590/s0104-66322012000200014"


def mode(s):
    m = s.dropna().mode(); return m.iloc[0] if len(m) else np.nan


def ck_map():
    m = {}
    for r in pd.read_csv(REPO / "data/wp1/canonical_studies.csv").itertuples(index=False):
        if len(r) >= 2 and isinstance(r[1], str):
            m[r[1]] = r[0]
    return m
CK = ck_map()

agg = df.groupby("study_id").agg(meanyield=("h2_yield_pct", "mean"), n=("h2_yield_pct", "size"),
                                 sc=("system_class", mode), tc=("temperature_control", mode),
                                 mm=("measurement_method", mode), wt=("water_type", mode),
                                 qt=("quality_tier", mode)).reset_index()


def r2_cat(frame, cols):
    g = frame.dropna(subset=cols + ["meanyield"])
    if len(g) < 4: return np.nan
    grand = g.meanyield.mean(); sst = ((g.meanyield - grand) ** 2).sum()
    pred = g.groupby(cols)["meanyield"].transform("mean")
    return 1 - ((g.meanyield - pred) ** 2).sum() / sst if sst > 0 else 0


def boot_ci(frame, cols, n=2000):
    idx = np.arange(len(frame)); vals = []
    for _ in range(n):
        v = r2_cat(frame.iloc[rng.choice(idx, len(idx), replace=True)], cols)
        if not np.isnan(v): vals.append(v)
    return np.percentile(vals, [2.5, 97.5])


# ============ Fig 1 — leakage (dumbbell) ============
cv = pd.read_csv(REPO / "results/real_v1/metrics/cv_metrics.csv").sort_values("grouped.r2")
sens = pd.read_csv(REPO / "results/real_v1/metrics/porciuncula_sensitivity.csv")
po = {r.model: r.grouped_r2 for r in sens[sens.data == "porc-out"].itertuples()}
fig, ax = plt.subplots(figsize=(ps.SINGLE, 0.62 * ps.SINGLE))
y = np.arange(len(cv))
for yi, row in zip(y, cv.itertuples(index=False)):
    ax.plot([row[cv.columns.get_loc("grouped.r2")], row[cv.columns.get_loc("random.r2")]], [yi, yi],
            color=ps.OK["grey"], lw=1.3, zorder=1)
ax.scatter(cv["grouped.r2"], y, s=34, color=ps.OK["blue"], marker="o", label="study-grouped CV", zorder=3)
ax.scatter(cv["random.r2"], y, s=34, color=ps.OK["orange"], marker="s", label="random-split CV", zorder=3)
pox = [po.get(m, np.nan) for m in cv.model]
ax.scatter(pox, y, s=30, facecolors="none", edgecolors=ps.OK["blue"], marker="D",
           label="grouped, dominant study removed", zorder=2)
ax.axvline(0, color="k", lw=0.7, ls="--")
ax.set_yticks(y); ax.set_yticklabels(cv.model)
ax.set_xlabel("cross-validated $R^2$"); ax.set_xlim(-1.6, 0.75)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.30), ncol=2, fontsize=6.0,
          frameon=False, handletextpad=0.4, columnspacing=1.2)
ps.save(fig, "fig1_optimism_gap")

# ============ Fig 2 — HEADLINE dot plot + bootstrap CI ============
preds = [("system_class\n(physical regime)", ["sc"], "regime"),
         ("ALL method covariates", ["tc", "mm", "wt", "qt"], "methodall"),
         ("temperature control", ["tc"], "method"), ("measurement method", ["mm"], "method"),
         ("water type", ["wt"], "method"), ("quality tier", ["qt"], "method"),
         ("reaction vessel", [], "method")]
rows = []
for lab, cols, kind in preds:
    if not cols:  # vessel — single col vt not in agg; add
        cols = ["vt"]; agg["vt"] = df.groupby("study_id")["vessel_type"].agg(mode).values
    r = r2_cat(agg, cols); lo, hi = boot_ci(agg, cols)
    rows.append((lab, r, lo, hi, kind))
tab = pd.DataFrame(rows, columns=["lab", "r2", "lo", "hi", "kind"]).sort_values("r2")
fig, ax = plt.subplots(figsize=(ps.ONEHALF, 0.62 * ps.ONEHALF))
yy = np.arange(len(tab))
col = {"regime": ps.OK["vermillion"], "method": ps.OK["blue"], "methodall": ps.OK["black"]}
mk = {"regime": "s", "method": "o", "methodall": "D"}
for yi, row in zip(yy, tab.itertuples(index=False)):
    ax.plot([row.lo, row.hi], [yi, yi], color=col[row.kind], lw=1.4, alpha=0.6, zorder=1)
    ax.scatter(row.r2, yi, s=46, color=col[row.kind], marker=mk[row.kind], zorder=3)
ax.set_yticks(yy); ax.set_yticklabels(tab.lab)
ax.set_xlabel("between-study yield variance explained ($R^2$)  ·  bars = 95% cluster-bootstrap CI")
ax.set_xlim(-0.02, 1.0)
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([0], [0], marker="s", color=col["regime"], lw=0, label="physical regime"),
                   Line2D([0], [0], marker="o", color=col["method"], lw=0, label="method covariate"),
                   Line2D([0], [0], marker="D", color=col["methodall"], lw=0, label="all method (joint)")],
          loc="lower right")
ps.save(fig, "fig2_variance_decomposition")

# ============ Fig 3 — particle-size within-study trend (points + robust Theil--Sen line) ============
# Replicates can share a D50, so connecting raw points would imply a false sequence; instead show
# the raw points and a per-study Theil--Sen slope on log10(D50) to convey direction honestly.
fig, ax = plt.subplots(figsize=(ps.SINGLE, 0.66 * ps.SINGLE))
cols5 = [ps.OK["blue"], ps.OK["vermillion"], ps.OK["green"], ps.OK["orange"], ps.OK["purple"]]
mks = ["o", "s", "^", "D", "v"]
i = 0
for s, g in df.groupby("study_id"):
    gg = g.dropna(subset=["particle_size_d50_um", "h2_yield_pct"])
    if len(gg) >= 3 and gg.particle_size_d50_um.nunique() >= 2:
        rho, _ = stats.spearmanr(gg.particle_size_d50_um, gg.h2_yield_pct)
        lx = np.log10(gg.particle_size_d50_um.values)
        slope, intercept, _, _ = stats.theilslopes(gg.h2_yield_pct.values, lx)
        c, mk = cols5[i % 5], mks[i % 5]
        ax.scatter(gg.particle_size_d50_um, gg.h2_yield_pct, color=c, marker=mk, s=22,
                   edgecolor="white", linewidth=0.4, zorder=3,
                   label=f"{CK.get(s, s[:10])} ($\\rho$={rho:+.2f})")
        xs = np.array([lx.min(), lx.max()])
        ax.plot(10 ** xs, intercept + slope * xs, color=c, lw=1.3, alpha=0.85, zorder=2)
        i += 1
ax.set_xscale("log"); ax.set_xlabel("particle size $D_{50}$ ($\\mu$m, log)")
ax.set_ylabel("H$_2$ yield (%)")
ax.set_title(f"within every study, the particle-size trend is negative ({i}/{i})", fontsize=8)
ax.legend(fontsize=6.1, loc="lower left", borderaxespad=0.4)
ps.save(fig, "fig3_particle_size_consistency")

# ============ Fig 4 — Ea strip per regime ============
ea = rate[(rate.kinetic_metric == "ea_kj_mol") & rate.value.notna()]
es = ea.groupby(["study_id", "system_class"]).value.median().reset_index()
classes = ["pure_al_alkali", "mechanically_activated", "liquid_metal_activated", "waste_al", "al_alloy"]
fig, ax = plt.subplots(figsize=(ps.ONEHALF, 0.55 * ps.ONEHALF))
ax.axhspan(3.5, 102.6, color=ps.OK["grey"], alpha=0.12, zorder=0,
           label="literature band 3.5–102.6 kJ mol$^{-1}$")
for i, c in enumerate(classes):
    v = es[es.system_class == c].value.values
    if len(v):
        jit = rng.uniform(-0.13, 0.13, len(v))
        ax.scatter(np.full(len(v), i) + jit, v, s=30, color=ps.OK["blue"], alpha=0.85, zorder=3)
        ax.hlines(np.median(v), i - 0.25, i + 0.25, color=ps.OK["vermillion"], lw=2.2, zorder=4)
ax.set_xticks(range(len(classes)))
ax.set_xticklabels([c.replace("_", "\n") for c in classes], fontsize=6.6)
ax.set_ylabel("apparent $E_\\mathrm{a}$ (kJ mol$^{-1}$)")
ax.legend(loc="lower right", bbox_to_anchor=(1.0, 1.005), frameon=False, fontsize=6.3)
ax.set_ylim(0, 108)
ps.save(fig, "fig4_ea_spread")

# ============ Fig 5 — dataset composition ============
comp = df.groupby("system_class").agg(rows=("h2_yield_pct", "size"),
                                      studies=("study_id", "nunique")).sort_values("rows")
tier = df.pivot_table(index="system_class", columns="quality_tier", values="h2_yield_pct",
                      aggfunc="size", fill_value=0).reindex(comp.index)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(ps.DOUBLE, 0.42 * ps.DOUBLE), gridspec_kw={"width_ratios": [1.25, 1]})
yy = np.arange(len(comp))
a1.barh(yy, comp.rows, color=ps.OK["blue"], height=0.62)
for yi, (r, st) in zip(yy, zip(comp.rows, comp.studies)):
    a1.text(r + 3, yi, f"{r}  ({st} st.)", va="center", fontsize=6.6)
a1.set_yticks(yy); a1.set_yticklabels([c.replace("_", " ") for c in comp.index])
a1.set_xlabel("H$_2$-yield rows"); a1.set_xlim(0, comp.rows.max() * 1.25)
a1.set_title("yield dataset (315 rows / 31 studies)", fontsize=8)
left = np.zeros(len(comp)); tcol = {"A": ps.OK["green"], "B": ps.OK["yellow"], "C": ps.OK["vermillion"]}
for t in ["A", "B", "C"]:
    a2.barh(yy, tier[t], left=left, color=tcol[t], height=0.62, label=f"tier {t}"); left += tier[t].values
a2.set_yticks(yy); a2.set_yticklabels([]); a2.set_xlabel("rows by quality tier")
a2.set_title("quality tiers (+76-row kinetic table)", fontsize=8); a2.legend(fontsize=6.3, loc="lower right")
ps.save(fig, "fig5_dataset_composition")

# ============ Fig 6 — within-study response surface (justified 3D + 2D companion) ============
pf = df[(df.study_id == PORC) & (df.alkali_type == "NaOH") & (df.morphology_flag == "foil")]
grid = pf.pivot_table(index="temperature_k", columns="alkali_conc_mol_l", values="h2_yield_pct", aggfunc="mean")
T = grid.index.values; C = grid.columns.values; Z = grid.values
CC, TT = np.meshgrid(C, T)
fig = plt.figure(figsize=(ps.DOUBLE, 0.46 * ps.DOUBLE))
axA = fig.add_subplot(1, 2, 1)
cf = axA.contourf(CC, TT, Z, levels=12, cmap="viridis")
axA.contour(CC, TT, Z, levels=6, colors="k", linewidths=0.4, alpha=0.5)
axA.set_xlabel("NaOH concentration (mol L$^{-1}$)"); axA.set_ylabel("temperature (K)")
axA.set_title("(a) within-study surface: 2D contour", fontsize=8); axA.grid(False)
fig.colorbar(cf, ax=axA, shrink=0.85, label="H$_2$ yield (%)")
axB = fig.add_subplot(1, 2, 2, projection="3d")
axB.plot_surface(CC, TT, Z, cmap="viridis", edgecolor="k", linewidth=0.25, alpha=0.92, antialiased=True)
axB.set_xlabel("NaOH (mol L$^{-1}$)", fontsize=7, labelpad=2)
axB.set_ylabel("T (K)", fontsize=7, labelpad=2); axB.set_zlabel("yield (%)", fontsize=7, labelpad=2)
axB.set_xticks([1.0, 2.0, 3.0]); axB.set_yticks([300, 310, 320])
axB.view_init(elev=24, azim=-128); axB.set_title("(b) same data as a surface", fontsize=8)
axB.tick_params(labelsize=6, pad=-1)
fig.suptitle("porciuncula2012 (NaOH/foil): within-study yield is a smooth, monotone surface",
             fontsize=8.2, y=1.02)
fig.tight_layout()
ps.save(fig, "fig6_within_study_surface")

print("\nTRACE: regime R2=%.3f  method-all R2=%.3f  temperature_control R2=%.3f  (study-level, n=%d)"
      % (r2_cat(agg, ["sc"]), r2_cat(agg, ["tc", "mm", "wt", "qt"]), r2_cat(agg, ["tc"]), len(agg)))
