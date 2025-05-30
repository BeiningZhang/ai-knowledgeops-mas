from app.agents.base_agent import BaseAgent
from app.chains.rag_chain import RAGChain
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
import os
from app.utils.prompt_templates import finance_template


class FinanceExpertAgent(BaseAgent):
    def __init__(self):
        self.rag_chain = RAGChain()
        self.llm = HuggingFaceHub(
            repo_id = "mistralai/Mistral-7B-Instruct-v0.1",
            huggingfacehub_api_token = os.environ.get("HF_API_TOKEN")
        )
        self.prompt_template = PromptTemplate(
            input_variables = ["context", "query"],
            template = finance_template
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)

    async def respond(self, query: str) -> str:
        docs = self.rag_chain.retrieve(query)
        context = "\n\n".join(docs)
        return self.chain.run({"context": context, "query": query})