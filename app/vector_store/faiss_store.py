import faiss
import numpy as np
import pickle

# Dummy placeholder, in real case use persistent storage
with open("data/index.pkl", "rb") as f:
    index, docs = pickle.load(f)

def search_documents(embedding: np.ndarray, k: int = 3):
    _, I = index.search(np.array([embedding]), k)
    return [docs[i] for i in I[0]]