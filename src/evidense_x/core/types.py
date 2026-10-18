"""Type aliases and common TypedDicts for Evidense-X."""
from typing import TypedDict, List, Dict, Any, Union
import numpy as np

class AuditMetricsDict(TypedDict, total=False):
    exact_duplicate_count: int
    exact_leakage_rate: float
    near_duplicate_count: int
    near_leakage_rate: float
    gower_mean_distance: float
    lsi_score: float
    eri_score: float

class DefectProfile(TypedDict):
    mechanism: str
    rate: float
    affected_columns: List[str]
    random_seed: int
