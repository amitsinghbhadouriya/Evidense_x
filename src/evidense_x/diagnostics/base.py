"""Abstract base protocols for unsupervised anomaly detection and distribution diagnostics."""
from abc import ABC, abstractmethod
from typing import Dict, Any, Tuple
import numpy as np
import pandas as pd


class BaseAnomalyDetector(ABC):
    """Abstract interface for detecting corrupt, anomalous, or out-of-distribution records."""

    def __init__(self, contamination: float = 0.05) -> None:
        self.contamination = contamination
        self.is_fitted = False

    @abstractmethod
    def fit(self, X: pd.DataFrame, **kwargs: Any) -> "BaseAnomalyDetector":
        """Fit detector on baseline reference data."""
        pass

    @abstractmethod
    def score_samples(self, X: pd.DataFrame) -> np.ndarray:
        """Compute continuous anomaly score for each row (higher indicates more anomalous)."""
        pass

    @abstractmethod
    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """Predict binary indicator: 1 for inlier, -1 for anomaly."""
        pass
