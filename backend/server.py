import logging

from fastapi import FastAPI, HTTPException

from agent.core import AgentError, run_agent_task

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Educational AI Agent is running!"}


@app.post("/run")
def run_agent(query: str):
    try:
        response = run_agent_task(query)
        return {"result": response}
    except AgentError as exc:
        logger.error("Agent task failed: %s", exc)
        raise HTTPException(status_code=500, detail=str(exc))
    except Exception as exc:
        logger.exception("Unexpected error in /run endpoint")
        raise HTTPException(
            status_code=500, detail="Internal server error"
        ) from exc
