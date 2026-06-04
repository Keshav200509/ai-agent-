import logging
import os

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# Lazy-initialised singleton — created on first call to ``_get_agent()`` so
# that importing this module does not require valid Google credentials (which
# would break test collection in CI).
_agent = None


def _get_agent():
    """Return the LangChain agent, creating it on first use."""
    global _agent
    if _agent is not None:
        return _agent

    try:
        from agent.tools import tools_list
        from langchain_google_genai import ChatGoogleGenerativeAI
        from langchain.agents import initialize_agent, AgentType

        llm = ChatGoogleGenerativeAI(
            model="models/gemini-1.5-flash-latest",
            temperature=0,
        )
        _agent = initialize_agent(
            tools=tools_list,
            llm=llm,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
        )
    except Exception as exc:
        logger.exception("Failed to initialise the AI agent")
        raise AgentError(f"Agent initialisation failed: {exc}") from exc

    return _agent


class AgentError(Exception):
    """Raised when the AI agent fails to execute a task."""


def run_agent_task(query: str) -> str:
    """Execute *query* via the pre-initialised AI agent.

    Returns the agent's textual output on success.
    Raises ``AgentError`` on failure so callers can distinguish success from
    failure without inspecting the return type.
    """
    if not query or not query.strip():
        raise AgentError("query must be a non-empty string")
    try:
        agent = _get_agent()
        result = agent.run(query)
        return result
    except AgentError:
        raise
    except Exception as exc:
        logger.exception("Agent task failed for query: %s", query)
        raise AgentError(str(exc)) from exc


# Main manual test runner
if __name__ == "__main__":
    test_query = "Send an email summary of the last Discord message."
    print("\n--- [main] Running test query ---")
    try:
        output = run_agent_task(test_query)
        print("Result:", output)
    except AgentError as err:
        print("Agent error:", err)