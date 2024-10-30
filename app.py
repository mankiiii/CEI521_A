
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
    background-color: #242424; /* Set background color for the body */
}
[data-testid="stAppViewContainer"] {
    background-color: #242424; /* Set background color for the main container */
}
[data-testid="stHeader"] {
    background-color: #242424; /* Set background color for the header */
}

h2,h3 {
    color: #D4AF37; /* Main text color */
    font-size: 24px; /* Adjust size as needed */
    font-weight: bold;
    text-align: center;
    text-shadow:
        -1px -1px 0 #000, /* Top-left outline */
         1px -1px 0 #000, /* Top-right outline */
        -1px  1px 0 #000, /* Bottom-left outline */
         1px  1px 0 #000; /* Bottom-right outline */
}

h1{
color: #D4AF37; /* Main text color */
    font-weight: bold;
    text-align: center;
    text-shadow:
        -1px -1px 0 #000, /* Top-left outline */
         1px -1px 0 #000, /* Top-right outline */
        -1px  1px 0 #000, /* Bottom-left outline */
         1px  1px 0 #000; /* Bottom-right outline */
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
st.markdown("<p style='text-align: center;'>Ο τρόπος που αποφασίσαμε να δουλέψουμε ήταν ο Χαράλαμπος να κανει τα 3 widgets που θα είχαν σχέση με τα web services και ο Ματθαίος να κάνει τα AWS Lambda Functions γιατί ήδη είχε λογαριασμό στα AWS services. <br/>Στον διαμοιρασμό interactive/non-interactive APIs δεν υπήρχε κάποια συνεννόηση ποιος θα πάρει 2 και ποιος 1.<br/> Ο Χαράλαμπος ήταν αυτός που είχε κάνει set up το αρχικο Application structure και ο Ματθαίος πρόσθεσε στο Application τα υπόλοιπα widgets και έφτιαξε το structure. <br/> Επίσης για καλύτερη κατανόηση ο καθένας μας εξήγησε και ανάλυσε το πως δουλεύει ο κώδικας του άλλου για να έχουμε μια πιο ολοκληρωμένη γνώση του συστήματος.</p>",unsafe_allow_html=True)
    