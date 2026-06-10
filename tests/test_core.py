"""Unit tests for agent/core.py — run_agent_task function."""

from unittest.mock import MagicMock, patch

import agent.core as core_mod


def test_run_agent_task_returns_result():
    """run_agent_task delegates to agent.run and returns the result."""
    fake_agent = MagicMock()
    fake_agent.run.return_value = "mocked answer"

    with patch.object(core_mod, "agent", fake_agent):
        result = core_mod.run_agent_task("hello")

    assert result == "mocked answer"
    fake_agent.run.assert_called_once_with("hello")


def test_run_agent_task_returns_error_dict_on_exception():
    """On exception run_agent_task returns a dict with status=error."""
    fake_agent = MagicMock()
    fake_agent.run.side_effect = RuntimeError("boom")

    with patch.object(core_mod, "agent", fake_agent):
        result = core_mod.run_agent_task("fail query")

    assert isinstance(result, dict)
    assert result["status"] == "error"
    assert "boom" in result["error"]


def test_run_agent_task_passes_query_string():
    """Various query strings are forwarded verbatim."""
    fake_agent = MagicMock()
    fake_agent.run.return_value = "ok"

    queries = [
        "",
        "short",
        "a much longer query with multiple words and special chars: !@#$%",
    ]
    with patch.object(core_mod, "agent", fake_agent):
        for q in queries:
            core_mod.run_agent_task(q)
            fake_agent.run.assert_called_with(q)
