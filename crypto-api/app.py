from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Crypto API is running!"

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/coins', methods=['GET'])
def list_coins():
    # Get pagination parameters (default page_num=1, per_page=10)
    page_num = request.args.get('page_num', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    # Construct the CoinGecko API URL with INR and CAD as the target currencies
    url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&page={page_num}&per_page={per_page}'

    # Send the GET request to CoinGecko
    response = requests.get(url)

    # Parse the JSON response from CoinGecko
    data = response.json()

    # Return the data as a JSON response
    return jsonify(data)

@app.route('/coin/<coin_id>', methods=['GET'])
def get_coin_by_id(coin_id):
    # Construct the CoinGecko API URL for a specific coin
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}?localization=false'

    # Send the GET request to CoinGecko
    response = requests.get(url)

    # Parse the JSON response from CoinGecko
    data = response.json()

    # Return the data as a JSON response
    return jsonify(data)

import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'your_secret_key'

def generate_token():
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': 'user_id'
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

from functools import wraps

def token_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing!"}), 403
        try:
            jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 403
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 403
        return f(*args, **kwargs)
    return wrap

@app.route('/coins', methods=['GET'])
@token_required
def list_coins():
    # Existing code here
    ...