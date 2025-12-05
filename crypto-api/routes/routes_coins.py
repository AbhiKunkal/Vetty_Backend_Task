from flask import Blueprint, jsonify, request
from services.coingecko_client import CoinGeckoClient

coins_bp = Blueprint('coins', __name__)

@coins_bp.route('/', methods=['GET'])
def list_coins():
    page_num = request.args.get('page_num', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    coingecko = CoinGeckoClient()
    coins = coingecko.get_coins(page_num, per_page)
    
    return jsonify(coins)

@coins_bp.route('/<coin_id>', methods=['GET'])
def get_coin_by_id(coin_id: str):
    coingecko = CoinGeckoClient()
    coin = coingecko.get_coin_by_id(coin_id)
    
    return jsonify(coin)