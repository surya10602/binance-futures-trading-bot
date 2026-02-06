from binance.client import Client
from binance.exceptions import BinanceAPIException  # <--- CHANGED THIS
from bot.config import API_KEY, API_SECRET
from bot.logger import logger

class BinanceClientWrapper:
    def __init__(self):
        # Initialize client with testnet=True
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        logger.info("Binance Futures Testnet Client Initialized.")

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        """
        Places an order on Binance Futures Testnet.
        Supports: MARKET, LIMIT, STOP_MARKET
        """
        try:
            logger.info(f"Sending Order -> Symbol: {symbol}, Side: {side}, Type: {order_type}, Qty: {quantity}, Price: {price}, StopPrice: {stop_price}")
            
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity,
            }

            # Logic for different order types
            if order_type == 'LIMIT':
                params['timeInForce'] = 'GTC'
                params['price'] = price
            
            elif order_type == 'STOP_MARKET':
                if not stop_price:
                    raise ValueError("Stop Price is required for STOP_MARKET orders")
                params['stopPrice'] = stop_price
                params['closePosition'] = 'true'  # Common for simple stop-losses, or remove if opening new pos

            # API Request
            response = self.client.futures_create_order(**params)
            
            logger.info(f"Order Success! ID: {response.get('orderId')}, Status: {response.get('status')}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message}")
            return {"error": e.message}
        except Exception as e:
            logger.error(f"Network/Unexpected Error: {str(e)}")
            return {"error": str(e)}
