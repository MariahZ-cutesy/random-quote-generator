import streamlit as st
import requests

st.set_page_config(page_title="Random Quote Generator", page_icon="📝")

st.title("📝 Random Quote Generator")
st.write("Click the button below to fetch a random quote from ZenQuotes API!")

# --- Theme Selection ---
theme = st.selectbox("Choose a theme:", ["Classic", "Dark", "Colorful"])

# --- Quote Fetching Function ---
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    
    # Debugging output
    st.write("Status Code:", response.status_code)
    st.write("Response Text:", response.text)
    
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
        # Apply theme styles
        if theme == "Classic":
            quote_style = "font-size:24px; font-style:italic; margin-top:20px;"
            author_style = "font-size:20px; margin-top:10px;"
        elif theme == "Dark":
            quote_style = "font-size:24px; font-style:italic; margin-top:20px; color:white; background-color:#333; padding:10px; border-radius:5px;"
            author_style = "font-size:20px; margin-top:10px; color:white;"
        elif theme == "Colorful":
            quote_style = "font-size:24px; font-style:italic; margin-top:20px; color:#2E8B57; background-color:#FFFACD; padding:10px; border-radius:5px;"
            author_style = "font-size:20px; margin-top:10px; color:#FF4500;"

        st.markdown(f"<div style='{quote_style}'>{quote}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='{author_style}'>— {author}</div>", unsafe_allow_html=True)

# Attribution
st.caption("Quotes provided by ZenQuotes API")
