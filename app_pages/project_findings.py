import streamlit as st
import pandas as pd


def project_findings_body():
    # Function to render page.
    st.header("**Findings**")



    # show df of strongly correlated features
    st.subheader(f"Combined Pearson and Spearman correlations")
    st.write(f"We combined the Spearman and Pearson studies and "
             f"extracted the features which were strongly or very "
             f"strongly correlated (i.e. with a combined correlation "
             f"coefficient of 1.2 or higher).")
    categories_to_study_df = (
        pd.read_csv(
            f"outputs/datasets/correlation_study/categories_to_study_df.csv"
                    ))
    categories_to_study_df.drop(columns=['Study'], axis=1, inplace=True)
    st.write(categories_to_study_df)

    # checkbox to see all correlation coefficiancies
    if st.checkbox(f"Tick to view the correlation coefficiancies of all features "):
        combined_correlation_df = (
            pd.read_csv(
                f"outputs/datasets/correlation_study/combined_correlation_df.csv"
                        ))
        combined_correlation_df.drop(columns=['Study'], axis=1, inplace=True)
        st.write(combined_correlation_df)
    
    # display image of price correlation study
    st.subheader(f"Strongly correlated features")
    st.write(f"We can see relative strengths of the correlation between "
             f"SalePrice and different features in the bar chart below.")
    st.write(f"The red line is a correlation coefficiancy of 1.2.")
    st.image(
        "docs/plots/correlation_between_salesprice_and_features.png"
        )

