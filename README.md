# Resume Advisor (Multi-Agent RAG Project)

This is a beginner-friendly AI agents project using a custom message-passing protocol (ACP style).

## What It Does

- Takes a resume and job description
- Parses and compares them using embeddings
- Gives a match score
- Suggests improvements

## Agents

- User Input Agent
- Resume Extractor Agent
- JD Extractor Agent
- Scoring Agent
- Improvement Advisor Agent

## Requirements

```bash
pip install PyPDF2 sentence-transformers numpy