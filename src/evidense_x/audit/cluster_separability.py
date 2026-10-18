"""Cluster separability and intra-partition silhouette diagnostic auditor."""
import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score
from typing import Dict, Any

class ClusterSeparabilityAuditor:
    """Measures partition boundary fuzziness and overlap using silhouette analysis."""
    
    def evaluate_separability(self, train_df: pd.DataFrame, test_df: pd.DataFrame) -> Dict[str, Any]:
        num_cols = list(train_df.select_dtypes(include=[np.number]).columns)
        if not num_cols:
            return {"silhouette_overlap_score": 0.0}
            
        X_train = train_df[num_cols].fillna(0).values
        X_test = test_df[num_cols].fillna(0).values
        
        X = np.vstack([X_train, X_test])
        labels = np.array([0] * len(X_train) + [1] * len(X_test))
        
        if len(X) > 2000:
            idx = np.random.choice(len(X), size=2000, replace=False)
            X = X[idx]
            labels = labels[idx]
            
        score = float(silhouette_score(X, labels))
        return {
            "silhouette_overlap_score": score,
            "partitions_separable": score > 0.1
        }
