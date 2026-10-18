"""Scikit-Learn Random Forest adapter with automatic out-of-fold scoring."""
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from .model_protocol import TabularModelWrapper

class RandomForestAdapter(TabularModelWrapper):
    """Adapter wrapping scikit-learn's RandomForestClassifier with robust defaults."""
    
    def __init__(self, n_estimators: int = 100, max_depth: int = 8, random_state: int = 42) -> None:
        self.clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)
        
    def fit(self, X: np.ndarray, y: np.ndarray) -> "RandomForestAdapter":
        self.clf.fit(X, y)
        return self
        
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        return self.clf.predict_proba(X)
