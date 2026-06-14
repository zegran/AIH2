from pathlib import Path

from run.pipeline.run_phase1 import run_pipeline
from src.data_module.fixture import write_fixture


def test_pipeline_produces_metrics_and_importance(tmp_path: Path):
    data_path = tmp_path / "fix.csv"
    write_fixture(str(data_path), n_studies=25, rows_per_study=8, seed=9)
    out = run_pipeline(
        data_path=str(data_path), model_names=["lightgbm"], n_splits=4, seed=0,
        output_dir=str(tmp_path / "out"), primary_model="lightgbm",
    )
    assert (Path(out) / "metrics" / "cv_metrics.csv").exists()
    assert (Path(out) / "tables" / "permutation_importance.csv").exists()
