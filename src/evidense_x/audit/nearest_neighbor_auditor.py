"""KD-Tree accelerated nearest neighbor distance leakage auditor."""
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from typing import Dict, Any
from ..core.audit_interface import BaseLeakageAuditor

class KDTreeLeakageAuditor(BaseLeakageAuditor):
    """Computes minimum Euclidean distance from each test instance to the training partition."""
    
    def audit(self, train_df: pd.DataFrame, test_df: pd.DataFrame, threshold: float = 1e-4, **kwargs) -> Dict[str, Any]:
        num_cols = list(train_df.select_dtypes(include=[np.number]).columns)
        if not num_cols:
            return {"error": "No numerical features available for KD-Tree audit."}
            
        X_train = train_df[num_cols].fillna(0).values
        X_test = test_df[num_cols].fillna(0).values
        
        nn = NearestNeighbors(n_neighbors=1, algorithm="auto").fit(X_train)
        distances, _ = nn.kneighbors(X_test)
        min_distances = distances.flatten()
        
        near_leaks = int((min_distances < threshold).sum())
        return {
            "near_leakage_count": near_leaks,
            "near_leakage_rate": float(near_leaks / max(len(test_df), 1)),
            "min_distance_observed": float(min_distances.min()),
            "mean_min_distance": float(min_distances.mean())
        }
