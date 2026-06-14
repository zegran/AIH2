"""Study-aware cross-validation splitters (leakage control)."""
from __future__ import annotations

from collections.abc import Iterator

import numpy as np
from sklearn.model_selection import GroupKFold, LeaveOneGroupOut


def grouped_kfold_splits(
    n_rows: int, groups: np.ndarray, n_splits: int = 5, seed: int = 0
) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    x = np.zeros((n_rows, 1))
    # Shuffle group order deterministically for fold balance.
    rng = np.random.default_rng(seed)
    order = rng.permutation(np.unique(groups))
    remap = {g: i for i, g in enumerate(order)}
    shuffled = np.array([remap[g] for g in groups])
    yield from GroupKFold(n_splits=n_splits).split(x, groups=shuffled)


def loso_splits(groups: np.ndarray) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    x = np.zeros((len(groups), 1))
    yield from LeaveOneGroupOut().split(x, groups=groups)
