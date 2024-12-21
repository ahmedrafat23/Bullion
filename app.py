# File: app.py
# Description: Flask backend for the BULLION project

from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# Replace with your actual API key and URL
gold_price_api_url = "https://www.goldapi.io/api/XAU/USD"
gold_price_api_key = "your_api_key_here"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/gold-price')
def gold_price():
    headers = {"x-access-token": gold_price_api_key}
    response = requests.get(gold_price_api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "price": data.get("price", "N/A"),
            "currency": data.get("currency", "USD")
        })
    else:
        return jsonify({"error": "Unable to fetch gold price."}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)

