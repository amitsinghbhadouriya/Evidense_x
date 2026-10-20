"""UCI Machine Learning Repository automated dataset fetcher and parser."""
import pandas as pd
import urllib.request
from typing import Optional, List

class UCIDatasetLoader:
    """Downloads and formats standard tabular datasets from the UCI repository."""
    
    UCI_BASE = "https://archive.ics.uci.edu/ml/machine-learning-databases"
    
    def fetch_csv(self, relative_url: str, column_names: Optional[List[str]] = None, sep: str = ",") -> pd.DataFrame:
        full_url = f"{self.UCI_BASE}/{relative_url}"
        df = pd.read_csv(full_url, names=column_names, sep=sep)
        return df
