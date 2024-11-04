import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.project_summary import page_summary_body
from app_pages.project_findings import project_findings_body
from app_pages.predict_sale_price import predict_sale_price_body
from app_pages.project_hypothosis import project_hypothosis_body
from app_pages.project_technical_information import project_technical_information_body


app = MultiPage(app_name= "House Price Predictions") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Findings", project_findings_body)
app.add_page("Predict Sale Price", predict_sale_price_body)
app.add_page("Project Hypothosis", project_hypothosis_body)
app.add_page("Technical Information", project_technical_information_body)


app.run() # Run the  app