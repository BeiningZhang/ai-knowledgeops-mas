import faiss
import os
import pickle
import numpy as np
from app.embeddings.embedder import get_embedding

# Replace with your corpus
documents = [
    "A breach of contract occurs when one party fails to meet their obligations.",
    "UK law requires all contracts over £500 to be in writing.",
    "Non-disclosure agreements protect sensitive company information."
]

embeddings = [get_embedding(doc) for doc in documents]
index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))

os.makedirs("data", exist_ok=True)
with open("data/index.pkl", "wb") as f:
    pickle.dump((index, documents), f)

print("Index built and saved to data/index.pkl")
