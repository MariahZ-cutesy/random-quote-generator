import streamlit as st
import requests
import time
from streamlit_lottie import st_lottie

# --- Page Config ---
st.set_page_config(page_title="ZenQuotes Generator", page_icon="🧘", layout="centered")

# --- Load Lottie Animation ---
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return None

lottie_meditation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")

# --- Custom CSS ---
st.markdown("""
    <style>
        .quote-box {
            background-color: #f0f8ff;
            padding: 20px;
            border-radius: 10px;
            font-size: 1.3em;
            font-style: italic;
            color: #333;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            animation: fadeIn 2s ease-in;
        }
        .author {
            text-align: right;
            font-weight: bold;
            margin-top: 10px;
            color: #555;
        }
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("🧘 Random Zen Quote Generator")
st.subheader("Get inspired by wisdom from ZenQuotes API")

# --- Lottie Animation ---
st_lottie(lottie_meditation, height=200, key="meditate")

# --- Fetch Quote ---
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return quote, author
    else:
       
