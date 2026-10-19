"""Temporal non-overlapping block splitter preventing lookahead contamination."""
import numpy as np
import pandas as pd
from typing import Generator, Tuple

class TemporalBlockSplitter:
    """Forward-chaining sliding window temporal splitter with zero future leakage."""
    
    def __init__(self, train_window_size: int, test_window_size: int, step_size: int) -> None:
        self.train_window_size = train_window_size
        self.test_window_size = test_window_size
        self.step_size = step_size
        
    def split(self, df: pd.DataFrame) -> Generator[Tuple[np.ndarray, np.ndarray], None, None]:
        n = len(df)
        start = 0
        while start + self.train_window_size + self.test_window_size <= n:
            train_idx = np.arange(start, start + self.train_window_size)
            test_idx = np.arange(start + self.train_window_size, start + self.train_window_size + self.test_window_size)
            yield train_idx, test_idx
            start += self.step_size
