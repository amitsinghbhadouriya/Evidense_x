# Evidense-X Changelog

All notable changes to this project are documented in this file.

## [v1.3.0] - 2026-10-18

### Added
- **Core Architecture:** Defined `BaseDefectSimulator` and `BaseLeakageAuditor` abstract protocols, registry mechanisms, timer contexts, and provenance metadata recorders.
- **Defect Injectors:** Added `MARLogisticSimulator`, `ContinuousCensoringInjector`, `GaussianJitterInjector`, `CategoricalDriftInjector`, and `ClassificationLabelNoiseInjector`.
- **Auditing Suite:** Added `ExactHashLeakageAuditor`, `KDTreeLeakageAuditor`, `ClusterSeparabilityAuditor`, `AdversarialValidationAuditor`, and export formats (JSON-LD, Markdown, HTML).
- **Models & Calibration:** Added `RandomForestAdapter`, `HistGradientBoostingAdapter`, `LogisticRegressionAdapter`, `ExpectedCalibrationError`, and `BrierDecomposition`.
- **Statistical Meta-Analysis:** Added paired Wilcoxon signed-rank test, Friedman ranking, Benjamini-Hochberg FDR correction, and DerSimonian-Laird random effects.
- **Visualization Suite:** Added multivariate radar charts, 2D heatmap surfaces, 3D loss projections, reliability diagrams, and camera-ready LaTeX table exporters.
- **MLOps Production:** Implemented KS-test drift detection, deployment leakage gatekeepers, and Docker container support.
- **Case Studies & Benchmarks:** Added clinical ICU telemetry and consumer credit risk empirical case studies with reproducible JSON configs.
