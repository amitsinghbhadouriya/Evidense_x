"""Computes contamination index matrix across k-fold cross validation splits."""
import numpy as np
import pandas as pd
from typing import List, Dict, Any

class ContaminationMatrixCalculator:
    """Computes pairwise overlap matrix across K cross-validation folds."""
    
    def compute(self, folds: List[pd.DataFrame]) -> np.ndarray:
        k = len(folds)
        matrix = np.zeros((k, k))
        hashes = [set(f.astype(str).apply("".join, axis=1)) for f in folds]
        
        for i in range(k):
            for j in range(k):
                if i == j:
                    matrix[i, j] = 1.0
                else:
                    overlap = len(hashes[i].intersection(hashes[j]))
                    matrix[i, j] = overlap / max(len(hashes[i]), 1)
        return matrix
