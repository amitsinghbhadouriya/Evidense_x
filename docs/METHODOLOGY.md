# Empirical & Statistical Methodology

## 1. Experimental Design Overview

The experimental design investigates the dual-defect interaction across three benchmark datasets, three classifier architectures, four missingness levels, and four duplicate overlap tiers across ten random seeds ($2,160$ model evaluations).

### Partitioning & Controlled Leakage Injection

1. **Duplicate-Aware Reference Split ($0\%$ Overlap):**
   Group splitting partitions rows such that identical feature-label tuples are isolated entirely within either train or test sets.

2. **Controlled Overlap Injection ($10\%, 25\%, 50\%$ Overlap):**
   A predetermined fraction $\alpha \in \{0.10, 0.25, 0.50\}$ of test set records are randomly sampled and injected into the training set prior to model fitting.

3. **MCAR Defect Injection:**
   Features are masked with Missing Completely at Random probability $p \in \{0.0, 0.10, 0.20, 0.30\}$.

## 2. Quantitative Diagnostic Metrics

### Leakage Sensitivity Index (LSI)
$$\text{LSI} = \Delta F1_{50\% \text{ overlap}} = F1(50\% \text{ overlap}, 0\% \text{ missing}) - F1(0\% \text{ overlap}, 0\% \text{ missing})$$

### Error-Reduction Illusion (ERI)
$$\text{ERI} = \frac{\text{Error}_{\text{ref}} - \text{Error}_{\text{leak}}}{\text{Error}_{\text{ref}}} = \frac{(1 - F1_{\text{ref}}) - (1 - F1_{\text{leak}})}{1 - F1_{\text{ref}}}$$

## 3. Econometric OLS Interaction Model
$$F1_{i} = \beta_0 + \beta_1 \cdot \text{Overlap}_{i} + \beta_2 \cdot \text{Missing}_{i} + \beta_3 \cdot (\text{Overlap}_{i} \times \text{Missing}_{i}) + \epsilon_i$$
