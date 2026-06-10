"""Unit tests for backend/routes/ingestion.py — ingestion endpoint."""

from unittest.mock import MagicMock, patch

from fastapi import FastAPI
from fastapi.testclient import TestClient
from backend.routes.ingestion import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)


def test_ingest_youtube_returns_queued():
    """POST /ingest/youtube queues the task and returns status=queued."""
    mock_agent = MagicMock()
    with patch("backend.routes.ingestion.agent", mock_agent, create=True):
        response = client.post(
            "/ingest/youtube",
            params={"video_url": "https://youtube.com/watch?v=abc"},
        )

    assert response.status_code == 200
    assert response.json() == {"status": "queued"}
