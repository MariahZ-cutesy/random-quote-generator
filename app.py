import streamlit as st
import requests
import random

st.set_page_config(page_title="Quote Quiz", page_icon="🧠")
st.title("🧠 Who Said It?")

# --- Get a random quote ---
def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()[0]
            return data["q"], data["a"]
    except:
        return "Could not fetch quote.", "Unknown"

# --- Generate fake authors ---
def generate_options(correct_author):
    fake_authors = ["Albert Einstein", "Maya Angelou", "Oscar Wilde", "Mark Twain", "Confucius"]
    options = random.sample([a for a in fake_authors if a != correct_author], 3)
    options.append(correct_author)
    random.shuffle(options)
    return options

# --- Quiz Mode ---
if "quote" not in st.session_state:
    st.session_state.quote, st.session_state.author = get_quote()
    st.session_state.options = generate_options(st.session_state.author)

st.markdown(f"**Quote:** _\"{st.session_state.quote}\"_")
user_answer = st.radio("Who said this?", st.session_state.options)

if st.button("Submit Answer"):
    if user_answer == st.session_state.author:
        st.success("🎉 Correct!")
    else:
        st.error(f"❌ Nope! The correct answer was **{st.session_state.author}**.")

if st.button("🔁 Try Another"):
    st.session_state.quote, st.session_state.author = get_quote()
    st.session_state.options = generate
