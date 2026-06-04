from langchain.tools import tool

from agent.config import get_composio_client


@tool("upload_to_drive")
def upload_to_drive(filename: str, file_content: str):
    """Upload a file to Google Drive via Composio."""
    composio = get_composio_client()
    return composio.actions.google_drive.upload(filename, file_content)


@tool("list_drive_files")
def list_drive_files(folder_id: str):
    """List files in a Google Drive folder via Composio."""
    composio = get_composio_client()
    return composio.actions.google_drive.list_files(folder_id)


tools_list = [upload_to_drive, list_drive_files]
