import streamlit as st
import requests

st.set_page_config(page_title="Random Quote Generator", page_icon="📝")

st.title("📝 Random Quote Generator")
st.write("Click the button below to fetch a random quote from ZenQuotes API!")

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()[0]
        return data["q"], data["a"]
    else:
        return "Could not fetch quote.", "Unknown"

# --- Display Quote ---
if st.button("✨ Generate Quote"):
    quote, author = get_quote()
    st.markdown(f"<div class='quote-box'>{quote}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='author'>— {author}</div>", unsafe_allow_html=True)
