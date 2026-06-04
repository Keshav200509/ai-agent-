"""Unit tests for agent/tools/ — dynamic tool loader and individual tool modules.

All Composio calls are mocked so tests run without real API keys.
"""

from unittest.mock import MagicMock, patch


# ---------------------------------------------------------------------------
# Dynamic loader (__init__.py)
# ---------------------------------------------------------------------------

def test_tools_list_is_list():
    """agent.tools.tools_list should be a list."""
    from agent.tools import tools_list
    assert isinstance(tools_list, list)


def test_tools_list_contains_expected_tools():
    """Each *_tools.py module contributes its tools to the aggregate list."""
    from agent.tools import tools_list
    names = [t.name for t in tools_list]
    expected = [
        "create_calendar_event",
        "list_calendar_events",
        "get_latest_discord_message",
        "send_discord_message",
        "create_google_doc",
        "summarize_google_doc",
        "upload_to_drive",
        "list_drive_files",
        "send_gmail",
        "read_gmail",
        "youtube_search_videos",
        "youtube_fetch_transcript",
    ]
    for name in expected:
        assert name in names, f"Missing tool: {name}"


# ---------------------------------------------------------------------------
# Calendar tools
# ---------------------------------------------------------------------------

def test_create_calendar_event_calls_composio():
    from agent.tools import calendar_tools
    mock_composio = MagicMock()
    mock_composio.actions.google_calendar.create_event.return_value = {"id": "evt1"}
    with patch.object(calendar_tools, "composio", mock_composio):
        result = calendar_tools.create_calendar_event.func(
            "Meeting", "2025-01-01T10:00:00Z", "2025-01-01T11:00:00Z"
        )
    assert result == {"id": "evt1"}
    mock_composio.actions.google_calendar.create_event.assert_called_once()


def test_list_calendar_events_calls_composio():
    from agent.tools import calendar_tools
    mock_composio = MagicMock()
    mock_composio.actions.google_calendar.list_events.return_value = []
    with patch.object(calendar_tools, "composio", mock_composio):
        result = calendar_tools.list_calendar_events.func(
            "2025-01-01T00:00:00Z", "2025-01-31T23:59:59Z"
        )
    assert result == []


# ---------------------------------------------------------------------------
# Discord tools
# ---------------------------------------------------------------------------

def test_get_latest_discord_message():
    from agent.tools import discord_tools
    mock_composio = MagicMock()
    mock_composio.actions.discord.get_latest_message.return_value = "Hello!"
    with patch.object(discord_tools, "composio", mock_composio):
        result = discord_tools.get_latest_discord_message.func("chan123")
    assert result == "Hello!"


def test_send_discord_message():
    from agent.tools import discord_tools
    mock_composio = MagicMock()
    mock_composio.actions.discord.send_message.return_value = {"ok": True}
    with patch.object(discord_tools, "composio", mock_composio):
        result = discord_tools.send_discord_message.func("chan123", "hi")
    assert result == {"ok": True}


# ---------------------------------------------------------------------------
# Docs tools
# ---------------------------------------------------------------------------

def test_create_google_doc():
    from agent.tools import docs_tools
    mock_composio = MagicMock()
    mock_composio.actions.google_docs.create_doc.return_value = {"docId": "d1"}
    with patch.object(docs_tools, "composio", mock_composio):
        result = docs_tools.create_google_doc.func("Title", "Body")
    assert result == {"docId": "d1"}


def test_summarize_google_doc():
    from agent.tools import docs_tools
    mock_composio = MagicMock()
    mock_composio.actions.google_docs.summarize_doc.return_value = "summary"
    with patch.object(docs_tools, "composio", mock_composio):
        result = docs_tools.summarize_google_doc.func("d1")
    assert result == "summary"


# ---------------------------------------------------------------------------
# Drive tools
# ---------------------------------------------------------------------------

def test_upload_to_drive():
    from agent.tools import drive_tools
    mock_composio = MagicMock()
    mock_composio.actions.google_drive.upload.return_value = {"fileId": "f1"}
    with patch.object(drive_tools, "composio", mock_composio):
        result = drive_tools.upload_to_drive.func("file.txt", "content")
    assert result == {"fileId": "f1"}


def test_list_drive_files():
    from agent.tools import drive_tools
    mock_composio = MagicMock()
    mock_composio.actions.google_drive.list_files.return_value = [{"name": "a.txt"}]
    with patch.object(drive_tools, "composio", mock_composio):
        result = drive_tools.list_drive_files.func("folder1")
    assert result == [{"name": "a.txt"}]


# ---------------------------------------------------------------------------
# Gmail tools
# ---------------------------------------------------------------------------

def test_send_gmail():
    from agent.tools import gmail_tools
    mock_composio = MagicMock()
    mock_composio.actions.gmail.send_email.return_value = {"status": "sent"}
    with patch.object(gmail_tools, "composio", mock_composio):
        result = gmail_tools.send_gmail.func("Subject", "Body", "a@b.com")
    assert result == {"status": "sent"}


def test_read_gmail():
    from agent.tools import gmail_tools
    mock_composio = MagicMock()
    mock_composio.actions.gmail.read_email.return_value = [{"id": "m1"}]
    with patch.object(gmail_tools, "composio", mock_composio):
        result = gmail_tools.read_gmail.func("is:unread")
    assert result == [{"id": "m1"}]


def test_read_gmail_default_query():
    from agent.tools import gmail_tools
    mock_composio = MagicMock()
    mock_composio.actions.gmail.read_email.return_value = []
    with patch.object(gmail_tools, "composio", mock_composio):
        result = gmail_tools.read_gmail.func()
    mock_composio.actions.gmail.read_email.assert_called_once_with("")
    assert result == []


# ---------------------------------------------------------------------------
# YouTube tools
# ---------------------------------------------------------------------------

def test_youtube_search_videos():
    from agent.tools import youtube_tools
    mock_composio = MagicMock()
    mock_composio.actions.youtube.search_videos.return_value = [{"videoId": "v1"}]
    with patch.object(youtube_tools, "composio", mock_composio):
        result = youtube_tools.youtube_search_videos.func("python tutorial", 3)
    assert result == [{"videoId": "v1"}]
    mock_composio.actions.youtube.search_videos.assert_called_once_with("python tutorial", 3)


def test_youtube_fetch_transcript():
    from agent.tools import youtube_tools
    mock_composio = MagicMock()
    mock_composio.actions.youtube.get_transcript.return_value = "transcript text"
    with patch.object(youtube_tools, "composio", mock_composio):
        result = youtube_tools.youtube_fetch_transcript.func("v1")
    assert result == "transcript text"
