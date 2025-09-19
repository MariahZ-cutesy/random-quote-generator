import streamlit as st
import requests
import random

st.set_page_config(page_title="Random Quote Generator", page_icon="📝")

st.title("📝 Random Quote Generator")
st.write("Choose a genre and click the button to fetch a random quote!")

# --- Genre Options ---
genres = ["Motivational", "Wisdom", "Humor", "Life", "Love"]
selected_genre = st.selectbox("Choose a genre:", genres)

# --- Sample Quotes by Genre (as fallback or demo) ---
local_quotes = {
    "Motivational": [
        ("The only way to do great work is to love what you do.", "Steve Jobs"),
        ("Push yourself, because no one else is going to do it for you.", "Unknown")
    ],
    "Wisdom": [
        ("Knowing yourself is the beginning of all wisdom.", "Aristotle"),
        ("The only true wisdom is in knowing you know nothing.", "Socrates")
    ],
    "Humor": [
        ("I'm not arguing, I'm just explaining why I'm right.", "Unknown"),
        ("I used to think I was indecisive, but now I'm not so sure.", "Unknown")
    ],
    "Life": [
        ("Life is what happens when you're busy making other plans.", "John Lennon"),
        ("In the end, we only regret the chances we didn’t take.", "Lewis Carroll")
    ],
    "Love": [
        ("Love all, trust a few, do wrong to none.", "William Shakespeare"),
        ("To love and be loved is to feel the sun from both sides.", "David Viscott")
    ]
}

# --- API Fetch (fallback to local if needed) ---
def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()[0]
            return data["q"], data["a"]
    except:
        pass
    # fallback to local genre-based quote
    return random.choice(local_quotes[selected_genre])

# --- Display Quote ---
if st.button("✨ Generate Quote"):
    quote, author = get_quote()
    st.markdown(f"<div class='quote-box'>{quote}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='author'>— {author}</div>", unsafe_allow_html=True)
