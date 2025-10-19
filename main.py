# main.py
from dotenv import load_dotenv
from agent.core import YouTubeCommunityAgent
from agent.tools import ComposioTools
from agent.rag import RAGIndex

load_dotenv()

# create mock clients (replace with real Composio & vector db clients)
composio_client = None
vector_client = None
discord_bot = None

tools = ComposioTools(composio_client)
rag = RAGIndex(vector_client)
agent = YouTubeCommunityAgent(llm=None, tools=tools, rag=rag, discord_bot=discord_bot)

# smoke-run
res = agent.ingest_youtube_video("https://www.youtube.com/watch?v=EXAMPLE", source_user="teacher@example.com")
print(res)  # should return dict per contract; fill internals step by step
