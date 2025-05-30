from app.embeddings.embedder import get_embedding
from app.vector_store.faiss_store import search_documents

def retrieve_docs(query: str, k: int = 3):
    query_emb = get_embedding(query)
    return search_documents(query_emb, k)