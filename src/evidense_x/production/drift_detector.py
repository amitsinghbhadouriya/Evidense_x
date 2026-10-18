"""Production Kolmogorov-Smirnov drift detector for online inference batches."""
import numpy as np
import pandas as pd
from scipy import stats
from typing import Dict, Any

class OnlineBatchDriftDetector:
    """Detects continuous distribution drift on incoming production inference batches."""
    
    def __init__(self, reference_df: pd.DataFrame, alpha: float = 0.05) -> None:
        self.reference_df = reference_df
        self.alpha = alpha
        
    def check_batch(self, batch_df: pd.DataFrame) -> Dict[str, Any]:
        drifted_features = []
        num_cols = list(self.reference_df.select_dtypes(include=[np.number]).columns)
        
        for col in num_cols:
            if col in batch_df.columns:
                stat, pval = stats.ks_2samp(self.reference_df[col].dropna(), batch_df[col].dropna())
                if pval < self.alpha:
                    drifted_features.append(col)
                    
        return {
            "drift_detected": len(drifted_features) > 0,
            "drifted_feature_count": len(drifted_features),
            "drifted_features": drifted_features
        }
