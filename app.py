import streamlit as st

from chat_function import chat_bot_logic

st.title('🎙️🤖Chatbot for ML🤖🎙️')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt}) 
    # get the string back from your bot
    response = chat_bot_logic(prompt)

    # display it in the chat window
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add user message to chat history
    st.session_state.messages.append({"role": "assistant","content": response})
   