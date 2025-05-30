from app.agents.base_agent import BaseAgent
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
import os
from app.utils.prompt_templates import general_template

class GeneralAgent(BaseAgent):
    def __init__(self):
        self.llm = HuggingFaceHub(
            repo_id="mistralai/Mistral-7B-Instruct-v0.1",
            huggingfacehub_api_token=os.environ.get("HF_API_TOKEN")
        )
        self.prompt_template = PromptTemplate(
            input_variables=["query"],
            template=general_template
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)

    async def respond(self, query: str) -> str:
        return self.chain.run({"query": query})