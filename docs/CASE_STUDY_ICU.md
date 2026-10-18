# Case Study: Sepsis Prediction and ICU Clinical Telemetry Defect Leakage

## Context
In critical care predictive modeling, sensors record vital signs at 1-minute intervals. Missingness occurs due to sensor disconnection (MNAR), while duplicate telemetry arises from retrospective database exports.

## Empirical Findings with Evidense-X
- **Baseline Naive Model AUC:** 0.892 (Under 15% duplicate overlap and 20% block missingness).
- **Leakage-Audited Clean AUC:** 0.731.
- **Discrepancy (LSI):** +0.161 over-optimistic performance inflation.

## Recommendations
Mandate group-isolated patient splitting (`GroupKFold` on Patient ID) and verify through `ExactHashLeakageAuditor`.
