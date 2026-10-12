import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("AI_API_KEY")

ia_model = OpenAI(
    api_key = api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
)

st.write("## AI chatbot")

if not "message_list" in st.session_state:
    st.session_state["message_list"] = []

user_input = st.chat_input("Write your message...")

#Retrieving and displaying
for message in st.session_state["message_list"]:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).write(content)


#Processing and storage
if user_input:
    st.chat_message("user").write(user_input)
    user_message_to_store = {"role": "user", "content": user_input}
    st.session_state["message_list"].append(user_message_to_store)

    ai_answer = ia_model.chat.completions.create(
        messages = st.session_state["message_list"],
        model="gemini-flash-lite-latest"
    )
    ai_answer_to_show = ai_answer.choices[0].message.content

    st.chat_message("assistant").write(ai_answer_to_show)
    assistant_message_to_store = {"role": "assistant", "content": ai_answer_to_show}
    st.session_state["message_list"].append(assistant_message_to_store)