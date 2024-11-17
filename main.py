from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel
import numpy as np

# Load your KNN model and scaler
model = joblib.load('knn_model.joblib')
scaler = joblib.load('scaler.joblib')

app = FastAPI()

# Define the input data model using the correct features
class InputFeatures(BaseModel):
    
    age: float
    appearance: int
    assists: float
    minutes_played: float
    days_injured: int
    games_injured: int
    award: int
    highest_value: float

# Preprocessing function
def preprocess_input(input_features: InputFeatures):
    try:
        # Convert the input features to a list
        feature_list = [
             input_feature.age,
             input_features.appearance,
             input_features.assists,
             input_features.minutes_played,
             input_features.days_injured,
             input_features.games_injured,
             input_features.award,
             input_features.highest_value,]
            
        # Scale the features using the loaded scaler
        scaled_features = scaler.transform([feature_list])  # Reshapes into a 2D array
        return np.array(scaled_features)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during preprocessing: {e}")


# POST request for making predictions
@app.post("/predict")
async def predict(input_features: InputFeatures):
    try:
        # Preprocess the input features
        data = preprocess_input(input_features)
        # Make a prediction using the model
        y_pred = model.predict(data)
        # Return the prediction as a dictionary
        return {"prediction": y_pred.tolist()[0]}
    except Exception as e:
        # Handle any errors that occur during processing or prediction
        raise HTTPException(status_code=500, detail=str(e))


# GET request
@app.get("/")
def read_root():
    return {"message": "Welcome to Football Price Prediction API"}

# Example endpoint (you can modify as needed)
@app.get("/items/")
def create_item(item: dict):
    return {"item": item}
