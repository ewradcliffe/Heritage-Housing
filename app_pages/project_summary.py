import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/ewradcliffe/Heritage-Housing/blob/main/README.md).")
    

    # Business Requirements
    st.success(
        f"The project has 2 business requirements:\n"
        f"1 - The client is interested in discovering how the house attributes correlate with the sale price."
        f"Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.\n"
        f"2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa."
        )

        