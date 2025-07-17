# Analysis of Wallet Credit Scores

This document provides an analysis of the credit scores assigned to wallets based on their Aave V2 transaction history. The scoring model evaluates wallets on a scale of 0 to 1000.

## Score Distribution

The distribution of credit scores across all processed wallets is shown below. The scores are grouped into 100-point bins.

![Credit Score Distribution](score_distribution.png)

### Key Observations from the Graph:
- A significant number of wallets fall into the 400-500 and 900-1000 score ranges.
- The peak in the 400-500 range likely represents users who have borrowed and repaid but may not have a long history or exhibit other less-than-perfect behaviors.
- The peak in the 900-1000 range represents ideal users who have a solid history, perfect repayment records, and no liquidations.
- The number of wallets with very low scores (0-100) is relatively small, which corresponds to the most severe negative event: liquidation.

## Behavior of Wallets in Different Score Ranges

### High-Range Wallets (Score 800-1000)

Wallets in this top tier are the most reliable and responsible users of the Aave protocol. Their on-chain behavior is characterized by:
- **Zero Liquidations**: They have never been liquidated.
- **Perfect Repayment History**: Their repayment ratio is 1.0 or very close to it, indicating they always pay back what they borrow.
- **Established History**: They tend to have a longer transaction history on the protocol.
- **Prudent Capital Management**: They often maintain a low loan-to-value (LTV) ratio, borrowing cautiously against their collateral.

These users are the bedrock of the protocol, providing stability and generating consistent revenue through interest payments.

### Mid-Range Wallets (Score 400-799)

This is the largest group, representing the "average" Aave user. Their profiles are typically a mix of positive and neutral indicators:
- **No Liquidations**: Like high-scorers, they generally avoid liquidation.
- **Good Repayment History**: Most have a high repayment ratio, but some may have outstanding loans, which temporarily lowers their repayment score.
- **Variable History**: May include both new users and those with moderate activity levels.
- **Standard Leverage**: They might utilize higher LTVs than the top-tier users but still manage their positions effectively to avoid liquidation.

### Lower-Range Wallets (Score 0-399)

Wallets at the lower end of the spectrum exhibit clear signs of high-risk or problematic behavior.
- **Primary Cause for Low Score: Liquidation**: The single most significant factor landing a wallet in this range is having at least one `liquidationCall` event. The model penalizes this event severely, often resulting in a score below 100.
- **Poor Repayment Ratio**: Some wallets in this category may have a low repayment ratio, indicating a large amount of outstanding debt relative to repayments.
- **Short or Erratic History**: While not the primary driver, a very new wallet with significant borrowing could also be scored lower until a positive repayment history is established.

These wallets represent the highest risk to the protocol, and their low score accurately reflects the financial danger they have either fallen into (liquidation) or are currently in.