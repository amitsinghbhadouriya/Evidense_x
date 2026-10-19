# Production Deployment Runbook: Evidense-X Automated Leakage Gate

## 1. Objective
Establish standardized pre-deployment operational checks for machine learning pipelines to guarantee zero duplicate contamination.

## 2. Pipeline Gate Verification
Prior to deploying any model to production, the CI/CD runner executes:
```bash
python -m evidense_x.cli audit --train ./data/train.csv --test ./data/test.csv
```

## 3. Strict Pass/Fail Criteria
- **Exact Hash Contamination Rate:** Must equal `0.00%`.
- **Near-Duplicate Overlap (Euclidean < 1e-4):** Must not exceed `0.10%`.
- **Adversarial Partition AUC:** Must remain below `0.65`.
- **Zero Variance Invariants:** Zero degenerate features permitted.

## 4. Incident Response
If any gate fails, automatic deployment halts and notifications dispatch via `DefectAlertNotifier`.
