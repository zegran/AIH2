import numpy as np

from src.cv.metrics import optimism_gap, regression_metrics


def test_regression_metrics_perfect_prediction():
    y = np.array([1.0, 2.0, 3.0])
    m = regression_metrics(y, y)
    assert m["rmse"] == 0.0
    assert m["r2"] == 1.0


def test_optimism_gap_positive_when_random_better():
    gap = optimism_gap(random_score=0.9, grouped_score=0.6)
    assert abs(gap - 0.3) < 1e-9
