"""Super Learner stacking classifier with out-of-fold cross-validated meta-feature training."""
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from typing import List, Any
from .base_ensemble import BaseEnsembleCombiner

class SuperLearnerStackingClassifier(BaseEnsembleCombiner):
    """Stacking meta-learner trained on out-of-fold level-0 cross-validation probability outputs."""
    
    def __init__(self, n_splits: int = 3) -> None:
        self.n_splits = n_splits
        self.meta_learner = LogisticRegression()
        self.models: List[Any] = []
        
    def fit(self, base_models: List[Any], X: np.ndarray, y: np.ndarray) -> "SuperLearnerStackingClassifier":
        self.models = base_models
        skf = StratifiedKFold(n_splits=self.n_splits, shuffle=True, random_state=42)
        oof_preds = np.zeros((len(X), len(base_models)))
        
        for tr, val in skf.split(X, y):
            for m_idx, model in enumerate(base_models):
                clone = type(model)()
                clone.fit(X[tr], y[tr])
                oof_preds[val, m_idx] = clone.predict_proba(X[val])[:, 1]
                
        self.meta_learner.fit(oof_preds, y)
        for m in self.models:
            m.fit(X, y)
        return self
        
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        level0_preds = np.column_stack([m.predict_proba(X)[:, 1] for m in self.models])
        return self.meta_learner.predict_proba(level0_preds)
