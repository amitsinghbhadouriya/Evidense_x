"""Composite pipeline auditor running all exact, nearest neighbor, and statistical checks."""
from typing import Dict, Any
import pandas as pd
from .exact_hash_auditor import ExactHashLeakageAuditor
from .nearest_neighbor_auditor import KDTreeLeakageAuditor
from .adversarial_validation import AdversarialValidationAuditor

class CompositeAuditor:
    """Coordinates multi-modal auditing routines into a single comprehensive evaluation."""
    
    def __init__(self) -> None:
        self.hash_auditor = ExactHashLeakageAuditor()
        self.kdtree_auditor = KDTreeLeakageAuditor()
        self.adv_auditor = AdversarialValidationAuditor()
        
    def audit_partitions(self, train_df: pd.DataFrame, test_df: pd.DataFrame) -> Dict[str, Any]:
        results: Dict[str, Any] = {}
        results.update(self.hash_auditor.audit(train_df, test_df))
        results.update(self.kdtree_auditor.audit(train_df, test_df))
        results.update(self.adv_auditor.run_audit(train_df, test_df))
        return results
