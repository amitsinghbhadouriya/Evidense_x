"""Abstract protocol definition for model hyperparameter optimization algorithms."""
from abc import ABC, abstractmethod
from typing import Dict, Any, List
import pandas as pd

class BaseHyperparameterOptimizer(ABC):
    """Protocol for searching model configuration spaces under cross-validation."""
    
    @abstractmethod
    def optimize(self, X: pd.DataFrame, y: Any, param_space: Dict[str, List[Any]]) -> Dict[str, Any]:
        """Execute search over parameter combinations and return best configuration."""
        pass
