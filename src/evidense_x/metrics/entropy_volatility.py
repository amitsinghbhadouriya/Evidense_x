"""Prediction entropy volatility measuring uncertainty variance under defect perturbations."""
import numpy as np

def compute_prediction_entropy_volatility(prob_matrices: np.ndarray) -> float:
    """Calculates empirical variance of Shannon entropy across stochastic benchmark seeds."""
    # prob_matrices shape: (n_seeds, n_samples)
    entropies = []
    for probs in prob_matrices:
        p = np.clip(probs, 1e-7, 1.0 - 1e-7)
        ent = - (p * np.log2(p) + (1.0 - p) * np.log2(1.0 - p))
        entropies.append(np.mean(ent))
    return float(np.var(entropies))
