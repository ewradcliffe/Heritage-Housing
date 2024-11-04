import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.project_summary import page_summary_body


app = MultiPage(app_name= "House Price predictions") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)


app.run() # Run the  app