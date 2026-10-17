import numpy as np

def compute_brier_score(y_true, y_prob) -> float:
    return float(np.mean((np.array(y_prob) - np.array(y_true)) ** 2))
