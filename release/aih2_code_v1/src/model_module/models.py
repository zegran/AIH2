"""Concrete comparative models. Tree models keep NaN; others use linear preprocessing."""
from __future__ import annotations

from lightgbm import LGBMRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor

from src.data_module.preprocessing import make_preprocessor
from src.model_module.registry import register_model

_SEED = 42


def _pipe(kind: str, estimator) -> Pipeline:
    return Pipeline([("pre", make_preprocessor(kind)), ("model", estimator)])


@register_model("elasticnet")
def _elasticnet() -> Pipeline:
    return _pipe("linear", ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=_SEED))


@register_model("knn")
def _knn() -> Pipeline:
    return _pipe("linear", KNeighborsRegressor(n_neighbors=7))


@register_model("random_forest")
def _rf() -> Pipeline:
    return _pipe("tree", RandomForestRegressor(n_estimators=400, random_state=_SEED, n_jobs=-1))


@register_model("xgboost")
def _xgb() -> Pipeline:
    return _pipe(
        "tree",
        XGBRegressor(
            n_estimators=400, max_depth=4, learning_rate=0.05,
            subsample=0.8, colsample_bytree=0.8, random_state=_SEED,
        ),
    )


@register_model("lightgbm")
def _lgbm() -> Pipeline:
    return _pipe(
        "tree",
        LGBMRegressor(
            n_estimators=400, num_leaves=31, learning_rate=0.05,
            subsample=0.8, random_state=_SEED, verbose=-1,
        ),
    )


@register_model("gaussian_process")
def _gp() -> Pipeline:
    kernel = RBF(length_scale=1.0) + WhiteKernel(noise_level=1.0)
    return _pipe(
        "linear",
        GaussianProcessRegressor(kernel=kernel, normalize_y=True, random_state=_SEED),
    )
