import argparse
import sys
from bot.client import BinanceClientWrapper
from bot.validators import validate_order_params
from bot.logger import logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    
    # Updated choices to include STOP_MARKET
    parser.add_argument("--symbol", type=str, required=True, help="Trading Pair (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, choices=['BUY', 'SELL'], required=True, help="Order Side")
    parser.add_argument("--type", type=str, choices=['MARKET', 'LIMIT', 'STOP_MARKET'], required=True, help="Order Type")
    parser.add_argument("--qty", type=float, required=True, help="Quantity to trade")
    parser.add_argument("--price", type=float, help="Price (Required for LIMIT orders)")
    parser.add_argument("--stop-price", type=float, help="Stop Price (Required for STOP_MARKET orders)") # New Argument

    args = parser.parse_args()

    try:
        # Basic validation (You can expand validators.py if you wish)
        validate_order_params(args.symbol, args.side, args.type, args.qty, args.price)

        client = BinanceClientWrapper()

        # Pass the new stop_price argument
        response = client.place_order(
            symbol=args.symbol, 
            side=args.side, 
            order_type=args.type, 
            quantity=args.qty, 
            price=args.price,
            stop_price=args.stop_price 
        )

        print("\n" + "="*30)
        print("       ORDER SUMMARY       ")
        print("="*30)
        if "error" in response:
            print(f"FAILED: {response['error']}")
        else:
            print(f"Status:       {response.get('status')}")
            print(f"Order ID:     {response.get('orderId')}")
            print(f"Type:         {response.get('type')}")
            print(f"Executed Qty: {response.get('executedQty', '0')}")
        print("="*30 + "\n")

    except Exception as e:
        logger.critical(f"Critical Failure: {e}")
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
