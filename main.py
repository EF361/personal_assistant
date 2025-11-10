# main.py
import streamlit as st
from streamlit import Page
from pages.dashboard import dashboard_page
from pages.add_task import add_task_page
from pages.chatbot_page import chatbot_page

st.set_page_config(page_title="Personal Assistant", layout="wide")

# Fix: Make sidebar match dark theme
st.markdown("""
    <style>
        /* Sidebar background */
        section[data-testid="stSidebar"] {
            background-color: #1E1E1E !important;  /* dark gray */
            color: #FFFFFF !important;
        }

        /* Sidebar text and icons */
        section[data-testid="stSidebar"] * {
            color: #FFFFFF !important;
        }

        /* Adjust logo padding & alignment */
        [data-testid="stSidebar"] img {
            margin: 0 auto;
            display: block;
            border-radius: 12px;
        }

        /* Sidebar links hover effect */
        div[data-testid="stSidebarNav"] a:hover {
            background-color: #333333 !important;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar logo
st.logo("images/logo.png", size="large", icon_image="images/logo.png")

# Define pages
dashboard = st.Page(dashboard_page, title="Dashboard", icon="📋")
add_task = st.Page(add_task_page, title="Add Task", icon="➕")
chatbot = st.Page(chatbot_page, title="Chatbot", icon="💬")

pages = {
    "Task Dashboard": [dashboard, add_task],
    "Assistant": [chatbot],
}

# Navigation
pg = st.navigation(pages, position="sidebar")
pg.run()
