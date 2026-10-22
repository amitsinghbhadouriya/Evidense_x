"""Isolation Forest based anomaly and contamination drift detector."""
from typing import Dict, Any, Optional
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from .base import BaseAnomalyDetector


class IsolationForestDriftDetector(BaseAnomalyDetector):
    """Measures shifts in average path length and anomaly density using Isolation Forests."""

    def __init__(
        self,
        n_estimators: int = 100,
        contamination: float = 0.05,
        random_state: int = 42,
    ) -> None:
        super().__init__(contamination=contamination)
        self.n_estimators = n_estimators
        self.random_state = random_state
        self.model = IsolationForest(
            n_estimators=n_estimators,
            contamination=contamination,
            random_state=random_state,
        )
        self.baseline_mean_score: Optional[float] = None

    def fit(self, X: pd.DataFrame, **kwargs: Any) -> "IsolationForestDriftDetector":
        """Fit forest on numerical features of baseline dataset."""
        numeric_cols = X.select_dtypes(include=[np.number]).columns
        X_num = X[numeric_cols].fillna(0.0)
        self.model.fit(X_num)
        self.baseline_mean_score = float(np.mean(-self.model.score_samples(X_num)))
        self.is_fitted = True
        return self

    def score_samples(self, X: pd.DataFrame) -> np.ndarray:
        """Return inverted anomaly score (higher = more anomalous)."""
        numeric_cols = X.select_dtypes(include=[np.number]).columns
        X_num = X[numeric_cols].fillna(0.0)
        return -self.model.score_samples(X_num)

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """Classify records as inlier (1) or anomaly (-1)."""
        numeric_cols = X.select_dtypes(include=[np.number]).columns
        X_num = X[numeric_cols].fillna(0.0)
        return self.model.predict(X_num)

    def evaluate_drift(self, test_df: pd.DataFrame) -> Dict[str, Any]:
        """Compare test set anomaly score distribution against baseline."""
        if not self.is_fitted:
            raise ValueError("Detector must be fitted prior to evaluating drift.")
        test_scores = self.score_samples(test_df)
        test_mean = float(np.mean(test_scores))
        drift_delta = test_mean - (self.baseline_mean_score or 0.0)
        anomaly_ratio = float(np.mean(self.predict(test_df) == -1))
        return {
            "baseline_mean_anomaly_score": self.baseline_mean_score,
            "test_mean_anomaly_score": test_mean,
            "anomaly_score_drift": drift_delta,
            "detected_anomaly_ratio": anomaly_ratio,
            "drift_detected": bool(abs(drift_delta) > 0.10 or anomaly_ratio > self.contamination * 2),
        }
