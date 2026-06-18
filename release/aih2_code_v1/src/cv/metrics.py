"""Regression metrics and the random-vs-grouped optimism gap."""
from __future__ import annotations

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def regression_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    return {
        "rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))),
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "r2": float(r2_score(y_true, y_pred)),
    }


def optimism_gap(random_score: float, grouped_score: float) -> float:
    """Headline metric: how much random-split R2 overstates grouped-split R2."""
    return float(random_score - grouped_score)
