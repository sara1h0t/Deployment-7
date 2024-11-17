
import streamlit as st
import requests

# Set up the Streamlit app
st.title("Football Price Range Prediction")

# User inputs for the features defined in FastAPI
age = st.number_input("Age", min_value=18, max_value=40, value=25)
appearance = st.number_input("Appearance", min_value=0, max_value=100, value=30)
assists = st.number_input("Assists", min_value=0.0, max_value=50.0, value=5.0)
minutes_played = st.number_input("Minutes Played", min_value=0, max_value=10000, value=2000)
days_injured = st.number_input("Days Injured", min_value=0, max_value=365, value=30)
games_injured = st.number_input("Games Injured", min_value=0, max_value=100, value=5)
award = st.selectbox("Award", options=[0, 1], index=0)  # Assuming 0 = No, 1 = Yes
highest_value = st.number_input("Highest Value", min_value=0, max_value=50000000, value=5000000)

# Prediction button
if st.button("Predict Price Range"):
    # API request URL (FastAPI URL)
    url = "https://deployment-7-e2gn.onrender.com"  # Use your deployed URL

    # Data for the POST request
    data = {
        "age": age,
        "appearance": appearance,
        "assists": assists,
        "minutes_played": minutes_played,
        "days_injured": days_injured,
        "games_injured": games_injured,
        "award": award,
        "highest_value": highest_value
    }

    # Send the POST request
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Check for request errors

        # Check if 'prediction' exists in the response JSON
        if "prediction" in response.json():
            prediction = response.json()["prediction"]
            # Interpret the prediction
            price_range = {0: "Cheap Price", 1: "Good Price", 2: "High Price"}
            st.write(f"Estimated Price Range: {price_range.get(prediction, 'Unknown Price Range')}")
        else:
            st.error("Prediction not found in API response.")
    except requests.exceptions.RequestException as e:
        st.error("Error requesting prediction from API. Please try again.")
        st.write(e)
    except KeyError as e:
        st.error("Unexpected response format.")
        st.write(f"Error: {e}")
