# Resume Advisor (Multi-Agent RAG Project)

This is a beginner-friendly AI agents project using a custom message-passing protocol (ACP style).

## What It Does

- Takes a resume and job description
- Parses the skills and compares them using embeddings
- Gives a match score
- Suggests improvements

## Agents

- User Input Agent
- Resume Parser Agent
- JD Parser Agent
- Scoring Agent
- Improvement Advisor Agent

## Requirements

Place the resume.pdf into the /data directory and the jd.txt in the /data/job_descriptions directory

Download the phi-2.Q4_K_M.gguf llama model and place in /models/phi-2.Q4_K_M.gguf directory

Install all required python dependencies

Run:
```bash
python -m spacy download en_core_web_sm
```

## Tech/Libraries Used

### spaCy
spaCy is a popular open-source Python library for Natural Language Processing (NLP).
It helps with:
- Tokenization (splitting text into words, punctuation, etc.)
- Part-of-speech tagging (e.g., NOUN, VERB, etc.)
- Named Entity Recognition (NER)
- Dependency parsing
- Pattern matching
- Lemmatization (reducing words to their root form)

### Llama cpp
llama.cpp is a high-performance C++ implementation that lets you run LLaMA-family large language models locally — on your CPU, GPU, or even mobile devices — without needing the internet, cloud APIs, or a GPU.
It’s the engine behind many local, private AI chat setups (like Ollama, LM Studio, etc.).

Stores quantized weights and tokenizer info as a .gguf file.