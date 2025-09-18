import streamlit as st
import random
from quotes import quotes

st.set_page_config(page_title="Random Quote Generator", page_icon="📝")

st.title("📝 Random Quote Generator")
st.write("Click the button below to see a random quote!")

if st.button("Generate Quote"):
    quote = random.choice(quotes)
    st.markdown(f"> *{quote['text']}*")
    st.markdown(f"— **{quote['author']}**")
