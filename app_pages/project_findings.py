import streamlit as st
import pandas as pd


def project_findings_body():
    # Function to render page.
    st.header("**Findings**")
    st.write(f"Our client has asked us to determine which features"
             f"in a house correlated most closely with the SalePrice."
             )
    st.write(f"To do this we performed both Pearson and "
             f"Spearman correlations. Both studies measure "
             f"The mathematical relationship between the"
             f"features. A coefficient of between 0.6 and "
             f"0.8 is considered strong. Higher than 0.8 is "
             f"considered very strong."
             )

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

    # checkbox to see all correlation coefficient
    if st.checkbox(f"Tick to view the correlation coefficient "
                   f"of all features "):
        combined_correlation_df = (
            pd.read_csv(
                f"outputs/datasets/correlation_study/"
                f"combined_correlation_df.csv"
                        ))
        combined_correlation_df.drop(columns=['Study'], axis=1, inplace=True)
        st.write(combined_correlation_df)

    # display image of price correlation study
    st.subheader(f"Strongly correlated features")
    st.write(f"We can see relative strengths of the correlation between "
             f"SalePrice and different features in the bar chart below.")
    st.write(f"The red line is a correlation coefficient of 1.2.")
    st.image(
        "docs/plots/correlation_between_salesprice_and_features.png"
        )

    st.subheader(f"Conclusion")
    st.write(f"We can conclude that OverallQual is very "
             f"strongly correlated with Saleprice, with "
             f"an average coefficient of 0.8 or higher "
             f"across the two methodologies."
             )
    st.write(f"We can further conclude that GrLivArea, KitchenQual, "
             f"GarageArea and TotalBsmtSF are strongly correlated "
             f"with SalePrice, with average coefficient of "
             f"0.6 or higher."
             )
