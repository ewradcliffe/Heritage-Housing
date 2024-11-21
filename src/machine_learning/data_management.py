import streamlit as st
import pandas as pd
import numpy as np
import joblib


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_price_data():
    """Allows us to load house price data to dashboard"""
    df = pd.read_csv(
        "outputs/datasets/most_important_features_data/X_train.csv"
        )
    return df


def load_pkl_file(file_path):
    """Allows us to load pipeline & model to dashboard"""
    return joblib.load(filename=file_path)
