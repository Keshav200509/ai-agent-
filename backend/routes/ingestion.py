# backend/routes/ingestion.py
from fastapi import APIRouter, BackgroundTasks
router = APIRouter()

@router.post("/ingest/youtube")
def ingest_youtube(video_url: str, notify_email: str = None, background_tasks: BackgroundTasks = None):
    background_tasks.add_task(agent.ingest_youtube_video, video_url, notify_email)
    return {"status": "queued"}
