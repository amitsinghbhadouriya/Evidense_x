"""Local Outlier Factor (LOF) auditor for neighborhood density defects."""
from typing import Dict, Any
import numpy as np
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor
from .base import BaseAnomalyDetector


class LocalOutlierFactorAuditor(BaseAnomalyDetector):
    """Detects rows residing in sparse feature neighborhoods using Local Outlier Factor."""

    def __init__(
        self,
        n_neighbors: int = 20,
        contamination: float = 0.05,
    ) -> None:
        super().__init__(contamination=contamination)
        self.n_neighbors = n_neighbors
        self.model = LocalOutlierFactor(
            n_neighbors=n_neighbors,
            contamination=contamination,
            novelty=True,
        )

    def fit(self, X: pd.DataFrame, **kwargs: Any) -> "LocalOutlierFactorAuditor":
        """Fit LOF model on numeric representation of training records."""
        self.feature_names = X.select_dtypes(include=[np.number]).columns.tolist()
        X_num = X[self.feature_names].fillna(0.0)
        self.model.fit(X_num)
        self.is_fitted = True
        return self

    def score_samples(self, X: pd.DataFrame) -> np.ndarray:
        """Compute negative local outlier factor (negated so higher = more anomalous)."""
        cols = getattr(self, "feature_names", None) or X.select_dtypes(include=[np.number]).columns.tolist()
        X_num = X[cols].fillna(0.0)
        return -self.model.score_samples(X_num)

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """Predict outlier status (1 for inlier, -1 for outlier)."""
        cols = getattr(self, "feature_names", None) or X.select_dtypes(include=[np.number]).columns.tolist()
        X_num = X[cols].fillna(0.0)
        return self.model.predict(X_num)

    def audit_sparsity(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Audit dataset for localized density collapse or cluster outliers."""
        scores = self.score_samples(df)
        preds = self.predict(df)
        outlier_indices = np.where(preds == -1)[0].tolist()
        return {
            "total_records": len(df),
            "outlier_count": len(outlier_indices),
            "outlier_percentage": float(len(outlier_indices) / max(1, len(df))),
            "max_lof_score": float(np.max(scores)),
            "mean_lof_score": float(np.mean(scores)),
            "outlier_row_indices": outlier_indices[:50],  # Sample first 50
        }
