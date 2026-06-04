# backend/routes/ingestion.py
import logging

from fastapi import APIRouter, BackgroundTasks, HTTPException

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/ingest/youtube")
def ingest_youtube(
    video_url: str,
    notify_email: str = None,
    background_tasks: BackgroundTasks = None,
):
    if background_tasks is None:
        raise HTTPException(
            status_code=500,
            detail="Background task runner is not available",
        )
    if not video_url or not video_url.strip():
        raise HTTPException(status_code=400, detail="video_url is required")

    logger.info("Queuing YouTube ingestion for %s", video_url)
    # NOTE: `agent` must be wired up via dependency injection or a shared
    # module before this route is functional.  Importing at the top level
    # would create a circular dependency, so we defer the import.
    try:
        from agent.core import run_agent_task  # noqa: WPS433

        background_tasks.add_task(run_agent_task, f"Ingest YouTube video: {video_url}")
    except Exception as exc:
        logger.exception("Failed to queue YouTube ingestion")
        raise HTTPException(
            status_code=500, detail=f"Failed to queue task: {exc}"
        ) from exc

    return {"status": "queued"}
