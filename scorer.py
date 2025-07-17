import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def calculate_scores(feature_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates credit scores for wallets based on engineered features.

    Args:
        feature_df (pd.DataFrame): DataFrame of engineered features for each wallet.

    Returns:
        pd.DataFrame: DataFrame with wallet addresses and their final credit scores.
    """
    scores_df = feature_df.copy()
    
    # --- Define weights for the final score ---
    weights = {
        'history_score': 0.15,
        'repayment_score': 0.35,
        'liquidation_score': 0.40,
        'capital_management_score': 0.10
    }

    # --- 1. History & Stability Score (0-1) ---
    scores_df['history_score'] = MinMaxScaler().fit_transform(
        np.log1p(scores_df[['wallet_age_days', 'transaction_count']])
    ).mean(axis=1)

    # --- 2. Repayment Score (0-1) ---
    scores_df['repayment_score'] = scores_df['repayment_ratio'].clip(0, 1)

    # --- 3. Liquidation Score (0-1) ---
    scores_df['liquidation_score'] = np.where(scores_df['liquidation_count'] > 0, 0, 1)
    
    # --- 4. Capital Management Score (0-1) ---
    health_proxy_scaled = MinMaxScaler().fit_transform(scores_df[['avg_health_ratio_proxy']])
    scores_df['capital_management_score'] = 1 - health_proxy_scaled.flatten()

    # --- Final Score Calculation (0-1000) ---
    scores_df['final_score'] = (
        scores_df['history_score'] * weights['history_score'] +
        scores_df['repayment_score'] * weights['repayment_score'] +
        scores_df['liquidation_score'] * weights['liquidation_score'] +
        scores_df['capital_management_score'] * weights['capital_management_score']
    )

    scores_df['final_score'] = (scores_df['final_score'] * 1000).astype(int)

    # Reset index to ensure wallet addresses are a column
    scores_df = scores_df.reset_index()
    # Rename the index column to 'wallet_address' if needed
    if 'userWallet' in scores_df.columns:
        scores_df = scores_df.rename(columns={'userWallet': 'wallet_address'})
    elif 'index' in scores_df.columns:
        scores_df = scores_df.rename(columns={'index': 'wallet_address'})
    else:
        first_col = scores_df.columns[0]
        if isinstance(first_col, str):
            scores_df = scores_df.rename(columns={first_col: 'wallet_address'})
    scores_df = scores_df.sort_values('final_score', ascending=False)
    return scores_df[['wallet_address', 'final_score']].copy()