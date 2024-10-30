import requests
import streamlit as st

url = "https://f5q5mlvfj2.execute-api.eu-north-1.amazonaws.com/http-cat-image"

def getFacts():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error("Failed to retrieve the cat fact")
        return None

def show_cat_fact():
        st.markdown("<h2 style='text-align: center;'>Cat facts of the day</h2>",unsafe_allow_html=True)
        catFacts = getFacts()
        if catFacts:
            st.markdown(f'<div style="text-align: center; color: #FFFFFF;">{catFacts['image_url']}</div>',unsafe_allow_html=True)

