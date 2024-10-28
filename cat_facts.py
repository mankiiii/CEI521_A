import requests
import streamlit as st

url = "https://cat-fact.herokuapp.com/facts"

def getFacts():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error("Failed to retrieve the cat fact")
        return None

def show_cat_fact():
        st.markdown("<h1 style='text-align: center;'>Cat facts of the day</h1>",unsafe_allow_html=True)
        catFacts = getFacts()
        
        if catFacts:
            for fact in catFacts:
                st.write(fact["text"])

