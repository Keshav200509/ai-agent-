from langchain.tools import tool

from agent.config import get_composio_client


@tool("send_gmail")
def send_gmail(subject: str, body: str, recipient: str):
    """Send an email using Gmail via Composio."""
    composio = get_composio_client()
    return composio.actions.gmail.send_email(subject, body, recipient)


@tool("read_gmail")
def read_gmail(query: str = ""):
    """Read emails from Gmail using Composio. Query can be a search string."""
    composio = get_composio_client()
    return composio.actions.gmail.read_email(query)


tools_list = [send_gmail, read_gmail]
