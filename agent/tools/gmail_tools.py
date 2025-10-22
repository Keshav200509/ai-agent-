from composio import Composio
from langchain.tools import tool
import os

composio = Composio(api_key=os.getenv("COMPOSIO_API_KEY"))

@tool("send_gmail")
def send_gmail(subject: str, body: str, recipient: str):
    """Send an email using Gmail via Composio."""
    return composio.actions.gmail.send_email(subject, body, recipient)

@tool("read_gmail")
def read_gmail(query: str = ""):  # Default empty for all inbox
    """Read emails from Gmail using Composio. Query can be a search string."""
    return composio.actions.gmail.read_email(query)

tools_list = [send_gmail, read_gmail]
