"""Continuous feature perturbation injector simulating measurement sensor noise."""
import numpy as np
import pandas as pd
from typing import Optional, List
from ..core.interfaces import BaseDefectSimulator

class GaussianJitterInjector(BaseDefectSimulator):
    """Applies zero-mean Gaussian jitter proportional to feature standard deviation."""
    
    def inject(self, df: pd.DataFrame, rate: float, target_cols: Optional[List[str]] = None, noise_scale: float = 0.1, **kwargs) -> pd.DataFrame:
        out = df.copy()
        num_cols = target_cols or list(out.select_dtypes(include=[np.number]).columns)
        
        mask = self.rng.uniform(0, 1, size=len(out)) < rate
        for col in num_cols:
            std = out[col].std()
            if np.isnan(std) or std == 0:
                std = 1.0
            noise = self.rng.normal(0, noise_scale * std, size=mask.sum())
            out.loc[mask, col] += noise
        return out
