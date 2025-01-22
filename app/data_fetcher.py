import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve API keys from environment variables
METALS_API_KEY = os.getenv("METALS_API_KEY")  # API key for accessing metals data
STOCKS_API_KEY = os.getenv("STOCKS_API_KEY")  # API key for accessing stock market data
FINANCE_API_KEY = os.getenv("FINANCE_API_KEY")  # API key for accessing financial data

# Base URLs for the APIs
METALS_URL = f'https://metals-api.com/api/latest?access_key={METALS_API_KEY}'  # Endpoint for metals data
STOCKS_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={STOCKS_API_KEY}'  # Endpoint for stock market data
FINANCE_URL = f'https://api.currencylayer.com/live?access_key={FINANCE_API_KEY}'  # Endpoint for currency exchange data

def fetch_metals_data():
    """Fetches data from the Metals API."""
    try:
        print("Sending request to Metals API...")  # Log the request initiation
        response = requests.get(METALS_URL)  # Send GET request to the Metals API
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Received response from Metals API.")  # Log successful response
        data = response.json()  # Parse the JSON response

        # Extract specific information (example: gold, silver rates)
        metals_data = {
            "gold": data.get("rates", {}).get("XAU", "N/A"),  # Get gold rate
            "silver": data.get("rates", {}).get("XAG", "N/A")  # Get silver rate
        }
        print("Extracted metals data:", metals_data)  # Log extracted data
        return metals_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching metals data: {e}")  # Log the error
        return {"error": f"Failed to fetch metals data: {e}"}  # Return error information

def fetch_stocks_data():
    """Fetches data from the Stocks API."""
    try:
        print("Sending request to Stocks API...")  # Log the request initiation
        response = requests.get(STOCKS_URL)  # Send GET request to the Stocks API
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Received response from Stocks API.")  # Log successful response
        data = response.json()  # Parse the JSON response

        # Extract specific information (example: time series data)
        time_series = data.get("Time Series (5min)", {})  # Access time series data
        latest_timestamp = next(iter(time_series), "N/A")  # Get the latest timestamp
        stock_data = time_series.get(latest_timestamp, {})  # Get data for the latest timestamp

        result = {
            "timestamp": latest_timestamp,  # Include timestamp in the result
            "data": stock_data  # Include stock data
        }
        print("Extracted stocks data:", result)  # Log extracted data
        return result

    except requests.exceptions.RequestException as e:
        print(f"Error fetching stocks data: {e}")  # Log the error
        return {"error": f"Failed to fetch stocks data: {e}"}  # Return error information

def fetch_finance_data():
    """Fetches data from the Finance API."""
    try:
        print("Sending request to Finance API...")  # Log the request initiation
        response = requests.get(FINANCE_URL)  # Send GET request to the Finance API
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Received response from Finance API.")  # Log successful response
        data = response.json()  # Parse the JSON response

        # Extract specific information (example: USD to other currencies)
        finance_data = data.get("quotes", {})  # Access currency exchange rates
        print("Extracted finance data:", finance_data)  # Log extracted data
        return finance_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching finance data: {e}")  # Log the error
        return {"error": f"Failed to fetch finance data: {e}"}  # Return error information

# Example usage
if __name__ == "__main__":
    print("Fetching metals data...")
    print(fetch_metals_data())  # Fetch and print metals data

    print("\nFetching stocks data...")
    print(fetch_stocks_data())  # Fetch and print stocks data

    print("\nFetching finance data...")
    print(fetch_finance_data())  # Fetch and print finance data

