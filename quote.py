import requests
import streamlit as st

url = "https://p8t6irmk3b.execute-api.eu-north-1.amazonaws.com/motivationalQuote"
def get_quote():

    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('quote')  # Get image_url from JSON response
    return None 

def show_quote():
    st.markdown("<h2>Motivational Quote</h2>", unsafe_allow_html=True)
    todays_quote = get_quote()

    if todays_quote:
        st.markdown(f'<div style="text-align: center; color: #FFFFFF;">{todays_quote}</div>',unsafe_allow_html=True)
    else:
        st.error("Error: Unable to retrieve weather information.")
