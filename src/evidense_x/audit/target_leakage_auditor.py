"""Target leakage scanner identifying surrogate features with extreme correlation to target."""
import pandas as pd
import numpy as np
from typing import Dict, List, Any

class TargetLeakageCorrelationAuditor:
    """Flags features whose mutual information or correlation exceeds safe predictive bounds."""
    
    def __init__(self, max_abs_correlation: float = 0.95) -> None:
        self.max_abs_corr = max_abs_correlation
        
    def audit_features(self, df: pd.DataFrame, target_col: str) -> Dict[str, Any]:
        if target_col not in df.columns:
            return {"error": f"Target column '{target_col}' not present."}
            
        num_cols = [c for c in df.select_dtypes(include=[np.number]).columns if c != target_col]
        leaking_features: List[str] = []
        correlations: Dict[str, float] = {}
        
        for col in num_cols:
            corr = float(df[col].corr(df[target_col]))
            correlations[col] = corr
            if abs(corr) >= self.max_abs_corr:
                leaking_features.append(col)
                
        return {
            "target_leakage_detected": len(leaking_features) > 0,
            "leaking_features": leaking_features,
            "correlations": correlations
        }
