# Evidense-X: Measuring & Remediating Data Quality Defect Interactions in ML

[![Version](https://img.shields.io/badge/version-v1.6.0-blue.svg)](https://github.com/amitsinghbhadouriya/Evidense_x)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/downloads/)
[![CI / Tests](https://img.shields.io/badge/tests-61%20passed-brightgreen.svg)]()
[![Compliance](https://img.shields.io/badge/Governance-EU%20AI%20Act%20Art.%2010-orange.svg)]()
[![Target Venue](https://img.shields.io/badge/Target-IEEE%20TKDE%20%2F%20BigData-purple.svg)]()

> **Official Research & Production Framework for:**  
> *"When Data Quality Defects Interact: Measuring the Impact of Missing Values and Duplicate Leakage on Machine Learning Evaluation"*  
> **Author:** Amit Singh Bhadouriya ([abhaybhadouriya88@gmail.com](mailto:abhaybhadouriya88@gmail.com))

---

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Empirical Findings](#key-empirical-findings)
- [Enterprise Architecture (v1.6.0)](#enterprise-architecture-v160)
- [Quickstart & Installation](#quickstart--installation)
- [Python API Examples](#python-api-examples)
  - [1. Data Governance & EU AI Act Audit](#1-data-governance--eu-ai-act-audit)
  - [2. Automated Dataset Remediation & Auto-Cleaning](#2-automated-dataset-remediation--auto-cleaning)
  - [3. Real-Time Streaming Defect Surveillance](#3-real-time-streaming-defect-surveillance)
  - [4. Unsupervised Anomaly & Distribution Drift Diagnostics](#4-unsupervised-anomaly--distribution-drift-diagnostics)
- [Command-Line Interface (CLI)](#command-line-interface-cli)
- [Repository Structure](#repository-structure)
- [Testing & Quality Verification](#testing--quality-verification)
- [Citation](#citation)
- [License](#license)

---

## Executive Summary

Supervised machine learning validation relies on the foundational assumption that training and test partitions are independent and identically distributed ($i.i.d.$). However, enterprise and scientific data pipelines routinely suffer from co-occurring data quality defects:
- **Duplicate Leakage:** Unintentional cross-partition record contamination when repeated observations cross train/test split boundaries.
- **Feature Missingness:** Incomplete feature vectors altering the information geometry of observations (MCAR, MAR, MNAR).

While existing literature treats data leakage and missing values as separate concerns, **Evidense-X** demonstrates their significant empirical interaction across **3 tabular benchmark datasets**, **3 classifier families**, **4 missingness levels**, and **4 controlled overlap tiers** across 10 random seeds (**2,160 model evaluations**). 

In **v1.6.0**, Evidense-X expands from an empirical auditing suite into an end-to-end framework featuring **EU AI Act Article 10 compliance classification**, **automated self-healing remediation pipelines**, **unsupervised distribution diagnostics**, and **online streaming surveillance**.

---

## Key Empirical Findings

1. **Extreme, Model-Dependent F1 Inflation:** At $50\%$ duplicate overlap, F1 scores were inflated by $+0.142$ to $+0.202$ for Decision Trees and $+0.098$ to $+0.168$ for Random Forests ($p < 0.002$, Wilcoxon signed-rank tests), while Logistic Regression exhibited negligible sensitivity ($\Delta F1 \le +0.006$).
2. **The Error-Reduction Illusion (ERI):** Up to $60.8\%$ of apparent test errors were eliminated purely through duplicate memorization.
3. **Natural Duplicate Distortion:** Standard random splitting on datasets with naturally occurring duplicates ($15.0\%$ in Red Wine, $19.1\%$ in White Wine) caused $+0.035$ to $+0.066$ F1 inflation in tree models.
4. **Defect Interaction:** Ordinary least squares (OLS) regressions reveal that missingness significantly amplifies tree-based duplicate leakage in higher-dimensional spaces ($\beta_{\text{inter}} = +0.244, p < 10^{-9}$ for Random Forest on Adult).
5. **Coordinate Alignment Mechanism:** Independently masking duplicate copies destroys exact multi-dimensional coordinate alignment, reducing retained leakage to $15.0\% - 32.3\%$ at $30\%$ missingness.

---

## Enterprise Architecture (v1.6.0)

Evidense-X provides a modular, production-grade Python package structured under `src/evidense_x/`:

| Module | Core Functionality | Primary Components |
|---|---|---|
| **`evidense_x.governance`** | Model governance, lineage & regulatory compliance | `EUAIActRiskClassifier`, `ModelCardGenerator`, `CryptographicProvenanceTracker`, `GovernanceExportSuite` |
| **`evidense_x.remediation`** | Automated data healing & repair pipelines | `AutoCleanPipeline`, `DeduplicationAutoResolver`, `IntelligentImputationRouter`, `AdaptiveOutlierClipperRemediator`, `ConfidentLabelNoiseRemediator` |
| **`evidense_x.diagnostics`** | Unsupervised anomaly & distribution drift checks | `IsolationForestDriftDetector`, `LocalOutlierFactorAuditor`, `RobustMahalanobisAuditor`, `EnergyDistanceDriftDetector` |
| **`evidense_x.streaming`** | Online real-time defect & leakage monitoring | `SlidingWindowLeakageMonitor`, `AdaptiveWindowDriftDetector`, `ExponentialMovingAverageMissingnessAuditor` |
| **`evidense_x.audit`** | Multi-dimensional & near-duplicate leakage audits | `MinHashLSHNearDuplicateAuditor`, `EmbeddingCosineLeakageScanner`, `TargetLeakageCorrelationAuditor`, `ZeroVarianceFeatureAuditor` |
| **`evidense_x.defects`** | Empirical defect simulation & coordinate hashing | `apply_mcar_mask`, `apply_mar_mask`, `ContinuousCensoringInjector`, `GaussianJitterInjector`, `CategoricalDriftInjector` |
| **`evidense_x.splitters`** | Certified leakage-free & walk-forward CV | `DuplicateAwareGroupSplitter`, `GroupStratifiedKFold`, `TemporalBlockSplitter`, `PurgedWalkForwardCV` |
| **`evidense_x.imputation`** | Robust missingness imputation benchmarks | `IterativeChainedEquationsImputer` (MICE), `KNNNeighborImputer`, `MissForestRandomForestImputer` |
| **`evidense_x.transforms`** | Feature engineering with missingness awareness | `OutlierWinsorizer`, `MissingnessIndicatorAugmenter`, `RobustTargetEncoder`, `RobustQuantileTransformer` |
| **`evidense_x.ensemble`** | Robust model stacking & calibration | `SuperLearnerStackingClassifier`, `SoftVotingProbabilityEnsemble`, `BayesianModelAveragingEnsemble`, `TemperatureScaledEnsemble` |
| **`evidense_x.tuning`** | Defect-aware hyperparameter optimization | `RandomSearchCrossValidator`, `SuccessiveHalvingPruner`, `MultiObjectiveParetoOptimizer`, `EarlyStoppingCallback` |
| **`evidense_x.explainability`**| Attribution auditing under missingness & leakage | `TreeFeatureStabilityIndex`, `IntegratedGradientsApproximator`, `AttributionLeakageAuditor`, `KernelSHAPExplainer` |
| **`evidense_x.metrics`** | Diagnostic leakage & fairness statistics | `compute_lsi`, `compute_eri`, `AUPRG`, `ExpectedCalibrationError`, `DemographicParityDifference` |
| **`evidense_x.cli`** | Production command-line tool router | `evidense-x` subcommands: `info`, `audit`, `benchmark`, `report`, `clean`, `govern`, `stream-audit`, `remediate` |

---

## Quickstart & Installation

### Requirements
- Python `>= 3.10`
- Dependencies: `numpy`, `pandas`, `scikit-learn`, `scipy`, `statsmodels`, `matplotlib`, `seaborn`

### Setup
```bash
# Clone the repository
git clone https://github.com/amitsinghbhadouriya/Evidense_x.git
cd Evidense_x

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install package in editable mode
pip install -e .

# Or install dependencies via requirements.txt
pip install -r requirements.txt
```

---

## Python API Examples

### 1. Data Governance & EU AI Act Audit
Evaluate dataset compliance against EU AI Act Article 10 requirements and export structured transparency model cards:
```python
import pandas as pd
from evidense_x.governance import (
    EUAIActRiskClassifier,
    ModelCardGenerator,
    GovernanceExportSuite,
    CryptographicProvenanceTracker,
)

# Load data and evaluate regulatory risk
df = pd.read_csv("wine quality/winequality-red.csv")
classifier = EUAIActRiskClassifier(leakage_threshold=0.05, missingness_threshold=0.20)
record = classifier.evaluate_compliance(df, model_metadata={"model_name": "WineQuality-RandomForest"})

print(f"Risk Tier: {record.risk_tier}")
print(f"Contamination: {record.leakage_score:.2%}, Missingness: {record.missingness_vulnerability:.2%}")

# Export to Markdown, HTML Badge, or JSON-LD
markdown_report = GovernanceExportSuite.to_markdown(record)
jsonld_schema = GovernanceExportSuite.to_json_ld(record)

# Track cryptographic lineage
tracker = CryptographicProvenanceTracker()
lineage_entry = tracker.record_stage("initial_ingestion", df)
print(f"Dataset SHA-256 Fingerprint: {lineage_entry['fingerprint']}")
```

### 2. Automated Dataset Remediation & Auto-Cleaning
Heal multiple co-occurring data quality defects with unified audit trails:
```python
import pandas as pd
from evidense_x.remediation import AutoCleanPipeline

df_raw = pd.read_csv("raw_dataset_with_defects.csv")

# Create and execute automated clean pipeline
pipeline = AutoCleanPipeline()
cleaned_df, logs = pipeline.clean(df_raw)

summary = pipeline.summarize_logs(logs)
print(f"Executed {summary['total_repair_steps']} repair steps.")
print(f"Total defects healed: {summary['total_items_remediated']}")

# Save healed dataset
cleaned_df.to_csv("cleaned_dataset.csv", index=False)
```

### 3. Real-Time Streaming Defect Surveillance
Detect cross-partition leakage and streaming error rate drift in real-time:
```python
from evidense_x.streaming import (
    SlidingWindowLeakageMonitor,
    AdaptiveWindowDriftDetector,
    ExponentialMovingAverageMissingnessAuditor,
)

# Initialize monitors
leakage_mon = SlidingWindowLeakageMonitor(window_size=200, leakage_alert_rate=0.05)
drift_mon = AdaptiveWindowDriftDetector(window_size=100)
missing_mon = ExponentialMovingAverageMissingnessAuditor(alpha=0.1, missingness_alert_rate=0.15)

# Simulate streaming stream ingestion
for record in streaming_records:
    alert_leak = leakage_mon.ingest_record(record)
    alert_drift = drift_mon.ingest_record({"error": record["loss"]})
    alert_miss = missing_mon.ingest_record(record)
    
    if alert_leak:
        print(f"[ALERT] Leakage spike: {alert_leak.observed_value:.2%}")
    if alert_drift:
        print(f"[ALERT] Performance drift detected: {alert_drift.details}")
```

### 4. Unsupervised Anomaly & Distribution Drift Diagnostics
Detect corrupted records or out-of-distribution shifts without ground-truth labels:
```python
import pandas as pd
from evidense_x.diagnostics import (
    IsolationForestDriftDetector,
    RobustMahalanobisAuditor,
    EnergyDistanceDriftDetector,
)

train_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")

# Energy distance 2-sample distribution shift test
energy_detector = EnergyDistanceDriftDetector(drift_threshold=0.25)
energy_detector.fit(train_df)
drift_result = energy_detector.evaluate(test_df)
print(f"Energy Distance: {drift_result['energy_distance']:.4f} (Drift: {drift_result['is_drift_detected']})")

# Multivariate Mahalanobis covariance audit
maha_auditor = RobustMahalanobisAuditor(contamination=0.05)
maha_auditor.fit(train_df)
anomalies = maha_auditor.predict(test_df)
print(f"Detected multivariate outliers: {(anomalies == -1).sum()} / {len(test_df)}")
```

---

## Command-Line Interface (CLI)

The `evidense-x` CLI entrypoint provides full access to benchmarking, auditing, remediation, and governance:

```bash
# Display version and framework metadata
python -m evidense_x.cli --version
python -m evidense_x.cli info

# 1. Audit dataset partitions for duplicate leakage
python -m evidense_x.cli audit --train train.csv --test test.csv

# 2. Automated dataset remediation & cleaning
python -m evidense_x.cli remediate --input-file raw.csv --output-file cleaned.csv

# 3. EU AI Act regulatory compliance audit & report generation
python -m evidense_x.cli govern --data dataset.csv --name "CreditRiskModel" --output governance_report.md

# 4. Real-time streaming surveillance simulation
python -m evidense_x.cli stream-audit --data incoming_stream.csv --window-size 250

# 5. Execute full benchmark matrix
python -m evidense_x.cli benchmark --data benchmark_data.csv
```

---

## Repository Structure

```
Evidense_x/
├── .github/
│   └── workflows/
│       └── ci.yml                            # GitHub Actions CI workflow
├── Adult/                                    # Adult Census Income benchmark dataset
├── wine quality/                             # Wine Quality (Red & White) benchmark datasets
├── docs/                                     # Documentation, taxonomies & runbooks
│   ├── GOVERNANCE_AND_REMEDIATION.md         # Operational governance & auto-cleaning manual
│   ├── METHODOLOGY.md                        # Empirical testing methodology
│   ├── PROBLEM_STATEMENT.md                  # Theoretical defect formulation
│   ├── REPRODUCIBILITY.md                    # Exact reproduction guide
│   ├── DEPLOYMENT_RUNBOOK.md                 # Production deployment & CI checklist
│   └── API_REFERENCE.md                      # Comprehensive subpackage API catalog
├── figures/                                  # Camera-ready IEEE publication figures
├── results/                                  # Experimental CSV logs (2,160 evaluations)
├── tables/                                   # Statistical summary & OLS regression tables
├── src/
│   └── evidense_x/                           # Production framework package
│       ├── __init__.py                       # Package entrypoint & version definition (v1.6.0)
│       ├── analysis/                         # Econometric OLS, Friedman & Wilcoxon tests
│       ├── audit/                            # LSH MinHash, cosine embedding & leakage auditors
│       ├── cli/                              # CLI subcommands (govern, remediate, stream-audit)
│       ├── config/                           # Reproducible experimental matrix configurations
│       ├── core/                             # Abstract interfaces, timers, provenance, registries
│       ├── data/                             # Dataset loaders, preflight sanitizers, OpenML fetchers
│       ├── defects/                          # MCAR/MAR injectors, label noise, coordinate hashing
│       ├── diagnostics/                      # Isolation Forest, LOF, Mahalanobis, Energy Distance
│       ├── ensemble/                         # SuperLearner stacking, Bayes averaging, soft voting
│       ├── explainability/                   # Tree stability, Integrated Gradients, SHAP wrappers
│       ├── governance/                       # EU AI Act risk classifier, model cards, provenance
│       ├── imputation/                       # MICE, MissForest, and KNN neighbor imputers
│       ├── metrics/                          # LSI, ERI, AUPRG, ECE, Brier decomposition, fairness
│       ├── models/                           # Sklearn adapters, pipelines, and calibration wrappers
│       ├── production/                       # KS-test drift gates, deployment checks, container gates
│       ├── remediation/                      # AutoCleanPipeline, deduplication, outlier clipping
│       ├── splitters/                        # Duplicate-aware group splitters, walk-forward CV
│       ├── streaming/                        # Sliding window leakage, drift, and EMA monitors
│       ├── transforms/                       # Robust target encoders, winsorizers, missingness masks
│       ├── tuning/                           # Defect-aware CV, successive halving, Pareto optimizers
│       └── visualization/                    # Radar plots, 3D loss projections, Sankey flow diagrams
├── tests/                                    # Pytest automated test suite (61 tests)
├── CHANGELOG.md                              # Complete chronological changelog
├── pyproject.toml                            # Project build specifications (v1.6.0)
├── requirements.txt                          # Production dependency manifest
├── run_all_experiments.py                    # Master benchmark execution engine
├── analyze_and_plot.py                       # Plotting and visualization pipeline
├── generate_summary_tables.py                # Publication table compilation script
├── build_ieee_paper.py                       # Automated Word/PDF manuscript compiler
├── RESEARCH_PAPER.md                         # Complete camera-ready research manuscript
└── README.md                                 # Project documentation
```

---

## Testing & Quality Verification

Evidense-X includes an extensive test suite covering defect injection, statistical metrics, splitters, anomaly detectors, remediation pipelines, and CLI entrypoints:

```bash
# Run complete test suite
pytest tests/ -v

# Run tests with short summary
pytest -q
```

All 61 test modules run without external network requirements and complete in under 20 seconds.

---

## Citation

If you find this research framework or implementation useful in your research or production pipelines, please cite:

```bibtex
@article{bhadouriya2026evidense,
  title={When Data Quality Defects Interact: Measuring the Impact of Missing Values and Duplicate Leakage on Machine Learning Evaluation},
  author={Bhadouriya, Amit Singh},
  journal={IEEE Transactions on Knowledge and Data Engineering (Targeted)},
  year={2026}
}
```

---

## License

Distributed under the [MIT License](LICENSE). Copyright © 2026 Amit Singh Bhadouriya.
