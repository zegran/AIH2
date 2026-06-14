import numpy as np
import pytest

from src.analysis.physical_validation import shrinking_core


def test_regime_classification_is_phase2_stub():
    with pytest.raises(NotImplementedError):
        shrinking_core.classify_regime(np.array([1.0]), np.array([0.5]))
