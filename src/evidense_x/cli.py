import argparse
import sys
from . import __version__

def main():
    parser = argparse.ArgumentParser(description="Evidense-X: Data Quality Defect Interaction Benchmark CLI")
    parser.add_argument("--version", action="version", version=f"Evidense-X {__version__}")
    subparsers = parser.add_subparsers(dest="command")
    
    info_p = subparsers.add_parser("info", help="Display benchmark metadata")
    audit_p = subparsers.add_parser("audit", help="Audit dataset for duplicate leakage")
    audit_p.add_argument("--data", required=True, help="Path to CSV dataset")
    
    args = parser.parse_args()
    if args.command == "info":
        print(f"Evidense-X v{__version__} - Research Framework for Duplicate Leakage & Missing Values")
    elif args.command == "audit":
        print(f"Auditing dataset: {args.data}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
