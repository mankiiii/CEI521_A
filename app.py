
from Binance_API import choose_famous_crypto
from MCU_API import st, show_next_mcu_film
from Http_cat_code import show_cat_http_details

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)

with col1:
    choose_famous_crypto()

with col2:
    show_next_mcu_film()


with col3:
    show_cat_http_details()