"""Stability of SHAP-based feature importance ranking across grouped folds."""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from src.analysis.xai.shap_analysis import compute_tree_shap
from src.cv.splitters import grouped_kfold_splits
from src.data_module import schema


def shap_rank_stability(df: pd.DataFrame, n_splits: int = 4, seed: int = 0) -> float:
    groups = df[schema.GROUP_COLUMN].to_numpy()
    rankings = []
    for train_idx, _ in grouped_kfold_splits(len(df), groups, n_splits=n_splits, seed=seed):
        out = compute_tree_shap(df.iloc[train_idx], max_interaction_samples=1)
        importance = np.abs(out.values).mean(axis=0)
        rankings.append(importance)
    corrs = []
    for i in range(len(rankings)):
        for j in range(i + 1, len(rankings)):
            corrs.append(spearmanr(rankings[i], rankings[j]).statistic)
    return float(np.nanmean(corrs))
