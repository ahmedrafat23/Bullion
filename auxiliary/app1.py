from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Configuration
API_KEY_METALS = 'your_metals_api_key'  # Replace with your Metals-API key
API_KEY_CURRENCIES = 'your_currency_api_key'  # Replace with your currency API key
API_KEY_STOCKS = 'your_stock_api_key'  # Replace with your stock API key

# Base URLs
METALS_URL = 'https://metals-api.com/api/latest'
CURRENCY_URL = 'https://api.exchangerate-api.com/v4/latest/USD'
STOCK_URL = 'https://finnhub.io/api/v1/quote'  # Example for stock prices


@app.route('/')
def home():
    """Homepage with links to features."""
    return render_template('index.html')


@app.route('/metals')
def metals():
    """Metals prices page."""
    return render_template('metals.html')


@app.route('/currencies')
def currencies():
    """Currencies exchange rates page."""
    return render_template('currencies.html')


@app.route('/stocks')
def stocks():
    """Stock prices page."""
    return render_template('stocks.html')


@app.route('/get-metals')
def get_metals():
    """Fetch real-time metals prices."""
    symbols = 'XAU,XAG'  # XAU = Gold, XAG = Silver
    response = requests.get(
        METALS_URL, params={'access_key': API_KEY_METALS, 'symbols': symbols}
    )
    data = response.json()
    if response.status_code == 200:
        return jsonify(data['rates'])
    return jsonify({'error': 'Failed to fetch metals prices'}), 500


@app.route('/get-currencies')
def get_currencies():
    """Fetch real-time currency exchange rates."""
    response = requests.get(CURRENCY_URL)
    data = response.json()
    if response.status_code == 200:
        return jsonify(data['rates'])
    return jsonify({'error': 'Failed to fetch currency rates'}), 500


@app.route('/get-stocks')
def get_stocks():
    """Fetch real-time stock prices for selected companies."""
    companies = {'AAPL': 'Apple', 'TSLA': 'Tesla', 'GOOGL': 'Alphabet'}
    stock_prices = {}
    for symbol, name in companies.items():
        response = requests.get(
            STOCK_URL, params={'symbol': symbol, 'token': API_KEY_STOCKS}
        )
        data = response.json()
        if response.status_code == 200:
            stock_prices[name] = data['c']  # 'c' is the current price
    return jsonify(stock_prices)


if __name__ == '__main__':
    app.run(debug=True)

