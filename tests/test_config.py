import pytest
from evidense_x.config.benchmark_config import BenchmarkConfig
from evidense_x.config.validator import validate_config

def test_config_validation():
    cfg = BenchmarkConfig(name="test", dataset_name="synthetic", models=["Decision Tree"])
    assert validate_config(cfg) is True
