import streamlit as st
import requests


API_URL = "https://www.whenisthenextmcufilm.com/api"

def get_next_mcu_production():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}

def show_next_mcu_film():
    
    


    st.markdown("<h2 style='text-align: center;'>Next MCU Production</h2>", unsafe_allow_html=True)

    if 'button_pressed' not in st.session_state:
        st.session_state.button_pressed = False

   

    col1, col2, col3 = st.columns([1, 2, 1])

    
    with col2:
        st.markdown("<div style='margin-top: 42px;'></div>", unsafe_allow_html=True)
        if st.button("Fetch Next MCU Production", key="fetch_mcu_button"):
            st.session_state.button_pressed = not st.session_state.button_pressed 
            if st.session_state.button_pressed:
                next_mcu = get_next_mcu_production()
                st.session_state.next_mcu = next_mcu
 
    
    if st.session_state.button_pressed:
        if st.session_state.next_mcu and "error" not in st.session_state.next_mcu:
        
            next_mcu = get_next_mcu_production()

            if "error" not in next_mcu:
                st.subheader(f"Title of the movie: {next_mcu['title']}")
                st.write(f"**Release Date**: {next_mcu['release_date']}")
                st.write(f"**Days Until Release**: {next_mcu['days_until']}")
                st.write(f"**Type**: {next_mcu['type']}")
                st.write(f"**Overview**: {next_mcu['overview']}")
                
    
                image_url = next_mcu['poster_url'] 
                st.markdown(f'<div style="text-align: center;"><img src="{image_url}" width="300" /></div>', unsafe_allow_html=True)
                st.markdown(f'<div style="text-align: center;">{next_mcu['title']}</div>', unsafe_allow_html=True)
            else:
                st.error("Error: Could not fetch MCU production details.")
