"""L2-regularized Logistic Regression adapter with standard feature scaling."""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from .model_protocol import TabularModelWrapper

class LogisticRegressionAdapter(TabularModelWrapper):
    """Linear classification adapter with built-in variance standardization."""
    
    def __init__(self, C: float = 1.0, random_state: int = 42) -> None:
        self.pipeline = Pipeline([
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(C=C, random_state=random_state, max_iter=500))
        ])
        
    def fit(self, X: np.ndarray, y: np.ndarray) -> "LogisticRegressionAdapter":
        self.pipeline.fit(X, y)
        return self
        
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        return self.pipeline.predict_proba(X)
