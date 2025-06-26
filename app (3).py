import streamlit as st
import requests

st.set_page_config(page_title="Live GBP Prices", layout="centered")
st.title("💷 Live GBP Prices - Core Portfolio")

token_ids = {
    "Bitcoin (BTC)": "bitcoin",
    "Tether (USDT)": "tether",
    "PAAL": "paal-ai",
    "RIO": "realio-network",
    "NAKA": "nakamoto-games",
    "ANYONE": "anyone-protocol",
    "DEVVE": "devve",
    "PROPS": "propbase"
}

def get_price(token_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies=gbp"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()[token_id]["gbp"]
    except:
        return "£Error"

for name, id_ in token_ids.items():
    price = get_price(id_)
    st.markdown(f"**{name}**: £{price}")
