"""End-to-end composable pipeline for automated data quality defect remediation."""
from typing import List, Tuple, Dict, Any, Optional
import pandas as pd
from .base import BaseRemediator, RemediationActionLog
from .deduplicator import DeduplicationAutoResolver
from .imputation_router import IntelligentImputationRouter
from .outlier_clipper import AdaptiveOutlierClipperRemediator


class AutoCleanPipeline:
    """Orchestrates an ordered series of defect remediation steps with unified audit logging."""

    def __init__(self, remediators: Optional[List[BaseRemediator]] = None) -> None:
        if remediators is None:
            self.remediators: List[BaseRemediator] = [
                DeduplicationAutoResolver(),
                AdaptiveOutlierClipperRemediator(),
                IntelligentImputationRouter(),
            ]
        else:
            self.remediators = list(remediators)

    def add_step(self, remediator: BaseRemediator) -> "AutoCleanPipeline":
        """Add custom remediation step to end of pipeline."""
        self.remediators.append(remediator)
        return self

    def clean(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, List[RemediationActionLog]]:
        """Run all remediation steps sequentially, passing healed data forward."""
        current_df = df.copy()
        logs: List[RemediationActionLog] = []

        for remediator in self.remediators:
            current_df, log = remediator.remediate(current_df)
            logs.append(log)

        return current_df, logs

    def summarize_logs(self, logs: List[RemediationActionLog]) -> Dict[str, Any]:
        """Generate high-level report of all applied repair interventions."""
        total_affected = sum(log.rows_affected for log in logs)
        return {
            "total_repair_steps": len(logs),
            "total_items_remediated": total_affected,
            "steps_executed": [log.action_type for log in logs],
            "audit_trail": [log.to_dict() for log in logs],
        }
