# Evidense-X Changelog

All notable changes to this project are documented in this file.

## [v1.5.0] - 2026-10-20

### Added
- **Synthetic Data Generators:** Added `SyntheticDefectDatasetGenerator`, `MultiModalTabularGenerator`, `LongitudinalPatientTrajectoryGenerator`, and `FinancialTransactionStreamGenerator`.
- **Robust Feature Transforms:** Implemented `OutlierWinsorizer`, `RobustQuantileTransformer`, `MissingnessIndicatorAugmenter`, and `RobustTargetEncoder`.
- **Interpretability & Attributions:** Added `PermutationFeatureExplainer`, `ApproximateKernelShapExplainer`, `AttributionLeakageAuditor`, and `TreeFeatureStabilityIndex`.
- **Hyperparameter Optimization:** Added `RandomizedCVOptimizer`, `SuccessiveHalvingScheduler`, `MultiObjectiveParetoFilter`, and `EarlyStoppingTracker`.
- **Ensemble Architectures:** Implemented `SoftVotingEnsemble`, `SuperLearnerStackingClassifier`, and `TemperatureScalingCalibrator`.
- **CLI Enhancements:** Added `evidense-x benchmark`, `report`, and `clean` subcommands.

## [v1.4.0] - 2026-10-19

### Added
- **Resampling & Partitioning:** Implemented `GroupStratifiedKFold`, `TemporalBlockSplitter`, `PurgedWalkForwardCV`, and `ClusterBasedSpatialSplitter`.
- **Imputation Benchmarks:** Introduced `IterativeChainedEquationsImputer` (MICE), `KNNNeighborImputer`, and `MissForestRandomForestImputer`.
- **High-Dimensional & Vector Audit:** Implemented `MinHashLSHNearDuplicateAuditor`, `EmbeddingCosineLeakageScanner`, `TargetLeakageCorrelationAuditor`, and `ZeroVarianceFeatureAuditor`.
- **Fairness & Gain Metrics:** Added `DemographicParityDifference`, `EqualizedOddsDisparity`, `PredictionEntropyVolatility`, and Area Under Precision-Recall Gain (`AUPRG`).
- **Interactive Visualization:** Added standalone HTML/SVG report generator, Sankey defect migration flow, and calibration drift strip plots.
- **Operational Runbook:** Added production deployment checklist and automated CI/CD gate runbook (`DEPLOYMENT_RUNBOOK.md`).

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
