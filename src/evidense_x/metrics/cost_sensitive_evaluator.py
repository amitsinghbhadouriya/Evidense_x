"""Cost-sensitive evaluation matrix supporting asymmetric false positive/negative penalties."""
import numpy as np
from typing import Dict, Any

class CostSensitiveEvaluator:
    """Calculates expected operational loss given an asymmetric cost matrix."""
    
    def __init__(self, cost_fp: float = 1.0, cost_fn: float = 5.0) -> None:
        self.cost_fp = cost_fp
        self.cost_fn = cost_fn
        
    def evaluate(self, y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
        fp = int(((y_true == 0) & (y_pred == 1)).sum())
        fn = int(((y_true == 1) & (y_pred == 0)).sum())
        total_cost = fp * self.cost_fp + fn * self.cost_fn
        return {
            "false_positives": float(fp),
            "false_negatives": float(fn),
            "total_asymmetric_cost": float(total_cost),
            "mean_cost_per_instance": float(total_cost / max(len(y_true), 1))
        }
