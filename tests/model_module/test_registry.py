from sklearn.pipeline import Pipeline

from src.model_module import models  # noqa: F401  (registers estimators)
from src.model_module.registry import MODEL_REGISTRY, build_model


def test_all_six_models_registered():
    assert set(MODEL_REGISTRY) == {
        "elasticnet", "knn", "random_forest", "xgboost", "lightgbm", "gaussian_process"
    }


def test_build_model_returns_pipeline():
    pipe = build_model("xgboost")
    assert isinstance(pipe, Pipeline)
