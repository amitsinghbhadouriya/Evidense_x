"""Webhook and alert notifier for automated defect notification."""
from typing import Dict, Any

class DefectAlertNotifier:
    """Formats payload alerts for notification channels when leakage is detected."""
    
    def create_alert_payload(self, model_id: str, leakage_rate: float) -> Dict[str, Any]:
        return {
            "alert": "DATA_CONTAMINATION_DETECTED",
            "model_id": model_id,
            "severity": "CRITICAL" if leakage_rate > 0.05 else "WARNING",
            "leakage_percentage": round(leakage_rate * 100, 2),
            "message": f"Dataset contamination of {leakage_rate:.2%} exceeds compliance limit."
        }
