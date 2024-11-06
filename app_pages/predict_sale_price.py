import streamlit as st
import pandas as pd
from src.machine_learning.predict_house_price import load_house_price_predictor_model
from src.machine_learning.data_management import load_house_price_data

def predict_sale_price_body():
    # Load house price data
    #load_house_price_data = (pd.read_csv(f"outputs/datasets/most_important_features_data/X_train.csv").columns.to_list())
    pipeline = load_pkl_file(f"outputs/pipeline_2/pipeline_2.pkl")

    st.write("### Predict Sale Price.")

    st.write(
        f"This page displays the predicted sale prices of the clients houses, and inputs for live house price prediction."
    )

    st.write("---")
    
    # Model Performance criteria
    st.write(
        f"Please note that out model meets the agreed performance criteria of R2 of at least 0.75.\n"
        f"Train set:   "
        f"Validation set:   "
        f"Test Set set:   "
    )

    st.write("---")

    # Display attributes and predicted price of clients houses.

    st.write("---")
    # Input widget for live predictions.

    ## Display input widget
    X_live = predict_price_input_widget()
    pipeline_features = pd.read_csv(f'outputs/datasets/most_important_features_data/X_train.csv').columns.to_list()

    # Predict on live data
    if st.button("Get my house price."):
        # Place the inputs in the same order as the data set used to train the model.
        X_live = X_live.filter(pipeline_features)
        print(X_live)

        prediction = load_house_price_predictor_model(X_live)
        st.write(f"We predict the house is worth **${prediction}**")


def predict_price_input_widget():
    """Function to display input widget"""
    # We need to load the dataset to get the min/max values for numerical inputs, and choices for catagorical data.
    df = load_house_price_data()
    st.write(f'{df}')
    percentageMin, percentageMax = 0.4, 2.0


    # we create input widgets for the 12 features not dropped.
    col1, col2, col3, col4, col5 = st.beta_columns(5)

    # Empty dataframe for the live data.
    X_live = pd.DataFrame([], index=[0])

    # Draw the widget based on the variable type (numerical or categorical)
    # and set initial values
    with col1:
        feature = 'KitchenQual'
        st_widget = st.selectbox(
            label=feature,
            options=df[0]
            #options=["Ex: Excellent", "Gd: Good", "TA: Typical/Average", "Fa: Fair; Po: Poor"]
        )
    X_live[feature] = st_widget

    with col2:
        feature = 'GarageArea'
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget
    
    with col3:
        feature = 'GrLivArea'
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget
    
    with col4:
        feature = 'OverallQual'
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col5:
        feature = 'TotalBsmtSF'
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    st.write(X_live)

    return X_live
