"""Automated OpenML benchmark dataset downloader and local disk cacher."""
import os
import pandas as pd
from typing import Optional, Tuple
from sklearn.datasets import fetch_openml

class OpenMLBenchmarkLoader:
    """Fetches benchmark datasets from OpenML with offline caching support."""
    
    def __init__(self, cache_dir: str = ".cache/openml") -> None:
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        
    def load_dataset(self, name_or_id: str) -> Tuple[pd.DataFrame, pd.Series]:
        cache_path = os.path.join(self.cache_dir, f"{name_or_id}.parquet")
        if os.path.exists(cache_path):
            df = pd.read_parquet(cache_path)
            y = df.pop("target")
            return df, y
            
        data = fetch_openml(name=name_or_id, as_frame=True, parser="auto")
        X = data.data
        y = data.target
        full = X.copy()
        full["target"] = y
        try:
            full.to_parquet(cache_path)
        except Exception:
            pass
        return X, y
