import argparse
import sys
from bot.client import BinanceClientWrapper
from bot.validators import validate_order_params
from bot.logger import logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    
    # CLI Arguments 
    parser.add_argument("--symbol", type=str, required=True, help="Trading Pair (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, choices=['BUY', 'SELL'], required=True, help="Order Side")
    parser.add_argument("--type", type=str, choices=['MARKET', 'LIMIT'], required=True, help="Order Type")
    parser.add_argument("--qty", type=float, required=True, help="Quantity to trade")
    parser.add_argument("--price", type=float, help="Price (Required for LIMIT orders)")

    args = parser.parse_args()

    try:
        # Validation
        validate_order_params(args.symbol, args.side, args.type, args.qty, args.price)

        # Initialize Client
        client = BinanceClientWrapper()

        # Place Order
        response = client.place_order(
            symbol=args.symbol, 
            side=args.side, 
            order_type=args.type, 
            quantity=args.qty, 
            price=args.price
        )

        # Output Summary [cite: 27]
        print("\n" + "="*30)
        print("       ORDER SUMMARY       ")
        print("="*30)
        if "error" in response:
            print(f"FAILED: {response['error']}")
        else:
            print(f"Status:       {response.get('status')}")
            print(f"Order ID:     {response.get('orderId')}")
            print(f"Symbol:       {response.get('symbol')}")
            print(f"Side:         {response.get('side')}")
            print(f"Type:         {response.get('type')}")
            print(f"Executed Qty: {response.get('executedQty', '0')}")
            print(f"Avg Price:    {response.get('avgPrice', '0.0')}")
        print("="*30 + "\n")

    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        logger.critical(f"Critical Failure: {e}")
        print("An unexpected error occurred. Check logs for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()