# import necessary libraries

import streamlit as st
import pandas as pd 
import numpy as np
import joblib 
from datetime import datetime 


# import the trained model
model = joblib.load('model.pkl')

st.title("Energy Consumption Forecasting")


# user input
import streamlit as st
from datetime import datetime

# Initialize session state on first load
if "date_selected" not in st.session_state:
    st.session_state.date_selected = datetime.now().date()
if "time_selected" not in st.session_state:
    st.session_state.time_selected = datetime.now().time()

# user input
# Date input
date_selected = st.date_input(
    "Select Date", 
    value=st.session_state.date_selected
)
st.session_state.date_selected = date_selected  # update session state

# Time input
time_selected = st.time_input(
    "Select Time", 
    value=st.session_state.time_selected
)
st.session_state.time_selected = time_selected  # update session state

# Combine into a datetime object for features
date_time = datetime.combine(date_selected, time_selected)

st.write("Selected datetime:", date_time)

# Lag feature input
lag1 = st.number_input("Energy consumption of previous hour (lag1)", min_value=0.0, step=0.1)

# Extract features from datetime
hour = date_time.hour
day = date_time.day
month = date_time.month
weekday = date_time.weekday()  # Monday=0, Sunday=6

# prepare features for prediction
features = pd.DataFrame([[hour, day, month, weekday, lag1]],
                        columns=["hour", "day", "month", "weekday", "lag1"])


# prediction button
if st.button("Predict"):
    prediction = model.predict(features)[0]
    st.success(f"Forecasted Energy Consumption: {prediction:.2f} units")



