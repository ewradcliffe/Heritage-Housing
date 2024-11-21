import streamlit as st
import pandas as pd
from src.machine_learning.predict_house_price import \
    load_house_price_predictor_model
from src.machine_learning.data_management import load_house_price_data


def predict_sale_price_body():
    # Function to render page.
    st.header("**Predict Sale Price.**")
    st.write(
        f"The client is interested in predicting the house sale prices from "
        f"her 4 inherited houses, and any other house in Ames, Iowa."
    )
    st.write(
        f"This page displays the sale prices of the clients houses predicted "
        f"with our model, and inputs for live house price prediction using "
        f"the same model."
    )

    # Display attributes and predicted price of clients houses.
    st.subheader(f"**Inherited house price predictions**")
    st.write(f"The client provided us with a data set for the houses she "
             f"inherited. We used our model to predict the price using the "
             f"most important features as detailed on the Project Findings "
             f"page.")
    st.write(f"The results are displayed below.")

    inherited_houses_prediction_df = (
        pd.read_csv(
            "outputs/datasets/predicted_prices_2/house_price_predictions_2.csv"
                    ))
    inherited_houses_prediction_df.rename(
        columns={'0': 'Price (USD)'}, inplace=True)
    st.write(inherited_houses_prediction_df)

    # Input widget for live predictions.
    st.subheader(f"**Predict a house price.**")
    st.write(f"To predict the price of any other house using the same model,"
             f"please enter the details below.")

    # Display input widget
    X_live = predict_price_input_widget()
    pipeline_features = pd.read_csv(
        f'outputs/datasets/most_important_features_data/X_train.csv'
        ).columns.to_list()

    # Predict on live data
    if st.button("Get my house price"):
        # Place the inputs in the same order as the data
        # set used to train the model.
        X_live = X_live.filter(pipeline_features)
        prediction = load_house_price_predictor_model(X_live)
        st.write(f"We predict the house is worth **${prediction}**")


def predict_price_input_widget():
    # Function to display input widget"""
    # Load the dataset to get choices for KitchenQual
    # and start value for OverallQual.
    df = load_house_price_data()

    # Empty dataframe for the live data.
    X_live = pd.DataFrame([], index=[0])

    # Render input widget to screen.
    col1, col2 = st.beta_columns(2)
    col3, col4 = st.beta_columns(2)

    with col1:
        feature = 'KitchenQual'
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col2:
        feature = 'OverallQual'
        st_widget = st.number_input(
            label=feature,
            min_value=1.0,
            max_value=10.0,
            value=df[feature].median(),
            step=1.0
        )
    X_live[feature] = st_widget

    with col3:
        st.write(f'Please grade the overall quality of the kitchen')
        st.write(f'Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair')

    with col4:
        st.write(f'Please grade the overall quality of the house on a scale ')
        st.write(f'of 1 - 10')

    feature = 'GarageArea'
    st_widget = st.slider(
        label=feature,
        min_value=0.0,
        max_value=3000.0,
        value=0.0,
        step=0.01
    )
    X_live[feature] = st_widget

    st.write(f'Size of garage in square feet')

    feature = 'GrLivArea'
    st_widget = st.slider(
        label=feature,
        min_value=0.0,
        max_value=10000.0,
        value=1000.0,
        step=0.01
    )
    X_live[feature] = st_widget

    st.write(f'Above grade (ground) living area square feet')

    feature = 'TotalBsmtSF'
    st_widget = st.slider(
        label=feature,
        min_value=0.0,
        max_value=10000.0,
        value=1000.0,
        step=0.01
    )
    X_live[feature] = st_widget

    st.write(f'Total square feet of basement area')

    return X_live
