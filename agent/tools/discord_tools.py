import logging
import os

from composio import Composio
from langchain.tools import tool

logger = logging.getLogger(__name__)

_api_key = os.getenv("COMPOSIO_API_KEY")
if not _api_key:
    logger.warning("COMPOSIO_API_KEY is not set; Discord tools will fail at runtime")
composio = Composio(api_key=_api_key)


@tool("get_latest_discord_message")
def get_latest_discord_message(channel_id: str):
    """Fetch the latest message from a Discord channel via Composio."""
    try:
        return composio.actions.discord.get_latest_message(channel_id)
    except Exception as exc:
        logger.exception("Failed to fetch latest Discord message")
        return {"error": f"Discord message fetch failed: {exc}"}


@tool("send_discord_message")
def send_discord_message(channel_id: str, content: str):
    """Send a message to a Discord channel via Composio."""
    try:
        return composio.actions.discord.send_message(channel_id, content)
    except Exception as exc:
        logger.exception("Failed to send Discord message")
        return {"error": f"Discord send failed: {exc}"}


tools_list = [get_latest_discord_message, send_discord_message]
