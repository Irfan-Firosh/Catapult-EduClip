import streamlit as st
import google.generativeai as genai
import keys

st.title("Question Bot")
client = 'AIzaSyAA6BCdze835zhzzzQaZ4gygHfZvK4OpDI'  # Make sure keys.GOOGLE_API_KEY is correctly defined

genai.configure(api_key=client)
model = genai.GenerativeModel('gemini-pro')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter any questions you have"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Generating response..."):
        stream = model.generate_content(prompt)
        response = stream.text
        st.session_state.messages.append({"role": "assistant", "content": stream.text})

        with st.chat_message("assistant"):
            st.markdown(response)
