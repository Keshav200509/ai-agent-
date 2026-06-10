"""Unit tests for backend/server.py — FastAPI endpoints."""

from unittest.mock import patch

from fastapi.testclient import TestClient
from backend.server import app


client = TestClient(app)


def test_home_endpoint():
    """GET / returns a JSON greeting."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "running" in data["message"].lower()


def test_run_endpoint_success():
    """POST /run returns agent result on success."""
    with patch("backend.server.run_agent_task", return_value="mocked"):
        response = client.post("/run", params={"query": "test query"})

    assert response.status_code == 200
    assert response.json() == {"result": "mocked"}


def test_run_endpoint_error():
    """POST /run returns 500 when the agent raises."""
    with patch("backend.server.run_agent_task", side_effect=RuntimeError("fail")):
        response = client.post("/run", params={"query": "bad"})

    assert response.status_code == 500
    assert "fail" in response.json()["detail"]


def test_run_endpoint_missing_query():
    """POST /run without query param returns 422."""
    response = client.post("/run")
    assert response.status_code == 422
