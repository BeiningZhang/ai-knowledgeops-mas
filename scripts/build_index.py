import faiss
import os
import pickle
import numpy as np
from app.vector_store.faiss_store import FaissStore
from app.embeddings.embedder import get_embedding

# Replace with your corpus
documents = [
    "A breach of contract occurs when one party fails to meet their obligations.",
    "UK law requires all contracts over £500 to be in writing.",
    "Non-disclosure agreements protect sensitive company information."
]

embeddings = [get_embedding(doc) for doc in documents]
store = FaissStore(dim=len(embeddings[0]))
store.add(embeddings, documents)
store.save()
print("Index built and saved to data/index.pkl")