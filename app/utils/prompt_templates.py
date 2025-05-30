def legal_template(query: str, docs: list[str]) -> str:
    context = "\n\n".join(docs)
    return f"""
Context:
{context}

User Query: {query}

Answer the question based on the context. If unsure, say you don't know.
"""
