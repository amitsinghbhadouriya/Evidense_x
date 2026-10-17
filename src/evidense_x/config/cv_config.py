from dataclasses import dataclass

@dataclass
class CrossValidationConfig:
    n_splits: int = 5
    stratified: bool = True
    group_aware: bool = True
    random_state: int = 42
