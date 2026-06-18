"""Arrhenius activation-energy fitting and literature-band validation."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

_R = 8.314  # J/mol/K
LITERATURE_EA_BAND_KJ = (3.5, 102.6)


@dataclass
class ArrheniusFit:
    ea_j_mol: float
    pre_exponential: float
    r2: float


def fit_arrhenius(temperature_k: np.ndarray, rate_constant: np.ndarray) -> ArrheniusFit:
    """Fit ln k = ln A - Ea/(R T). Slope = -Ea/R."""
    inv_t = (1.0 / np.asarray(temperature_k, dtype=float)).reshape(-1, 1)
    ln_k = np.log(np.asarray(rate_constant, dtype=float))
    reg = LinearRegression().fit(inv_t, ln_k)
    ea = -reg.coef_[0] * _R
    r2 = r2_score(ln_k, reg.predict(inv_t))
    return ArrheniusFit(
        ea_j_mol=float(ea), pre_exponential=float(np.exp(reg.intercept_)), r2=float(r2)
    )


def within_literature_band(ea_j_mol: float) -> bool:
    lo, hi = LITERATURE_EA_BAND_KJ
    return lo * 1000 <= ea_j_mol <= hi * 1000
