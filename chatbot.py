import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAR3AHYGDIqVq32XeA_bbDomo69tCIyxQQ")
model = genai.GenerativeModel("gemini-1.5-pro")

st.title("My ChatBot")
prompt = st.text_input("Enter your prompt")
if st.button("Ask me"):
    response = model.generate_content(prompt,stream=True)
    for i in response:
        st.markdown(i.text)