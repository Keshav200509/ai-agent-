from langchain.tools import tool

from agent.config import get_composio_client


@tool("youtube_search_videos")
def youtube_search_videos(query: str, max_results: int = 5):
    """Search for educational YouTube videos using Composio."""
    composio = get_composio_client()
    return composio.actions.youtube.search_videos(query, max_results)


@tool("youtube_fetch_transcript")
def youtube_fetch_transcript(video_id: str):
    """Fetch transcript for a YouTube video using Composio."""
    composio = get_composio_client()
    return composio.actions.youtube.get_transcript(video_id)


tools_list = [youtube_search_videos, youtube_fetch_transcript]
