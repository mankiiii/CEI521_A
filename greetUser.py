import requests
import streamlit as st

url = "https://pcgu02uikh.execute-api.eu-north-1.amazonaws.com/greetUser"

def greeting(nameOfUser):
    response = requests.get(f"{url}?name={nameOfUser}")
    if response.status_code == 200:
        return response.json().get('message')  # Get image_url from JSON response
    return None 

def greetUser():
    st.markdown("<h2 style='text-align: center;'>Lambda function Greeting</h2>",unsafe_allow_html=True)
    name = st.text_input("Enter your name")

    if name:
        try:
            response = greeting(name)
            if response:
                st.success(response)
        except Exception as e:
            st.error("An error occurred: " + str(e))