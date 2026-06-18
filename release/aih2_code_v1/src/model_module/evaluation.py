"""Cross-validated evaluation under random vs grouped protocols."""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.model_selection import KFold

from src.cv.metrics import optimism_gap, regression_metrics
from src.cv.splitters import grouped_kfold_splits
from src.data_module import schema
from src.model_module.registry import build_model


def _cv_predict(model, x: pd.DataFrame, y: np.ndarray, splits) -> tuple[np.ndarray, np.ndarray]:
    y_true, y_pred = [], []
    for train_idx, test_idx in splits:
        m = clone(model)
        m.fit(x.iloc[train_idx], y[train_idx])
        y_pred.append(m.predict(x.iloc[test_idx]))
        y_true.append(y[test_idx])
    return np.concatenate(y_true), np.concatenate(y_pred)


def evaluate_model(name: str, df: pd.DataFrame, n_splits: int = 5, seed: int = 0) -> dict:
    x = df[schema.MODEL_FEATURES]
    y = df[schema.TARGET].to_numpy()
    groups = df[schema.GROUP_COLUMN].to_numpy()
    model = build_model(name)

    random_splits = list(KFold(n_splits=n_splits, shuffle=True, random_state=seed).split(x))
    grouped = list(grouped_kfold_splits(len(df), groups, n_splits=n_splits, seed=seed))

    yt_r, yp_r = _cv_predict(model, x, y, random_splits)
    yt_g, yp_g = _cv_predict(model, x, y, grouped)
    random_m = regression_metrics(yt_r, yp_r)
    grouped_m = regression_metrics(yt_g, yp_g)
    return {
        "model": name,
        "random": random_m,
        "grouped": grouped_m,
        "optimism_gap_r2": optimism_gap(random_m["r2"], grouped_m["r2"]),
    }
