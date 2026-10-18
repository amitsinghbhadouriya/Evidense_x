"""Abstract auditor base protocol for data leakage and quality certificates."""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import pandas as pd

class BaseLeakageAuditor(ABC):
    """Abstract base class for data contamination and duplicate leakage auditing."""
    
    def __init__(self, tolerance: float = 1e-5) -> None:
        self.tolerance = tolerance
        
    @abstractmethod
    def audit(self, train_df: pd.DataFrame, test_df: pd.DataFrame, **kwargs: Any) -> Dict[str, Any]:
        """Audit train and test partitions for record contamination and overlap."""
        pass
