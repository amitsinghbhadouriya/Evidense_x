# Guide to Configuring Group-Aware Cross-Validation

Standard `KFold` fails when duplicate instances are present. Use `DuplicateAwareGroupSplitter` to isolate identical feature vectors into distinct folds.
