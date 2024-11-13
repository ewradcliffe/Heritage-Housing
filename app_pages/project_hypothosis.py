import streamlit as st

def project_hypothosis_body():
    # Function to render page.
    st.header("**Project Hypothosis**")

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
    
    
    # Checkboxes supporting hypothesis 2.
    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and KitchenQual"
                   ):
        st.image("docs/plots/box-plot_of_saleprice_and_KitchenQual.png")

    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and OverallQual"
                   ):
        st.image("docs/plots/box-plot_of_saleprice_and_OverallQual.png")
    

    # Checkboxes supporting hypothesis 3.
    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and YearBuilt"
                   ):
        st.image("docs/plots/scatter_plot_of_saleprice_and_YearBuilt.png")
    
    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and YearRemodAd"
                   ):
        st.image("docs/plots/scatter_plot_of_saleprice_and_YearRemodAdd.png")
    