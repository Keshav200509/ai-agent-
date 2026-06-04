from agent.config import get_llm
from agent.tools import tools_list
from langchain.agents import initialize_agent, AgentType

# Initialize the Gemini LLM via shared factory
llm = get_llm()

# Create the Agent using LangChain 0.1.16 compatible method
agent = initialize_agent(
    tools=tools_list,
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)


def run_agent_task(query: str):
    """
    Executes the given query using the pre-initialized AI agent.
    Returns agent output or error as a dictionary.
    """
    try:
        result = agent.run(query)
        return result
    except Exception as e:
        return {"status": "error", "error": str(e)}


if __name__ == "__main__":
    test_query = "Send an email summary of the last Discord message."
    print("\n--- [main] Running test query ---")
    output = run_agent_task(test_query)
    print("Result:", output)
