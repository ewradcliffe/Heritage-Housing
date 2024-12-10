import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def project_findings_body():
    # load dataset.
    combined_correlation_df = (
    pd.read_csv(
        "outputs/datasets/correlation_study/combined_correlation_df.csv"
                ))
    
    # Function to render page.
    st.header("**Findings**")
    st.write(f"Our client has asked us to determine which features "
             f"in a house correlated most closely with the SalePrice."
             )
    st.write(f"To do this we performed both Pearson and "
             f"Spearman correlations. Both studies measure "
             f"the mathematical relationship between the"
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

    # display image of price correlation study
    st.subheader(f"Strongly correlated features")
    st.write(f"We can see relative strengths of the correlation between "
             f"SalePrice and different features in the bar chart below.")
    st.write(
        f"Adjust the input slider to see which features would be "
        f"included or excluded by changing the coefficiancy at which we "
        f"select features.")

    def show_correlation(correlation_df, threshold):
        """
        Create interactive Plotly bar chart to display correlations.
        """
        # Filter DataFrame based on the threshold
        features_exceed_threshold = correlation_df[correlation_df["Score"] >= threshold]
        features_below_threshold = correlation_df[correlation_df["Score"] < threshold]

        # Create the Plotly figure
        fig = go.Figure()

        # Features exceeding the threshold
        fig.add_trace(go.Bar(
            x=features_exceed_threshold['Feature'],
            y=features_exceed_threshold['Score'],
            name="Exceeding Threshold",
            marker_color='indigo',
            hoverinfo='x+y'
        ))

        # Features below the threshold
        fig.add_trace(go.Bar(
            x=features_below_threshold['Feature'],
            y=features_below_threshold['Score'],
            name="Below Threshold",
            marker_color='plum',
            hoverinfo='x+y',
        ))

        fig.update_layout(
            title="Correlation between SalesPrice and Features",
            xaxis_title="House Features",
            yaxis_title="Combined Pearson and Spearman Correlation Coefficient",
            barmode="group",
            hovermode="x unified",
            legend=dict(x=1.05, y=1),
            margin=dict(l=40, r=40, t=80, b=40),
            xaxis_tickangle=45,
            template="plotly_white"
        )

        return fig

    # Input slider to adjust threshold.
    select_threshold = st.slider(label="Select threshold",
                            min_value=0.0,
                            max_value=2.0,
                            value=1.2,
                            step=0.01)

    # Call function.
    st.plotly_chart(show_correlation(combined_correlation_df, select_threshold))


    # checkbox to see all correlation coefficient
    if st.checkbox(f"Tick to view the correlation coefficient "
                   f"of all features "):
        combined_correlation_df.drop(columns=['Study'], axis=1, inplace=True)
        st.write(combined_correlation_df)


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
