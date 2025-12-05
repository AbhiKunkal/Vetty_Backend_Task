import unittest
from app import app
from app.routes.auth import generate_token
from flask import jsonify

class TestSecurity(unittest.TestCase):
    def setUp(self):
        # Set up the Flask testing client
        self.app = app.test_client()
        self.app.testing = True

        # Generate a valid token (you can use any user ID)
        self.token = generate_token('user_id')

    def test_generate_token(self):
        """Test that a valid JWT token is generated correctly."""
        # Test if the token contains the 'sub' claim (user_id)
        token_data = jwt.decode(self.token, "your_secret_key", algorithms=["HS256"])
        self.assertEqual(token_data['sub'], 'user_id')  # Check the 'sub' claim

    def test_valid_token(self):
        """Test that the /coins route works with a valid token."""
        # Use the token in the Authorization header as Bearer Token
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        response = self.app.get('/coins?page_num=1&per_page=10', headers=headers)
        self.assertEqual(response.status_code, 200)  # Check for 200 OK

    def test_missing_token(self):
        """Test that the /coins route returns 403 if no token is provided."""
        response = self.app.get('/coins?page_num=1&per_page=10')
        self.assertEqual(response.status_code, 403)  # Token is missing, should return 403

    def test_invalid_token(self):
        """Test that the /coins route returns 403 if an invalid token is provided."""
        invalid_token = 'invalid_token_example'
        headers = {
            'Authorization': f'Bearer {invalid_token}'
        }
        response = self.app.get('/coins?page_num=1&per_page=10', headers=headers)
        self.assertEqual(response.status_code, 403)  # Invalid token, should return 403

    def test_expired_token(self):
        """Test that the /coins route returns 403 if an expired token is provided."""
        # Create an expired token manually
        expired_token = generate_token('user_id')
        expired_token_data = jwt.decode(expired_token, "your_secret_key", algorithms=["HS256"])
        expired_token_data['exp'] = 1  # Set an expired timestamp
        expired_token = jwt.encode(expired_token_data, "your_secret_key", algorithm="HS256")

        headers = {
            'Authorization': f'Bearer {expired_token}'
        }
        response = self.app.get('/coins?page_num=1&per_page=10', headers=headers)
        self.assertEqual(response.status_code, 403)  # Expired token, should return 403


if __name__ == '__main__':
    unittest.main()