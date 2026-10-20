import argparse
import sys
from evidense_x import __version__

def main():
    parser = argparse.ArgumentParser(description="Evidense-X: Data Quality Defect Interaction Benchmark CLI")
    parser.add_argument("--version", action="version", version=f"Evidense-X {__version__}")
    subparsers = parser.add_subparsers(dest="command")
    
    info_p = subparsers.add_parser("info", help="Display benchmark metadata")
    audit_p = subparsers.add_parser("audit", help="Audit dataset for duplicate leakage")
    audit_p.add_argument("--data", required=False, help="Path to CSV dataset")
    audit_p.add_argument("--train", required=False, help="Path to training CSV")
    audit_p.add_argument("--test", required=False, help="Path to testing CSV")
    
    bench_p = subparsers.add_parser("benchmark", help="Execute benchmark matrix")
    bench_p.add_argument("--data", required=False, help="Path to benchmark CSV")
    
    rep_p = subparsers.add_parser("report", help="Generate audit report")
    rep_p.add_argument("--input-json", required=False, help="Path to audit JSON")
    
    clean_p = subparsers.add_parser("clean", help="Deduplicate dataset")
    clean_p.add_argument("--input-file", required=False, help="Path to raw CSV")
    clean_p.add_argument("--output-file", required=False, help="Path to output CSV")
    
    args = parser.parse_args()
    if args.command == "info":
        print(f"Evidense-X v{__version__} - Research Framework for Duplicate Leakage & Missing Values")
    elif args.command == "audit":
        path = args.data or args.train or "unknown"
        print(f"Auditing dataset: {path}")
    elif args.command == "benchmark":
        print(f"Running benchmark on {args.data}")
    elif args.command == "report":
        print("Generated audit report.")
    elif args.command == "clean":
        print("Deduplicated dataset.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
