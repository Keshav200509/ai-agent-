from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

settings = Settings()
