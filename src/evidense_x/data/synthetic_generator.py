"""Synthetic tabular dataset generator with controllable covariance and non-linear interactions."""
import numpy as np
import pandas as pd
from typing import Tuple, Optional

class SyntheticDefectDatasetGenerator:
    """Generates synthetic classification datasets with specified covariance topologies."""
    
    def __init__(self, n_samples: int = 1000, n_features: int = 10, random_state: Optional[int] = 42) -> None:
        self.n_samples = n_samples
        self.n_features = n_features
        self.rng = np.random.default_rng(random_state)
        
    def generate(self) -> Tuple[pd.DataFrame, np.ndarray]:
        # Generate random positive-definite covariance matrix
        A = self.rng.standard_normal((self.n_features, self.n_features))
        cov = np.dot(A, A.T) + np.eye(self.n_features) * 0.1
        X = self.rng.multivariate_normal(np.zeros(self.n_features), cov, size=self.n_samples)
        
        # Non-linear logit combination for target
        logits = X[:, 0] * 1.5 - X[:, 1] * 2.0 + (X[:, 2] ** 2) * 0.5 - np.sin(X[:, 3]) * 1.2
        probs = 1.0 / (1.0 + np.exp(-logits))
        y = (self.rng.uniform(0, 1, size=self.n_samples) < probs).astype(int)
        
        feature_names = [f"feat_{i:02d}" for i in range(self.n_features)]
        df = pd.DataFrame(X, columns=feature_names)
        return df, y
