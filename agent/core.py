# import os
# from typing import Dict, Any
# from dotenv import load_dotenv

# # Composio client (used by tools)
# from composio import Composio

# # LangChain (v0.3.x compatible imports)
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.agents import initialize_agent, AgentType

# # Local tools (expects tools_list to be defined in agent.tools)
# from agent.tools import tools_list

# # Load environment variables from .env
# load_dotenv()

# # Initialize Composio client (tools may also initialize their own client,
# # but we create a top-level one here for consistency)
# COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY")
# composio = Composio(api_key=COMPOSIO_API_KEY) if COMPOSIO_API_KEY else Composio()

# # Initialize the LLM using langchain_openai (compatible with LangChain v0.3.x)
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# # ChatOpenAI in the 0.3.x ecosystem typically accepts model_name (or model/model parameter
# # variations across releases). Using model_name for compatibility; adjust if your
# # langchain_openai version expects a different kwarg.


# # ... (other imports) ...

# # 3. Create an LLM
# llm = ChatGoogleGenerativeAI(
#     model="models/gemini-1.5-flash-latest",  # Add the prefix
#     temperature=0
# )
# # Initialize the agent using the older initialize_agent API.
# # We intentionally do NOT import or use create_react_agent or AgentExecutor here.
# try:
#     agent = initialize_agent(
#         tools_list,
#         llm,
#         agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
#         verbose=True,
#     )
# except Exception as e:
#     # In environments where agent initialization can fail (missing keys, incompatible LLM, etc.)
#     # keep agent as None so run_agent_task can return a helpful error.
#     agent = None
#     _init_error = e


# # def run_agent_task(query: str) -> Dict[str, Any]:
# #     """
# #     Execute a query with the initialized LangChain agent.

# #     Returns a dict with status and response or an error message:
# #       { "status": "success", "response": "<agent output>" }
# #       { "status": "error", "error": "<error text>" }

# #     This signature matches usage from agent/test_agent.py:
# #         from agent.core import run_agent_task
# #         print(run_agent_task("Send an email summary of the last Discord message"))
# #     """
# #     if agent is None:
# #         # Return initialization error information
# #         err_msg = f"Agent not initialized. Initialization error: {_init_error!s}" if "_init_error" in globals() else "Agent not initialized."
# #         return {"status": "error", "error": err_msg}

# #     try:
# #         # For LangChain v0.3.x initialize_agent returns an executor with a .run(...) method.
# #         result = agent.run(query)
# #         return {"status": "success", "response": result}
# #     except Exception as e:
# #         return {"status": "error", "error": str(e)}

# def run_agent_task(query: str):
#     """
#     Executes the given query using the pre-initialized agent.
#     """
#     print(f"\n[run_agent_task] Executing query: '{query}'")
#     try:
#         # Use .invoke() which takes a dictionary and returns one
#         result_dict = agent.invoke({"input": query})
#         # The actual answer is in the 'output' key
#         return result_dict.get("output")
#     except Exception as e:
#         print(f"[run_agent_task] Error during agent execution: {e}")
#         # Format the error as a dictionary to match the old 'status' output
#         return {"status": "error", "error": str(e)}

# # Allow quick manual testing when running this module directly.
# if __name__ == "__main__":
#     test_query = "Get the last message from Discord and send it as an email to test@example.com"
#     result = run_agent_task(test_query)
#     print("Agent Response:", result)










import os
from dotenv import load_dotenv

# We need to load .env before any other imports
# to ensure agent/tools.py gets the API key
load_dotenv() 

from agent.tools import tools_list
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor # This is the standard path
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.format_scratchpad.structured_chat import format_to_structured_chat_messages
from langchain.agents.output_parsers.structured_chat import StructuredChatOutputParser
from langchain.tools.render import render_text_description_structured

print("Initializing modern agent and tools...")

# 1. Initialize Tools (This is now done by importing from agent.tools)
print(f"Successfully loaded {len(tools_list)} tools.")

# 2. Create an LLM
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash-latest",  # Using the model that works
    temperature=0
    # GOOGLE_API_KEY is loaded automatically from .env
)

# 3. Create the Prompt
# This is the modern replacement for AgentType.STRUCTURED_CHAT...
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. You have access to the following tools:\n\n"
                   "{tools}\n\n"
                   "You must always use the tools for any user request."),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# 4. Create the Agent
# We bind the tools and formatting functions to the LLM
agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_structured_chat_messages(
            x["intermediate_steps"]
        ),
        "tools": lambda x: render_text_description_structured(tools_list),
    }
    | prompt
    | llm.with_structured_output(
        include_raw=False,
    )
    | StructuredChatOutputParser()
)

# 5. Create the Agent Executor
# This is the new way to run the agent
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools_list, 
    verbose=True
)

print("Agent initialized successfully.")

# 6. Define a function to run the agent task
def run_agent_task(query: str):
    """
    Executes the given query using the pre-initialized agent executor.
    """
    print(f"\n[run_agent_task] Executing query: '{query}'")
    try:
        # Use .invoke() which takes a dictionary and returns one
        result_dict = agent_executor.invoke({"input": query})
        # The actual answer is in the 'output' key
        return result_dict.get("output")
    except Exception as e:
        print(f"[run_agent_task] Error during agent execution: {e}")
        return {"status": "error", "error": str(e)}

# 7. Print the response if the file is run directly
if __name__ == "__main__":
    """
    This block allows you to test this file directly by running:
    python -m agent.core
    """
    print("\n--- [main] Running test query ---")
    
    test_query = "Send an email summary of the last Discord message"
    
    response = run_agent_task(test_query)
    
    print("\n--- [main] Agent Response ---")
    print(response)
    print("-----------------------------")