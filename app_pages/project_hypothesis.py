import streamlit as st


def project_hypothesis_body():
    # Function to render page.
    # Conclusions based off studies in PriceCorrelationStudy

    st.header("**Project Hypothesis**")
    st.write(f"Prior to undertaking our study we formulated three "
             f"hypothesis:"
             )

    # Hypothesis 1
    st.subheader(f"Hypothesis 1")
    st.write(f"H0 (Null hypothesis): There is no correlation "
             f"between the size of the house and the price of a house."
             )
    st.write(f"H1 (Alternative hypothesis): There is positive correlation "
             f"between the size of the house and the price of a house."
             )

    # Checkboxes supporting hypothesis 1.
    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and GarageArea"
                   ):
        st.image(
            "docs/plots/scatter_plot_of_saleprice_and_GarageArea.png"
            )

    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and GrLivArea"
                   ):
        st.image("docs/plots/scatter_plot_of_saleprice_and_GrLivArea.png")

    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and TotalBsmtSF"
                   ):
        st.image("docs/plots/scatter_plot_of_saleprice_and_TotalBsmtSF.png")
    st.write(f"**Conclusion**")
    st.write(f"There is a positive relationship between SalePrice and "
             f"'GarageArea', 'GrLivArea', 'TotalBsmtSF'.")
    st.write(f"As these factors increase in size, so does the house price.")
    st.write(
        f"The null hypothesis  is disproven, the alternative hypothesis is "
        f"true."
            )
    st.write("---")

    # Hypothesis 2
    st.subheader(f"Hypothesis 2")
    st.write(
        f"H0 (Null hypothesis): There is no correlation "
        f"between the condition of the house and the price of a house."
            )
    st.write(
        f"H1 (Alternative hypothesis): There is positive correlation "
        f"between the condition of the house and the price of a house."
            )

    # Checkboxes supporting hypothesis 2.
    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and KitchenQual"
                   ):
        st.image("docs/plots/box-plot_of_saleprice_and_KitchenQual.png")

    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and OverallQual"
                   ):
        st.image("docs/plots/box-plot_of_saleprice_and_OverallQual.png")
    st.write(f"**Conclusion**")
    st.write(f"There is a positive relationship between SalePrice and "
             f"'KitchenQual' and 'OverallQual'.")
    st.write(f"As quality ratings increase, so does the house price.")
    st.write(
        f"The null hypothesis  is disproven, the alternative hypothesis "
        f" is true."
            )
    st.write("---")

    # Hypothesis 3
    st.subheader(f"Hypothesis 3")
    st.write(f"H0 (Null hypothesis): There is no correlation between age "
             f"of the house and when it was last reconditioned and the "
             f"price of a house."
             )
    st.write(f"H0 (Null hypothesis): There is positive correlation between age"
             f" of the house and when it was last reconditioned and the "
             f"price of a house."
             )

    # Checkboxes supporting hypothesis 3.
    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and YearBuilt"
                   ):
        st.image("docs/plots/scatter_plot_of_saleprice_and_YearBuilt.png")

    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and YearRemodAd"
                   ):
        st.image("docs/plots/scatter_plot_of_saleprice_and_YearRemodAdd.png")
    st.write(f"**Conclusion**")
    st.write(f"")
    st.write(
        f"There is a positive relationship between SalePrice and 'YearBuilt',"
        f" and  'YearRemodAdd'.")
    st.write(
        f"Newer houses and those recently remodelled have higher prices than"
        f"older houses."
        )
    st.write(
        f"The null hypothesis  is disproven, the alternative hypothesis is "
        f"true."
            )
