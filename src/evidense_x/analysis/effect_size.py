"""Standardized effect size estimators including Cohen's d and Hedges' g."""
import numpy as np
from typing import Dict, Any

def compute_hedges_g(group1: np.ndarray, group2: np.ndarray) -> float:
    """Calculates bias-corrected Hedges' g effect size between two sample distributions."""
    n1, n2 = len(group1), len(group2)
    s1, s2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    s_pooled = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
    
    if s_pooled == 0:
        return 0.0
    d = (np.mean(group1) - np.mean(group2)) / s_pooled
    correction = 1.0 - (3.0 / (4.0 * (n1 + n2) - 9.0))
    return float(d * correction)
