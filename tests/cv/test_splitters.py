import numpy as np

from src.cv.splitters import grouped_kfold_splits, loso_splits


def _groups():
    return np.array([f"s{i // 4}" for i in range(40)])  # 10 studies x 4 rows


def test_grouped_kfold_no_study_leak():
    groups = _groups()
    for train_idx, test_idx in grouped_kfold_splits(n_rows=40, groups=groups, n_splits=5, seed=0):
        assert set(groups[train_idx]).isdisjoint(set(groups[test_idx]))


def test_loso_leaves_one_study_out():
    groups = _groups()
    splits = list(loso_splits(groups))
    assert len(splits) == 10
    for train_idx, test_idx in splits:
        assert len(set(groups[test_idx])) == 1
        assert set(groups[train_idx]).isdisjoint(set(groups[test_idx]))
