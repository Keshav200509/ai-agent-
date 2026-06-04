import logging
import os

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# Keys that the agent cannot function without.
_REQUIRED_KEYS = ("COMPOSIO_API_KEY",)


class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

    def validate(self) -> list[str]:
        """Return a list of missing required env-var names."""
        missing = [k for k in _REQUIRED_KEYS if not getattr(self, k)]
        if missing:
            logger.warning("Missing required environment variables: %s", missing)
        return missing


settings = Settings()
_missing = settings.validate()
if _missing:
    logger.warning(
        "Application may not work correctly — missing: %s", ", ".join(_missing)
    )
