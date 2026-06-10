"""Shared test fixtures — stub out heavy external SDKs globally.

agent/core.py executes `initialize_agent(tools=..., llm=...)` at import time.
The MagicMock for ChatGoogleGenerativeAI doesn't satisfy LangChain's Runnable
check, so we also need to stub `langchain.agents.initialize_agent` *before*
agent.core is ever imported.
"""

import sys
import types
from unittest.mock import MagicMock

# --- Composio ---
if "composio" not in sys.modules:
    _composio = types.ModuleType("composio")
    _composio.Composio = MagicMock
    sys.modules["composio"] = _composio

# --- langchain_google_genai ---
if "langchain_google_genai" not in sys.modules:
    _lg = types.ModuleType("langchain_google_genai")
    _lg.ChatGoogleGenerativeAI = MagicMock
    sys.modules["langchain_google_genai"] = _lg

# --- Patch initialize_agent to return a MagicMock agent ---
import langchain.agents as _lc_agents

_original_init_agent = _lc_agents.initialize_agent


def _fake_initialize_agent(*args, **kwargs):
    """Return a fake agent whose .run() is a MagicMock."""
    fake = MagicMock()
    fake.run.return_value = "stub-response"
    return fake


_lc_agents.initialize_agent = _fake_initialize_agent
