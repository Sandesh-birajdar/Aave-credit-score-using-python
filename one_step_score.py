import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import argparse

def engineer_features(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    grouped = df.groupby('userWallet').agg(
        total_transactions=('userWallet', 'count'),
        total_amount_borrowed=('amount', lambda x: x[df.loc[x.index, 'action'] == 'borrow'].sum()),
        total_amount_supplied=('amount', lambda x: x[df.loc[x.index, 'action'] == 'deposit'].sum()),
        num_borrows=('action', lambda x: (x == 'borrow').sum()),
        num_deposits=('action', lambda x: (x == 'deposit').sum()),
        num_liquidations=('action', lambda x: (x == 'liquidation').sum()),
        first_txn=('timestamp', 'min'),
        last_txn=('timestamp', 'max')
    )
    grouped['active_days'] = (grouped['last_txn'] - grouped['first_txn']).dt.days + 1
    return grouped.reset_index()

def calculate_scores(df):
    df = df.copy()
    max_tx = df['total_transactions'].max() or 1
    max_deposit = df['total_amount_supplied'].max() or 1
    max_liquidations = df['num_liquidations'].max() or 1

    df['credit_score'] = (
        (df['total_transactions'] / max_tx) * 30 +
        (df['total_amount_supplied'] / max_deposit) * 30 +
        (1 - df['num_liquidations'] / max_liquidations) * 40
    ).clip(0, 100)

    return df

def plot_scores(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['credit_score'], bins=20, kde=True)
    plt.title("Credit Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Wallets")
    plt.grid(True)
    plt.savefig("score_distribution.png")
    plt.close()

def main():
    parser = argparse.ArgumentParser(description="One-step wallet scoring tool")
    parser.add_argument("--input", required=True, help="Path to the JSON transaction file")
    parser.add_argument("--output", default="wallet_scores.csv", help="Path to save wallet scores CSV")
    args = parser.parse_args()

    try:
        print("Loading data...")
        df = pd.read_json(args.input)
        print("Data loaded.")
    except Exception as e:
        print(f"Failed to load file: {e}", file=sys.stderr)
        sys.exit(1)

    print("Engineering features...")
    feature_df = engineer_features(df)

    print("Calculating scores...")
    scored_df = calculate_scores(feature_df)

    print("Saving scores to CSV...")
    scored_df.to_csv(args.output, index=False)

    print("Generating score distribution plot...")
    plot_scores(scored_df)

    print("✅ Done. Output saved to:", args.output)
    print("📊 Score graph: score_distribution.png")

if __name__ == "__main__":
    main()
