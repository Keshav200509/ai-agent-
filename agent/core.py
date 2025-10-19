import os
from dotenv import load_dotenv
from composio import Composio
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from agent.tools import tools_list

# Load environment variables
load_dotenv()

# Initialize Composio
composio = Composio()

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3, openai_api_key=os.getenv("OPENAI_API_KEY"))

# Initialize agent with the older syntax
agent = initialize_agent(
    tools_list,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent_task(query: str) -> dict:
    """
    Executes a query with the LangChain agent and returns the response.
    """
    try:
        response = agent.run(input=query)
        return {"status": "success", "response": response}
    except Exception as e:
        return {"status": "error", "error": str(e)}

# Main execution block for testing
if __name__ == "__main__":
    test_query = "Get the last message from Discord and send it as an email to test@example.com"
    result = run_agent_task(test_query)
    print(f"Agent Response: {result}")
