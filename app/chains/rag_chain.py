import requests
import os
from app.agents.retrieval_agent import retrieve_docs

class RAGChain:
    def __init__(self):
        self.api_url = os.environ.get("HF_API_URL")
        self.headers = {"Authorization": f"Bearer {os.environ.get('HF_API_TOKEN')}"}

    def retrieve(self, query: str):
        return retrieve_docs(query)

    def generate(self, prompt: str):
        response = requests.post(
            self.api_url,
            headers=self.headers,
            json={"inputs": prompt}
        )
        return response.json()[0]["generated_text"]
