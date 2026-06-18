import os
import random

import numpy as np


def set_seed(seed: int = 42) -> None:
    """Set process-wide RNG seeds for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
