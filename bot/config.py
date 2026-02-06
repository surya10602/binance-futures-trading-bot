import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('BINANCE_TESTNET_API_KEY')
API_SECRET = os.getenv('BINANCE_TESTNET_SECRET_KEY')

if not API_KEY or not API_SECRET:
    raise ValueError("API credentials not found. Please set BINANCE_TESTNET_API_KEY and BINANCE_TESTNET_SECRET_KEY in a .env file.")