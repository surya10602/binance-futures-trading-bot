from bot.logger import logger

def validate_order_params(symbol, side, order_type, quantity, price):
    """
    Validates input parameters for the order.
    """
    if quantity <= 0:
        msg = f"Invalid quantity: {quantity}. Must be greater than 0."
        logger.error(msg)
        raise ValueError(msg)

    if order_type.upper() == 'LIMIT':
        if price is None or price <= 0:
            msg = "Price is required and must be > 0 for LIMIT orders."
            logger.error(msg)
            raise ValueError(msg)
    
    return True