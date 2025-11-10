import streamlit as st
from database import add_task
import datetime
import time

def add_task_page():
    st.header("➕ Add a New Task")
    st.caption("Organize your tasks effectively.")
    st.divider()
    container = st.container(border=True)
    with container:
        title = st.text_input("Task Title")
        category = st.selectbox("Category", ["School", "Project", "Personal"])
        due_date = st.date_input("Due Date", datetime.date.today(),min_value="today")

        if st.button("Add Task"):
            if not title:
                st.error("Title cannot be empty.")
            else:
                add_task(title, category, str(due_date))
                st.success("Task added!")
                time.sleep(0.5)
                st.rerun()
