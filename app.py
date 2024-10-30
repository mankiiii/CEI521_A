
from Binance_API import choose_famous_crypto
from MCU_API import st, show_next_mcu_film
from Http_cat_code import show_cat_http_details
from greetUser import greetUser
from cat_facts import show_cat_fact
from quote import show_quote

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>EXERCISE CEI 521</h1>",unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    choose_famous_crypto()

with col2:
    show_next_mcu_film()


with col3:
    show_cat_http_details()

col4, col5, col6 = st.columns(3)

with col4:
    greetUser()  # Replace with another function if desired

with col5:
     show_cat_fact()  # Replace with another function if desired

with col6:
     show_quote()  # Replace with another function if desired


st.markdown("<h3 style='text-align: center;'>Report</h3>",unsafe_allow_html=True)
st.markdown("<p></p>",unsafe_allow_html=True)
    