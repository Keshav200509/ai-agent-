import os
from dotenv import load_dotenv
load_dotenv()
from agent.tools import tools_list
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import initialize_agent, AgentType

# 1. Load environment variables
env_loaded = load_dotenv()

# 2. Initialize the Gemini LLM via LangChain
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash-latest",
    temperature=0
)

# 3. Create the Agent using LangChain 0.1.16 compatible method
agent = initialize_agent(
    tools=tools_list, 
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# 4. Agent runner function for integration with scripts/tests
def run_agent_task(query: str):
    """
    Executes the given query using the pre-initialized AI agent.
    Returns agent output or error as a dictionary.
    """
    try:
        # The agent uses .run for execution in LangChain 0.1.16
        result = agent.run(query)
        return result
    except Exception as e:
        return {"status": "error", "error": str(e)}

# 6. Main manual test runner
if __name__ == "__main__":
    test_query = "Send an email summary of the last Discord message."
    print("\n--- [main] Running test query ---")
    output = run_agent_task(test_query)
    print("Result:", output)