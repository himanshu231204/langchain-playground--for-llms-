from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Streamlit page config
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Gemini Chatbot (LangChain + Streamlit)")
st.markdown("Chat with Google's **Gemini 2.5 Flash** model using LangChain")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful AI assistant.")]

# Display chat history
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Chat input box
user_input = st.chat_input("Type your message here...")

# When user sends a message
if user_input:
    # Add user message to history
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    result = model.invoke(st.session_state.chat_history)
    ai_reply = result.content

    # Add AI message to history
    st.session_state.chat_history.append(AIMessage(content=ai_reply))

    # Display AI message
    with st.chat_message("assistant"):
        st.markdown(ai_reply)

# Add a "Clear Chat" button
if st.button("🧹 Clear Chat"):
    st.session_state.chat_history = [SystemMessage(content="You are a helpful AI assistant.")]
    st.rerun()
