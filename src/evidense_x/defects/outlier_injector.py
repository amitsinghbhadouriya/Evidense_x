"""Heavy-tailed Cauchy outlier injector for robustness testing."""
import numpy as np
import pandas as pd
from ..core.interfaces import BaseDefectSimulator

class CauchyOutlierInjector(BaseDefectSimulator):
    """Injects extreme heavy-tailed outliers sampled from a standard Cauchy distribution."""
    
    def inject(self, df: pd.DataFrame, rate: float, **kwargs) -> pd.DataFrame:
        out = df.copy()
        num_cols = list(out.select_dtypes(include=[np.number]).columns)
        if not num_cols:
            return out
            
        mask = self.rng.uniform(0, 1, size=len(out)) < rate
        n_outliers = mask.sum()
        if n_outliers == 0:
            return out
            
        for col in num_cols:
            iqr = out[col].quantile(0.75) - out[col].quantile(0.25)
            scale = iqr if iqr > 0 else (out[col].std() or 1.0)
            cauchy_noise = self.rng.standard_cauchy(size=n_outliers) * scale * 3.0
            out.loc[mask, col] += cauchy_noise
        return out
