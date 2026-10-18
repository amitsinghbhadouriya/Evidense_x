"""Core abstract protocol interfaces for Evidense-X data defect auditors and injectors."""
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Tuple
import numpy as np
import pandas as pd

class BaseDefectSimulator(ABC):
    """Abstract base class for all tabular defect simulation routines."""
    
    def __init__(self, random_state: Optional[int] = None) -> None:
        self.random_state = random_state
        self.rng = np.random.default_rng(random_state)
        
    @abstractmethod
    def inject(self, df: pd.DataFrame, rate: float, **kwargs: Any) -> pd.DataFrame:
        """Inject synthetic data defects into the provided tabular dataframe."""
        pass
