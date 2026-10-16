import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Profile data quality defects (missingness & duplicates)")
    parser.add_argument("csv_path", help="Path to input CSV file")
    args = parser.parse_args()
    
    df = pd.read_csv(args.csv_path)
    null_counts = df.isnull().sum()
    total_nulls = null_counts.sum()
    total_cells = df.size
    
    print("=" * 60)
    print(f"Data Quality Profile: {args.csv_path}")
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"Total Missing Cells: {total_nulls} ({total_nulls / total_cells * 100:.2f}%)")
    print("Column-wise Missing Counts:")
    for col, count in null_counts[null_counts > 0].items():
        print(f"  - {col}: {count} ({count/len(df)*100:.1f}%)")
    print("=" * 60)

if __name__ == '__main__':
    main()
