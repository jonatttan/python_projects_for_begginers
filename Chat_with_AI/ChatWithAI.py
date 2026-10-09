import streamlit as st

st.write("AI chatbot")

user_input = st.chat_input("Write your message...")
if user_input:
    st.chat_message("user").write(user_input)

    ai_output = "You ask: " + user_input
    st.chat_message("assistant").write(ai_output)