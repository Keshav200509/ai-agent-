import logging
import os
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from backend.auth import require_api_key

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Educational AI Agent",
    docs_url=None,       # disable Swagger UI in production
    redoc_url=None,       # disable ReDoc in production
    openapi_url=None,     # disable OpenAPI schema in production
)

# ---------------------------------------------------------------------------
# CORS – restrict to explicitly-allowed origins.
# Set ALLOWED_ORIGINS as a comma-separated list, e.g.
#   ALLOWED_ORIGINS=https://example.com,https://app.example.com
# Defaults to no origins allowed (empty list).
# ---------------------------------------------------------------------------
_raw_origins = os.getenv("ALLOWED_ORIGINS", "")
_allowed_origins: List[str] = [
    o.strip() for o in _raw_origins.split(",") if o.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["X-API-Key", "Content-Type"],
)


# ---------------------------------------------------------------------------
# Request / response models
# ---------------------------------------------------------------------------
class RunRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=5000)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "Educational AI Agent is running!"}


@app.post("/run", dependencies=[Depends(require_api_key)])
def run_agent(payload: RunRequest):
    # Import lazily to avoid circular-import issues when the module is loaded
    # without the full environment (e.g., during tests).
    from agent.core import run_agent_task

    try:
        response = run_agent_task(payload.query)
        return {"result": response}
    except Exception:
        logger.exception("Agent execution failed")
        raise HTTPException(
            status_code=500,
            detail="An internal error occurred. Please try again later.",
        )
