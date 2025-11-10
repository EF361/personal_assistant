from supabase import create_client, Client
import time
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def get_tasks():
    retries = 3
    for attempt in range(retries):
        try:
            response = supabase.table("tasks").select("*").execute()
            return response.data
        except httpx.ReadError as e:
            print(f"⚠️ Attempt {attempt + 1} failed: {e}")
            time.sleep(1.5)  
    return []

def update_task_status(task_id: int, new_status: str):
    """
    Update the status of a task in the Supabase 'tasks' table.
    Example: new_status = 'completed' or 'in-progress'
    """
    try:
        response = supabase.table("tasks").update({"status": new_status}).eq("id", task_id).execute()
        return response.data
    except Exception as e:
        print(f"⚠️ Failed to update task status: {e}")
        return None

def add_task(title: str, category: str, due_date: str, status: str = "Pending"):
    """
    Insert a new task into the 'tasks' table.
    Called from [pages/add_task.py](pages/add_task.py).
    """
    try:
        payload = {
            "title": title,
            "category": category,
            "due_date": due_date,
            "status": status
        }
        response = supabase.table("tasks").insert(payload).execute()
        return response.data
    except Exception as e:
        print(f"⚠️ Failed to add task: {e}")
        return None

def delete_task(task_id: int):
    """Delete a task by ID from the Supabase 'tasks' table."""
    try:
        response = supabase.table("tasks").delete().eq("id", task_id).execute()
        return response.data
    except Exception as e:
        print(f"⚠️ Failed to delete task: {e}")
        return None

