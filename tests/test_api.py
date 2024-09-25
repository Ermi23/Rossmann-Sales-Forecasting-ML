import unittest
from flask import Flask
from src import app  # Import the Flask app from app.py

class FlaskTest(unittest.TestCase):
    def setUp(self):
        # Create a test client for the Flask app
        self.app = app.test_client()
        self.app.testing = True  # Enable testing mode

    def test_index(self):
        # Test the index route
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'), 'Hello, World!')

    def test_predict(self):
        # Test the predict route with some dummy data
        result = self.app.post('/predict', json={'input': [1, 2, 3, 4, 5]})  # Replace with appropriate test data
        self.assertEqual(result.status_code, 200)
        json_data = result.get_json()
        self.assertIn('prediction', json_data)

    def test_predict_no_data(self):
        # Test the predict route when no data is provided
        result = self.app.post('/predict', json=None)
        self.assertEqual(result.status_code, 400)
        json_data = result.get_json()
        self.assertIn('error', json_data)

if __name__ == '__main__':
    unittest.main()
