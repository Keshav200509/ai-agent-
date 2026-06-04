import logging
import os

from dotenv import load_dotenv

load_dotenv()

from agent.tools import tools_list
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType

logger = logging.getLogger(__name__)

# 1. Load environment variables
env_loaded = load_dotenv()

# 2. Initialize the Gemini LLM via LangChain
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash-latest",
    temperature=0,
)

# 3. Create the Agent using LangChain 0.1.16 compatible method
agent = initialize_agent(
    tools=tools_list,
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)


class AgentError(Exception):
    """Raised when the AI agent fails to execute a task."""


# 4. Agent runner function for integration with scripts/tests
def run_agent_task(query: str) -> str:
    """Execute *query* via the pre-initialised AI agent.

    Returns the agent's textual output on success.
    Raises ``AgentError`` on failure so callers can distinguish success from
    failure without inspecting the return type.
    """
    if not query or not query.strip():
        raise AgentError("query must be a non-empty string")
    try:
        result = agent.run(query)
        return result
    except Exception as exc:
        logger.exception("Agent task failed for query: %s", query)
        raise AgentError(str(exc)) from exc


# 6. Main manual test runner
if __name__ == "__main__":
    test_query = "Send an email summary of the last Discord message."
    print("\n--- [main] Running test query ---")
    try:
        output = run_agent_task(test_query)
        print("Result:", output)
    except AgentError as err:
        print("Agent error:", err)