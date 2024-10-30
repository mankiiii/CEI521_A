
from Binance_API import choose_famous_crypto
from MCU_API import st, show_next_mcu_film
from Http_cat_code import show_cat_http_details
from greetUser import greetUser
from cat_facts import show_cat_fact
from quote import show_quote

st.set_page_config(layout="wide")

page_bg_color = '''
<style>
body {
    background-color: #242424;
}
</style>
'''
st.markdown(page_bg_color, unsafe_allow_html=True)

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
st.markdown("<p style='text-align: center;'>Ο τρόπος που αποφασίσαμε να δουλέψουμε ήταν ο Χαράλαμπος να κανει τα 3 widgets που θα είχαν σχέση με τα web services και ο Ματθαίος να κάνει τα AWS Lambda Functions γιατί ήδη είχε λογαριασμό στα AWS services. <br/>Στον διαμοιρασμό interactive/non-interactive APIs δεν υπήρχε κάποια συνεννόηση ποιος θα πάρει 2 και ποιος 1. Ο Χαράλαμπος ήταν αυτός που είχε κάνει set up το αρχικο Application structure και ο Ματθαίος πρόσθεσε στο Application τα υπόλοιπα widgets και έφτιαξε το structure.</p>",unsafe_allow_html=True)
    