## AI KnowledgeOps MAS – System Architecture & Project Plan

### Overview

AI KnowledgeOps MAS is a modular, containerised multi-agent system (MAS) designed to support Retrieval-Augmented Generation (RAG) for enterprise knowledge management. It leverages LangChain for workflow orchestration, HuggingFace Inference API for LLM interaction (Mistral-7B), and FAISS for semantic search.

---

### Key Capabilities

* Multi-agent architecture with domain-specific agents (Legal, Finance, Medical, Tools)
* Retrieval-Augmented Generation (RAG) pipeline
* LangChain for prompt templating, memory, and agent control
* Mistral-7B via HuggingFace Inference API
* Support for code execution and simulated web search
* Memory-enabled conversational agents
* Dockerised for local and cloud deployment (AWS/GCP)

---

### System Architecture

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
|   Coordinator Agent   | -- Routes based on query intent
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

### Project Structure

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

### Deployment Options

**Docker**

```bash
docker build -t ai-knowledgeops .
docker run -p 8000:8000 \
  -e HF_API_TOKEN=your_token \
  -e HF_API_URL=https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1 \
  ai-knowledgeops
```

**AWS EC2**

```bash
sudo apt update && sudo apt install docker.io
docker run -d -p 80:8000 \
  -e HF_API_TOKEN=your_token \
  -e HF_API_URL=https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1 \
  ai-knowledgeops
```

**Google Cloud Run**

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT/ai-knowledgeops
gcloud run deploy ai-knowledgeops \
  --image gcr.io/YOUR_PROJECT/ai-knowledgeops \
  --platform managed --allow-unauthenticated \
  --set-env-vars HF_API_TOKEN=your_token,HF_API_URL=https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1
```

---

### Next Development Goals

1. **Fine-tuning per domain**

   * Use domain-specific open datasets (PubMed, SEC filings, case law, etc.)
   * LoRA or QLoRA adaptation for Mistral-7B

2. **Expand tool integration**

   * Integrate real-time APIs (e.g. SerpAPI, WolframAlpha, PDF parsers)

3. **Memory enhancement**

   * Multi-turn memory using LangChain’s conversation memory modules

4. **Realtime Indexing**

   * Add pipelines for live ingestion and re-indexing of new documents

5. **Frontend UI**

   * React or Streamlit-based interface for querying and interacting with agents

---

### Contact

Project maintained internally. For feedback or collaboration, please reach out through the development team channel.
