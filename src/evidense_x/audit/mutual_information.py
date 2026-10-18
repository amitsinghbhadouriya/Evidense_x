"""Mutual information leakage scanner between train/test feature representations."""
import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_classif
from typing import Dict, Any

class MutualInformationLeakageScanner:
    """Scans for features carrying anomalous partition membership information."""
    
    def scan(self, train_df: pd.DataFrame, test_df: pd.DataFrame) -> Dict[str, float]:
        num_cols = list(train_df.select_dtypes(include=[np.number]).columns)
        if not num_cols:
            return {}
            
        X_train = train_df[num_cols].fillna(0)
        X_test = test_df[num_cols].fillna(0)
        
        X = pd.concat([X_train, X_test], ignore_index=True)
        y = np.array([0] * len(X_train) + [1] * len(X_test))
        
        mi_scores = mutual_info_classif(X, y, random_state=42)
        return {col: float(score) for col, score in zip(num_cols, mi_scores)}
