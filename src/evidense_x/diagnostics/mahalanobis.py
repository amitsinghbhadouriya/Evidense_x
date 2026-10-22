"""Multivariate Mahalanobis distance auditor with empirical covariance regularization."""
from typing import Dict, Any, Optional
import numpy as np
import pandas as pd
from scipy.spatial.distance import mahalanobis
from scipy.stats import chi2
from .base import BaseAnomalyDetector


class RobustMahalanobisAuditor(BaseAnomalyDetector):
    """Audits multivariate numerical records using regularized Mahalanobis distance."""

    def __init__(
        self,
        contamination: float = 0.05,
        shrinkage: float = 0.1,
    ) -> None:
        super().__init__(contamination=contamination)
        self.shrinkage = shrinkage
        self.mean_vector: Optional[np.ndarray] = None
        self.inv_cov_matrix: Optional[np.ndarray] = None
        self.critical_value: Optional[float] = None
        self.num_features: int = 0
        self.feature_names: list = []

    def fit(self, X: pd.DataFrame, **kwargs: Any) -> "RobustMahalanobisAuditor":
        """Compute empirical centroid and regularized inverse covariance matrix."""
        numeric_cols = X.select_dtypes(include=[np.number]).columns.tolist()
        self.feature_names = numeric_cols
        self.num_features = len(numeric_cols)
        if self.num_features == 0:
            raise ValueError("RobustMahalanobisAuditor requires at least one numeric feature.")

        vals = X[numeric_cols].fillna(0.0).to_numpy()
        self.mean_vector = np.mean(vals, axis=0)
        cov = np.cov(vals, rowvar=False)
        if cov.ndim == 0:
            cov = np.array([[float(cov)]])
        # Regularize covariance matrix to prevent singularity
        cov = (1 - self.shrinkage) * cov + self.shrinkage * np.eye(self.num_features) * np.trace(cov) / max(1, self.num_features)
        self.inv_cov_matrix = np.linalg.pinv(cov)
        # Determine chi-squared critical threshold
        self.critical_value = float(chi2.ppf(1.0 - self.contamination, df=max(1, self.num_features)))
        self.is_fitted = True
        return self

    def score_samples(self, X: pd.DataFrame) -> np.ndarray:
        """Compute squared Mahalanobis distance for each row."""
        if not self.is_fitted or self.mean_vector is None or self.inv_cov_matrix is None:
            raise ValueError("Auditor must be fitted before scoring samples.")
        vals = X[self.feature_names].fillna(0.0).to_numpy()
        diff = vals - self.mean_vector
        # Vectorized quadratic form: diag(diff @ inv_cov @ diff.T)
        left = np.dot(diff, self.inv_cov_matrix)
        distances = np.sum(left * diff, axis=1)
        return distances

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """Predict 1 for inlier and -1 for multivariate outlier."""
        distances = self.score_samples(X)
        threshold = self.critical_value if self.critical_value is not None else 10.0
        return np.where(distances <= threshold, 1, -1)
