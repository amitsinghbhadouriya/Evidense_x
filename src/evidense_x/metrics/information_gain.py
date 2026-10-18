"""Information gain and entropy reduction metric across defect levels."""
import numpy as np

def compute_binary_entropy(p: float) -> float:
    """Compute Shannon entropy for a binary probability value."""
    if p <= 0 or p >= 1:
        return 0.0
    return float(-p * np.log2(p) - (1.0 - p) * np.log2(1.0 - p))
