"""EU AI Act Article 10 Data Governance and Quality Risk Classifier."""
from typing import Dict, Any, List, Optional
import pandas as pd
from .base import BaseGovernanceAuditor, GovernanceAuditRecord


class EUAIActRiskClassifier(BaseGovernanceAuditor):
    """Classifies risk level under EU AI Act Article 10 (Data and data governance)."""

    def __init__(
        self,
        leakage_threshold: float = 0.05,
        missingness_threshold: float = 0.20,
    ) -> None:
        super().__init__(standard="EU-AI-Act-Article-10")
        self.leakage_threshold = leakage_threshold
        self.missingness_threshold = missingness_threshold

    def evaluate_compliance(
        self,
        dataset: pd.DataFrame,
        model_metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> GovernanceAuditRecord:
        """Evaluate dataset for statistical quality, bias vulnerabilities, and leakage."""
        meta = model_metadata or {}
        model_name = meta.get("model_name", "Tabular-Classifier")
        
        # Calculate missingness rate
        missingness_rate = float(dataset.isna().mean().mean())
        
        # Calculate internal duplication rate
        duplicate_count = int(dataset.duplicated().sum())
        leakage_score = float(duplicate_count / max(1, len(dataset)))
        
        defects = []
        recommendations = []
        
        if leakage_score > self.leakage_threshold:
            defects.append(f"Excessive duplicate records ({leakage_score:.2%}) risking evaluation leakage")
            recommendations.append("Apply deterministic deduplication prior to train/test partitioning.")
            
        if missingness_rate > self.missingness_threshold:
            defects.append(f"High global missingness ({missingness_rate:.2%}) without imputed guarantee")
            recommendations.append("Employ missingness indicator masks and MICE/MissForest imputation.")
            
        # Determine risk tier based on Article 10 requirements
        if leakage_score > 0.15 or missingness_rate > 0.40:
            risk_tier = "High"
            recommendations.append("Mandatory conformity assessment required under Article 43.")
        elif leakage_score > self.leakage_threshold or missingness_rate > self.missingness_threshold:
            risk_tier = "Moderate"
        else:
            risk_tier = "Low"

        return GovernanceAuditRecord(
            model_name=model_name,
            compliance_standard=self.standard,
            risk_tier=risk_tier,
            identified_defects=defects,
            leakage_score=leakage_score,
            missingness_vulnerability=missingness_rate,
            remediation_recommendations=recommendations,
            metadata={
                "total_rows": len(dataset),
                "total_columns": len(dataset.columns),
                "exact_duplicates": duplicate_count,
            },
        )
