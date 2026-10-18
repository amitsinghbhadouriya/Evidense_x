"""Near-duplicate cluster generator creating dense semantic neighborhood contamination."""
import numpy as np
import pandas as pd
from ..core.interfaces import BaseDefectSimulator

class NearDuplicateClusterGenerator(BaseDefectSimulator):
    """Generates synthetic clusters centered around anchor points with controlled dispersion."""
    
    def inject(self, df: pd.DataFrame, rate: float, n_clusters: int = 5, dispersion: float = 0.05, **kwargs) -> pd.DataFrame:
        out = df.copy()
        num_cols = list(out.select_dtypes(include=[np.number]).columns)
        if not num_cols:
            return out
            
        n_perturbed = int(len(out) * rate)
        if n_perturbed == 0:
            return out
            
        anchors = out.sample(n=min(n_clusters, len(out)), random_state=self.random_state)
        new_records = []
        for _ in range(n_perturbed):
            anchor = anchors.sample(n=1, random_state=self.rng.integers(0, 10000)).copy()
            for col in num_cols:
                noise = self.rng.normal(0, dispersion * (out[col].std() or 1.0))
                anchor[col] += noise
            new_records.append(anchor)
            
        return pd.concat([out] + new_records, ignore_index=True)
