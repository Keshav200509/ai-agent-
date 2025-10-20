# # test_agent.py (new file for testing)
# from agent.core import run_agent_task

# query = """
# Fetch the most recent message from my Discord channel with ID 123456789012345678
# and send it as an email to my address: your_email@gmail.com
# """

# result = run_agent_task(query)
# print("Result:", result)


# agent/test_agent.py
from agent.core import run_agent_task
import os
import pytest # Make sure to import pytest

def test_run_agent():
    """
    This is a test function that pytest will automatically find and run.
    It runs a simple, non-destructive query to see if the agent works.
    """
    print("\n--- [Pytest] Running test_run_agent ---")
    
    # Check if secrets are available in the test environment
    if not os.getenv("COMPOSIO_API_KEY") or not os.getenv("OPENAI_API_KEY"):
        pytest.skip("API keys not found in environment. Skipping integration test.")

    # A simple test query
    query = "What is the capital of France?"
    
    response = run_agent_task(query)
    
    # A simple check to see if we got a real, non-empty response
    assert response is not None
    assert len(response) > 0
    
    print(f"Agent query: {query}")
    print(f"Agent response: {response}")
    print("--- [Pytest] Test completed successfully ---")


# This block still lets you run the file directly as a script
if __name__ == "__main__":
    print("\n--- [Main] Running test_agent.py as a script ---")
    
    # Your original test query
    script_query = "Send an email summary of the last Discord message"
    response = run_agent_task(script_query)
    
    print("\n--- [Main] Script Response ---")
    print(response)
    print("----------------------------")