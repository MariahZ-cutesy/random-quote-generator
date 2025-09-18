import streamlit as st
import requests
import time

st.set_page_config(page_title="ZenQuotes Generator", page_icon="🧘", layout="centered")

st.title("🧘 Random Zen Quote Generator")
st.subheader("Get inspired by wisdom from ZenQuotes API")

# Add GIF animation
st.markdown("""
    <div style="text-align: center;">
        https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif
    </div>
""", unsafe_allow_html=True)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()
        return data[0]['q'], data[0]['a']
    else:
        return "Could not fetch quote.", "ZenQuotes API"

if st.button("✨ Generate Quote"):
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("⏳ Loading wisdom... 🧠")
        time.sleep(1.5)
        quote, author = get_quote()
        placeholder.empty()
        st.markdown(f"> *{quote}*")
        st.markdown(f"**— {author}**")

st.markdown("---")
st.caption("Powered by ZenQuotes • Made with ❤️ using Streamlit")
