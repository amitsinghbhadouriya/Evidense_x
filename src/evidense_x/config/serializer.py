import json
from dataclasses import asdict
from .benchmark_config import BenchmarkConfig

def serialize_config_to_json(cfg: BenchmarkConfig, out_path: str):
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(asdict(cfg), f, indent=2)
