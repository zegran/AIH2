"""SHAP <-> physics sign-agreement metric (Phase 2 - interface defined)."""
from __future__ import annotations

import numpy as np


def sign_agreement_rate(
    shap_local_gradients: np.ndarray, physics_gradients: np.ndarray
) -> float:
    """Fraction of points where SHAP-local and physics-predicted gradients share sign.

    Implemented in Phase 2 once SCM regimes are available.
    """
    raise NotImplementedError("Phase 2: SHAP<->physics consistency metric")
