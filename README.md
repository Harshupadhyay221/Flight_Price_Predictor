# Flight Price Predictor

Flight Price Predictor is a Streamlit-based application that predicts the price of flights based on user input. It utilizes a machine learning model trained on historical flight data.

## Overview

The Flight Price Predictor takes input from users regarding various parameters such as airline, source, destination, and total stops of their intended flight. It then utilizes a pre-trained machine learning model to predict the price of the flight based on these inputs.
## Usage

1. Input details about your flight, including airline, source, destination, and total stops, in the provided fields.

2. Click the "Predict" button to see the predicted price of the flight.

## Model

The machine learning model used for prediction is stored in `pipe.pkl`. This file contains the trained model serialized using Python's `pickle` module.

## Data

The flight data used to train the machine learning model is stored in `df.pkl`. This file contains a preprocessed dataset with features such as airline, source, destination, total stops, and flight price.






