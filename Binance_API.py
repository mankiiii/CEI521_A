import streamlit as st
import requests

# Binance API URL for 24hr price statistics
API_URL = "https://api.binance.com/api/v3/ticker/24hr"


famous_cryptos = [
    "BTCUSDT (Bitcoin)",  
    "ETHUSDT (Ethereum)",  
    "BNBUSDT (Binance Coin)",  
    "XRPUSDT (Ripple)",  
    "ADAUSDT (Cardano)", 
    "DOGEUSDT (Dogecoin)", 
]


def get_crypto_data(crypto):
    crypto = crypto.split()[0] 
    response = requests.get(f"{API_URL}?symbol={crypto}")
    return response.json()


def choose_famous_crypto():
    st.markdown("<h1 style='text-align: center;'>Cryptocurrencies Info</h1>", unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
    selected_crypto = st.selectbox("**Select a cryptocurrency**", [""] + famous_cryptos, index=0)
   
    if selected_crypto != "":
        crypto_data = get_crypto_data(selected_crypto)

        if "error" in crypto_data:
            st.error(crypto_data["error"])
            return

        st.write(f"**Crypto**: {selected_crypto}")
        st.write(f"**Last Price**: {crypto_data['lastPrice']}")
        st.write(f"**Price Change (24h)**: {crypto_data['priceChangePercent']}%")
        st.write(f"**High Price (24h)**: {crypto_data['highPrice']}")
        st.write(f"**Low Price (24h)**: {crypto_data['lowPrice']}")
        st.write(f"**Volume**: {crypto_data['volume']}")
        st.write(f"**Quote Volume**: {crypto_data['quoteVolume']}")