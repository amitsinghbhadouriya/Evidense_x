"""High-throughput cryptographic MD5/SHA256 exact partition leakage detector."""
import hashlib
import pandas as pd
from typing import Dict, Any, Set
from ..core.audit_interface import BaseLeakageAuditor

class ExactHashLeakageAuditor(BaseLeakageAuditor):
    """Computes row-level hash digests to detect exact record contamination across splits."""
    
    def audit(self, train_df: pd.DataFrame, test_df: pd.DataFrame, **kwargs) -> Dict[str, Any]:
        def row_hashes(df: pd.DataFrame) -> Set[str]:
            return set(df.astype(str).apply(lambda r: hashlib.sha256("".join(r).encode("utf-8")).hexdigest(), axis=1))
            
        train_hashes = row_hashes(train_df)
        test_hashes = row_hashes(test_df)
        intersection = train_hashes.intersection(test_hashes)
        
        n_leak = len(intersection)
        leakage_rate = n_leak / max(len(test_hashes), 1)
        
        return {
            "exact_leakage_count": n_leak,
            "exact_leakage_rate": float(leakage_rate),
            "test_unique_records": len(test_hashes),
            "has_exact_leakage": n_leak > 0
        }
