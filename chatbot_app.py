import streamlit as st
import openai

# ⚠️ Temporary hardcoded API key — replace with your actual key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("💬 Chatbot App")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if user_input := st.chat_input("Type your message..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant reply
    with st.chat_message("assistant"):
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages
            )
            bot_reply = response.choices[0].message.content
            st.markdown(bot_reply)
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            st.error(f"Error: {e}")
