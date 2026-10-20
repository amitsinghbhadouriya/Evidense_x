"""Abstract base class protocol for feature engineering and transformation transformers."""
from abc import ABC, abstractmethod
import pandas as pd
from typing import Any

class BaseRobustTransformer(ABC):
    """Protocol for robust feature scalers and transformers."""
    
    @abstractmethod
    def fit(self, X: pd.DataFrame, y: Any = None) -> "BaseRobustTransformer":
        """Compute transformation parameters from training distribution."""
        pass
        
    @abstractmethod
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Apply transformation to input distribution."""
        pass
        
    def fit_transform(self, X: pd.DataFrame, y: Any = None) -> pd.DataFrame:
        """Fit parameters and return transformed data."""
        return self.fit(X, y).transform(X)
