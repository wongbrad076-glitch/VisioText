import os
import zipfile

# Project structure and file contents
project_name = "conversation-analyzer"
files = {
    f"{project_name}/requirements.txt": """fastapi==0.111.1
uvicorn==0.25.0
pydantic==2.6.2
""",
    f"{project_name}/README.md": """# Conversation Analyzer API

A FastAPI service to analyze conversations for emotional patterns, speaker behavior, and reply suggestions.

## Endpoints

- `GET /healthz` - Health check
- `POST /analyze` - Analyze conversation text

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload