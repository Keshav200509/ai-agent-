# Educational AI Ecosystem Agent

## Overview
This project implements an intelligent educational AI agent using Gemini (LLM via LangChain), Composio for tool/service integrations, and LangChain for orchestration and workflow automation.

## Architecture

- **/agent/**
  - `/tools/`: Modular tool integrations (Discord, Gmail, Google Drive, Docs, Calendar, YouTube). Each has a corresponding *_tools.py file providing tool functions.
  - `core.py`: Main agent logic, initializes Gemini LLM, tools via Composio, and orchestrates tasks using LangChain agents.
  - `test_agent.py`: Test runner and pipeline.
  - other supporting files.

- **Gemini via LangChain**: Replaces OpenAI as the reasoning/planning engine for all agent tasks.
- **Composio**: Seamlessly connects 3rd-party APIs (Discord, Google, YouTube, etc.) using their plug-and-play SDK. All tool actions are defined in /agent/tools/ as LangChain tools.

## How It Works
1. User inputs a natural language command.
2. Agent (LangChain + Gemini) interprets task, determines required tools.
3. Selected tools are invoked via Composio from modular agent/tools/*.py files.
4. Outputs/results are composed, stored, and can trigger downstream actions.

## Adding Tools
- Add new *_tools.py files to /agent/tools/
- Each file must define a `tools_list` variable with valid LangChain tool objects (see other modules for examples)

## .env Required Keys
- DISCORD_TOKEN
- GOOGLE_CLIENT_ID
- GOOGLE_CLIENT_SECRET
- GOOGLE_REFRESH_TOKEN
- GOOGLE_DRIVE_FOLDER_ID
- GMAIL_ADDRESS
- COMPOSIO_API_KEY
- GEMINI_API_KEY

## Testing
See `agent/test_agent.py` for usage and validation pipeline.

## Internal File Flow
- `core.py` loads all tools, initializes LLM, sets up orchestration using LangChain’s AgentExecutor.
- Test and entry modules show agent workflows in action.
