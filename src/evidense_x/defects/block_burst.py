"""Correlated temporal and batch burst missingness defect simulator."""
import numpy as np
import pandas as pd
from typing import Optional, List
from ..core.interfaces import BaseDefectSimulator

class BlockBurstMissingness(BaseDefectSimulator):
    """Simulates sensor outages where contiguous blocks of rows experience simultaneous missingness."""
    
    def inject(self, df: pd.DataFrame, rate: float, burst_length: int = 10, **kwargs) -> pd.DataFrame:
        out = df.copy()
        total_rows = len(out)
        target_missing_rows = int(total_rows * rate)
        n_bursts = max(1, target_missing_rows // burst_length)
        
        for _ in range(n_bursts):
            start_idx = self.rng.integers(0, max(1, total_rows - burst_length))
            end_idx = min(total_rows, start_idx + burst_length)
            cols = self.rng.choice(out.columns, size=max(1, len(out.columns) // 2), replace=False)
            out.iloc[start_idx:end_idx, [out.columns.get_loc(c) for c in cols]] = np.nan
        return out
