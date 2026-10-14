# Experiment Reproduction Protocol

This guide outlines the exact commands required to reproduce all experimental evaluations, summary tables, publication figures, and the IEEE research paper.

## Prerequisites
- Python 3.10 or 3.11
- Microsoft Word (Windows only, required for `build_ieee_paper.py`)

## Setup
```bash
git clone https://github.com/amitsinghbhadouriya/Evidense_x.git
cd Evidense_x
python -m venv venv
source venv/bin/activate  # Or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

## Running Full Experiments
To execute the complete 2,160 experiment grid:
```bash
python run_all_experiments.py
```

## Generating Tables & Figures
```bash
python generate_summary_tables.py
python analyze_and_plot.py
```

## Compiling the IEEE Research Paper
```bash
python build_ieee_paper.py
```
