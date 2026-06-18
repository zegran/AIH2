"""Accumulated Local Effects on raw (untransformed) numeric features.

ALE is computed on the original feature scale by wrapping the fitted pipeline so the
predict function consumes raw model features. This avoids PDP extrapolation bias under
the correlated features in this dataset.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from src.data_module import schema
from src.model_module.registry import build_model


@dataclass
class AleResult:
    feature: str
    grid: np.ndarray
    effect: np.ndarray


def ale_for_feature(
    df: pd.DataFrame, feature: str, model_name: str = "lightgbm", bins: int = 20
) -> AleResult:
    pipe = build_model(model_name)
    x = df[schema.MODEL_FEATURES].copy()
    y = df[schema.TARGET].to_numpy()
    pipe.fit(x, y)

    values = x[feature].to_numpy(dtype=float)
    quantiles = np.unique(np.nanquantile(values, np.linspace(0, 1, bins + 1)))
    local_effects = []
    for lo, hi in zip(quantiles[:-1], quantiles[1:], strict=False):
        mask = (values >= lo) & (values <= hi)
        if mask.sum() == 0:
            local_effects.append(0.0)
            continue
        x_lo, x_hi = x[mask].copy(), x[mask].copy()
        x_lo[feature] = lo
        x_hi[feature] = hi
        delta = pipe.predict(x_hi) - pipe.predict(x_lo)
        local_effects.append(float(np.mean(delta)))
    effect = np.cumsum(local_effects)
    effect = effect - effect.mean()  # center
    centers = (quantiles[:-1] + quantiles[1:]) / 2
    return AleResult(feature=feature, grid=centers, effect=effect)
