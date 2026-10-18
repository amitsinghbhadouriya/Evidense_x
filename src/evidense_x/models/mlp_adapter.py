"""Multi-layer Perceptron Neural Network adapter for tabular classification."""
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from .model_protocol import TabularModelWrapper

class MLPAdapter(TabularModelWrapper):
    """Deep feedforward neural network adapter for complex non-linear boundary modeling."""
    
    def __init__(self, hidden_layer_sizes=(64, 32), random_state: int = 42) -> None:
        self.pipeline = Pipeline([
            ("scaler", StandardScaler()),
            ("mlp", MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, max_iter=300, random_state=random_state))
        ])
        
    def fit(self, X: np.ndarray, y: np.ndarray) -> "MLPAdapter":
        self.pipeline.fit(X, y)
        return self
        
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        return self.pipeline.predict_proba(X)
