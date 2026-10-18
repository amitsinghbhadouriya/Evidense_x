"""Schema and boundary validation utilities for tabular datasets."""
from typing import List, Optional
import pandas as pd
from .exceptions import PartitionInconsistencyError

def validate_dataframe_schema(df: pd.DataFrame, required_cols: Optional[List[str]] = None) -> None:
    """Validate that dataframe is non-empty and contains required columns."""
    if df is None or df.empty:
        raise ValueError("DataFrame cannot be null or empty.")
    if required_cols:
        missing = [c for c in required_cols if c not in df.columns]
        if missing:
            raise PartitionInconsistencyError(f"Missing required columns: {missing}")
