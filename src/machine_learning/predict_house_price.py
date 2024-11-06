import streamlit as st
import numpy as np
import pandas as pd
from src.machine_learning.data_management import load_pkl_file
from tensorflow.keras.models import load_model


def load_house_price_predictor_model(user_input):
    """
    Load and perform house price prediction
    """

    pipeline = load_pkl_file(f"outputs/pipeline_2/pipeline_2.pkl")
    model = load_model(f"outputs/model_2/house_price_predictor_model_2.h5")

    user_input_transformed = pipeline.transform(user_input)
    house_price_prediction = model.predict(user_input_transformed)

    return house_price_prediction