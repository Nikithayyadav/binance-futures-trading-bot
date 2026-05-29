# Binance Futures Trading Bot

A simplified Python trading bot for Binance Futures Testnet (USDT-M) that supports MARKET and LIMIT orders with CLI-based interaction, logging, and error handling.

---

# Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL sides
- Binance Futures Testnet integration
- Command-line interface using argparse
- Input validation
- Logging of API requests/responses/errors
- Structured modular codebase
- Environment variable support using `.env`

---

# Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── test_connection.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# Requirements

- Python 3.x
- Binance Futures Testnet Account
- Binance API Key and Secret

---

# Installation

## Clone Repository

```bash
git clone <your-github-repo-url>
cd trading_bot
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
``` 

---

# Binance Testnet Setup

Register/Login to Binance Futures Testnet:

https://testnet.binancefuture.com

Generate API credentials from Demo Trading API section.

Create a `.env` file in project root:

```env
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

---

# Running the Application

## Test Binance Connection

```bash
python test_connection.py
```

---

# Place MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Example:

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

---

# Place LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
```

---

# Example Output

```text
Order Request Summary
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

Order Successful
Order ID: 13160662530
Status: NEW
Executed Qty: 0.0000
Avg Price: 0.00
```

---

# Logging

Logs are stored in:

```text
logs/trading_bot.log
```

The log file contains:
- API requests
- API responses
- Order details
- Error logs
- Exception traces

---

# Validation & Error Handling

The application validates:
- BUY/SELL sides
- MARKET/LIMIT order types
- Positive quantity values
- Price requirement for LIMIT orders

Handled exceptions include:
- Invalid user input
- Binance API errors
- Network issues
- Timestamp synchronization issues

---

# Assumptions

- Orders are placed only on Binance Futures Testnet
- User has valid API credentials
- Internet connection is available
- BTCUSDT symbol is available on testnet

---

# Technologies Used

- Python 3
- python-binance
- python-dotenv
- rich
- argparse
- logging

---

# Author

Chandavena Nikitha yadav
