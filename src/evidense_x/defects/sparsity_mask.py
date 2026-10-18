"""Structured checkerboard and block sparsity pattern mask generator."""
import numpy as np
import pandas as pd
from ..core.interfaces import BaseDefectSimulator

class StructuredSparsityMask(BaseDefectSimulator):
    """Imposes non-random checkerboard sparsity patterns across feature dimensions."""
    
    def inject(self, df: pd.DataFrame, rate: float, **kwargs) -> pd.DataFrame:
        out = df.copy()
        rows, cols = out.shape
        mask = (np.arange(rows)[:, None] + np.arange(cols)[None, :]) % 2 == 0
        prob_mask = self.rng.uniform(0, 1, size=(rows, cols)) < rate
        final_mask = mask & prob_mask
        
        for c_idx, col in enumerate(out.columns):
            out.loc[final_mask[:, c_idx], col] = np.nan
        return out
