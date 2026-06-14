"""Synthetic, schema-conforming fixture with embedded Arrhenius + regime-switch signal."""
from __future__ import annotations

import numpy as np
import pandas as pd

from src.data_module import schema

_R = 8.314  # J/mol/K

# Per-class apparent activation energy (J/mol) inside the literature 3.5-102.6 kJ/mol band,
# and the sign of the particle-size effect (the contradiction).
_CLASS_PARAMS = {
    "pure_al_alkali":         {"ea": 60_000, "size_sign": +1},
    "al_alloy":               {"ea": 35_000, "size_sign": -1},
    "mechanically_activated": {"ea": 20_000, "size_sign": -1},
    "liquid_metal_activated": {"ea": 8_000,  "size_sign": -1},
    "waste_al":               {"ea": 75_000, "size_sign": +1},
}


def make_fixture(n_studies: int = 40, rows_per_study: int = 10, seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    classes = list(_CLASS_PARAMS)
    rows = []
    for s in range(n_studies):
        study_id = f"10.0000/synthetic.{s:03d}"
        system_class = classes[s % len(classes)]
        params = _CLASS_PARAMS[system_class]
        for _ in range(rows_per_study):
            t_k = rng.uniform(298, 363)
            size = rng.uniform(1, 200)
            conc = rng.uniform(0.0, 6.0)
            # Arrhenius curve normalized to [0, 1] across the temperature window, so the
            # temperature effect is bounded and monotonically increasing in T per class.
            ea = params["ea"]
            rate = np.exp(-ea / (_R * t_k))
            rate_cold = np.exp(-ea / (_R * 298.0))
            rate_hot = np.exp(-ea / (_R * 363.0))
            progress = (rate - rate_cold) / (rate_hot - rate_cold)
            size_term = params["size_sign"] * (np.log(size) - np.log(50)) * 5
            yield_pct = 30 + 45 * progress + size_term + 7 * np.tanh(conc - 2)
            yield_pct = float(np.clip(yield_pct + rng.normal(0, 2.5), 0, 100))
            rows.append(_row(rng, study_id, system_class, t_k, size, conc, yield_pct))
    df = pd.DataFrame(rows)
    for col in schema.RESERVED_TARGETS:
        df[col] = np.nan
    return df


def _row(rng, study_id, system_class, t_k, size, conc, yield_pct) -> dict:
    has_alloy = system_class in ("al_alloy", "liquid_metal_activated")
    return {
        schema.GROUP_COLUMN: study_id,
        schema.TARGET: yield_pct,
        "temperature_k": t_k,
        "alkali_conc_mol_l": conc,
        "particle_size_d50_um": size,
        "activator_ratio": float(rng.uniform(0, 0.2)),
        "al_wt_pct": 100.0 - (5.0 if has_alloy else 0.0),
        "ga_wt_pct": 3.0 if has_alloy else 0.0,
        "in_wt_pct": 2.0 if has_alloy else 0.0,
        "sn_wt_pct": 0.0,
        "bi_wt_pct": 0.0,
        "mg_wt_pct": np.nan,  # unreported example (distinct from absent=0)
        "zn_wt_pct": 0.0,
        "alkali_type": "NaOH" if conc > 0.1 else "none",
        "activation_method": (
            "liquid_metal" if system_class == "liquid_metal_activated"
            else "ball_milling" if system_class == "mechanically_activated"
            else "none"
        ),
        "water_type": "DI",
        "morphology_flag": rng.choice(["powder", "flake", "nano", "foil"]),
        "system_class": system_class,
        "source_ref": "fig.2",
        "extractor": "synthetic",
        "extraction_date": "2026-06-14",
        "extraction_method": "table",
        "measurement_method": "water_displacement",
        "temperature_control": "isothermal_bath",
        "vessel_type": "closed",
        "rate_definition": "initial",
        "value_origin": "reported",
        "quality_tier": rng.choice(["A", "B", "C"], p=[0.5, 0.3, 0.2]),
    }


def write_fixture(path: str, **kwargs) -> pd.DataFrame:
    df = make_fixture(**kwargs)
    df.to_csv(path, index=False)
    return df
