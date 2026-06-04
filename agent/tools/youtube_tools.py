import logging
import os

from composio import Composio
from langchain.tools import tool

logger = logging.getLogger(__name__)

_api_key = os.getenv("COMPOSIO_API_KEY")
if not _api_key:
    logger.warning("COMPOSIO_API_KEY is not set; YouTube tools will fail at runtime")
composio = Composio(api_key=_api_key)


@tool("youtube_search_videos")
def youtube_search_videos(query: str, max_results: int = 5):
    """Search for educational YouTube videos using Composio."""
    try:
        return composio.actions.youtube.search_videos(query, max_results)
    except Exception as exc:
        logger.exception("Failed to search YouTube videos")
        return {"error": f"YouTube search failed: {exc}"}


@tool("youtube_fetch_transcript")
def youtube_fetch_transcript(video_id: str):
    """Fetch transcript for a YouTube video using Composio."""
    try:
        return composio.actions.youtube.get_transcript(video_id)
    except Exception as exc:
        logger.exception("Failed to fetch YouTube transcript")
        return {"error": f"YouTube transcript fetch failed: {exc}"}


tools_list = [youtube_search_videos, youtube_fetch_transcript]
