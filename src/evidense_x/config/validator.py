from .benchmark_config import BenchmarkConfig

def validate_config(cfg: BenchmarkConfig) -> bool:
    if not cfg.models:
        raise ValueError("Config must specify at least one model.")
    if any(m < 0.0 or m > 1.0 for m in cfg.missing_rates):
        raise ValueError("Missing rates must be within [0.0, 1.0].")
    return True
