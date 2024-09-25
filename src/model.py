import numpy as np
import pickle
from flask import Flask

# Load the trained model
with open('models/sales_model.pkl', 'rb') as f:
    model = pickle.load(f)

def preprocess_input(data):
    # Here, you would implement any input preprocessing steps such as scaling
    # or handling categorical variables.
    # Assuming data is already preprocessed and passed in the correct format.
    return np.array(data).reshape(1, -1)  # Convert to the format expected by the model

def predict_sales(data):
    # Preprocess input data
    processed_data = preprocess_input(data)
    
    # Make prediction using the loaded model
    prediction = model.predict(processed_data)
    
    return prediction[0]  # Return the prediction result
