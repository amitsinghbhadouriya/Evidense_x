"""Abstract protocol definition for tabular missing value imputation algorithms."""
from abc import ABC, abstractmethod
import pandas as pd
from typing import Any

class BaseTabularImputer(ABC):
    """Abstract protocol for tabular imputation transformers."""
    
    @abstractmethod
    def fit_transform(self, df: pd.DataFrame, **kwargs: Any) -> pd.DataFrame:
        """Fit imputation parameters on input data and return completed DataFrame."""
        pass
