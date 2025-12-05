from flask import Flask
from flask_testing import TestCase
from app import app

class TestRoutes(TestCase):
    
    def create_app(self):
        return app
    
    def test_list_coins(self):
        response = self.client.get('/coins?page_num=1&per_page=10')
        self.assert200(response)  # Check for 200 OK
        self.assertIn('id', response.json[0])  # Check if 'id' is in the response
    
    def test_get_coin_by_id(self):
        response = self.client.get('/coins/bitcoin')
        self.assert200(response)  # Check for 200 OK
        self.assertIn('id', response.json)  # Check if 'id' is in the response