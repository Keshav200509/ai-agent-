# test_agent.py (new file for testing)
from agent.core import run_agent_task

query = """
Fetch the most recent message from my Discord channel with ID 123456789012345678
and send it as an email to my address: your_email@gmail.com
"""

result = run_agent_task(query)
print("Result:", result)
