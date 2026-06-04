from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


settings = Settings()


# ---------------------------------------------------------------------------
# Shared Composio client (singleton)
# ---------------------------------------------------------------------------
_composio_client = None


def get_composio_client():
    """Return a shared Composio client instance, lazily initialized."""
    global _composio_client
    if _composio_client is None:
        from composio import Composio

        _composio_client = Composio(api_key=settings.COMPOSIO_API_KEY)
    return _composio_client


# ---------------------------------------------------------------------------
# Shared LLM factory
# ---------------------------------------------------------------------------
def get_llm(model: str = "models/gemini-1.5-flash-latest", temperature: float = 0):
    """Return a configured ChatGoogleGenerativeAI instance."""
    from langchain_google_genai import ChatGoogleGenerativeAI

    return ChatGoogleGenerativeAI(model=model, temperature=temperature)
