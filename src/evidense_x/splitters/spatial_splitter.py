"""Cluster-based spatial cross-validation partitioner to attenuate spatial autocorrelation."""
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from typing import Generator, Tuple

class ClusterBasedSpatialSplitter:
    """Partitions spatial coordinates into distinct spatial clusters to prevent spatial leakage."""
    
    def __init__(self, n_clusters: int = 5, random_state: int = 42) -> None:
        self.n_clusters = n_clusters
        self.random_state = random_state
        
    def split(self, coords: np.ndarray) -> Generator[Tuple[np.ndarray, np.ndarray], None, None]:
        kmeans = KMeans(n_clusters=self.n_clusters, random_state=self.random_state, n_init=10)
        labels = kmeans.fit_predict(coords)
        for c in range(self.n_clusters):
            test_idx = np.where(labels == c)[0]
            train_idx = np.where(labels != c)[0]
            yield train_idx, test_idx
