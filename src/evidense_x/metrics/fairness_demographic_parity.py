"""Demographic parity difference metric assessing subgroup selection rate parity."""
import numpy as np
from typing import Dict, Any

def compute_demographic_parity_difference(y_pred: np.ndarray, sensitive_attr: np.ndarray) -> Dict[str, float]:
    """Calculates absolute disparity in positive rate across binary sensitive groups."""
    groups = np.unique(sensitive_attr)
    if len(groups) < 2:
        return {"demographic_parity_difference": 0.0}
        
    rates = []
    for g in groups:
        mask = sensitive_attr == g
        rates.append(float(y_pred[mask].mean()))
        
    diff = max(rates) - min(rates)
    return {
        "demographic_parity_difference": float(diff),
        "group_rates": {str(g): r for g, r in zip(groups, rates)}
    }
