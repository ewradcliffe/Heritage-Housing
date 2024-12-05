import streamlit as st


def project_technical_information_body():
    # Renders technical information page.

    st.header("**Technical Information**")
    st.write(
        f"This page shows information which may be useful for data analysts "
        f"and developers."
    )
    # Model Performance criteria. Please note that although we have trained two
    # models we are only providing data for the deployed model. The information
    # is hard copiedfrom 07 - ModellingMostImportantFeatures
    st.subheader(f"Model Performance")
    st.write(f"**Train Set**")
    st.write(
        f"Please see below for details of the performance of train, validation"
        f" and test data sets. Please note that our model meets the agreed "
        f"performance criteria of R2 of at least 0.75."
        )

    # Train set
    st.write(f"**Train Set**")
    st.write(
        f"R2 Score: 0.841  \n Mean Absolute Error: 20725.343  \n"
        f"Mean Squared Error: 1003982222.455  \n Root Mean Squared Error: "
        f"31454.246"
            )

    # Validation set.
    st.write(f"**Validation Set**")
    st.write(
        f"R2 Score: 0.841  \n Mean Absolute Error: 21274.337  \n"
        f"Mean Squared Error: 870859719.18  \n Root Mean Squared Error: "
        f"29510.332"
            )

    # Test set.
    st.write(f"**Test Set**")
    st.write(
        f"R2 Score: 0.771  \n Mean Absolute Error:23296.594  \n"
        f"Mean Squared Error: 1584495831.166  \n Root Mean Squared Error: "
        f"39805.726"
        )
    st.write(
        "We can see all three data sets exceed out target metric of R2 "
        "of at least 0.75."
        )

    # Pipeline steps. Based on the pipeline in 07 -
    # ModellingMostImportantFeatures
    st.subheader(f"**Pipeline steps**")
    st.write(f"The steps below were taken to prepare the data.")

    st.write(
        f"In the data set provided EnclosedPorch and WoodDeckSF had 90.7% and "
        f"89.4% of their respective data missing. These features were removed "
        f"before any other steps were taken as there was too much missing "
        f"data to reliably impute and it was not possible to impute the "
        f"missing data from another category."
        )

    st.write(
        f"The features identified as strongly or very strongly correlated with"
        f" SalePrice (GarageArea, GrLivArea, KitchenQual, OverallQual, "
        f"TotalBsmtSF) were extracted from the data set. Other features were "
        f"dropped."
        )
    st.write(f"The data was split into train, validate and test sets.")
    st.write(f"OrdinalCategoricalEncoder was applied to KitchenQual.")
    st.write(
        f"PowerTransformer was applied to GarageArea, GrLivArea,  OverallQual,"
        f" TotalBsmtSF."
        )
    st.write(
        f"The data was then Windsorised to cap outliers based on the Inter-"
        f"Quartile Range (IQR)."
        )
    st.write(f"The data was scaled with StandardScaler")

    # The Model
    st.subheader(f"The model")
    st.write(f"The model itself consists of a neural network.")
    st.write(f"The input layer is equal to the number of features (i.e. 5).")
    st.write(
        f"This is followed by four hidden layers of 512 nodes, each "
        f"alternating with a droput layer set to 0.25."
        )
    st.write(f"Activation functions are all rectified linear unit (ReLU).")
    st.write(
        f"As we created a linear regression model, the output layer consisted "
        f"of one node, The loss function was Mean Squared Error (MSE). The "
        f"optimizer was Adam."
        )
