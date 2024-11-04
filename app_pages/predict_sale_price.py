import streamlit as st
import pandas as pd
from src.machine_learning.predict_house_price import load_house_price_predictor_model
from src.machine_learning.data_management import load_house_price_data

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

    def predict_price_input_widget():

        # We need to load the dataset to get the min/max values for numerical inputs, and choices for catagorical data.
        df = load_house_price_data()
        percentageMin, percentageMax = 0.4, 2.0


        # we create input widgets for the 12 features not dropped.
        col1, col2, col3, col4 = st.beta_columns(4)
        col5, col6, col7, col8 = st.beta_columns(4)
        col9, col10, col11, col12 = st.beta_columns(4)
        col3, col14, col15, col16 = st.beta_columns(4)


        # Empty dataframe for the live data.
        X_live = pd.DataFrame([], index=[0])

        # Draw the widget based on the variable type (numerical or categorical)
        # and set initial values
        with col1:
            feature = "BsmtExposure"
            st_widget = st.selectbox(
                label=feature,
                options=df[feature].unique()
            )
        X_live[feature] = st_widget

        with col2:
            feature = "BsmtFinType1"
            st_widget = st.selectbox(
                label=feature,
                options=df[feature].unique()
            )
        X_live[feature] = st_widget

        with col3:
            feature = "GarageFinish"
            st_widget = st.selectbox(
                label=feature,
                options=df[feature].unique()
            )
        X_live[feature] = st_widget

        with col4:
            feature = "KitchenQual"
            st_widget = st.selectbox(
                label=feature,
                options=df[feature].unique()
            )
        X_live[feature] = st_widget

        with col5:
            feature = "BedroomAbvGr"
            st_widget = st.number_input(
                label=feature,
                min_value=df[feature].min()*percentageMin,
                max_value=df[feature].max()*percentageMax,
                value=df[feature].median()
            )
        X_live[feature] = st_widget

        with col6:
            feature = "BsmtFinSF1"
            st_widget = st.number_input(
                label=feature,
                min_value=df[feature].min()*percentageMin,
                max_value=df[feature].max()*percentageMax,
                value=df[feature].median()
            )
        X_live[feature] = st_widget

        with col7:
            feature = "BsmtUnfSF"
            st_widget = st.number_input(
                label=feature,
                min_value=df[feature].min()*percentageMin,
                max_value=df[feature].max()*percentageMax,
                value=df[feature].median()
            )
        X_live[feature] = st_widget

        with col8:
            feature = "GrLivArea"
            st_widget = st.number_input(
                label=feature,
                min_value=df[feature].min()*percentageMin,
                max_value=df[feature].max()*percentageMax,
                value=df[feature].median()
            )
        X_live[feature] = st_widget

        with col9:
            feature = "LotArea"
            st_widget = st.number_input(
                label=feature,
                min_value=df[feature].min()*percentageMin,
                max_value=df[feature].max()*percentageMax,
                value=df[feature].median()
            )
        X_live[feature] = st_widget

        with col10:
            feature = "LotFrontage"
            st_widget = st.number_input(
                label=feature,
                min_value=df[feature].min()*percentageMin,
                max_value=df[feature].max()*percentageMax,
                value=df[feature].median()
            )
        X_live[feature] = st_widget

        with col11:
            feature = "MasVnrArea"
            st_widget = st.number_input(
                label=feature,
                min_value=df[feature].min()*percentageMin,
                max_value=df[feature].max()*percentageMax,
                value=df[feature].median()
            )
        X_live[feature] = st_widget

        with col12:
            feature = "OpenPorchSF"
            st_widget = st.number_input(
                label=feature,
                min_value=df[feature].min()*percentageMin,
                max_value=df[feature].max()*percentageMax,
                value=df[feature].median()
            )
        X_live[feature] = st_widget

        with col13:
            feature = "OverallCond"
            st_widget = st.number_input(
                label=feature,
                min_value=df[feature].min().unique()
                max_value=df[feature].max().unique()
                value=df[feature].median()
            )
        X_live[feature] = st_widget

        with col14:
            feature = "OverallQual"
            st_widget = st.number_input(
                label=feature,
                min_value=df[feature].min().unique()
                max_value=df[feature].max().unique()
                value=df[feature].median()
            )
        X_live[feature] = st_widget

        with col15:
            feature = "TotalBsmtSF"
            st_widget = st.number_input(
                label=feature,
                min_value=df[feature].min()*percentageMin,
                max_value=df[feature].max()*percentageMax,
                value=df[feature].median()
            )
        X_live[feature] = st_widget

        with col16:
            feature = "YearRemodAdd"
            st_widget = st.number_input(
                label=feature,
                min_value=df[feature].min().unique()
                max_value=df[feature].max().unique()
                value=df[feature].median()
            )
        X_live[feature] = st_widget


        return X_live



    




