# File: app.py
# Description: Flask backend for the BULLION project

from flask import Flask, render_template, jsonify
from data_fetcher import fetch_metal_data, fetch_stock_data, fetch_currency_data

app = Flask(__name__)

@app.route("/")
def home():
    """
    Home route that renders the index page.
    """
    return render_template("index.html")

@app.route("/metals")
def metals():
    """
    Fetch and display metal prices.
    """
    try:
        metals_data = fetch_metal_data()
        return render_template("metals.html", metals=metals_data)
    except Exception as e:
        return f"Error fetching metals data: {str(e)}", 500

@app.route("/stocks")
def stocks():
    """
    Fetch and display stock market data.
    """
    try:
        stocks_data = fetch_stock_data()
        return render_template("stocks.html", stocks=stocks_data)
    except Exception as e:
        return f"Error fetching stock data: {str(e)}", 500

@app.route("/currencies")
def currencies():
    """
    Fetch and display currency exchange rates.
    """
    try:
        currency_data = fetch_currency_data()
        return render_template("currencies.html", currencies=currency_data)
    except Exception as e:
        return f"Error fetching currency data: {str(e)}", 500

@app.route("/api/metals")
def api_metals():
    """
    API endpoint for fetching metal prices in JSON format.
    """
    try:
        metals_data = fetch_metal_data()
        return jsonify(metals_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/stocks")
def api_stocks():
    """
    API endpoint for fetching stock market data in JSON format.
    """
    try:
        stocks_data = fetch_stock_data()
        return jsonify(stocks_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/currencies")
def api_currencies():
    """
    API endpoint for fetching currency exchange rates in JSON format.
    """
    try:
        currency_data = fetch_currency_data()
        return jsonify(currency_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

