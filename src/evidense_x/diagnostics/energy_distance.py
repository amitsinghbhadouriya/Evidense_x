"""Energy distance non-parametric two-sample distribution drift detector."""
from typing import Dict, Any, Optional
import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist


class EnergyDistanceDriftDetector:
    """Computes statistical energy distance between baseline and production test partitions.
    
    Energy distance E(X, Y) = 2 E||X - Y|| - E||X - X'|| - E||Y - Y'||.
    Equals 0 if and only if distributions are identical.
    """

    def __init__(self, drift_threshold: float = 0.25, max_samples: int = 1000) -> None:
        self.drift_threshold = drift_threshold
        self.max_samples = max_samples
        self.reference_matrix: Optional[np.ndarray] = None
        self.numeric_features: list = []

    def fit(self, reference_df: pd.DataFrame) -> "EnergyDistanceDriftDetector":
        """Store reference baseline distribution."""
        cols = reference_df.select_dtypes(include=[np.number]).columns.tolist()
        self.numeric_features = cols
        vals = reference_df[cols].fillna(0.0).to_numpy()
        if len(vals) > self.max_samples:
            indices = np.random.RandomState(42).choice(len(vals), size=self.max_samples, replace=False)
            vals = vals[indices]
        self.reference_matrix = vals
        return self

    def compute_energy_distance(self, target_df: pd.DataFrame) -> float:
        """Compute statistical energy distance between target dataset and reference."""
        if self.reference_matrix is None:
            raise ValueError("Detector must be fitted with reference data.")
        target_vals = target_df[self.numeric_features].fillna(0.0).to_numpy()
        if len(target_vals) > self.max_samples:
            indices = np.random.RandomState(42).choice(len(target_vals), size=self.max_samples, replace=False)
            target_vals = target_vals[indices]

        # Calculate pairwise Euclidean distance terms
        d_xy = np.mean(cdist(self.reference_matrix, target_vals, metric="euclidean"))
        d_xx = np.mean(cdist(self.reference_matrix, self.reference_matrix, metric="euclidean"))
        d_yy = np.mean(cdist(target_vals, target_vals, metric="euclidean"))

        energy_dist = 2.0 * d_xy - d_xx - d_yy
        return float(max(0.0, energy_dist))

    def evaluate(self, target_df: pd.DataFrame) -> Dict[str, Any]:
        """Evaluate distribution drift and alert if energy distance breaches threshold."""
        dist = self.compute_energy_distance(target_df)
        return {
            "energy_distance": dist,
            "drift_threshold": self.drift_threshold,
            "is_drift_detected": bool(dist > self.drift_threshold),
            "evaluated_features_count": len(self.numeric_features),
        }
