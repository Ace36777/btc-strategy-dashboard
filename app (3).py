
import streamlit as st
import requests

st.set_page_config(page_title="Live GBP Prices", layout="centered")
st.markdown("<h1>💷 Live GBP Prices - Core Portfolio</h1>", unsafe_allow_html=True)

# Define the token list with correct CoinGecko IDs
tokens = {
    "Bitcoin (BTC)": "bitcoin",
    "Tether (USDT)": "tether",
    "PAAL": "paal",
    "RIO": "realio-network",
    "NAKA": "nakamoto-games",
    "ANYONE": "anyone-protocol",
    "DEVVE": "devve",
    "PROPS": "props"
}

def fetch_price(token_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies=gbp"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data[token_id]["gbp"]
    except Exception as e:
        return f"Error"

for name, token_id in tokens.items():
    price = fetch_price(token_id)
    st.markdown(f"**{name}:** £{price}")
