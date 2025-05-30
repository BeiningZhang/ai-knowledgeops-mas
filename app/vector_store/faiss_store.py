import faiss
import numpy as np
import pickle
import os

class FaissStore:
    def __init__(self, dim: int, path: str = "data/index.pkl"):
        self.index = faiss.IndexFlatL2(dim)
        self.docs = []
        self.path = path

    def search_documents(self, embedding: np.ndarray, k: int = 3):
        _, I = self.index.search(np.array([embedding]), k)
        return [self.docs[i] for i in I[0]]

    def add(self, vectors, documents):
        self.index.add(np.array(vectors))
        self.docs.extend(documents)

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "wb") as f:
            pickle.dump((self.index, self.docs), f)

    def load(self):
        with open(self.path, "rb") as f:
            self.index, self.docs = pickle.load(f)