"""
app.py
------
Streamlit UI for phishing URL detection.
"""
import streamlit as st
from phishing_detector import load_model, predict_url

st.title("Phishing URL Detection System")
st.write("Enter a URL to check if it's phishing or legitimate.")

url_input = st.text_input("URL:", "https://example.com")

if 'model' not in st.session_state:
    st.session_state['model'] = load_model()

if st.button("Check URL"):
    result = predict_url(url_input, st.session_state['model'])
    st.success(f"Result: {result}")
