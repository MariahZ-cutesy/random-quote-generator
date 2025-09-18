import streamlit as st
import requests
import random

# --- Page Config ---
st.set_page_config(page_title="ZenQuotes Generator", page_icon="🧘", layout="centered")

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
        }
        .author {
            text-align: right;
            font-weight: bold;
            margin-top: 10px;
            color: #555;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("🧘 Random Zen Quote Generator")
st.subheader("Get inspired by wisdom from ZenQuotes API")

# --- Fetch Quote ---
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return quote, author
    else:
        return "Could not fetch quote at the moment.", "ZenQuotes API"

# --- Display Quote ---
if st.button("✨ Generate Quote"):
    quote, author = get_quote()
    st.markdown(f"<div class='quote-box'>{quote}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='author'>— {author}</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.caption("Powered by [ZenQuotes API](https://zenquotes.io/) • Made with ❤️ using Streamlit")
