"""Base governance protocols and audit metadata schemas for Evidense-X."""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional
import pandas as pd


@dataclass
class GovernanceAuditRecord:
    """Standardized audit entry documenting governance, risk, and data compliance."""
    model_name: str
    assessment_timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    compliance_standard: str = "EU-AI-Act-Article-10"
    risk_tier: str = "Low"
    identified_defects: List[str] = field(default_factory=list)
    leakage_score: float = 0.0
    missingness_vulnerability: float = 0.0
    remediation_recommendations: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert audit record to serializable dictionary."""
        return {
            "model_name": self.model_name,
            "assessment_timestamp": self.assessment_timestamp,
            "compliance_standard": self.compliance_standard,
            "risk_tier": self.risk_tier,
            "identified_defects": self.identified_defects,
            "leakage_score": self.leakage_score,
            "missingness_vulnerability": self.missingness_vulnerability,
            "remediation_recommendations": self.remediation_recommendations,
            "metadata": self.metadata,
        }


class BaseGovernanceAuditor(ABC):
    """Abstract interface for regulatory compliance and governance auditing."""

    def __init__(self, standard: str = "EU-AI-Act-Article-10") -> None:
        self.standard = standard

    @abstractmethod
    def evaluate_compliance(
        self,
        dataset: pd.DataFrame,
        model_metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> GovernanceAuditRecord:
        """Evaluate dataset and model metadata against governance requirements."""
        pass
