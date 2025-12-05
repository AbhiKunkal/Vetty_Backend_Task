import requests

class CoinGeckoClient:
    BASE_URL = 'https://api.coingecko.com/api/v3'

    def get_coins(self, page_num, per_page):
        url = f'{self.BASE_URL}/coins/markets?vs_currency=inr&page={page_num}&per_page={per_page}'
        response = requests.get(url)
        return response.json()

    def get_coin_by_id(self, coin_id):
        url = f'{self.BASE_URL}/coins/{coin_id}?localization=false'
        response = requests.get(url)
        return response.json()