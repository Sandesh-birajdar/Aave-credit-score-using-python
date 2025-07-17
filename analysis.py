import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_score_distribution_graph(scored_df: pd.DataFrame, output_path: str = "score_distribution.png"):
    """
    Creates and saves a histogram of the score distribution.

    Args:
        scored_df (pd.DataFrame): DataFrame containing the final scores.
        output_path (str): Path to save the output image.
    """
    plt.figure(figsize=(12, 7))
    sns.histplot(scored_df['final_score'], bins=10, kde=False, color='#2b7cff')
    
    plt.title('Credit Score Distribution Across Wallets', fontsize=16)
    plt.xlabel('Credit Score (0-1000)', fontsize=12)
    plt.ylabel('Number of Wallets', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Set x-axis ticks to be the ranges
    bin_edges = range(0, 1001, 100)
    plt.xticks(ticks=bin_edges, labels=[f'{i}-{i+100}' for i in bin_edges[:-1]], rotation=45)
    
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Score distribution graph saved to {output_path}")

def analyze_wallet_behaviors(scored_df: pd.DataFrame, feature_df: pd.DataFrame):
    """
    Prints an analysis of wallet behaviors at different score ranges.
    """
    full_df = feature_df.join(scored_df)

    print("\n--- Wallet Behavior Analysis ---")

    # High-scoring wallets
    print("\n--- Characteristics of High-Scoring Wallets (Score > 800) ---")
    high_scorers = full_df[full_df['final_score'] > 800]
    if not high_scorers.empty:
        print(high_scorers[['wallet_age_days', 'repayment_ratio', 'liquidation_count', 'total_borrow_usd']].describe())
    else:
        print("No wallets found in this score range.")

    # Low-scoring wallets
    print("\n--- Characteristics of Low-Scoring Wallets (Score < 200) ---")
    low_scorers = full_df[full_df['final_score'] < 200]
    if not low_scorers.empty:
        print(low_scorers[['wallet_age_days', 'repayment_ratio', 'liquidation_count', 'total_borrow_usd']].describe())
    else:
        print("No wallets found in this score range.")