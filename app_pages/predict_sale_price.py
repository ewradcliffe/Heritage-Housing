import streamlit as st
import pandas as pd

def predict_sale_price_body():

    st.write("### Predict Sale Price.")

    st.write(
        f"This page displays the predicted sale prices of the clients houses, and inputs for live house price prediction."
    )

    # Model Performance criteria
    st.write(
        f"Please note that out model meets the agreed performance criteria of R2 of at least 0.75.\n"
        f"Train set:   "
        f"Validation set:   "
        f"Test Set set:   "
    )

    # Display attributes and predicted price of clients houses.


    # Input widget for live predictions.

