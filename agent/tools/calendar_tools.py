from langchain.tools import tool

from agent.config import get_composio_client


@tool("create_calendar_event")
def create_calendar_event(summary: str, start_time: str, end_time: str):
    """Create an event on Google Calendar using Composio (times in RFC3339)."""
    composio = get_composio_client()
    return composio.actions.google_calendar.create_event(summary, start_time, end_time)


@tool("list_calendar_events")
def list_calendar_events(time_min: str, time_max: str):
    """List events in a date range on Google Calendar using Composio (times in RFC3339)."""
    composio = get_composio_client()
    return composio.actions.google_calendar.list_events(time_min, time_max)


tools_list = [create_calendar_event, list_calendar_events]
