from flask import Flask, jsonify, request
from src.model import predict_sales

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return 'Hello, World!'

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get the input data
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Call the prediction function from model.py
    prediction = predict_sales(data)
    
    # Return the prediction result as a JSON response
    return jsonify({'prediction': prediction})

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
