"""Abstract protocol definition for ensemble model combination methods."""
from abc import ABC, abstractmethod
import numpy as np
from typing import List, Any

class BaseEnsembleCombiner(ABC):
    """Protocol for ensembling predictions from multiple base model wrappers."""
    
    @abstractmethod
    def fit(self, base_models: List[Any], X: np.ndarray, y: np.ndarray) -> "BaseEnsembleCombiner":
        """Fit ensemble meta-weights or estimators."""
        pass
        
    @abstractmethod
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Combine probability distributions across ensemble learners."""
        pass
