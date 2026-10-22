"""CLI subcommand for EU AI Act compliance checks and Model Card generation."""
import argparse
import os
import pandas as pd
from evidense_x.governance import EUAIActRiskClassifier, ModelCardGenerator, GovernanceExportSuite


def execute_govern_cli(args: argparse.Namespace) -> None:
    """Execute AI Act risk evaluation and output model card."""
    df = pd.read_csv(args.data)
    classifier = EUAIActRiskClassifier()
    record = classifier.evaluate_compliance(df, model_metadata={"model_name": args.name or "Model"})
    
    if args.output:
        md = GovernanceExportSuite.to_markdown(record)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Governance report written to: {args.output}")
    else:
        print(f"Risk Tier: {record.risk_tier} (Standard: {record.compliance_standard})")
        print(f"Leakage Score: {record.leakage_score:.2%}, Missingness: {record.missingness_vulnerability:.2%}")
        if record.identified_defects:
            print("Defects:", record.identified_defects)
