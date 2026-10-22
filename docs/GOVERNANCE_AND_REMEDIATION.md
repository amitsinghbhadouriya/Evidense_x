# Evidense-X Model Governance & Defect Remediation Guide

This operational manual documents the enterprise compliance, automated dataset healing, and streaming telemetry architecture introduced in Evidense-X v1.6.0.

---

## 1. Regulatory Governance & EU AI Act (Article 10)

Article 10 of the European Union Artificial Intelligence Act establishes stringent requirements on data quality, integrity, and mitigation of statistical biases and contamination.

Evidense-X implements automated governance auditing via:
- **`EUAIActRiskClassifier`**: Evaluates data partitions against contamination thresholds and missingness vulnerabilities, assigning a risk tier (`Low`, `Moderate`, `High`).
- **`ModelCardGenerator`**: Programmatically synthesizes model transparency artifacts following Mitchell et al. (2019).
- **`CryptographicProvenanceTracker`**: Generates SHA-256 lineage chains ensuring data transformations maintain cryptographic auditability.
- **`GovernanceExportSuite`**: Renders compliance certificates in JSON-LD, Markdown, and static HTML badges.

### Quick Example
```python
from evidense_x.governance import EUAIActRiskClassifier, GovernanceExportSuite
import pandas as pd

df = pd.read_csv("data/clinical_telemetry.csv")
classifier = EUAIActRiskClassifier(leakage_threshold=0.05, missingness_threshold=0.20)
record = classifier.evaluate_compliance(df, model_metadata={"model_name": "ICU-Sepsis-Predictor"})

print(f"Assigned Risk Tier: {record.risk_tier}")
markdown_report = GovernanceExportSuite.to_markdown(record)
```

---

## 2. Advanced Unsupervised Diagnostics & Drift

When ground-truth labels are absent or delayed, unsupervised diagnostics detect latent defect migrations:
- **`IsolationForestDriftDetector`**: Computes shifts in average isolation tree path lengths and contamination ratios.
- **`LocalOutlierFactorAuditor`**: Uncovers localized neighborhood density collapse and sparse anomalies.
- **`RobustMahalanobisAuditor`**: Calculates shrinkage-regularized covariance distances with Chi-square critical value cutoffs.
- **`EnergyDistanceDriftDetector`**: Executes non-parametric multi-dimensional two-sample testing between baseline and test sets.

---

## 3. Automated Defect Remediation & Healing

The `AutoCleanPipeline` orchestrates sequential, non-destructive dataset repairs:
1. **`DeduplicationAutoResolver`**: Identifies duplicate record clusters and resolves them via priority tie-breaking (e.g. `least_missing`).
2. **`AdaptiveOutlierClipperRemediator`**: Computes interquartile range (IQR) boundaries and clips extreme distribution tails.
3. **`IntelligentImputationRouter`**: Routes features dynamically between KNN neighbor imputation and median imputation based on column missingness severity.
4. **`ConfidentLabelNoiseRemediator`**: Detects misannotated labels through out-of-fold probability disagreement.

```bash
evidense-x remediate --input-file raw_data.csv --output-file cleaned_data.csv
```

---

## 4. Online Streaming Surveillance

For real-time operational streams:
- **`SlidingWindowLeakageMonitor`**: Tracks duplicate leakage against pre-compiled train record hashes.
- **`AdaptiveWindowDriftDetector`**: Evaluates streaming performance decay using Hoeffding bounds.
- **`ExponentialMovingAverageMissingnessAuditor`**: Maintains exponential moving averages of record null densities.
