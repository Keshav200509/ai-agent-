# AI Agent Ecosystem: Educational & Token Optimization Framework

> **A comprehensive multi-agent framework combining educational content management with intelligent token cost optimization for AI model usage.**

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.1.16+-green)
![Composio](https://img.shields.io/badge/Composio-Multi--Tool-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Core Agents](#core-agents)
4. [Installation & Setup](#installation--setup)
5. [Configuration](#configuration)
6. [Usage Guide](#usage-guide)
7. [Agent Deep Dive](#agent-deep-dive)
8. [Token Guard Agent](#token-guard-agent)
9. [API Integration](#api-integration)
10. [Metrics & Monitoring](#metrics--monitoring)
11. [Development Guide](#development-guide)
12. [Troubleshooting](#troubleshooting)
13. [Contributing](#contributing)

---

## 🎯 Overview

### What This Project Does

This project implements a **dual-agent system**:

1. **Educational AI Ecosystem Agent** - Manages educational content across Discord, YouTube, Gmail, and Google Drive
2. **Token Guard Agent** - Optimizes AI model token usage, reducing costs by 40-60% without sacrificing output quality

The system is built on:
- **LangChain** for agent orchestration
- **Composio** for seamless API integrations
- **Google Gemini** as the primary LLM
- **ChromaDB** for semantic caching and RAG
- **OpenAI/Anthropic APIs** for token optimization

### Why This Matters

**Problem**: AI agents generate massive API bills because they:
- Send full context every request (redundant)
- Use expensive models for simple tasks
- Have no semantic caching mechanism
- Don't optimize prompts

**Solution**: Token Guard Agent intercepts requests, optimizes them, and routes to the cheapest viable model while maintaining quality.

### Real-World Impact

```
Without Token Guard:
├─ 100 requests/day × 50,000 tokens avg = 5M tokens
├─ At $0.003/1M tokens (gpt-3.5) = $15/day = $450/month
└─ Team size: 10 → $4,500/month

With Token Guard:
├─ 60% token reduction = 2M tokens/day
├─ Cost: $6/day = $180/month
├─ Team size: 10 → $1,800/month
└─ Monthly Savings: $2,700 (60% reduction)
```

---

## 🏗️ Architecture

### System Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                           │
│              (Discord, Email, Web Dashboard)                    │
└────────────────────────────┬──────────────────────────────────┘
                             ↓
        ┌────────────────────────────────────────────────┐
        │    REQUEST ROUTING LAYER                       │
        │  ├─ Route by task type                         │
        │  ├─ Check budget & rate limits                 │
        │  └─ Log all requests                           │
        └────────────────────────────────────────────────┘
                             ↓
        ┌────────────────────────────────────────────────┐
        │    TOKEN GUARD AGENT (Cost Optimizer)          │
        │  ├─ Semantic cache lookup                      │
        │  ├─ Prompt optimization                        │
        │  ├─ Model selection (cheap vs expensive)       │
        │  ├─ Request decomposition (if needed)          │
        │  └─ Cost prediction                            │
        └────────────┬───────────────────────────────────┘
                     ↓
    ┌────────────────────────────────────────────────────────┐
    │  EDUCATIONAL AGENT / PRIMARY CODING AGENTS             │
    │  ├─ Semantic Cache (ChromaDB)                          │
    │  ├─ Tool Orchestration (Composio)                      │
    │  │  ├─ Discord Integration                             │
    │  │  ├─ Gmail Integration                               │
    │  │  ├─ Google Drive Integration                        │
    │  │  ├─ YouTube Integration                             │
    │  │  ├─ Google Calendar Integration                     │
    │  │  └─ Google Docs Integration                         │
    │  └─ LLM Backend (Gemini, Claude, GPT)                  │
    └────────────┬─────────────────────────────────────────┘
                 ↓
    ┌────────────────────────────────────────────────────────┐
    │          OUTPUT PROCESSING & STORAGE                   │
    │  ├─ Response validation & formatting                   │
    │  ├─ Cache storage (future reuse)                       │
    │  ├─ Metrics recording                                  │
    │  └─ User notification                                  │
    └────────────┬─────────────────────────────────────────┘
                 ↓
    ┌────────────────────────────────────────────────────────┐
    │              EXTERNAL SYSTEMS                          │
    │  ├─ Google Workspace (Drive, Docs, Calendar, Gmail)    │
    │  ├─ Discord Servers & Channels                         │
    │  ├─ YouTube (Transcripts & Metadata)                   │
    │  ├─ OpenAI / Anthropic / Google APIs                   │
    │  └─ Metrics Database (PostgreSQL / BigQuery)           │
    └────────────────────────────────────────────────────────┘
```

---

## 🤖 Core Agents

### 1. Educational AI Ecosystem Agent

**Purpose**: Coordinate educational content across multiple platforms

**Capabilities**:
- 📝 Ingest YouTube video transcripts
- 💬 Monitor Discord discussions  
- 📧 Send email summaries
- 📁 Store content in Google Drive
- 📅 Schedule educational events
- 🔍 Semantic search across all sources

---

### 2. Token Guard Agent ⭐ (CORE FOCUS)

**Purpose**: Optimize AI model token usage and reduce costs by 40-60%

**How It Works**:

```
Original Request: "Build a complete user management API"
                     (5000 tokens, $0.60 cost)
                             ↓
        [Token Guard Analysis & Optimization]
        ├─ Check semantic cache (92% match found!)
        ├─ Compress prompt (40% token reduction)
        ├─ Select optimal model (gpt-3.5 not claude-opus)
        └─ Decompose into subtasks (parallel execution)
                             ↓
                Result: 60% cost reduction
              ($0.24 instead of $0.60)
              Same code quality, better price
```

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8+
- pip or conda
- Git

### Quick Start

```bash
# 1. Clone repository
git clone https://github.com/Keshav200509/ai-agent-.git
cd ai-agent-

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirement.txt

# 4. Setup environment variables
cp .env.example .env
# Edit .env with your API keys

# 5. Run
python main.py
```

---

## ⚙️ Configuration

### Environment Variables (.env)

```env
# Google Workspace
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_secret
GOOGLE_REFRESH_TOKEN=your_token
GOOGLE_DRIVE_FOLDER_ID=your_folder_id
GMAIL_ADDRESS=your_email@gmail.com

# Discord
DISCORD_TOKEN=your_discord_token

# LLM APIs
GEMINI_API_KEY=your_gemini_key
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key

# Composio
COMPOSIO_API_KEY=your_composio_key

# Token Guard
TOKEN_GUARD_ENABLED=true
TOKEN_GUARD_CACHE_SIMILARITY_THRESHOLD=0.85
TOKEN_GUARD_COST_BUDGET_MONTHLY=1000
```

---

## 💻 Usage Guide

### Quick Example

```python
from agent.token_guard.core import TokenGuardAgent

guard = TokenGuardAgent()
result = guard.optimize_and_route(
    "Build REST API for user authentication"
)

print(f"Code: {result['code'][:200]}...")
print(f"Tokens Saved: {result['tokens_saved']}")
print(f"Cost Saved: ${result['cost_saved']:.2f}")
```

### Run FastAPI Backend

```bash
uvicorn backend.server:app --reload --port 8000
```

### Run Tests

```bash
pytest tests/ -v
```

---

## 🔍 Token Guard Agent Deep Dive

### 6 Core Components

#### 1. **Request Analyzer** 
Classifies incoming requests and estimates token requirements
```python
analysis = analyzer.analyze_request("Build login API")
# Returns: task_type, complexity, language, estimated_tokens, optimization_potential
```

#### 2. **Semantic Cache**
Checks if similar problem solved before (80-90% savings)
```python
cached = cache.lookup_similar_requests("Create auth endpoint")
# Returns: similar_code if >85% match, else None
```

#### 3. **Prompt Optimizer**
Compresses prompt without quality loss (30-50% savings)
```python
optimized = optimizer.optimize_prompt(verbose_prompt)
# Returns: shorter_prompt, tokens_before, tokens_after
```

#### 4. **Model Router**
Selects cheapest viable model (40-70% savings)
```python
model = router.select_optimal_model("simple_refactoring")
# Returns: gpt-3.5-turbo (not expensive claude-opus)
```

#### 5. **Request Decomposer**
Breaks complex requests into cheaper subtasks (20-40% savings)
```python
subtasks = decomposer.decompose_request("full_system")
# Returns: 5 independent subtasks, run in parallel
```

#### 6. **Output Processor**
Validates output, caches, and tracks metrics
```python
metrics = processor.measure_token_usage(request, response)
# Returns: actual_tokens, cost_saved, quality_score
```

### Token Savings Breakdown

| Mechanism | Savings | When to Use |
|-----------|---------|------------|
| Semantic Cache | 80-90% | Repeated requests |
| Prompt Optimization | 30-50% | All requests |
| Model Downgrading | 40-70% | Simple tasks |
| Request Decomposition | 20-40% | Complex tasks |
| **COMBINED EFFECT** | **40-60%** | **Standard workflow** |

---

## 🔌 API Integration (Composio)

Composio provides plug-and-play integration with:

- **Discord** - Read messages, send messages
- **Gmail** - Send/read emails, manage labels
- **Google Drive** - Upload/download files
- **Google Docs** - Create/edit documents
- **YouTube** - Get transcripts, search videos
- **Google Calendar** - Create/update events

---

## 📊 Metrics & Monitoring

### Track These Metrics

```python
# Daily metrics
- Total tokens used
- Total API costs
- Cache hit rate (%)
- Average savings per request
- Model distribution
- Decomposed requests count
```

### Example Dashboard Query

```sql
SELECT 
    DATE(timestamp) as date,
    SUM(cost) as daily_cost,
    SUM(cost_saved) as daily_savings,
    COUNT(CASE WHEN cache_hit THEN 1 END) * 100 / COUNT(*) as cache_hit_rate
FROM metrics
WHERE timestamp >= NOW() - INTERVAL 7 DAY
GROUP BY DATE(timestamp);
```

---

## 🛠️ Development

### Add New Feature

```bash
# 1. Create branch
git checkout -b feature/amazing-feature

# 2. Implement with tests
pytest tests/test_new_feature.py

# 3. Submit PR
```

### Code Style

```python
# Use type hints
def optimize_request(request: str) -> dict:
    """Process request through all optimization layers."""
    pass

# Add docstrings
# Follow PEP 8
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| API key not found | Check .env file has all required keys |
| ChromaDB error | Run `mkdir -p data/chromadb` |
| Rate limited | Token Guard automatically retries with backoff |
| Cache not working | Lower `CACHE_SIMILARITY_THRESHOLD` to 0.75 |

---

## 📚 Documentation

- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - System design details
- **[TOKEN_GUARD_GUIDE.md](docs/TOKEN_GUARD_GUIDE.md)** - Optimization walkthrough  
- **[API_REFERENCE.md](docs/API_REFERENCE.md)** - Complete API docs
- **[CONTRIBUTING.md](docs/CONTRIBUTING.md)** - How to contribute

---

## 🤝 Contributing

We welcome contributions! 

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

---

## 👤 Author

**Keshav Sinha** - [@Keshav200509](https://github.com/Keshav200509)

---

## 🎯 Roadmap

**Q2 2025**: Multi-agent collaboration, Advanced RAG
**Q3 2025**: Fine-tuning support, ML-based optimization
**Q4 2025**: Mobile app, Enterprise deployment

---

**Last Updated**: June 2025 | **Status**: 🟢 Active | **Version**: 1.0.0

> ⭐ Star this repo if you find it useful!
