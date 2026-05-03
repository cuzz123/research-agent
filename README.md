# 📊 Multi-Agent Research Assistant

> Automatically decompose research topics, search real data, and generate structured Markdown reports.
> Built with LangChain, Tavily API, and FastAPI.

## ✨ Features

- **Auto Decomposition** — LLM splits a broad topic into 3-5 sub-questions
- **Real Search** — Tavily API for real-time data retrieval
- **AI Analysis** — Extracts key findings from search results
- **Report Generation** — Writes structured Markdown reports
- **REST API** — FastAPI endpoint for HTTP access

## 🏗️ Architecture

```
Supervisor → Decompose topic → Sub-questions
                                  ↓
Searcher → Tavily API → Raw search results
                                  ↓
Analyzer → LLM extracts → Structured Findings
                                  ↓
Writer → LLM composes → Markdown Report
```

## 🚀 Quick Start

```bash
git clone https://github.com/cuzz123/research-agent.git
cd research-agent

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Set API keys
echo "DEEPSEEK_API_KEY=sk-your-key" >> .env
echo "TAVILY_API_KEY=tvly-your-key" >> .env

# CLI mode
python main.py

# API mode
uvicorn app:app --reload --port 8000
```

## 🔧 API

```bash
curl -X POST http://localhost:8000/research \
  -H "Content-Type: application/json" \
  -d '{"topic": "AI Agent development in 2025"}'
```

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Agent Orchestration | LangChain Supervisor-Worker |
| Search | Tavily API |
| LLM | DeepSeek Chat |
| Backend | FastAPI |
| Data Models | Pydantic |

## 📁 Project Structure

```
research-agent/
├── agent/
│   ├── supervisor.py   # Decompose topic
│   ├── searcher.py     # Search tool wrapper
│   ├── analyzer.py     # Extract findings
│   └── writer.py       # Generate report
├── models/
│   └── schemas.py      # Pydantic models
├── tools/
│   └── search_tool.py  # Tavily integration
├── main.py             # CLI entry
├── app.py              # FastAPI entry
└── requirements.txt
```

## 📝 License

MIT
