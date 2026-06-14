from src.data_module.fixture import make_fixture
from src.model_module import models  # noqa: F401
from src.model_module.evaluation import evaluate_model


def test_evaluate_model_returns_both_protocols():
    df = make_fixture(n_studies=30, rows_per_study=8, seed=3)
    result = evaluate_model("lightgbm", df, n_splits=5, seed=0)
    assert "grouped" in result and "random" in result
    assert "r2" in result["grouped"] and "r2" in result["random"]
    assert "optimism_gap_r2" in result
