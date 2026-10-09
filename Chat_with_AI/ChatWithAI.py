import streamlit as st

st.write("AI chatbot")

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

    ai_output = "You ask: " + user_input
    st.chat_message("assistant").write(ai_output)
    assistant_message_to_store = {"role": "assistant", "content": ai_output}
    st.session_state["message_list"].append(assistant_message_to_store)

print(st.session_state["message_list"])
