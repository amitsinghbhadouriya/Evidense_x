"""Riemann numerical integrated gradients approximation for differentiable tabular models."""
import numpy as np
from typing import Dict, Any

def approximate_integrated_gradients(predict_fn, baseline: np.ndarray, x: np.ndarray, m_steps: int = 20) -> np.ndarray:
    """Approximates path integral along straight line from reference baseline to input sample."""
    diff = x - baseline
    alphas = np.linspace(0.0, 1.0, m_steps + 1)
    accum = np.zeros_like(x)
    eps = 1e-5
    
    for a in alphas:
        point = baseline + a * diff
        # Numerical finite difference gradient
        grad = np.zeros_like(x)
        for i in range(len(x)):
            p_plus = point.copy()
            p_plus[i] += eps
            grad[i] = (predict_fn(p_plus.reshape(1, -1)) - predict_fn(point.reshape(1, -1))) / eps
        accum += grad
    return (diff * accum / (m_steps + 1)).flatten()
