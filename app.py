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
    with st.spinner("Fetching a quote..."):
        quote, author = get_quote()
    
    if quote == "Could not fetch quote.":
        st.error("Oops! Something went wrong while fetching the quote.")
    else:
        st.markdown(
            f"<div style='font-size:24px; font-style:italic; margin-top:20px;'>{quote}</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<div style='font-size:20px; margin-top:10px;'>— {author}</div>",
            unsafe_allow_html=True
        )

# Attribution
st.caption("Quotes provided by ZenQuotes API")
