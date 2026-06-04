import os
import secrets

from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)


def _get_configured_api_key() -> str | None:
    return os.getenv("APP_API_KEY")


async def require_api_key(
    api_key: str | None = Security(API_KEY_HEADER),
) -> str:
    """FastAPI dependency that rejects requests without a valid API key.

    Set the APP_API_KEY environment variable to enable key-based auth.
    If APP_API_KEY is not configured the endpoint is unreachable (fail-closed).
    """
    configured_key = _get_configured_api_key()
    if configured_key is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Server API key not configured. Set APP_API_KEY env var.",
        )
    if api_key is None or not secrets.compare_digest(api_key, configured_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key.",
        )
    return api_key
