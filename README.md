# Binance Futures Testnet Trading Bot

A simplified Python command-line application that places BUY/SELL orders on the Binance Futures Testnet. This project demonstrates structured API interaction, input validation, and logging.

## Features
- Supports **Market** and **Limit** orders.
- Validates user inputs (quantity, price, side).
- Logs all activities to `trading_bot.log`.
- Handles API errors and network exceptions gracefully.

## Prerequisites
- Python 3.x
- A Binance Futures Testnet Account
- API Key & Secret from the Testnet Dashboard

## Setup

1. **Clone/Download the repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Credentials: Create a .env file in the root directory:**
   ```bash
   BINANCE_TESTNET_API_KEY=your_api_key_here
   BINANCE_TESTNET_SECRET_KEY=your_secret_key_here
   ```
4. **Usage**
Run the bot using main.py with the required arguments.

## Examples
1. Place a Market Buy Order
```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.002
```
2. Place a Limit Sell Order
```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.002 --price 95000
```
3. Implement a Stop Limit
```bash
python main.py --symbol BTCUSDT --side SELL --type STOP_MARKET --qty 0.002 --stop-price 20000
```

## Assumptions
* The user has a stable internet connection to testnet.binancefuture.com.
* The user has sufficient USDT balance in their Testnet account (use the "Faucet" on the dashboard if empty).
* GTC (Good Till Cancel) is used as the default TimeInForce for Limit orders.
* closePosition=True is not enforced by default to allow for flexible opening/closing of positions.
