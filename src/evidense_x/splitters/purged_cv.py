"""Purged Walk-Forward Cross Validation with embargo buffers to eliminate serial correlation."""
import numpy as np
import pandas as pd
from typing import Generator, Tuple

class PurgedWalkForwardCV:
    """Walk-forward cross-validator with post-test embargo buffers to eliminate overlapping returns."""
    
    def __init__(self, n_splits: int = 5, embargo_pct: float = 0.02) -> None:
        self.n_splits = n_splits
        self.embargo_pct = embargo_pct
        
    def split(self, df: pd.DataFrame) -> Generator[Tuple[np.ndarray, np.ndarray], None, None]:
        n = len(df)
        fold_size = n // (self.n_splits + 1)
        embargo_size = int(n * self.embargo_pct)
        
        for i in range(1, self.n_splits + 1):
            train_end = i * fold_size
            test_start = train_end + embargo_size
            test_end = min(n, test_start + fold_size)
            if test_start >= n:
                break
            train_idx = np.arange(0, train_end)
            test_idx = np.arange(test_start, test_end)
            yield train_idx, test_idx
