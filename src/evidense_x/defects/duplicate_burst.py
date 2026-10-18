"""Batch duplicate burst injector simulating replay attacks or telemetry double-counting."""
import pandas as pd
from ..core.interfaces import BaseDefectSimulator

class DuplicateBurstInjector(BaseDefectSimulator):
    """Samples clustered record batches and duplicates them repeatedly into the dataset."""
    
    def inject(self, df: pd.DataFrame, rate: float, cluster_size: int = 5, **kwargs) -> pd.DataFrame:
        n_duplicates = int(len(df) * rate)
        if n_duplicates <= 0:
            return df.copy()
            
        sample_indices = self.rng.choice(len(df), size=min(n_duplicates, len(df)), replace=True)
        sampled_rows = df.iloc[sample_indices].copy()
        return pd.concat([df, sampled_rows], ignore_index=True)
