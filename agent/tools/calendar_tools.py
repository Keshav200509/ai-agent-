import logging
import os

from composio import Composio
from langchain.tools import tool

logger = logging.getLogger(__name__)

_api_key = os.getenv("COMPOSIO_API_KEY")
if not _api_key:
    logger.warning("COMPOSIO_API_KEY is not set; calendar tools will fail at runtime")
composio = Composio(api_key=_api_key)


@tool("create_calendar_event")
def create_calendar_event(summary: str, start_time: str, end_time: str):
    """Create an event on Google Calendar using Composio (times in RFC3339)."""
    try:
        return composio.actions.google_calendar.create_event(summary, start_time, end_time)
    except Exception as exc:
        logger.exception("Failed to create calendar event")
        return {"error": f"Calendar event creation failed: {exc}"}


@tool("list_calendar_events")
def list_calendar_events(time_min: str, time_max: str):
    """List events in a date range on Google Calendar using Composio (times in RFC3339)."""
    try:
        return composio.actions.google_calendar.list_events(time_min, time_max)
    except Exception as exc:
        logger.exception("Failed to list calendar events")
        return {"error": f"Calendar event listing failed: {exc}"}


tools_list = [create_calendar_event, list_calendar_events]
