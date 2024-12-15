import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


def scatter_plot(df, x_axis):
    """
    Function to generate a scatter plot with regression line.
    """
    x = df[x_axis]
    y = df['SalePrice']
    slope, intercept = np.polyfit(x, y, 1)
    df["Regression"] = slope * x + intercept

    # Scatter plot
    fig = px.scatter(
        df, x=x_axis,
        y='SalePrice',
        title=f"Scatter Plot of SalePrice and {x_axis}")

    # Regression line.
    fig.add_scatter(
        x=df[x_axis],
        y=df["Regression"],
        mode='lines',
        line=dict(color='red'),
        showlegend=False
    )

    return fig


def box_plot(df, x_axis, x_order):
    """
    Function to render a box plot.
    """
    # Create the box plot
    fig = px.box(
        df,
        x=x_axis,
        y='SalePrice',
        title=f"Box Plot of 'SalePrice' and {x_axis}",
        category_orders={x_axis: x_order}
    )

    return fig


def project_hypothesis_body():
    # Function to render page.
    # Conclusions based off studies in PriceCorrelationStudy

    # Load data set
    house_prices_clean_df = (
        pd.read_csv(
         "outputs/datasets/clean_data/House_prices_records_clean.csv"
                ))

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
                   f" SalePrice and GarageArea"
                   ):

        st.plotly_chart(scatter_plot(house_prices_clean_df, 'GarageArea'))

    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and GrLivArea"
                   ):
        st.plotly_chart(scatter_plot(house_prices_clean_df, 'GrLivArea'))

    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and TotalBsmtSF"
                   ):
        st.plotly_chart(scatter_plot(house_prices_clean_df, 'TotalBsmtSF'))

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

        # Note that we need to manually order the categories as we are not
        # able to apply an ordinal encoder.
        kitchen_quality_categories = ['Fa', 'TA', 'Gd', 'Ex']
        st.plotly_chart(box_plot(
            house_prices_clean_df, 'KitchenQual', kitchen_quality_categories
            ))

    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and OverallQual"
                   ):
        # Note that we need to manually order the categories as we are not
        # able to apply an ordinal encoder.
        overall_quality_categories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        st.plotly_chart(box_plot(
            house_prices_clean_df, 'OverallQual', overall_quality_categories
            ))

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
        st.plotly_chart(scatter_plot(house_prices_clean_df, 'YearBuilt'))

    if st.checkbox(f"click here to see the relationship between"
                   f"SalePrice and YearRemodAdd"
                   ):
        st.plotly_chart(scatter_plot(house_prices_clean_df, 'YearRemodAdd'))

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
