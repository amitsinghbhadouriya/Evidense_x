# Empirical Case Studies

## 1. Clinical Risk Prediction
In healthcare diagnostics, patient retrials or repeated measurements often generate duplicate feature profiles. When naive train-test splitting leaks repeated patients, models appear to achieve near-perfect diagnostic discrimination, masking catastrophic failure on novel cohorts.

## 2. Automated Financial Underwriting
Loan applicants submitting multiple identical or near-identical inquiries can leak across underwriting models. As demonstrated by our findings, tree-based models memorize coordinate combinations, driving up to a 60% illusion of error reduction.
