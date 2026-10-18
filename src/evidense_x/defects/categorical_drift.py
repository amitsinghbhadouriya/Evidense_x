"""Categorical label flip and category substitution injector."""
import numpy as np
import pandas as pd
from typing import Optional, List
from ..core.interfaces import BaseDefectSimulator

class CategoricalDriftInjector(BaseDefectSimulator):
    """Permutes categorical attributes to simulate typographic errors or category mapping drift."""
    
    def inject(self, df: pd.DataFrame, rate: float, cat_cols: Optional[List[str]] = None, **kwargs) -> pd.DataFrame:
        out = df.copy()
        target_cats = cat_cols or list(out.select_dtypes(include=["object", "category"]).columns)
        
        for col in target_cats:
            unique_vals = out[col].dropna().unique()
            if len(unique_vals) <= 1:
                continue
            mask = self.rng.uniform(0, 1, size=len(out)) < rate
            replacements = self.rng.choice(unique_vals, size=mask.sum())
            out.loc[mask, col] = replacements
        return out
