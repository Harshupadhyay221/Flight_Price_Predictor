import streamlit as st
import pickle
import numpy as np

# Load the model and DataFrame
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Flight Price Predictor")

# Selectbox for Airline
Airline = st.selectbox('Airline', df['Airline'].unique())

# Selectbox for Source
Source = st.selectbox('Source', df['Source'].unique())

# Selectbox for Destination
Destination = st.selectbox('Destination', df['Destination'].unique())

# Selectbox for Total_Stops
Total_Stops = st.selectbox('Total_Stops', sorted(df['Total_Stops'].unique()))  # Sorting the unique values for better presentation

if st.button("Predict"):
    input_data = [[Airline, Source, Destination, Total_Stops]]
    prediction = pipe.predict(input_data)
    st.write("Flight price prediction:", prediction)
