import streamlit as st


def page_summary_body():
    # Renders summary page.
    st.header("**Project Summary**")

    st.write(
        f"Heritage Housing is a project aimed at predicting sales prices for "
        f"houses our client has inherited four houses in Ames, Iowa. They "
        f"have asked us to conduct a study to maximise the sale price of"
        f"these houses."
    )

    # Business Requirements
    st.subheader(f"**Business Requirements**")
    st.write(f"The project has 2 business requirements:")
    st.write(f"1: The client is interested in discovering how the house "
             f"attributes correlate with the sale price. Therefore, "
             f"the client expects data visualisations of the correlated "
             f"variables against the sale price to show that.")
    st.write(f"2: The client is interested in predicting the house sale price "
             f"from her four inherited houses and any other house in Ames, "
             f"Iowa.")

    # Dataset
    st.subheader(f"**Dataset**")
    st.write(
        f"The client has provided a publicly sourced data set listing features"
        f" and sale prices. The data set lists 23 features and the target"
        f"variable (SalePrice) and 1460 observations. They have also provided"
        f"a data set detailing the same 23 features for the houses they have  "
        f"inherited. The data sets have been uploaded to kaggle and dowloaded "
        f"to this programme for study."
    )

    st.write(f"The data set can be found on "
             f"[kaggle](\
        https://www.kaggle.com/datasets/codeinstitute/housing-prices-data).")

    # Project
    st.subheader(f"**Project Terms & Jargon**")
    st.write(f"**Features**: The individual characteristics of a house, such "
             f"as number of bedrooms.")
    st.write(f"**Target**: The characteristic we are interested in predicting."
             f" In this case Sale Price.")
    st.write(f"**Saleprice**: The price at which a house has been "
             f"sold in USD.")
    st.write(f"**Inherited house**: A house the client has inherited and "
             f"wishes to sell.")

    # Link to README file. Allows users to have full information.
    st.write(
        f"* For additional information, please visit the "
        f"[Project README file](\
        https://github.com/ewradcliffe/Heritage-Housing/blob/main/README.md)."
        )
