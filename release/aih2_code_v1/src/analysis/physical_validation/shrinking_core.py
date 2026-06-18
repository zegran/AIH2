"""Shrinking-core regime classification (Phase 2 - interface defined, not implemented)."""
from __future__ import annotations

import numpy as np


def reaction_controlled_conversion(time: np.ndarray, k: float) -> np.ndarray:
    """g(X) = 1 - (1 - X)^(1/3) = k t  ->  X(t). Implemented in Phase 2."""
    raise NotImplementedError("Phase 2: shrinking-core regime analysis")


def diffusion_controlled_conversion(time: np.ndarray, k: float) -> np.ndarray:
    """g(X) = 1 - 3(1-X)^(2/3) + 2(1-X) = k t  ->  X(t). Implemented in Phase 2."""
    raise NotImplementedError("Phase 2: shrinking-core regime analysis")


def classify_regime(time: np.ndarray, conversion: np.ndarray) -> str:
    """Return 'reaction' or 'diffusion'. Implemented in Phase 2."""
    raise NotImplementedError("Phase 2: shrinking-core regime analysis")
