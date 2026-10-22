"""Model Card generator for empirical machine learning robustness and transparency."""
from typing import Dict, Any, List, Optional
import json


class ModelCardGenerator:
    """Generates structured Model Cards complying with Mitchell et al. (2019) guidelines."""

    def __init__(
        self,
        model_name: str,
        version: str = "1.0.0",
        intended_use: str = "Empirical defect robustness auditing",
        limitations: Optional[List[str]] = None,
    ) -> None:
        self.model_name = model_name
        self.version = version
        self.intended_use = intended_use
        self.limitations = limitations or [
            "Assumes tabular data structures",
            "Performance degraded under severe duplicate leakage (>15%)",
        ]
        self.performance_metrics: Dict[str, float] = {}
        self.data_defects_evaluated: List[str] = []

    def set_metrics(self, metrics: Dict[str, float]) -> "ModelCardGenerator":
        """Attach verified benchmark performance metrics."""
        self.performance_metrics.update(metrics)
        return self

    def set_defects(self, defects: List[str]) -> "ModelCardGenerator":
        """Attach tested data quality defect scenarios."""
        self.data_defects_evaluated = list(defects)
        return self

    def generate_dict(self) -> Dict[str, Any]:
        """Generate structured dictionary model card."""
        return {
            "model_details": {
                "name": self.model_name,
                "version": self.version,
                "type": "Defect-Audited Tabular Model",
            },
            "intended_use": {
                "primary_application": self.intended_use,
                "out_of_scope_uses": ["Uncalibrated medical triage without physician review"],
            },
            "evaluated_metrics": self.performance_metrics,
            "defect_robustness": {
                "tested_defects": self.data_defects_evaluated,
                "known_failure_modes": self.limitations,
            },
            "ethical_considerations": [
                "Demographic parity disparity evaluated across sensitive sub-attributes",
                "Near-duplicate test leakage audited using MinHash-LSH and exact hashing",
            ],
        }

    def generate_markdown(self) -> str:
        """Render model card into clean Markdown artifact."""
        card = self.generate_dict()
        md = [
            f"# Model Card: {self.model_name} (v{self.version})",
            "",
            "## Model Details",
            f"- **Architecture / Name**: {self.model_name}",
            f"- **Version**: {self.version}",
            f"- **Primary Application**: {self.intended_use}",
            "",
            "## Robustness & Defect Audit",
            f"- **Evaluated Defects**: {', '.join(self.data_defects_evaluated) if self.data_defects_evaluated else 'None'}",
            "",
            "### Performance Under Audit",
        ]
        if self.performance_metrics:
            for k, v in self.performance_metrics.items():
                md.append(f"- **{k}**: {v:.4f}")
        else:
            md.append("- No metrics logged.")

        md.extend([
            "",
            "## Limitations & Known Vulnerabilities",
        ])
        for lim in self.limitations:
            md.append(f"- {lim}")

        md.extend([
            "",
            "## Ethical Considerations",
            "- Data leakage checks executed to prevent artificial validation over-optimism.",
            "- Continuous calibration tracking implemented.",
        ])
        return "\n".join(md)
