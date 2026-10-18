"""Informative right/left censoring defect injector for duration and continuous features."""
import numpy as np
import pandas as pd
from typing import List, Optional
from ..core.interfaces import BaseDefectSimulator

class ContinuousCensoringInjector(BaseDefectSimulator):
    """Censors continuous features above a specified percentile threshold."""
    
    def inject(self, df: pd.DataFrame, rate: float, target_cols: Optional[List[str]] = None, **kwargs) -> pd.DataFrame:
        out = df.copy()
        if target_cols is None:
            target_cols = list(out.select_dtypes(include=[np.number]).columns[:3])
            
        cutoff_quantile = max(0.01, min(0.99, 1.0 - rate))
        for col in target_cols:
            if col in out.columns:
                threshold = out[col].quantile(cutoff_quantile)
                out.loc[out[col] > threshold, col] = threshold
        return out
