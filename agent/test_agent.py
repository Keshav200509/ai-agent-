# # test_agent.py (new file for testing)
# from agent.core import run_agent_task

# query = """
# Fetch the most recent message from my Discord channel with ID 123456789012345678
# and send it as an email to my address: your_email@gmail.com
# """

# result = run_agent_task(query)
# print("Result:", result)


# agent/test_agent.py
from dotenv import load_dotenv
load_dotenv()

# --- Keep the rest of your imports below ---
from agent.core import run_agent_task
import os
import pytest

def test_discord_to_gmail_drive_workflow():
    """
    Full integration test:
    1. Fetch latest message from a test Discord channel.
    2. Send the message as an email via Gmail.
    3. Upload that message as a file to Google Drive.
    """
    discord_channel_id = os.getenv("TEST_DISCORD_CHANNEL_ID", "dummy_channel")
    email_to = os.getenv("GMAIL_ADDRESS", "your_email@gmail.com")
    drive_folder = os.getenv("GOOGLE_DRIVE_FOLDER_ID", "root")

    # Step 1: Fetch Discord message
    message = run_agent_task(f"Get the latest message from Discord channel {discord_channel_id}")
    assert message is not None and isinstance(message, str)

    # Step 2: Send message via Gmail
    email_res = run_agent_task(
        f"Send the following as an email to {email_to}: {message}"
    )
    assert "error" not in str(email_res).lower()

    # Step 3: Upload message as file to Google Drive
    upload_res = run_agent_task(
        f"Upload the following text as a file to Google Drive folder {drive_folder}: {message}"
    )
    assert "error" not in str(upload_res).lower()
    print("Integration workflow successful.")

# Allow CLI running
if __name__ == "__main__":
    print("\n--- [Main] Running full system workflow test ---")
    test_discord_to_gmail_drive_workflow()