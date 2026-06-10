import logging
import os

from composio import Composio
from langchain.tools import tool

logger = logging.getLogger(__name__)

_api_key = os.getenv("COMPOSIO_API_KEY")
if not _api_key:
    logger.warning("COMPOSIO_API_KEY is not set; Google Docs tools will fail at runtime")
composio = Composio(api_key=_api_key)


@tool("create_google_doc")
def create_google_doc(title: str, content: str):
    """Create a new Google Doc with specified title and content using Composio."""
    try:
        return composio.actions.google_docs.create_doc(title, content)
    except Exception as exc:
        logger.exception("Failed to create Google Doc")
        return {"error": f"Google Doc creation failed: {exc}"}


@tool("summarize_google_doc")
def summarize_google_doc(doc_id: str):
    """Summarize the content of a Google Doc using Composio."""
    try:
        return composio.actions.google_docs.summarize_doc(doc_id)
    except Exception as exc:
        logger.exception("Failed to summarize Google Doc")
        return {"error": f"Google Doc summarization failed: {exc}"}


tools_list = [create_google_doc, summarize_google_doc]
