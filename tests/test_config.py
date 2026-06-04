"""Unit tests for agent/config.py — Settings class."""

import os
from unittest.mock import patch


def test_settings_loads_env_vars():
    """Settings attributes reflect environment variables."""
    env = {
        "OPENAI_API_KEY": "sk-test-openai",
        "COMPOSIO_API_KEY": "comp-key-123",
        "GOOGLE_CLIENT_ID": "google-cid",
        "DISCORD_BOT_TOKEN": "discord-tok",
        "LANGSMITH_API_KEY": "ls-key",
    }
    with patch.dict(os.environ, env, clear=False):
        # Re-import to pick up patched env
        import importlib
        import agent.config as cfg_mod

        importlib.reload(cfg_mod)
        s = cfg_mod.Settings()

        assert s.OPENAI_API_KEY == "sk-test-openai"
        assert s.COMPOSIO_API_KEY == "comp-key-123"
        assert s.GOOGLE_CLIENT_ID == "google-cid"
        assert s.DISCORD_BOT_TOKEN == "discord-tok"
        assert s.LANGSMITH_API_KEY == "ls-key"


def test_settings_defaults_to_none():
    """When env vars are absent the attributes are None."""
    env_keys = [
        "OPENAI_API_KEY",
        "COMPOSIO_API_KEY",
        "GOOGLE_CLIENT_ID",
        "DISCORD_BOT_TOKEN",
        "LANGSMITH_API_KEY",
    ]
    cleaned = {k: v for k, v in os.environ.items() if k not in env_keys}
    with patch.dict(os.environ, cleaned, clear=True):
        import importlib
        import agent.config as cfg_mod

        importlib.reload(cfg_mod)
        s = cfg_mod.Settings()

        assert s.OPENAI_API_KEY is None
        assert s.COMPOSIO_API_KEY is None
        assert s.GOOGLE_CLIENT_ID is None
        assert s.DISCORD_BOT_TOKEN is None
        assert s.LANGSMITH_API_KEY is None


def test_settings_singleton_instance():
    """Module-level `settings` is a Settings instance."""
    from agent.config import settings, Settings

    assert isinstance(settings, Settings)
