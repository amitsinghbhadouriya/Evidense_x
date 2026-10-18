# Case Study: Consumer Credit Default Risk and Synthetic Leakage Overfitting

## Executive Summary
Financial underwriting models evaluate probability of default. Data pipelines merging credit bureau updates frequently ingest near-duplicates due to minor address or timestamp adjustments.

## Audit Results
- **Near-Duplicate Rate:** 4.2% undetected by exact string hashing.
- **KD-Tree Leakage Audit:** Detected 420 instances within normalized Euclidean distance < 1e-4.
- **Downside Risk:** Models deployed without audit suffered a 22% increase in default rate relative to test projections.
