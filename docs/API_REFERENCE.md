# Evidense-X API Reference (v1.6.0)

Comprehensive reference guide for all public subpackages and classes in `evidense_x`.

---

## 1. `evidense_x.governance`
Regulatory compliance, model transparency cards, and cryptographic provenance tracking.

- **`BaseGovernanceAuditor`**: Abstract base class for regulatory compliance auditing.
- **`GovernanceAuditRecord`**: Dataclass containing compliance standard, risk tier (`Low`, `Moderate`, `High`), identified defects, and remediation actions.
- **`EUAIActRiskClassifier`**: Evaluates dataset against EU AI Act Article 10 criteria for data contamination, leakage, and missingness vulnerabilities.
- **`ModelCardGenerator`**: Synthesizes model transparency artifacts adhering to Mitchell et al. (2019) in Markdown and JSON.
- **`CryptographicProvenanceTracker`**: Computes SHA-256 dataset fingerprints and maintains an immutable lineage audit chain.
- **`GovernanceExportSuite`**: Exports audit certificates into JSON-LD, Markdown, and static HTML reports.

---

## 2. `evidense_x.remediation`
Automated dataset healing, noise filtering, and composable auto-clean pipelines.

- **`BaseRemediator`**: Abstract base class for data defect repair operations.
- **`RemediationActionLog`**: Structured audit log detailing rows/columns repaired, timestamps, and diagnostic parameters.
- **`AutoCleanPipeline`**: End-to-end composable pipeline chaining deduplication, outlier clipping, and imputation.
- **`DeduplicationAutoResolver`**: Identifies duplicate record clusters and resolves them via priority tie-breaking rules (`least_missing`, `first`, `last`).
- **`IntelligentImputationRouter`**: Dynamically routes features to KNN or median imputation based on column missingness rate.
- **`AdaptiveOutlierClipperRemediator`**: Interquartile range (IQR) based winsorization and tail value clipping with audit metrics.
- **`ConfidentLabelNoiseRemediator`**: Detects misannotated labels using out-of-fold cross-validated probability disagreement.

---

## 3. `evidense_x.diagnostics`
Unsupervised anomaly detection, density degradation, and distribution drift diagnostics.

- **`BaseAnomalyDetector`**: Abstract interface for unsupervised anomaly scoring and prediction.
- **`IsolationForestDriftDetector`**: Measures shifts in average isolation tree path lengths and contamination ratios between partitions.
- **`LocalOutlierFactorAuditor`**: Density-based local outlier factor detection assessing neighborhood sparsity and cluster collapse.
- **`RobustMahalanobisAuditor`**: Multivariate covariance-regularized Mahalanobis distance auditor with Chi-square critical thresholds.
- **`EnergyDistanceDriftDetector`**: Statistical energy distance non-parametric two-sample test for continuous distribution shift.

---

## 4. `evidense_x.streaming`
Online streaming defect surveillance, sliding buffer monitors, and real-time alerting.

- **`BaseStreamMonitor`**: Base class managing sliding window ring buffers and alert thresholds.
- **`StreamAlert`**: Dataclass emitted upon defect threshold breach (`INFO`, `WARNING`, `CRITICAL`).
- **`SlidingWindowLeakageMonitor`**: Tracks cross-partition duplicate leakage in real-time streams against reference hashes.
- **`AdaptiveWindowDriftDetector`**: Monitors online prediction loss decay using adaptive Hoeffding bounds.
- **`ExponentialMovingAverageMissingnessAuditor`**: Tracks smoothed exponential moving averages (EMA) of missing value rates.

---

## 5. `evidense_x.audit`
High-dimensional duplicate auditing and multi-modal leakage scanners.

- **`ExactHashLeakageAuditor`**: Computes row-level MD5/SHA-256 hash sets across partitions to detect exact contamination.
- **`MinHashLSHNearDuplicateAuditor`**: Locality-Sensitive Hashing (LSH) for high-dimensional approximate duplicate detection.
- **`EmbeddingCosineLeakageScanner`**: Pairwise cosine similarity scanner detecting semantic vector leakage.
- **`TargetLeakageCorrelationAuditor`**: Flags features exhibiting implausibly high correlation with target labels.
- **`ZeroVarianceFeatureAuditor`**: Identifies degenerate, uninformative features before training.

---

## 6. `evidense_x.splitters`
Certified leakage-free resampling and controlled defect injection splitters.

- **`DuplicateAwareGroupSplitter`**: Enforces strict cluster-level group splitting guaranteeing 0% cross-split duplicate contamination.
- **`ControlledLeakageInjector`**: Injects controlled duplicate overlap tiers ($0\%, 10\%, 25\%, 50\%$) from test to train.
- **`GroupStratifiedKFold`**: Preserves both target class balance and cluster group boundaries across cross-validation folds.
- **`TemporalBlockSplitter`**: Chronological time-series split preventing lookahead leakage.
- **`PurgedWalkForwardCV`**: Embargo-aware rolling window walk-forward validation for temporal data.

---

## 7. `evidense_x.defects`
Empirical defect simulation, missingness mechanisms, and coordinate perturbation.

- **`apply_mcar_mask`**: Parameterized Missing Completely at Random (MCAR) feature masking.
- **`apply_mar_mask`**: Parameterized Missing at Random (MAR) logistic-conditioned feature masking.
- **`detect_duplicate_clusters`**: Identifies multi-dimensional coordinate equivalence clusters.
- **`ContinuousCensoringInjector`**: Injects right-censored or threshold-truncated feature values.
- **`GaussianJitterInjector`**: Adds controlled continuous Gaussian noise to numerical feature coordinates.
- **`CategoricalDriftInjector`**: Introduces rare and unobserved category levels to simulate covariate drift.

---

## 8. `evidense_x.imputation`
Benchmark imputation strategies under defect interaction.

- **`IterativeChainedEquationsImputer`**: Multivariate Imputation by Chained Equations (MICE) wrapper.
- **`KNNNeighborImputer`**: K-nearest neighbors distance-weighted imputation.
- **`MissForestRandomForestImputer`**: Non-parametric iterative random forest imputation.

---

## 9. `evidense_x.transforms`
Robust feature engineering and missingness awareness.

- **`MissingnessIndicatorAugmenter`**: Appends binary boolean indicator columns marking imputed locations.
- **`OutlierWinsorizer`**: Dynamic Tukey/IQR percentile clipping transformer.
- **`RobustTargetEncoder`**: Out-of-fold empirical Bayes smoothed target encoding for high-cardinality categoricals.
- **`QuantileRankTransformer`**: Non-linear uniform and normal quantile transformations for skewed features.

---

## 10. `evidense_x.ensemble`
Model stacking, post-hoc calibration, and robust ensemble combinations.

- **`SuperLearnerStackingClassifier`**: Out-of-fold meta-learner stacking combining diverse base models.
- **`SoftVotingProbabilityEnsemble`**: Weighted probability voting ensemble with confidence thresholding.
- **`BayesianModelAveragingEnsemble`**: Model averaging utilizing Bayesian Information Criterion (BIC) weights.
- **`TemperatureScaledEnsemble`**: Post-hoc logits temperature scaling for calibrated probability estimates.

---

## 11. `evidense_x.tuning`
Defect-aware hyperparameter optimization.

- **`DefectAwareCrossValidationTuner`**: Hyperparameter search utilizing duplicate-aware validation gates.
- **`SuccessiveHalvingPruner`**: Multi-fidelity early pruning scheduler for trial configurations.
- **`MultiObjectiveParetoOptimizer`**: Discovers Pareto-optimal hyperparameters balancing discrimination (AUC) and calibration (ECE).
- **`EarlyStoppingCallback`**: Plateaus monitoring callback preventing overfitting to contaminated validation folds.

---

## 12. `evidense_x.explainability`
Attribution auditing under missingness and duplicate contamination.

- **`TreeFeatureStabilityIndex`**: Measures Rank Correlation and Top-K attribution stability across duplicate injections.
- **`IntegratedGradientsApproximator`**: Path-integral feature attributions for continuous features.
- **`AttributionLeakageAuditor`**: Detects attribution collapse onto leaked duplicate coordinate markers.
- **`KernelSHAPExplainer`**: Tabular Shapley value explainer wrapper.

---

## 13. `evidense_x.metrics`
Formal evaluation metrics for defect interaction research.

- **`compute_lsi`**: Leakage Sensitivity Index ($LSI = \frac{F1_{\text{leaked}} - F1_{\text{clean}}}{F1_{\text{clean}}}$).
- **`compute_eri`**: Error-Reduction Illusion ($ERI = \frac{\text{Error}_{\text{clean}} - \text{Error}_{\text{leaked}}}{\text{Error}_{\text{clean}}}$).
- **`ExpectedCalibrationError`**: Binned expected calibration error ($ECE$).
- **`BrierDecomposition`**: Reliability, resolution, and uncertainty decomposition of Brier score.
- **`AreaUnderPrecisionRecallGain`**: Area under Precision-Recall Gain ($AUPRG$).
- **`DemographicParityDifference`**: Max difference in positive prediction rates across sensitive attributes.
- **`EqualizedOddsDisparity`**: Disparity across True Positive and False Positive rates between sub-populations.

---

## 14. `evidense_x.cli`
Production command router:

```bash
python -m evidense_x.cli {info, audit, benchmark, report, clean, govern, stream-audit, remediate} [OPTIONS]
```
