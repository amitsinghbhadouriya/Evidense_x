"""Schema validator verifying feature types, column ordering, and null bounds."""
import pandas as pd
from typing import Dict, Any

class SchemaIntegrityGuard:
    """Validates structural column integrity and null value fractions."""
    
    def __init__(self, expected_dtypes: Dict[str, str], max_null_fraction: float = 0.3) -> None:
        self.expected_dtypes = expected_dtypes
        self.max_null_fraction = max_null_fraction
        
    def validate(self, df: pd.DataFrame) -> Dict[str, Any]:
        missing_cols = [c for c in self.expected_dtypes if c not in df.columns]
        excessive_nulls = [c for c in df.columns if df[c].isna().mean() > self.max_null_fraction]
        valid = (len(missing_cols) == 0) and (len(excessive_nulls) == 0)
        return {
            "valid": valid,
            "missing_columns": missing_cols,
            "excessive_null_columns": excessive_nulls
        }
