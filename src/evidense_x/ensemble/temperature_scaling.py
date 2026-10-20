"""Post-hoc temperature scaling calibrator for ensemble probability logits."""
import numpy as np
from scipy.optimize import minimize
from typing import Any

class TemperatureScalingCalibrator:
    """Optimizes single temperature scalar T to calibrate ensemble logits."""
    
    def __init__(self) -> None:
        self.temperature: float = 1.0
        
    def fit(self, logits: np.ndarray, y_true: np.ndarray) -> "TemperatureScalingCalibrator":
        def nll(t):
            scaled = logits / max(t[0], 1e-4)
            probs = 1.0 / (1.0 + np.exp(-scaled))
            probs = np.clip(probs, 1e-7, 1.0 - 1e-7)
            loss = -np.mean(y_true * np.log(probs) + (1.0 - y_true) * np.log(1.0 - probs))
            return loss
            
        res = minimize(nll, x0=[1.0], bounds=[(0.05, 5.0)])
        self.temperature = float(res.x[0])
        return self
        
    def calibrate(self, logits: np.ndarray) -> np.ndarray:
        scaled = logits / self.temperature
        return 1.0 / (1.0 + np.exp(-scaled))
