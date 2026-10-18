"""Model memorization ratio measuring divergence between train and test accuracy."""
import numpy as np

def compute_memorization_ratio(train_acc: float, test_acc: float) -> float:
    """Computes empirical memorization ratio as normalized generalization gap."""
    if train_acc <= 0:
        return 0.0
    gap = max(0.0, train_acc - test_acc)
    return float(gap / train_acc)
