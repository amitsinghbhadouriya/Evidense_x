# Evidense-X: Measuring the Interaction of Missing Values and Duplicate Leakage on ML Evaluation

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Research Track](https://img.shields.io/badge/Research-Data%20Science%20%26%20Analytics-brightgreen.svg)]()
[![Target Venue](https://img.shields.io/badge/Target-IEEE%20TKDE%20%2F%20BigData-orange.svg)]()
[![CI Status](https://img.shields.io/badge/build-passing-success.svg)]()

> **Official Research Codebase for:**  
> *"When Data Quality Defects Interact: Measuring the Impact of Missing Values and Duplicate Leakage on Machine Learning Evaluation"*

---

## Executive Summary

Supervised machine learning validation relies on the foundational assumption that training and test partitions are independent and identically distributed ($i.i.d.$). However, real-world data pipelines routinely experience co-occurring data quality defects:
- **Duplicate Leakage:** Unintentional cross-partition contamination when repeated observations cross split boundaries.
- **Feature Missingness:** Incomplete feature vectors altering the information geometry of observations.

While existing literature treats data leakage and missing values as separate concerns, **Evidense-X** demonstrates their significant empirical interaction across **3 tabular benchmark datasets**, **3 classifier families**, **4 missingness levels**, and **4 controlled overlap tiers** across 10 random seeds (**2,160 model evaluations**).

---

## Key Empirical Findings

1. **Extreme, Model-Dependent F1 Inflation:** At $50\%$ duplicate overlap, F1 scores were inflated by $+0.142$ to $+0.202$ for Decision Trees and $+0.098$ to $+0.168$ for Random Forests ($p < 0.002$, Wilcoxon signed-rank tests), while Logistic Regression exhibited negligible sensitivity ($\Delta F1 \le +0.006$).
2. **The Error-Reduction Illusion (ERI):** Up to $60.8\%$ of apparent test errors were eliminated purely by duplicate memorization.
3. **Natural Duplicate Distortion:** Standard random splitting on datasets with naturally occurring duplicates ($15.0\%$ in Red Wine, $19.1\%$ in White Wine) caused $+0.035$ to $+0.066$ F1 inflation in tree models.
4. **Defect Interaction:** Ordinary least squares (OLS) regressions reveal that missingness significantly amplifies tree-based duplicate leakage in higher-dimensional spaces ($\beta_{\text{inter}} = +0.244, p < 10^{-9}$ for Random Forest on Adult).
5. **Coordinate Alignment Mechanism:** Independently masking duplicate copies destroys exact multi-dimensional coordinate alignment, reducing retained leakage to $15.0\% - 32.3\%$ at $30\%$ missingness.

---

## Repository Structure

```
Evidense_x/
├── .github/
│   └── workflows/
│       └── ci.yml                     # GitHub Actions continuous integration
├── Adult/                             # Adult Census Income dataset & documentation
│   ├── adult.data
│   ├── adult.names
│   ├── adult.test
│   ├── Index
│   └── old.adult.names
├── wine quality/                      # Wine Quality benchmark datasets
│   ├── winequality-red.csv
│   ├── winequality-white.csv
│   └── winequality.names
├── docs/                              # Detailed methodology & reproducibility docs
│   ├── METHODOLOGY.md
│   ├── PROBLEM_STATEMENT.md
│   └── REPRODUCIBILITY.md
├── figures/                           # High-resolution publication figures
│   ├── fig1_f1_inflation_by_overlap.png
│   ├── fig2_missingness_interaction.png
│   ├── fig3_ordinary_vs_duplicate_aware.png
│   └── fig4_exact_vs_independent_mask.png
├── results/                           # Raw experimental CSV logs
│   ├── results_main.csv
│   └── results_supp.csv
├── tables/                            # Generated publication tables
│   ├── comprehensive_summary_table.csv
│   ├── table1_dataset_characteristics.csv
│   ├── table2_inflation_50pct_0missing.csv
│   ├── table3_ordinary_vs_ref_0missing.csv
│   ├── table_lsi_eri.csv
│   ├── table_ols_interaction.csv
│   └── table_retention_30pct_missing.csv
├── tests/                             # Pytest test suite
│   ├── test_defect_injection.py
│   └── test_metrics_and_pipelines.py
├── Amity_Researchothon_Research_Paper.docx  # Formatted Word research manuscript
├── Amity_Researchothon_Research_Paper.pdf   # Camera-ready IEEE PDF manuscript
├── RESEARCH_PAPER.md                  # Complete IEEE manuscript in markdown
├── analyze_and_plot.py                # Publication visualization & plotting script
├── build_ieee_paper.py                # Automated IEEE Word/PDF compilation engine
├── experiment_runner.py               # Core preprocessing & pipeline modules
├── generate_summary_tables.py         # Summary statistics extraction script
├── run_all_experiments.py             # Full experimental grid execution engine
├── pyproject.toml                     # Python package configuration
├── requirements.txt                   # Dependency manifest
└── README.md                          # Repository overview & documentation
```

---

## Quickstart & Installation

```bash
# Clone the repository
git clone https://github.com/amitsinghbhadouriya/Evidense_x.git
cd Evidense_x

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Unit Tests
```bash
pytest tests/ -v
```

### Reproduce Figures and Tables
```bash
python generate_summary_tables.py
python analyze_and_plot.py
```

---

## Citation

```bibtex
@article{bhadouriya2026evidense,
  title={When Data Quality Defects Interact: Measuring the Impact of Missing Values and Duplicate Leakage on Machine Learning Evaluation},
  author={Bhadouriya, Amit Singh},
  journal={IEEE Transactions on Knowledge and Data Engineering (Targeted)},
  year={2026}
}
```

## License
Distributed under the [MIT License](LICENSE).
