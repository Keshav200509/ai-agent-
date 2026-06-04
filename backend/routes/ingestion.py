import re

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from pydantic import BaseModel, Field, field_validator

from backend.auth import require_api_key

router = APIRouter()

_YOUTUBE_URL_RE = re.compile(
    r"^https?://(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w\-]{11}"
)


class IngestRequest(BaseModel):
    video_url: str = Field(..., min_length=1, max_length=500)
    notify_email: str | None = Field(default=None, max_length=254)

    @field_validator("video_url")
    @classmethod
    def validate_youtube_url(cls, v: str) -> str:
        if not _YOUTUBE_URL_RE.match(v):
            raise ValueError("video_url must be a valid YouTube URL")
        return v


@router.post("/ingest/youtube", dependencies=[Depends(require_api_key)])
def ingest_youtube(
    payload: IngestRequest,
    background_tasks: BackgroundTasks,
):
    # Lazy import to avoid circular imports at module load time.
    from agent.core import YouTubeCommunityAgent  # noqa: F811

    background_tasks.add_task(
        # agent instance should be injected via app state in production;
        # this is a placeholder showing the validated data flow.
        lambda: None,  # TODO: wire up real agent.ingest_youtube_video
    )
    return {"status": "queued"}
