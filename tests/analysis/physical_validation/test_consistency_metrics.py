import numpy as np
import pytest

from src.analysis.physical_validation import consistency_metrics


def test_consistency_metric_is_phase2_stub():
    with pytest.raises(NotImplementedError):
        consistency_metrics.sign_agreement_rate(np.array([1.0]), np.array([1.0]))
