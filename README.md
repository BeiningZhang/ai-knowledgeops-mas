# AI KnowledgeOps MAS – Enterprise Knowledge Q\&A System

## Overview

**AI KnowledgeOps MAS** is a modular, containerised multi-agent system (MAS) built to support Retrieval-Augmented Generation (RAG) for enterprise-level knowledge management. The system integrates LangChain for workflow orchestration, Mistral-7B via HuggingFace Inference API for LLM-based interaction, and FAISS for high-performance semantic search.

It is designed with a microservice approach to handle domain-specific queries through dedicated agents, enabling robust, context-aware responses for legal, finance, medical, and technical domains.

---

## Key Capabilities

* Multi-agent architecture with domain-specific agents: Legal, Finance, Medical, Tools
* Retrieval-Augmented Generation (RAG) pipeline
* LangChain for prompt templating, memory, and control
* Mistral-7B model via HuggingFace Inference API
* Support for code execution and simulated web search
* Conversational memory for contextual follow-ups
* Fully dockerised for local or cloud deployment (AWS/GCP)

---

## System Architecture

```plaintext
+-----------------------+
|      User Query       |
+----------+------------+
           |
           v
+-----------------------+
|   FastAPI Web Server  |
+----------+------------+
           |
           v
+-----------------------+
|      Router Agent     | -- Routes based on query intent
+-----------------------+
  |      |         |         |
  v      v         v         v
Legal  Finance   Medical   Tools
Agent   Agent     Agent     Agent
  |       |         |         |
  |       |         |         +-------------------------------+
  |       |         |                                         |
  |       |         |         +-----------------------------+ |
  |       |         |         |       Tools Integration     | |
  |       |         |         |  - Python `eval()`          | |
  |       |         |         |  - Simulated Web Search     | |
  |       |         |         +-----------------------------+ |
  |       |         |                                         |
  |       |         |<----------------------------------------+
  |       |         |
  v       v         v
RAGChain (LangChain LLMChain + Prompt + Memory)
  |
  v
+---------------------------+
|  FAISS Index + Retriever  |
+---------------------------+
  |
  v
+----------------------------+
| HuggingFace Mistral-7B LLM |
+----------------------------+
```

---

## Project Structure

```bash
ai_knowledgeops_mas/
│
├── app/
│   ├── api.py
│   ├── agents/
│   │   ├── base_agent.py
│   │   ├── coordinator.py
│   │   ├── finance_agent.py
│   │   ├── legal_agent.py
│   │   ├── medical_agent.py
│   │   ├── retrieval_agent.py
│   │   └── tools_agent.py
│   ├── chains/
│   │   └── rag_chain.py
│   ├── embeddings/
│   │   └── embedder.py
│   ├── tools/
│   │   └── tools.py
│   ├── utils/
│   │   └── prompt_templates.py
│   └── vector_store/
│       └── faiss_store.py
│
├── data/
│   └── index.pkl
│
├── scripts/
│   ├── build_index.py
│   └── architecture_overview.md
│
├── Dockerfile
├── project_description.md
├── README.md
└── requirements.txt
```

---

## Setup

```bash
git clone https://github.com/your-org/ai-knowledgeops.git
cd ai-knowledgeops
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python scripts/build_index.py
uvicorn app.api:app --reload
```

---

## Usage

To query the system, POST to `/query` with JSON:

```json
{"query": "What is the penalty for breach of contract under UK law?"}
```

---

## Deployment Options

### Docker

```bash
docker build -t ai-knowledgeops-mas .
docker run -p 8000:8000 \
  -e HF_API_TOKEN=your_token \
  -e HF_API_URL=https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1 \
  ai-knowledgeops-mas
```

### AWS EC2

```bash
sudo apt update && sudo apt install docker.io
docker run -d -p 80:8000 \
  -e HF_API_TOKEN=your_token \
  -e HF_API_URL=https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1 \
  ai-knowledgeops-mas
```

### Google Cloud Run

* Build container image:

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT/ai-knowledgeops-mas
```

* Deploy:

```bash
gcloud run deploy ai-knowledgeops-mas \
  --image gcr.io/YOUR_PROJECT/ai-knowledgeops-mas \
  --platform managed --allow-unauthenticated \
  --set-env-vars HF_API_TOKEN=your_token,HF_API_URL=https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1
```

---

## Notes

* Ensure `data/index.pkl` exists. You can rebuild it with your corpus using `scripts/build_index.py`.
* The system uses LangChain for workflow orchestration and prompt chaining.
* Mistral-7B LLM is accessed through HuggingFace's Inference API.
* Python `eval()` is sandboxed for lightweight code execution.
* Simulated web search capabilities are included in the Tools Agent.

---

## Roadmap / Next Development Goals

1. **Domain-specific Fine-tuning**

   * Leverage datasets like PubMed, SEC filings, or case law
   * Use LoRA/QLoRA to fine-tune Mistral-7B on specialised corpora

2. **Tooling Enhancements**

   * Real-time APIs: SerpAPI, WolframAlpha, PDF readers, etc.

3. **Memory Improvements**

   * Enable multi-turn memory via LangChain’s memory modules

4. **Realtime Indexing**

   * Automate ingestion and re-indexing of documents as they change

5. **Frontend UI**

   * Build a React or Streamlit interface for interactive querying
