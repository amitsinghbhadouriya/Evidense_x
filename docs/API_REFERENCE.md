# Evidense-X API Reference

## Package: `evidense_x`

### Subpackages

#### `evidense_x.data`
- `DatasetLoader`: Static methods to load Wine Quality Red/White and Adult Census.
- `DatasetSchema`: Schema specification dataclass.

#### `evidense_x.defects`
- `apply_mcar_mask(df, feature_cols, mask_rate, seed)`: Injects MCAR missingness.
- `apply_mar_mask(df, feature_cols, conditioning_col, mask_rate, seed)`: Injects MAR missingness.
- `detect_duplicate_clusters(df, feature_cols, target_col)`: Identifies coordinate clusters.

#### `evidense_x.splitters`
- `DuplicateAwareGroupSplitter.split(...)`: Partitioning guaranteeing zero duplicate leakage.
- `ControlledLeakageInjector.inject(...)`: Controlled test-to-training leakage injection.

#### `evidense_x.metrics`
- `compute_lsi(f1_leak, f1_ref)`: Leakage Sensitivity Index.
- `compute_eri(f1_leak, f1_ref)`: Error-Reduction Illusion.
