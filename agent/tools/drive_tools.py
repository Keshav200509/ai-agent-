import logging
import os

from composio import Composio
from langchain.tools import tool

logger = logging.getLogger(__name__)

_api_key = os.getenv("COMPOSIO_API_KEY")
if not _api_key:
    logger.warning("COMPOSIO_API_KEY is not set; Google Drive tools will fail at runtime")
composio = Composio(api_key=_api_key)


@tool("upload_to_drive")
def upload_to_drive(filename: str, file_content: str):
    """Upload a file to Google Drive via Composio."""
    try:
        return composio.actions.google_drive.upload(filename, file_content)
    except Exception as exc:
        logger.exception("Failed to upload to Google Drive")
        return {"error": f"Drive upload failed: {exc}"}


@tool("list_drive_files")
def list_drive_files(folder_id: str):
    """List files in a Google Drive folder via Composio."""
    try:
        return composio.actions.google_drive.list_files(folder_id)
    except Exception as exc:
        logger.exception("Failed to list Drive files")
        return {"error": f"Drive file listing failed: {exc}"}


tools_list = [upload_to_drive, list_drive_files]
