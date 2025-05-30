def legal_template(query: str, docs: list[str]) -> str:
    context = "\n\n".join(docs)
    return f"""
Context:
{context}

User Query: {query}

Answer the question based on the context. If unsure, say you don't know.
"""

# Router Chain Template
router_template = """
You are a smart router that decides which domain expert should handle a user query.

Domains:
- legal: law, contracts, legal advice
- finance: investment, taxes, financial questions
- medical: symptoms, health, treatment
- tools: calculations, code, utilities
- general: anything else not covered above

Return only the name of the appropriate domain: one of [legal, finance, medical, tools].

Query: {input}
Domain:
"""

# Finance Expert Agent Template
finance_template = """
Context:
{context}

User Query: {query}

Provide a finance-specific answer using the provided context.
"""

# Legal Expert Agent Template
legal_template = """
Context:
{context}

Chat History:
{chat_history}

User Query: {query}

Answer the question based on the context and conversation history.
"""

# Medical Expert Agent Template
medical_template = """
Context:
{context}

User Query: {query}

Provide a medical-specific answer using the provided context.
"""

# General Purpose Assistant Template
general_template = """
You are a helpful general-purpose assistant. Please answer the following question clearly and concisely:
Query: {query}
"""