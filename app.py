from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# API Keys and URLs from environment variables
METALS_API_KEY = os.getenv("METALS_API_KEY")
STOCKS_API_KEY = os.getenv("STOCKS_API_KEY")
FINANCE_API_KEY = os.getenv("FINANCE_API_KEY")

METALS_URL = f'https://metals-api.com/api/latest?access_key={METALS_API_KEY}'
STOCKS_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={STOCKS_API_KEY}'
FINANCE_URL = f'https://api.currencylayer.com/live?access_key={FINANCE_API_KEY}'

# Fetch and process metals data
def fetch_metal_data():
    try:
        response = requests.get(METALS_URL)
        response.raise_for_status()
        data = response.json()

        # Transform API response into desired structure
        metals = [
            {"name": metal, "price": details["price"], "unit": "USD/oz"}
            for metal, details in data["rates"].items()
        ]
        return metals
    except Exception as e:
        print(f"Error fetching metals data: {e}")
        return []

# Fetch and process stocks data
def fetch_stock_data():
    try:
        response = requests.get(STOCKS_URL)
        response.raise_for_status()
        data = response.json()
        stock_data = data["Time Series (5min)"]
        
        # Transform API response into desired structure
        stocks = [
            {
                "symbol": "IBM",
                "price": float(details["1. open"]),
                "change": f"{float(details['4. close']) - float(details['1. open']):.2f}"
            }
            for time, details in list(stock_data.items())[:1]  # Show only the latest update
        ]
        return stocks
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return []

# Fetch and process currency data
def fetch_currency_data():
    try:
        response = requests.get(FINANCE_URL)
        response.raise_for_status()
        data = response.json()

        # Transform API response into desired structure
        currencies = [
            {"pair": f"USD/{currency}", "rate": rate}
            for currency, rate in data["quotes"].items()
        ]
        return currencies
    except Exception as e:
        print(f"Error fetching currency data: {e}")
        return []

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metals")
def metals():
    metals_data = fetch_metal_data()
    return render_template("metals.html", metals=metals_data)

@app.route("/stocks")
def stocks():
    stocks_data = fetch_stock_data()
    return render_template("stocks.html", stocks=stocks_data)

@app.route("/currencies")
def currencies():
    currencies_data = fetch_currency_data()
    return render_template("currencies.html", currencies=currencies_data)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

