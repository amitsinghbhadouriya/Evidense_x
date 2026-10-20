"""Bayesian Model Averaging (BMA) weighting models by posterior model probabilities."""
import numpy as np
from typing import List, Dict, Any

class BayesianModelAveragingCombiner:
    """Weights models proportional to their BIC-approximated posterior evidence."""
    
    def compute_posterior_weights(self, bic_scores: List[float]) -> np.ndarray:
        delta_bic = np.array(bic_scores) - np.min(bic_scores)
        raw_weights = np.exp(-0.5 * delta_bic)
        return raw_weights / np.sum(raw_weights)
