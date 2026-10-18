"""Adversarial validation classifier for detecting train/test covariate shift."""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from typing import Dict, Any

class AdversarialValidationAuditor:
    """Trains a discriminator to separate training from testing records."""
    
    def run_audit(self, train_df: pd.DataFrame, test_df: pd.DataFrame) -> Dict[str, Any]:
        num_cols = list(train_df.select_dtypes(include=[np.number]).columns)
        if not num_cols:
            return {"auc_roc": 0.5, "shift_detected": False}
            
        X_train = train_df[num_cols].fillna(0)
        X_test = test_df[num_cols].fillna(0)
        
        X = pd.concat([X_train, X_test], ignore_index=True)
        y = np.array([0] * len(X_train) + [1] * len(X_test))
        
        clf = RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42)
        scores = cross_val_score(clf, X, y, cv=3, scoring="roc_auc")
        mean_auc = float(np.mean(scores))
        
        return {
            "adversarial_auc": mean_auc,
            "significant_shift_detected": mean_auc > 0.65
        }
