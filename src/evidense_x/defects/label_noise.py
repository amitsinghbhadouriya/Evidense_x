"""Class-conditional and symmetric classification label noise simulator."""
import numpy as np
import pandas as pd
from typing import Optional
from ..core.interfaces import BaseDefectSimulator

class ClassificationLabelNoiseInjector(BaseDefectSimulator):
    """Injects symmetric label flipping noise into classification target labels."""
    
    def inject(self, df: pd.DataFrame, rate: float, target_col: str = "target", **kwargs) -> pd.DataFrame:
        out = df.copy()
        if target_col not in out.columns:
            target_col = out.columns[-1]
            
        classes = out[target_col].dropna().unique()
        if len(classes) < 2:
            return out
            
        mask = self.rng.uniform(0, 1, size=len(out)) < rate
        n_flipped = mask.sum()
        if n_flipped > 0:
            current = out.loc[mask, target_col].values
            new_vals = []
            for c in current:
                other_classes = [cl for cl in classes if cl != c]
                new_vals.append(self.rng.choice(other_classes))
            out.loc[mask, target_col] = new_vals
        return out
