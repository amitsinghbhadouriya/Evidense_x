"""Pre-flight dataset sanitizer verifying types, dropping empty features, and standardizing strings."""
import pandas as pd
import numpy as np
from typing import Tuple, List

class DatasetPreflightSanitizer:
    """Preprocesses raw tabular inputs into standardized formats for benchmark evaluation."""
    
    def sanitize(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, List[str]]:
        cleaned = df.copy()
        log = []
        
        # Drop columns with 100% missing values
        all_null = [c for c in cleaned.columns if cleaned[c].isna().all()]
        if all_null:
            cleaned.drop(columns=all_null, inplace=True)
            log.append(f"Dropped completely null columns: {all_null}")
            
        # Strip trailing whitespaces in string columns
        str_cols = cleaned.select_dtypes(include=["object"]).columns
        for c in str_cols:
            cleaned[c] = cleaned[c].astype(str).str.strip()
            
        return cleaned, log
