"""Zero and near-zero variance feature auditor identifying non-informative dimensions."""
import pandas as pd
import numpy as np
from typing import Dict, List, Any

class ZeroVarianceFeatureAuditor:
    """Scans datasets for invariant or near-zero variance attributes carrying zero entropy."""
    
    def __init__(self, variance_threshold: float = 1e-6) -> None:
        self.variance_threshold = variance_threshold
        
    def audit(self, df: pd.DataFrame) -> Dict[str, Any]:
        num_cols = list(df.select_dtypes(include=[np.number]).columns)
        zero_var_cols: List[str] = []
        
        for col in num_cols:
            var = float(df[col].var())
            if np.isnan(var) or var <= self.variance_threshold:
                zero_var_cols.append(col)
                
        return {
            "zero_variance_columns": zero_var_cols,
            "has_degenerate_features": len(zero_var_cols) > 0
        }
