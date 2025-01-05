import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from .env
METALS_API_KEY = os.getenv("METALS_API_KEY")
STOCKS_API_KEY = os.getenv("STOCKS_API_KEY")
CURRENCIES_API_KEY = os.getenv("CURRENCIES_API_KEY")

# API endpoints
METALS_API_URL = "https://api.example.com/metals"  # Replace with the actual API URL
STOCKS_API_URL = "https://api.example.com/stocks"  # Replace with the actual API URL
CURRENCIES_API_URL = "https://api.example.com/currencies"  # Replace with the actual API URL

def fetch_metal_data():
    """
    Fetch metal data from the API.

    Returns:
        list: A list of dictionaries containing metal data.
    """
    try:
        response = requests.get(METALS_API_URL, headers={"Authorization": f"Bearer {METALS_API_KEY}"})
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        data = response.json()  # Parse the JSON response
        return data  # Replace this with your desired data structure
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching metal data: {str(e)}")

def fetch_stock_data():
    """
    Fetch stock data from the API.

    Returns:
        list: A list of dictionaries containing stock data.
    """
    try:
        response = requests.get(STOCKS_API_URL, headers={"Authorization": f"Bearer {STOCKS_API_KEY}"})
        response.raise_for_status()
        data = response.json()
        return data  # Replace this with your desired data structure
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching stock data: {str(e)}")

def fetch_currency_data():
    """
    Fetch currency data from the API.

    Returns:
        list: A list of dictionaries containing currency data.
    """
    try:
        response = requests.get(CURRENCIES_API_URL, headers={"Authorization": f"Bearer {CURRENCIES_API_KEY}"})
        response.raise_for_status()
        data = response.json()
        return data  # Replace this with your desired data structure
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching currency data: {str(e)}")

