# AI-Enhanced Documentation Generator

An intelligent documentation generator that analyzes **source code**, **Git history**, and optionally **team communication data** to automatically create clean, structured, and AI-generated documentation for software projects.

---

## Features
- **Code Analysis** – Extracts functions, classes, and structure from code files.
- **Git History Insight** – Summarizes recent commit messages for context.
- **AI Summarization** – Uses NLP models (BART / Transformer pipelines) to generate clear summaries.
- **Organized Output** – Generates markdown documentation stored in `/output/data/documentation.md`.
- **Framework Ready** – Can be extended with NLP, embeddings, or vector databases later.

---

## Tech Stack
- **Language** : Python
- **Libraries** : Transformers, Torch, GitPython, Regex, JSON
- **AI Model** : facebook/bart-large-cnn (for summarization)
- **Optional Frontend** : Streamlit (for web app version)
