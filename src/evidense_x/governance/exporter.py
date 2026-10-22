"""Export utilities for regulatory governance audit certificates and reports."""
import json
from typing import Dict, Any
from .base import GovernanceAuditRecord


class GovernanceExportSuite:
    """Exports governance records into standardized enterprise compliance formats."""

    @staticmethod
    def to_json_ld(record: GovernanceAuditRecord) -> str:
        """Render audit record into JSON-LD compliant semantic schema."""
        data = {
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": record.model_name,
            "dateModified": record.assessment_timestamp,
            "riskAssessment": {
                "@type": "RiskAssessment",
                "standard": record.compliance_standard,
                "riskLevel": record.risk_tier,
                "leakageScore": record.leakage_score,
                "missingnessRate": record.missingness_vulnerability,
                "identifiedVulnerabilities": record.identified_defects,
                "correctiveActions": record.remediation_recommendations,
            },
            "applicationCategory": "Machine Learning Audited Pipeline",
        }
        return json.dumps(data, indent=2)

    @staticmethod
    def to_markdown(record: GovernanceAuditRecord) -> str:
        """Render audit certificate into human-readable Markdown."""
        lines = [
            f"# AI Governance Audit Certificate: {record.model_name}",
            "",
            f"- **Compliance Standard**: `{record.compliance_standard}`",
            f"- **Evaluated Risk Tier**: **{record.risk_tier}**",
            f"- **Audit Timestamp**: {record.assessment_timestamp}",
            f"- **Duplicate Contamination Rate**: {record.leakage_score:.2%}",
            f"- **Missingness Vulnerability**: {record.missingness_vulnerability:.2%}",
            "",
            "## Identified Compliance Defects",
        ]
        if record.identified_defects:
            for d in record.identified_defects:
                lines.append(f"- [WARNING] {d}")
        else:
            lines.append("- [OK] No critical governance non-conformities detected.")

        lines.extend([
            "",
            "## Required Remediation Actions",
        ])
        if record.remediation_recommendations:
            for r in record.remediation_recommendations:
                lines.append(f"1. {r}")
        else:
            lines.append("1. Maintain continuous production data monitoring.")

        return "\n".join(lines)

    @staticmethod
    def to_html(record: GovernanceAuditRecord) -> str:
        """Render self-contained HTML badge and report."""
        badge_color = "#28a745" if record.risk_tier == "Low" else ("#ffc107" if record.risk_tier == "Moderate" else "#dc3545")
        return f"""<!DOCTYPE html>
<html>
<head><title>Governance Certificate - {record.model_name}</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 40px; background: #f8f9fa; }}
.card {{ background: white; border-radius: 8px; padding: 24px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 700px; margin: auto; }}
.badge {{ display: inline-block; padding: 6px 12px; border-radius: 4px; color: white; background: {badge_color}; font-weight: bold; }}
</style>
</head>
<body>
<div class="card">
  <h2>AI Governance Certificate: {record.model_name}</h2>
  <p><span class="badge">Risk Tier: {record.risk_tier}</span></p>
  <p><strong>Standard:</strong> {record.compliance_standard} | <strong>Timestamp:</strong> {record.assessment_timestamp}</p>
  <hr/>
  <p><strong>Leakage Score:</strong> {record.leakage_score:.2%}</p>
  <p><strong>Missingness Vulnerability:</strong> {record.missingness_vulnerability:.2%}</p>
  <h3>Identified Defects</h3>
  <ul>{''.join(f'<li>{d}</li>' for d in record.identified_defects) or '<li>None</li>'}</ul>
  <h3>Remediation Guidance</h3>
  <ol>{''.join(f'<li>{r}</li>' for r in record.remediation_recommendations) or '<li>None</li>'}</ol>
</div>
</body>
</html>"""
