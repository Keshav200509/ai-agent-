import logging
import os

from composio import Composio
from langchain.tools import tool

logger = logging.getLogger(__name__)

_api_key = os.getenv("COMPOSIO_API_KEY")
if not _api_key:
    logger.warning("COMPOSIO_API_KEY is not set; Gmail tools will fail at runtime")
composio = Composio(api_key=_api_key)


@tool("send_gmail")
def send_gmail(subject: str, body: str, recipient: str):
    """Send an email using Gmail via Composio."""
    try:
        return composio.actions.gmail.send_email(subject, body, recipient)
    except Exception as exc:
        logger.exception("Failed to send Gmail")
        return {"error": f"Gmail send failed: {exc}"}


@tool("read_gmail")
def read_gmail(query: str = ""):
    """Read emails from Gmail using Composio. Query can be a search string."""
    try:
        return composio.actions.gmail.read_email(query)
    except Exception as exc:
        logger.exception("Failed to read Gmail")
        return {"error": f"Gmail read failed: {exc}"}


tools_list = [send_gmail, read_gmail]
