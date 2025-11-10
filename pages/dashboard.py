import streamlit as st
from database import get_tasks, update_task_status, delete_task

def dashboard_page():
    st.header("📋 Today’s Tasks")
    st.caption("Focus on what matters today.")
    st.divider()

    tasks = get_tasks()
    if not tasks:
        st.info("No tasks yet.")
        return

    for task in tasks:
        task_id = task.get("id")
        title = task.get("title", "")
        category = task.get("category", "")
        due_date = task.get("due_date", "")
        status = task.get("status", "Pending")

        # Create a card container
        with st.container(border=True):
            st.markdown(f"### {title}")
            st.markdown(f"**Category:** {category}  |  **Due:** {due_date}")
            st.progress(1.0 if status == "Completed" else 0.5 if status == "In Progress" else 0.0)

            col1, col2 = st.columns([3, 1])
            with col1:
                status_options = ["Pending", "In Progress", "Completed"]
                idx = status_options.index(status) if status in status_options else 0
                new_status = st.selectbox(
                    "Status", status_options, index=idx, key=f"status_{task_id}"
                )
            with col2:
                update_clicked = st.button("✅ Update", key=f"update_{task_id}")
                delete_clicked = st.button("🗑️ Delete", key=f"delete_{task_id}")

            if update_clicked:
                update_task_status(task_id, new_status)
                st.success("Task updated!")
                st.rerun()

            if delete_clicked:
                delete_task(task_id)
                st.warning("Task deleted.")
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
