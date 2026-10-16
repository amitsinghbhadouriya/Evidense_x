from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class DatasetSchema:
    name: str
    target_column: str
    numeric_features: List[str]
    categorical_features: List[str] = field(default_factory=list)
    positive_label: int = 1

@dataclass
class DataCharacteristics:
    dataset_name: str
    total_records: int
    total_features: int
    duplicate_rows: int
    duplicate_percentage: float
    positive_class_ratio: float
    source_missing_count: int

@dataclass
class SplitConfig:
    test_size: float = 0.25
    random_seed: int = 42
    stratify: bool = True
    enforce_group_isolation: bool = True
