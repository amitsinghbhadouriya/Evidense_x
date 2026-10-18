"""Histogram-based Gradient Boosting adapter for tabular data with native NaN support."""
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
from .model_protocol import TabularModelWrapper

class HistGradientBoostingAdapter(TabularModelWrapper):
    """Adapter wrapping HistGradientBoostingClassifier with native missing value tolerance."""
    
    def __init__(self, max_iter: int = 100, learning_rate: float = 0.1, random_state: int = 42) -> None:
        self.clf = HistGradientBoostingClassifier(max_iter=max_iter, learning_rate=learning_rate, random_state=random_state)
        
    def fit(self, X: np.ndarray, y: np.ndarray) -> "HistGradientBoostingAdapter":
        self.clf.fit(X, y)
        return self
        
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        return self.clf.predict_proba(X)
