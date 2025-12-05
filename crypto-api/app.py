# from flask import Flask, jsonify, request
# import requests
# import jwt
# from datetime import datetime, timedelta
# from functools import wraps

# app = Flask(__name__)  # Fixed the typo here

# # Secret key for JWT encoding
# SECRET_KEY = 'abcdefgh123'

# # Route for the home page
# @app.route('/')
# def home():
#     return "Crypto API is running!"

# # Function to generate JWT token
# def generate_token():
#     payload = {
#         'exp': datetime.utcnow() + timedelta(days=1),
#         'iat': datetime.utcnow(),
#         'sub': 'user_id'
#     }
#     token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
#     return token

# # JWT Authentication decorator
# def token_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         token = request.headers.get('Authorization')
#         if not token:
#             return jsonify({"message": "Token is missing!"}), 403
#         try:
#             jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             return jsonify({"message": "Token has expired!"}), 403
#         except jwt.InvalidTokenError:
#             return jsonify({"message": "Invalid token!"}), 403
#         return f(*args, **kwargs)
#     return wrap
# # Route to generate JWT token
# @app.route('/token', methods=['GET'])
# def get_token():
#     token = generate_token()  # Call the function to generate a token
#     return jsonify({"token": token})

# # Route to list all coins with pagination
# @app.route('/coins', methods=['GET'])
# @token_required
# def list_coins():
#     page_num = request.args.get('page_num', 1, type=int)
#     per_page = request.args.get('per_page', 10, type=int)

#     url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&page={page_num}&per_page={per_page}'

#     response = requests.get(url)
#     data = response.json()

#     return jsonify(data)

# # Route to get a specific coin by id (e.g., /coin/bitcoin)
# @app.route('/coin/<coin_id>', methods=['GET'])
# def get_coin_by_id(coin_id):
#     url = f'https://api.coingecko.com/api/v3/coins/{coin_id}?localization=false'

#     response = requests.get(url)
#     data = response.json()

#     return jsonify(data)

# # Run the Flask app
# if __name__ == '__main__':  # Fixed the typo here
#     app.run(debug=True)

from flask import Flask
from routes.routes_coins import coins_bp
from routes.routes_meta import meta_bp

app = Flask(__name__)

# Register blueprints for routes
app.register_blueprint(coins_bp, url_prefix='/coins')
app.register_blueprint(meta_bp, url_prefix='/meta')

if __name__ == '__main__':
    app.run(debug=True)