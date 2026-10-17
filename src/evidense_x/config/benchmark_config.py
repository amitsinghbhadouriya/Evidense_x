from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class BenchmarkConfig:
    name: str
    dataset_name: str
    models: List[str]
    missing_rates: List[float] = field(default_factory=lambda: [0.0, 0.1, 0.2, 0.3])
    overlap_rates: List[float] = field(default_factory=lambda: [0.0, 0.1, 0.25, 0.5])
    seeds: List[int] = field(default_factory=lambda: list(range(10)))
    test_size: float = 0.25
