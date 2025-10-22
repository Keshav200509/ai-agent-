import os
from composio import Composio
from langchain.tools import tool
composio = Composio(api_key=os.getenv("COMPOSIO_API_KEY"))

@tool("create_google_doc")
def create_google_doc(title: str, content: str):
    """Create a new Google Doc with specified title and content using Composio."""
    return composio.actions.google_docs.create_doc(title, content)

@tool("summarize_google_doc")
def summarize_google_doc(doc_id: str):
    """Summarize the content of a Google Doc using Composio."""
    return composio.actions.google_docs.summarize_doc(doc_id)

tools_list = [create_google_doc, summarize_google_doc]
