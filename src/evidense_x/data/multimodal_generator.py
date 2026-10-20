"""Mixed continuous and categorical tabular generator simulating realistic enterprise schemas."""
import numpy as np
import pandas as pd
from typing import Tuple, List, Optional

class MultiModalTabularGenerator:
    """Generates mixed-type tabular datasets containing numerical, categorical, and binary fields."""
    
    def __init__(self, n_samples: int = 1000, random_state: Optional[int] = 42) -> None:
        self.n_samples = n_samples
        self.rng = np.random.default_rng(random_state)
        
    def generate(self) -> pd.DataFrame:
        ages = self.rng.integers(18, 75, size=self.n_samples)
        incomes = np.exp(self.rng.normal(10.5, 0.8, size=self.n_samples))
        credit_scores = np.clip(self.rng.normal(680, 50, size=self.n_samples), 300, 850)
        
        education_levels = ["HighSchool", "Bachelor", "Master", "PhD"]
        education = self.rng.choice(education_levels, p=[0.3, 0.45, 0.2, 0.05], size=self.n_samples)
        
        marital_statuses = ["Single", "Married", "Divorced"]
        marital = self.rng.choice(marital_statuses, p=[0.4, 0.45, 0.15], size=self.n_samples)
        
        default_prob = 1.0 / (1.0 + np.exp((credit_scores - 650) / 40.0))
        target = (self.rng.uniform(0, 1, size=self.n_samples) < default_prob).astype(int)
        
        return pd.DataFrame({
            "age": ages,
            "annual_income": incomes,
            "credit_score": credit_scores,
            "education": education,
            "marital_status": marital,
            "target": target
        })
