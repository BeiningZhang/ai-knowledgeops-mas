# AI KnowledgeOps - MAS for Enterprise Knowledge Q&A

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

## Usage
POST to `/query` with JSON:
```json
{"query": "What is the penalty for breach of contract under UK law?"}
```

## Docker
```bash
docker build -t ai-knowledgeops .
docker run -p 8000:8000 -e HF_API_TOKEN=your_token -e HF_API_URL=https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1 ai-knowledgeops
```

## Cloud Deployment
### AWS EC2 (Ubuntu):
```bash
sudo apt update && sudo apt install docker.io
sudo docker run -d -p 80:8000 \
  -e HF_API_TOKEN=your_token \
  -e HF_API_URL=https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1 \
  ai-knowledgeops
```

### Google Cloud Run:
- Build container image:
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT/ai-knowledgeops
```
- Deploy:
```bash
gcloud run deploy ai-knowledgeops \
  --image gcr.io/YOUR_PROJECT/ai-knowledgeops \
  --platform managed --allow-unauthenticated \
  --set-env-vars HF_API_TOKEN=your_token,HF_API_URL=https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1
```

## Notes
- Ensure `data/index.pkl` exists with FAISS index and document list.
- You can modify `scripts/build_index.py` to include your own corpus.
- Uses HuggingFace Inference API with Mistral-7B for response generation.
- Supports basic code execution using Python `eval()` safely.
- Integrated with LangChain for prompt workflows and LLM orchestration.
