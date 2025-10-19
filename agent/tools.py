# from composio import Composio
# from dotenv import load_dotenv
# import os

# load_dotenv()

# composio = Composio(api_key=os.getenv("COMPOSIO_API_KEY"))

# def list_tools():
#     return composio.list_tools()

# def call_tool(tool_name: str, params: dict):
#     return composio.run_tool(tool_name, params)

# if __name__ == "__main__":
#     print(list_tools())



# import os
# from composio import Composio

# # Initialize the Composio client
# composio = Composio(api_key=os.getenv("COMPOSIO_API_KEY"))

# def list_tools():
#     # ✅ New API syntax for listing available tools
#     tools = composio.tools.list_tools()
#     return [tool.name for tool in tools]

# def call_tool(tool_name: str, params: dict):
#     # ✅ New API syntax for running tools
#     return composio.tools.run_tool(tool_name, params)

# if __name__ == "__main__":
#     print(list_tools())

# agent/tools.py

# from langchain.tools import tool
# from composio import Composio
# import os

# composio = Composio(api_key=os.getenv("COMPOSIO_API_KEY"))

# @tool("fetch_youtube_transcript")
# def fetch_youtube_transcript(video_url: str):
#     """Fetch transcript from a YouTube video."""
#     return composio.actions.youtube.get_transcript(video_url)

# @tool("create_google_doc")
# def create_google_doc(title: str, content: str):
#     """Create a Google doc with summary content."""
#     return composio.actions.google_docs.create_doc(title, content)

# @tool("upload_to_drive")
# def upload_to_drive(filename: str, file_content: str):
#     """Upload a file to Google Drive."""
#     return composio.actions.google_drive.upload(filename, file_content)

# @tool("send_gmail")
# def send_gmail(subject: str, body: str, recipient: str):
#     """Send an email through Gmail."""
#     return composio.actions.gmail.send_email(subject, body, recipient)

# tools_list = [fetch_youtube_transcript, create_google_doc, upload_to_drive, send_gmail]


# agent/tools.py
from composio import Composio
from langchain.tools import tool
import os

composio = Composio(api_key=os.getenv("COMPOSIO_API_KEY"))

@tool("read_discord_message")
def read_discord_message(channel_id: str):
    """Fetch the latest message from a Discord channel."""
    return composio.actions.discord.get_latest_message(channel_id)

@tool("send_gmail")
def send_gmail(subject: str, body: str, recipient: str):
    """Send a test email using Gmail."""
    return composio.actions.gmail.send_email(subject, body, recipient)

tools_list = [read_discord_message, send_gmail]
