"""Stability of SHAP-based feature importance ranking across grouped folds.

Per-fold |SHAP| importances are aggregated back to the ORIGINAL features (one-hot columns
summed per source categorical) before ranking. This keeps the ranking length fold-invariant
even when folds expose different categorical levels, and makes the metric reflect the
parameter hierarchy the study cares about rather than individual one-hot columns.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from src.analysis.xai.shap_analysis import compute_tree_shap
from src.cv.splitters import grouped_kfold_splits
from src.data_module import schema


def _aggregate_to_original(importance: np.ndarray, feature_names: list[str]) -> pd.Series:
    """Sum transformed-column importances back onto their original feature name."""
    agg: dict[str, float] = {}
    for imp, name in zip(importance, feature_names, strict=False):
        base = name.split("__", 1)[1] if "__" in name else name
        original = base
        for cat in schema.CATEGORICAL_FEATURES:
            if base == cat or base.startswith(cat + "_"):
                original = cat
                break
        agg[original] = agg.get(original, 0.0) + abs(float(imp))
    return pd.Series(agg)


def shap_rank_stability(df: pd.DataFrame, n_splits: int = 4, seed: int = 0) -> float:
    """Mean pairwise Spearman correlation of original-feature importance rankings across folds."""
    groups = df[schema.GROUP_COLUMN].to_numpy()
    rankings: list[pd.Series] = []
    for train_idx, _ in grouped_kfold_splits(len(df), groups, n_splits=n_splits, seed=seed):
        out = compute_tree_shap(df.iloc[train_idx], max_interaction_samples=1)
        importance = np.abs(out.values).mean(axis=0)
        rankings.append(_aggregate_to_original(importance, out.feature_names))
    corrs = []
    for i in range(len(rankings)):
        for j in range(i + 1, len(rankings)):
            a, b = rankings[i].align(rankings[j], fill_value=0.0)
            corrs.append(spearmanr(a.to_numpy(), b.to_numpy()).statistic)
    return float(np.nanmean(corrs))
