import os
from typing import Dict, Any
from dotenv import load_dotenv

# Composio client (used by tools)
from composio import Composio

# LangChain (v0.3.x compatible imports)
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType

# Local tools (expects tools_list to be defined in agent.tools)
from agent.tools import tools_list

# Load environment variables from .env
load_dotenv()

# Initialize Composio client (tools may also initialize their own client,
# but we create a top-level one here for consistency)
COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY")
composio = Composio(api_key=COMPOSIO_API_KEY) if COMPOSIO_API_KEY else Composio()

# Initialize the LLM using langchain_openai (compatible with LangChain v0.3.x)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# ChatOpenAI in the 0.3.x ecosystem typically accepts model_name (or model/model parameter
# variations across releases). Using model_name for compatibility; adjust if your
# langchain_openai version expects a different kwarg.
llm = ChatOpenAI(
    model_name=OPENAI_MODEL,
    temperature=0.3,
    openai_api_key=OPENAI_API_KEY,
)

# Initialize the agent using the older initialize_agent API.
# We intentionally do NOT import or use create_react_agent or AgentExecutor here.
try:
    agent = initialize_agent(
        tools_list,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
except Exception as e:
    # In environments where agent initialization can fail (missing keys, incompatible LLM, etc.)
    # keep agent as None so run_agent_task can return a helpful error.
    agent = None
    _init_error = e


def run_agent_task(query: str) -> Dict[str, Any]:
    """
    Execute a query with the initialized LangChain agent.

    Returns a dict with status and response or an error message:
      { "status": "success", "response": "<agent output>" }
      { "status": "error", "error": "<error text>" }

    This signature matches usage from agent/test_agent.py:
        from agent.core import run_agent_task
        print(run_agent_task("Send an email summary of the last Discord message"))
    """
    if agent is None:
        # Return initialization error information
        err_msg = f"Agent not initialized. Initialization error: {_init_error!s}" if "_init_error" in globals() else "Agent not initialized."
        return {"status": "error", "error": err_msg}

    try:
        # For LangChain v0.3.x initialize_agent returns an executor with a .run(...) method.
        result = agent.run(query)
        return {"status": "success", "response": result}
    except Exception as e:
        return {"status": "error", "error": str(e)}


# Allow quick manual testing when running this module directly.
if __name__ == "__main__":
    test_query = "Get the last message from Discord and send it as an email to test@example.com"
    result = run_agent_task(test_query)
    print("Agent Response:", result)
