from composio import Composio
from langchain.tools import tool
import os

composio = Composio(api_key=os.getenv("COMPOSIO_API_KEY"))

@tool("get_latest_discord_message")
def get_latest_discord_message(channel_id: str):
    """Fetch the latest message from a Discord channel via Composio."""
    return composio.actions.discord.get_latest_message(channel_id)

@tool("send_discord_message")
def send_discord_message(channel_id: str, content: str):
    """Send a message to a Discord channel via Composio."""
    return composio.actions.discord.send_message(channel_id, content)

tools_list = [get_latest_discord_message, send_discord_message]
