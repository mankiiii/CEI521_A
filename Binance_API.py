import streamlit as st
import requests

# Binance API URL for 24hr price statistics
API_URL = "https://api.coincap.io/v2/assets"


famous_cryptos = [
    "bitcoin (BTC)",       
    "ethereum (ETH)",      
    "binance-coin (BNB)",  
    "solana (SOL)",        
    "usd-coin (USDC)",     
    "dogecoin (DOGE)"      
]


def get_crypto_data(crypto):
    crypto = crypto.split()[0].lower()
    response = requests.get(f"{API_URL}/{crypto}")
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


        data = crypto_data['data']
        st.write(f"**Crypto**: {data['name']} ({data['symbol']})")
        st.write(f"**Rank**: {float(data['rank'])}")
        st.write(f"**Price Change (24h)**: {float(data['changePercent24Hr'])}%")
        st.write(f"**Price Usd**: ${float(data['priceUsd'])}")  
        st.write(f"**Volume (24h)**: {float(data['volumeUsd24Hr'])}")
        st.write(f"**Market Cap**: ${float(data['marketCapUsd'])}")