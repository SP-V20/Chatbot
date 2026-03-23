import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from inject_clarity import inject_clarity

# Inject Clarity script
inject_clarity()

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")

# System message - constant instruction to LLM
system_msg = {
    "role": "system",
    "content": "You are a helpful assistant who helps to answer user queries."
}

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

if "chat_active" not in st.session_state:
    st.session_state.chat_active = True


# User input
user_input = None
if st.session_state.chat_active:
    user_input = st.chat_input("Type your message...")

if user_input: 
    # Check for exit command
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.session_state.chat_active = False
        
        exit_message = "👋 Chat ended. Refresh to chat again."

        with st.chat_message("assistant"):
            st.markdown(exit_message)

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": exit_message
        })

        st.rerun()
        
    # Show and store user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Build prompt — system msg + full history (so LLM remembers)
    MAX_HISTORY = 50
    prompt = [system_msg] + st.session_state.chat_history[-MAX_HISTORY:]  # Limit history to last 50 messages for context

    # Call API correctly
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0,
            messages=prompt       
        )
    except Exception as e:
        st.error(f"Error occurred: {e}")

    reply = response.choices[0].message.content

    # Show and store assistant message
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.chat_history.append({"role": "assistant", "content": reply})
