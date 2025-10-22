from composio import Composio
from langchain.tools import tool
import os

composio = Composio(api_key=os.getenv("COMPOSIO_API_KEY"))

@tool("youtube_search_videos")
def youtube_search_videos(query: str, max_results: int = 5):
    """Search for educational YouTube videos using Composio."""
    return composio.actions.youtube.search_videos(query, max_results)

@tool("youtube_fetch_transcript")
def youtube_fetch_transcript(video_id: str):
    """Fetch transcript for a YouTube video using Composio."""
    return composio.actions.youtube.get_transcript(video_id)

tools_list = [youtube_search_videos, youtube_fetch_transcript]
