"""Benjamini-Hochberg False Discovery Rate (FDR) p-value correction."""
import numpy as np
from typing import List, Tuple

def benjamini_hochberg_correction(p_values: List[float], alpha: float = 0.05) -> Tuple[List[float], List[bool]]:
    """Applies Benjamini-Hochberg procedure controlling FDR under positive dependence."""
    p_arr = np.array(p_values)
    n = len(p_arr)
    sorted_indices = np.argsort(p_arr)
    sorted_p = p_arr[sorted_indices]
    
    adjusted = np.zeros(n)
    cummin = 1.0
    for i in range(n - 1, -1, -1):
        rank = i + 1
        adj = (sorted_p[i] * n) / rank
        cummin = min(cummin, adj)
        adjusted[i] = min(cummin, 1.0)
        
    rev_indices = np.argsort(sorted_indices)
    final_adj = adjusted[rev_indices]
    reject = final_adj < alpha
    return list(final_adj), list(reject)
