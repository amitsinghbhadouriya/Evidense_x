"""Attribution leakage auditor detecting feature importance concentration anomalies."""
from typing import Dict, Any

class AttributionLeakageAuditor:
    """Detects if model decisions depend pathologically on a single leaked attribute."""
    
    def __init__(self, dominance_threshold: float = 0.65) -> None:
        self.threshold = dominance_threshold
        
    def audit_importance(self, importance_dict: Dict[str, float]) -> Dict[str, Any]:
        total = sum(importance_dict.values())
        if total == 0:
            return {"dominant_feature": None, "concentration_leakage": False}
            
        shares = {k: v / total for k, v in importance_dict.items()}
        dominant_feature, max_share = max(shares.items(), key=lambda x: x[1])
        
        return {
            "dominant_feature": dominant_feature,
            "max_importance_share": float(max_share),
            "concentration_leakage": max_share >= self.threshold
        }
