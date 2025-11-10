import streamlit as st
from database import get_tasks
from chatbot import chat_with_assistant

def chatbot_page():
    st.header("💬 Chat with Lexi")
    st.caption("Your personal assistant powered by n8n ✨")

    st.markdown("""
    <style>
    [data-testid="stChatMessage"] {
        border-radius: 12px;
        padding: 8px 12px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.divider()

    # Summarize tasks (optional context)
    tasks = get_tasks() or []
    task_summary = "\n".join([
        f"- {t.get('title','')} ({t.get('category','')}) [{t.get('status','')}] - Due: {t.get('due_date','')}"
        for t in tasks
    ])

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"], avatar="🦖" if msg["role"] == "user" else "🤖"):
            st.markdown(msg["content"])

    # Input box
    if prompt := st.chat_input("Ask Lexi anything..."):
        # Save and immediately display the user's message so it appears above the assistant reply
        user_msg = {"role": "user", "content": prompt}
        st.session_state.messages.append(user_msg)
        with st.chat_message("user", avatar="🦖"):
            st.markdown(prompt)

        # Generate assistant reply and display it
        with st.chat_message("assistant", avatar="🤖"):
            reply = chat_with_assistant(prompt, task_summary)
            st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})