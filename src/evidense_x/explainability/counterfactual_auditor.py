"""Counterfactual perturbation distance auditor finding minimum defect change to flip label."""
import numpy as np
import pandas as pd
from typing import Dict, Any

class CounterfactualPerturbationAuditor:
    """Measures model boundary margin via minimal L1 perturbation required to flip classification."""
    
    def audit_sample_margin(self, model: Any, sample_x: np.ndarray, current_class: int, step_size: float = 0.05, max_steps: int = 50) -> float:
        x_mut = sample_x.copy().reshape(1, -1)
        direction = 1.0 if current_class == 0 else -1.0
        for step in range(1, max_steps + 1):
            x_mut += direction * step_size
            pred = np.argmax(model.predict_proba(x_mut)[0])
            if pred != current_class:
                return float(step * step_size)
        return float(max_steps * step_size)
