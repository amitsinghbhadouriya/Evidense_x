import argparse
import pandas as pd
from evidense_x.defects.duplicates import detect_duplicate_clusters

def main():
    parser = argparse.ArgumentParser(description="Audit CSV for duplicate records and leakage risks")
    parser.add_argument("csv_path", help="Path to input CSV file")
    parser.add_argument("--target", default=None, help="Optional target column name")
    args = parser.parse_args()
    
    df = pd.read_csv(args.csv_path)
    feature_cols = [c for c in df.columns if c != args.target]
    res = detect_duplicate_clusters(df, feature_cols, args.target)
    
    print("=" * 60)
    print(f"Dataset: {args.csv_path}")
    print(f"Total Rows: {len(df)}")
    print(f"Duplicate Rows: {res['total_duplicate_rows']} ({res['duplicate_rate']*100:.2f}%)")
    print(f"Duplicate Clusters: {res['cluster_count']}")
    print("=" * 60)

if __name__ == '__main__':
    main()
