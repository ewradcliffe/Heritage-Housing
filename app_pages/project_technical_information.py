import streamlit as st

def project_technical_information_body():
    #Renders technical information page.

    st.header("**Technical Information**")
    st.write(f"This page shows information which may be useful for data analysts and "
             f"developers."
    )
    # Model Performance criteria. Please note that although we have trained two models
    # we are only providing data for the deployed model. The information is hard copied
    # from 07 - ModellingMostImportantFeatures
    st.subheader(f"Model Performance")
    st.write(f"**Train Set**")
    st.write(
        f"Please see below for details of the performance of train, validation and "
        f"test data sets. Please note that our model meets the agreed performance "
        f"criteria of R2 of at least 0.75."
        )

    # Train set
    st.write(f"**Train Set**")
    st.write(f"R2 Score: 0.843  \n Mean Absolute Error: 20617.138  \n"
            f"Mean Squared Error: 989369562.043  \n Root Mean Squared Error: 31454.246"
            )

    # Validation set.
    st.write(f"**Validation Set**")
    st.write(f"R2 Score: 0.849  \n Mean Absolute Error: 21183.536  \n"
            f"Mean Squared Error: 829900380.727  \n Root Mean Squared Error: 28807.992"
            )

    # Test set.
    st.subheader(f"**Test Set**")
    st.write(f"R2 Score: 0.779  \n Mean Absolute Error:22401.275  \n"
            f"Mean Squared Error: 1529169051.688  \n Root Mean Squared Error: 39104.591"
            )

    # Pipeline steps


    # Other technical information
