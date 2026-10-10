# Research Problem Statement & Motivation

## The Challenge of Co-Occurring Data Quality Defects in ML Evaluation

Machine learning benchmarking and validation rely strictly on the independence between training and test sets ($i.i.d.$ assumption). However, tabular datasets sourced from observational, transactional, or sensor streams suffer from two endemic defect categories:

1. **Duplicate Leakage:** Identical or near-identical observations cross train-test partitions due to naive random splitting, turning generalization tests into memorization recall.
2. **Feature Missingness:** Incomplete feature vectors arising from non-response or sensor dropouts alter the information density and coordinate alignment of records.

While these defects have traditionally been studied in isolation, real-world data pipelines experience both simultaneously. This research investigates:
- Does feature missingness attenuate the artificial performance inflation caused by duplicate leakage?
- How do linear models vs. non-parametric tree ensembles differ in their vulnerability?
- What are the diagnostic metrics necessary to identify and prevent this Error-Reduction Illusion?
