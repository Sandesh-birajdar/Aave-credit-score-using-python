#Link to the user-transactions json file: 

:

📁 Dataset: Aave V2 User Transactions
This dataset contains raw transaction-level data for user interactions with the Aave V2 DeFi protocol, structured as JSON records. Each transaction represents an action taken by a wallet address on the Aave protocol, such as deposits, borrows, repayments, liquidations, or withdrawals.

### Link to the user-transactions json file:

The below file is raw json file (~87MB)

https://drive.google.com/file/d/1ISFbAXxadMrt7Zl96rmzzZmEKZnyW7FS/view?usp=sharing

Or if you prefer the compressed zip file (~10MB)

https://drive.google.com/file/d/14ceBCLQ-BTcydDrFJauVA_PKAZ7VtDor/view?usp=sharing

You can download and unzip the compressed version for easier local processing.

📋 Data Schema Overview
Each record in the JSON file represents a transaction object with fields similar to the following:

json
Copy
Edit
{
  "tx_hash": "0x123456789abcdef...",
  "timestamp": 1631022243,
  "wallet_address": "0xabc123...",
  "action": "deposit",
  "amount": 1000.0,
  "asset": "USDC",
  "pool": "Aave V2",
  "tx_type": "supply",
  "block_number": 12938475
}
🧾 Common Fields:
Field	Description
tx_hash	Unique hash for the transaction
timestamp	Unix timestamp of when the transaction occurred
wallet_address	Wallet involved in the transaction
action	Type of action (e.g., deposit, borrow)
amount	Amount of asset transacted
asset	Token used in the transaction (e.g., USDC)
tx_type	Specific type of transaction (supply, repay)
pool	Lending pool involved (e.g., Aave V2)
block_number	Ethereum block number of the transaction

🔧 Usage in This Project
The transaction data is used as the core input for:

Feature engineering: Deriving behavioral metrics per wallet (e.g., total deposits, repayment ratios).

Wallet-level credit scoring: Assigning scores based on financial health and protocol behavior.

Behavioral analysis: Understanding trends in borrowing/lending across wallets.

💡 Notes
Please do not commit the raw JSON file to the GitHub repo to avoid bloating the repository size.

Prefer loading and processing this data locally or via cloud notebooks (e.g., Google Colab, Jupyter).

