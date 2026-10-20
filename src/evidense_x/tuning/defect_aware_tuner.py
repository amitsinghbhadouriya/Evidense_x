"""Defect-aware hyperparameter tuner penalizing models with high memorization of duplicate records."""
from typing import Dict, Any

class DefectAwareLossAggregator:
    """Combines empirical AUC score with memorization ratio penalty."""
    
    def __init__(self, penalty_lambda: float = 0.5) -> None:
        self.penalty_lambda = penalty_lambda
        
    def compute_penalized_score(self, test_auc: float, memorization_ratio: float) -> float:
        return float(test_auc - self.penalty_lambda * memorization_ratio)
