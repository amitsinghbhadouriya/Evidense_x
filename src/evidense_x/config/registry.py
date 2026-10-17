from typing import Dict
from .benchmark_config import BenchmarkConfig

CONFIG_REGISTRY: Dict[str, BenchmarkConfig] = {}

def register_config(name: str, cfg: BenchmarkConfig):
    CONFIG_REGISTRY[name] = cfg

def get_registered_config(name: str) -> BenchmarkConfig:
    return CONFIG_REGISTRY[name]
