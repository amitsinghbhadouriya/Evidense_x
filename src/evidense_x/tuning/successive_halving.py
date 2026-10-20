"""Successive Halving multi-fidelity resource scheduler for fast candidate pruning."""
import numpy as np
from typing import List, Dict, Any

class SuccessiveHalvingScheduler:
    """Iteratively discards bottom candidate configurations while increasing sample budget."""
    
    def __init__(self, eta: int = 3, min_budget: float = 0.2) -> None:
        self.eta = eta
        self.min_budget = min_budget
        
    def filter_top_candidates(self, candidates: List[Dict[str, Any]], scores: List[float]) -> List[Dict[str, Any]]:
        n_survivors = max(1, len(candidates) // self.eta)
        top_indices = np.argsort(scores)[::-1][:n_survivors]
        return [candidates[i] for i in top_indices]
