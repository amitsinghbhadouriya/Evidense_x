"""Abstract protocol definition for model interpretability and feature attribution engines."""
from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from typing import Dict, Any

class BaseFeatureExplainer(ABC):
    """Protocol for calculating local and global feature importance attributions."""
    
    @abstractmethod
    def explain(self, model: Any, X: pd.DataFrame, y: np.ndarray) -> Dict[str, float]:
        """Compute attribution scores for each feature in X."""
        pass
