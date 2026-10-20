"""Optimization trial history logger exporting search trajectories to CSV."""
import pandas as pd
from typing import List, Dict, Any

class OptimizationHistoryLogger:
    """Maintains sequential record of hyperparameter trial evaluations."""
    
    def __init__(self) -> None:
        self.trials: List[Dict[str, Any]] = []
        
    def log_trial(self, trial_id: int, params: Dict[str, Any], score: float) -> None:
        entry = {"trial_id": trial_id, "score": score}
        entry.update(params)
        self.trials.append(entry)
        
    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self.trials)
