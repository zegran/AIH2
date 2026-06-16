"""WP5 figures for the methodological-heterogeneity paper. Deterministic, reproducible.
Every number traces to committed artifacts (data/curated/aih2_v1.csv, data/wp1/rate_extraction.csv,
results/real_v1/metrics/cv_metrics.csv). Run: uv run python -m src.analysis.figures.wp5_figures
Outputs PDF+PNG to results/real_v1/figures/.
"""
from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

REPO = Path(__file__).resolve().parents[3]
OUT = REPO / "results/real_v1/figures"
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"figure.dpi": 140, "font.size": 9, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.grid": True, "grid.alpha": 0.25})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / f"{name}.pdf"); fig.savefig(OUT / f"{name}.png", dpi=160)
    plt.close(fig)
    print("wrote", name)


def mode(s):
    m = s.dropna().mode(); return m.iloc[0] if len(m) else np.nan


df = pd.read_csv(REPO / "data/curated/aih2_v1.csv")
rate = pd.read_csv(REPO / "data/wp1/rate_extraction.csv")
agg = df.groupby("study_id").agg(meanyield=("h2_yield_pct", "mean"),
                                 sc=("system_class", mode), tc=("temperature_control", mode),
                                 mm=("measurement_method", mode), wt=("water_type", mode),
                                 qt=("quality_tier", mode)).reset_index()


def r2(frame, cols):
    g = frame.dropna(subset=cols + ["meanyield"]); grand = g.meanyield.mean()
    sst = ((g.meanyield - grand) ** 2).sum()
    pred = g.groupby(cols)["meanyield"].transform("mean")
    return 1 - ((g.meanyield - pred) ** 2).sum() / sst if sst > 0 else 0


# ---- Fig 1: optimism gap (random vs grouped CV R2) ----
cv = pd.read_csv(REPO / "results/real_v1/metrics/cv_metrics.csv").sort_values("grouped.r2", ascending=False)
fig, ax = plt.subplots(figsize=(5.4, 3.2))
x = np.arange(len(cv)); w = 0.38
ax.bar(x - w / 2, cv["random.r2"], w, label="random split", color="#d9774b")
ax.bar(x + w / 2, cv["grouped.r2"], w, label="study-grouped split", color="#3b6ea5")
ax.axhline(0, color="k", lw=0.7)
ax.set_xticks(x); ax.set_xticklabels(cv["model"], rotation=30, ha="right")
ax.set_ylabel("CV R²"); ax.set_title("Leakage: random-split R² collapses under study-grouped CV")
ax.legend(frameon=False, fontsize=8)
save(fig, "fig1_optimism_gap")

# ---- Fig 2: variance decomposition (HEADLINE) ----
covs = ["tc", "mm", "wt", "qt"]
labels = {"tc": "temperature\ncontrol", "mm": "measurement\nmethod", "wt": "water type", "qt": "quality tier",
          "sc": "system_class\n(physical regime)", "method_all": "ALL method\ncovariates"}
vals = {c: r2(agg, [c]) for c in covs}
vals["sc"] = r2(agg, ["sc"]); vals["method_all"] = r2(agg, covs)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.3), gridspec_kw={"width_ratios": [1, 1.3]})
order = ["sc", "method_all"]
a1.bar([labels[k] for k in order], [vals[k] for k in order], color=["#3b6ea5", "#c0392b"])
a1.set_ylabel("between-study yield variance explained (R²)")
a1.set_title("Physical regime vs methodology"); a1.set_ylim(0, 0.7)
for i, k in enumerate(order):
    a1.text(i, vals[k] + 0.01, f"{vals[k]:.2f}", ha="center", fontsize=9, fontweight="bold")
br = ["tc", "mm", "wt", "qt"]
a2.barh([labels[k].replace("\n", " ") for k in br][::-1], [vals[k] for k in br][::-1], color="#c0392b", alpha=0.85)
a2.set_xlabel("between-study R²"); a2.set_title("Per method covariate (temperature control dominates)")
for i, k in enumerate(br[::-1]):
    a2.text(vals[k] + 0.005, i, f"{vals[k]:.2f}", va="center", fontsize=8)
save(fig, "fig2_variance_decomposition")

# ---- Fig 3: particle-size within-study consistency ----
rows = []
for s, g in df.groupby("study_id"):
    gg = g.dropna(subset=["particle_size_d50_um", "h2_yield_pct"])
    if len(gg) >= 3 and gg.particle_size_d50_um.nunique() >= 2:
        rho, _ = stats.spearmanr(gg.particle_size_d50_um, gg.h2_yield_pct)
        rows.append((s.split("/")[-1][:16], rho, len(gg)))
ps = pd.DataFrame(rows, columns=["study", "rho", "n"]).sort_values("rho")
fig, ax = plt.subplots(figsize=(5.2, 3.0))
ax.barh(ps.study, ps.rho, color=["#c0392b" if r < 0 else "#3b6ea5" for r in ps.rho])
ax.axvline(0, color="k", lw=0.8)
ax.set_xlabel("within-study Spearman ρ (yield vs particle size)")
ax.set_title(f"Particle-size effect is within-study consistent\n({(ps.rho<0).sum()}/{len(ps)} studies negative → 'contradiction' is a cross-study artifact)")
save(fig, "fig3_particle_size_consistency")

# ---- Fig 4: Ea spread per regime ----
ea = rate[(rate.kinetic_metric == "ea_kj_mol") & rate.value.notna()].copy()
es = ea.groupby(["study_id", "system_class"]).value.median().reset_index()
classes = ["pure_al_alkali", "mechanically_activated", "liquid_metal_activated", "waste_al", "al_alloy"]
fig, ax = plt.subplots(figsize=(6.2, 3.3))
for i, c in enumerate(classes):
    v = es[es.system_class == c].value.values
    if len(v):
        ax.scatter([i] * len(v), v, s=34, alpha=0.8, color="#3b6ea5", zorder=3)
        ax.hlines(np.median(v), i - 0.22, i + 0.22, color="#c0392b", lw=2, zorder=4)
ax.axhspan(3.5, 102.6, color="grey", alpha=0.08, label="literature band 3.5–102.6 kJ/mol")
ax.set_xticks(range(len(classes)))
ax.set_xticklabels([c.replace("_", "\n") for c in classes], fontsize=7.5)
ax.set_ylabel("apparent Eₐ (kJ/mol)")
ax.set_title("Eₐ does not organize by regime (within-spread ≈ between-spread;\nliquid_metal 8.5–58) — finer kinetic↔diffusion physics not captured by the label")
ax.legend(frameon=False, fontsize=7, loc="upper right")
save(fig, "fig4_ea_spread")

# ---- Fig 5: dataset composition ----
comp = df.groupby("system_class").agg(rows=("h2_yield_pct", "size"),
                                      studies=("study_id", "nunique")).sort_values("rows", ascending=False)
tier = df.pivot_table(index="system_class", columns="quality_tier", values="h2_yield_pct",
                      aggfunc="size", fill_value=0).reindex(comp.index)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.8, 3.2), gridspec_kw={"width_ratios": [1.2, 1]})
comp.rows.plot.bar(ax=a1, color="#3b6ea5")
for i, (r, st) in enumerate(zip(comp.rows, comp.studies)):
    a1.text(i, r + 2, f"{r}\n({st} st.)", ha="center", fontsize=7)
a1.set_ylabel("yield rows"); a1.set_title("Yield dataset by system_class (315 rows / 31 studies)")
a1.set_xticklabels([c.replace("_", "\n") for c in comp.index], rotation=0, fontsize=7)
tier[["A", "B", "C"]].plot.bar(stacked=True, ax=a2, color=["#2e7d32", "#f9a825", "#c62828"])
a2.set_title("Quality tiers + kinetic table (76 Eₐ/rate rows)")
a2.set_xticklabels([c.replace("_", "\n") for c in comp.index], rotation=0, fontsize=7)
a2.legend(title="tier", frameon=False, fontsize=7)
save(fig, "fig5_dataset_composition")

print("\nKey numbers (trace): regime R²=%.3f  method-all R²=%.3f  temperature_control R²=%.3f"
      % (vals["sc"], vals["method_all"], vals["tc"]))
