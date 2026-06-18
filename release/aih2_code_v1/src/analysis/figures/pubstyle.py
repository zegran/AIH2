"""Shared publication style for AIH2 figures (Elsevier/IJHE).
Okabe--Ito colorblind-safe palette, >=7 pt sans-serif fonts, embedded-font vector PDF + 300 dpi PNG,
Elsevier print sizing. Import and call apply() before plotting; use save(fig, name) to export."""
from __future__ import annotations
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt

# Okabe--Ito (colorblind-safe; distinct in grayscale when paired with marker shape)
OK = {"black": "#000000", "orange": "#E69F00", "sky": "#56B4E9", "green": "#009E73",
      "yellow": "#F0E442", "blue": "#0072B2", "vermillion": "#D55E00", "purple": "#CC79A7",
      "grey": "#999999"}
CM = 1 / 2.54
SINGLE, ONEHALF, DOUBLE = 9 * CM, 14 * CM, 19 * CM   # Elsevier column widths (cm -> in)

_OUT = Path(__file__).resolve().parents[3] / "results/real_v1/figures"


def apply() -> None:
    mpl.rcParams.update({
        "figure.dpi": 150, "savefig.dpi": 300, "savefig.bbox": "tight",
        "pdf.fonttype": 42, "ps.fonttype": 42,                      # embed TrueType
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 8, "axes.titlesize": 8.5, "axes.labelsize": 8,
        "xtick.labelsize": 7, "ytick.labelsize": 7, "legend.fontsize": 7,
        "axes.linewidth": 0.7, "lines.linewidth": 1.3, "lines.markersize": 5,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.alpha": 0.22, "grid.linewidth": 0.5,
        "legend.frameon": False,
    })


def save(fig, name: str) -> None:
    _OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(_OUT / f"{name}.pdf")
    fig.savefig(_OUT / f"{name}.png", dpi=300)
    plt.close(fig)
    print("wrote", name)
