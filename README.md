# Aave-credit-score-using-python

This project provides a robust, explainable model to assign a credit score (0–1000) to Ethereum wallets based on their historical transaction behavior on the Aave V2 protocol.

## Features

- **Wallet-level feature engineering** from raw Aave transaction data
- **Hybrid heuristic scoring model** (transparent, no pre-labeled data required)
- **Score distribution analysis** and summary statistics
- **Easy-to-use CLI scripts** for batch scoring and analysis

---

## Project Structure

- `main.py` — Main pipeline: loads data, engineers features, calculates scores, saves results, and runs analysis.
- `feature_engineer.py` — Extracts and aggregates wallet-level features from raw transaction data.
- `scorer.py` — Calculates the final credit score for each wallet using engineered features.
- `analysis.py` — Generates a score distribution plot and prints behavioral analysis of high/low scoring wallets.
- `one_step_score.py` — Alternative all-in-one script for quick scoring and plotting.
- `requirements.txt` — Python dependencies.
- `user_transactions.json` — Input data: list of Aave V2 user transactions (not included in repo due to size).
- `wallet_scores.csv` — Output: CSV of wallet addresses and their credit scores.
- `score_distribution.png` — Output: Histogram of score distribution.
- `analysis.md` — Example analysis and interpretation of results.

---

## How It Works

### 1. Data Loading

- Loads a JSON file of Aave V2 user transactions into a pandas DataFrame.

### 2. Feature Engineering (`feature_engineer.py`)

- Extracts features per wallet, such as:
  - Total transactions
  - Total borrowed/supplied (USD)
  - Number of borrows, deposits, liquidations
  - Wallet age (days active)
  - Repayment ratio (placeholder if not available)
  - Capital management proxy (placeholder if not available)

### 3. Scoring (`scorer.py`)

- Calculates four sub-scores:
  - **History & Stability** (15%)
  - **Repayment** (35%)
  - **Liquidation** (40%)
  - **Capital Management** (10%)
- Combines sub-scores into a final score (0–1000).

### 4. Analysis (`analysis.py`)

- Generates a histogram of scores.
- Prints summary statistics for high- and low-scoring wallets.

---

## Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd aave-credit-scorer
```

### 2. Set Up Python Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Prepare Data

- Place your `user_transactions.json` file in the project root.

### 4. Run the Main Pipeline

```bash
python main.py --input_file user_transactions.json
```

This will:
- Process the data and generate features
- Calculate a credit score for each wallet
- Save results to `wallet_scores.csv`
- Create a score distribution plot `score_distribution.png`
- Print a summary analysis to the console

### 5. (Optional) Use the One-Step Script

```bash
python one_step_score.py --input user_transactions.json
```

---

## Output Files

- `wallet_scores.csv` — Wallet addresses and their credit scores
- `score_distribution.png` — Histogram of score distribution
- Console output — Summary analysis of wallet behaviors

---

## Requirements

- Python 3.8+
- See `requirements.txt` for dependencies

---

## Notes

- The model is fully explainable and does not require labeled training data.
- Repayment ratio and capital management features are placeholders if not present in your data.
- For more details, see `analysis.md`.
