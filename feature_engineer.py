import pandas as pd

def engineer_features(df):
    """
    Engineer wallet-level features from raw Aave transaction data.
    Returns a DataFrame indexed by wallet address.
    """

    # Extract 'amount' from nested 'actionData' and convert to numeric (USDC has 6 decimals, so divide by 1e6)
    df['amount'] = pd.to_numeric(df['actionData'].apply(lambda x: x.get('amount', 0)), errors='coerce') / 1e6
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Use 'userWallet' as the wallet address
    features = df.groupby('userWallet').agg(
        transaction_count=('userWallet', 'count'),
        total_borrow_usd=('amount', lambda x: x[df.loc[x.index, 'action'] == 'borrow'].sum()),
        total_supply_usd=('amount', lambda x: x[df.loc[x.index, 'action'] == 'deposit'].sum()),
        num_borrows=('action', lambda x: (x == 'borrow').sum()),
        num_deposits=('action', lambda x: (x == 'deposit').sum()),
        liquidation_count=('action', lambda x: (x == 'liquidation').sum()),
        first_txn=('timestamp', 'min'),
        last_txn=('timestamp', 'max')
    )

    # Active days in protocol
    features['wallet_age_days'] = (features['last_txn'] - features['first_txn']).dt.days + 1

    # Repayment ratio (dummy, as we don't have repayment info in this sample)
    features['repayment_ratio'] = 1.0  # Placeholder, update if repayment data is available
    # Capital management proxy (dummy, as we don't have health factor info)
    features['avg_health_ratio_proxy'] = 0.5  # Placeholder, update if health factor data is available

    return features.reset_index()
