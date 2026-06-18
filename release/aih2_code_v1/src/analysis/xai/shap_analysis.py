"""TreeSHAP main and 2-way interaction values on the fitted tree model."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import shap

from src.data_module import schema
from src.model_module.registry import build_model


@dataclass
class ShapResult:
    values: np.ndarray
    interaction_values: np.ndarray | None
    feature_names: list[str]
    data: np.ndarray


def compute_tree_shap(
    df: pd.DataFrame, model_name: str = "lightgbm", max_interaction_samples: int = 200
) -> ShapResult:
    pipe = build_model(model_name)
    x = df[schema.MODEL_FEATURES]
    y = df[schema.TARGET].to_numpy()
    pipe.fit(x, y)
    pre, model = pipe.named_steps["pre"], pipe.named_steps["model"]
    x_trans = np.asarray(pre.transform(x))
    names = list(pre.get_feature_names_out())

    explainer = shap.TreeExplainer(model)
    values = np.asarray(explainer.shap_values(x_trans))
    sample = x_trans[:max_interaction_samples]
    interaction = np.asarray(explainer.shap_interaction_values(sample))
    return ShapResult(values=values, interaction_values=interaction,
                      feature_names=names, data=x_trans)
