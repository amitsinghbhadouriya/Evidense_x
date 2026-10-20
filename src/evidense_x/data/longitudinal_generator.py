"""Longitudinal patient encounter generator simulating irregular temporal observation gaps."""
import numpy as np
import pandas as pd
from typing import Optional

class LongitudinalPatientTrajectoryGenerator:
    """Generates synthetic multi-visit patient records with stochastic inter-visit intervals."""
    
    def __init__(self, n_patients: int = 200, max_visits: int = 8, random_state: Optional[int] = 42) -> None:
        self.n_patients = n_patients
        self.max_visits = max_visits
        self.rng = np.random.default_rng(random_state)
        
    def generate(self) -> pd.DataFrame:
        records = []
        for pid in range(self.n_patients):
            n_v = self.rng.integers(2, self.max_visits + 1)
            t = 0.0
            vital = self.rng.normal(120, 15)
            for v_idx in range(n_v):
                t += self.rng.exponential(30.0)
                vital += self.rng.normal(0, 5)
                records.append({
                    "patient_id": f"P{pid:04d}",
                    "visit_index": v_idx,
                    "days_since_baseline": round(t, 1),
                    "systolic_bp": round(vital, 1),
                    "event_decompensated": int(vital > 145)
                })
        return pd.DataFrame(records)
