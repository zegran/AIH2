"""Permutation importance (model-agnostic sanity check)."""
from __future__ import annotations

import pandas as pd
from sklearn.inspection import permutation_importance

from src.data_module import schema
from src.model_module.registry import build_model


def permutation_scores(
    df: pd.DataFrame, model_name: str = "lightgbm", n_repeats: int = 10, seed: int = 0
) -> pd.Series:
    pipe = build_model(model_name)
    x = df[schema.MODEL_FEATURES]
    y = df[schema.TARGET].to_numpy()
    pipe.fit(x, y)
    result = permutation_importance(pipe, x, y, n_repeats=n_repeats, random_state=seed)
    return pd.Series(result.importances_mean, index=schema.MODEL_FEATURES).sort_values(
        ascending=False
    )
