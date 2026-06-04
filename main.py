# main.py
import logging

from dotenv import load_dotenv

load_dotenv()

from agent.core import AgentError, run_agent_task

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# smoke-run
if __name__ == "__main__":
    try:
        res = run_agent_task("Summarise the latest Discord message and email it.")
        print("Result:", res)
    except AgentError as err:
        logger.error("Smoke-run failed: %s", err)
    except Exception as err:
        logger.exception("Unexpected error during smoke-run")
