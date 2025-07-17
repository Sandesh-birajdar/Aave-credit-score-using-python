import pandas as pd
import argparse
import sys
import sklearn
from feature_engineer import engineer_features
from scorer import calculate_scores
from analysis import create_score_distribution_graph, analyze_wallet_behaviors

def main():
    """
    Main execution script for the Aave credit scoring tool.
    """
    parser = argparse.ArgumentParser(description="Aave Wallet Credit Scoring Tool")
    parser.add_argument(
    '--input_file',
    type=str,
    required=True,
    help=r"C:\Users\Sandesh\Downloads\aave-credit-scorer\user_transactions.json"
)

    parser.add_argument(
        '--output_file',
        type=str,
        default='wallet_scores.csv',
        help=r"C:\Users\Sandesh\Downloads\aave-credit-scorer\wallet_scores.csv"
    )
    args = parser.parse_args()

    # 1. Load Data
    print(f"Loading data from {args.input_file}...")
    try:
        # Assuming the JSON is a list of records
        df = pd.read_json(args.input_file)
    except Exception as e:
        print(f"Error loading JSON file: {e}", file=sys.stderr)
        sys.exit(1)
    
    print("Data loaded successfully.")

    # Debug: Show columns and first few rows
    print("Columns in loaded DataFrame:", df.columns.tolist())
    print("First 3 rows:\n", df.head(3))

    # 2. Engineer Features
    print("Engineering features for each wallet...")
    feature_df = engineer_features(df)
    print("Feature engineering complete.")
    print(f"Found and processed {len(feature_df)} unique wallets.")

    # 3. Calculate Scores
    print("Calculating credit scores...")
    scored_df = calculate_scores(feature_df)
    print("Scoring complete.")

    # 4. Save Results
    print(f"Saving scores to {args.output_file}...")
    scored_df.to_csv(args.output_file)
    print("Scores saved successfully.")

    # 5. Perform and Save Analysis
    print("Generating analysis...")
    create_score_distribution_graph(scored_df)
    analyze_wallet_behaviors(scored_df, feature_df)


if __name__ == '__main__':
    main()
