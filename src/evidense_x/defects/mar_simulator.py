"""Missing At Random (MAR) logistic defect simulator."""
import numpy as np
import pandas as pd
from typing import List, Optional
from ..core.interfaces import BaseDefectSimulator

class MARLogisticSimulator(BaseDefectSimulator):
    """Simulates Missing At Random (MAR) where missingness in target depends on a predictor."""
    
    def inject(self, df: pd.DataFrame, rate: float, predictor_col: Optional[str] = None, target_cols: Optional[List[str]] = None, **kwargs) -> pd.DataFrame:
        out = df.copy()
        if predictor_col is None or predictor_col not in out.columns:
            predictor_col = out.select_dtypes(include=[np.number]).columns[0]
        if target_cols is None:
            target_cols = [c for c in out.select_dtypes(include=[np.number]).columns if c != predictor_col][:2]
            
        vals = out[predictor_col].fillna(out[predictor_col].median()).values
        normed = (vals - vals.mean()) / (vals.std() + 1e-8)
        probs = 1.0 / (1.0 + np.exp(-normed))
        probs = probs * (rate / max(probs.mean(), 1e-5))
        probs = np.clip(probs, 0.0, 1.0)
        
        mask = self.rng.uniform(0, 1, size=len(out)) < probs
        for col in target_cols:
            out.loc[mask, col] = np.nan
        return out
