from langchain.tools import tool

from agent.config import get_composio_client


@tool("create_google_doc")
def create_google_doc(title: str, content: str):
    """Create a new Google Doc with specified title and content using Composio."""
    composio = get_composio_client()
    return composio.actions.google_docs.create_doc(title, content)


@tool("summarize_google_doc")
def summarize_google_doc(doc_id: str):
    """Summarize the content of a Google Doc using Composio."""
    composio = get_composio_client()
    return composio.actions.google_docs.summarize_doc(doc_id)


tools_list = [create_google_doc, summarize_google_doc]
