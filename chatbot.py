import requests
import streamlit as st

WEBHOOK_URL = "https://a1wnjhu0.rcsrv.net/webhook/3fb5c36f-c5c4-408f-9e8b-d971e8f5087f"

def chat_with_assistant(prompt, task_summary="", memory_context=""):
    """
    Forward all user messages to n8n webhook.
    The webhook will handle all logic (task creation, responses, etc.).
    """
    try:
        payload = {
            "prompt": prompt,
            "task_summary": task_summary,
            "context": memory_context,
            "sender": "Lexi Streamlit Frontend",
        }

        # Send to webhook
        response = requests.post(WEBHOOK_URL, json=payload, timeout=25)

        # Parse webhook reply
        if response.status_code == 200:
            data = response.json()
            return data.get("reply", "✅ Received response, but no message found.")
        else:
            return f"⚠️ Webhook error {response.status_code}: {response.text}"

    except requests.exceptions.RequestException as e:
        return f"❌ Failed to reach Lexi webhook: {e}"
