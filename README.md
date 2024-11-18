# Streamlit App
Description: Streamlit For creating the interactive web interface.
Deployment: The Streamlit app is hosted on Streamlit Cloud and sends requests to the FastAPI backend for predictions.
Streamlit App URL: https://football-prediction.streamlit.app/


# FastAPI App

Description: The backend is implemented using FastAPI, which provides a RESTful API for making predictions. The KNN model and a scaler are loaded to preprocess the input data and return the predicted price range.
Deployment: The FastAPI application is hosted on Render. The API accepts POST requests to the /predict endpoint with the input features and returns the prediction.
FastAPI App URL: https://deployment-7-e2gn.onrender.com
