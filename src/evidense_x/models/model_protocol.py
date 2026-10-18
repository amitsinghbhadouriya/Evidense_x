"""Model wrapper protocol standardizing fit and predict_proba across frameworks."""
from abc import ABC, abstractmethod
import numpy as np
from typing import Any

class TabularModelWrapper(ABC):
    """Protocol for training and inferring probabilistic classifications on tabular data."""
    
    @abstractmethod
    def fit(self, X: np.ndarray, y: np.ndarray) -> "TabularModelWrapper":
        """Train model parameters on feature matrix and target labels."""
        pass
        
    @abstractmethod
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Infer class probability distributions for test samples."""
        pass
