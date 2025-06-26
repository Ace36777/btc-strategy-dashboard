
import streamlit as st
import requests

st.set_page_config(page_title="BTC Strategy Dashboard", layout="centered")
st.title("💷 Live GBP Prices - Core Portfolio")

token_ids = {
    "Bitcoin (BTC)": "bitcoin",
    "Tether (USDT)": "tether",
    "PAAL": "paal-ai",
    "RIO": "realio-network",
    "NAKA": "nakamoto-games",
    "ANYONE": "anyone-protocol",
    "DEVVE": "devve",
    "PROPS": "props-token"
}

def get_price(token_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies=gbp"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[token_id]["gbp"]
    return "Error"

for name, coingecko_id in token_ids.items():
    price = get_price(coingecko_id)
    st.write(f"**{name}**: £{price}")
