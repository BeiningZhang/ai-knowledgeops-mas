import os

from langchain.chains.router import MultiRouteChain, RouterChain
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub

from app.agents.general_agent import GeneralAgent
from app.agents.legal_agent import LegalExpertAgent
from app.agents.finance_agent import FinanceExpertAgent
from app.agents.medical_agent import MedicalExpertAgent
from app.agents.tools_agent import ToolsAgent

from app.chains.adapters.async_agent_chain_adapter import AsyncAgentChainAdapter
from app.utils.prompt_templates import router_template

general_agent = GeneralAgent()
legal_agent = LegalExpertAgent()
finance_agent = FinanceExpertAgent()
medical_agent = MedicalExpertAgent()
tools_agent = ToolsAgent()
default_chain = AsyncAgentChainAdapter(general_agent)

router_prompt = PromptTemplate.from_template(router_template)

class RouterAgent:
    def __init__(self):
        self.llm = HuggingFaceHub(
            repo_id = "mistralai/Mistral-7B-Instruct-v0.1",
            huggingfacehub_api_token = os.environ.get("HF_API_TOKEN")
        )

        self.router_chain = RouterChain.from_llm(self.llm, router_prompt)

        self.multi_route_chain = MultiRouteChain(
            router_chain = self.router_chain,
            destination_chains = {
                "legal": legal_agent,
                "finance": finance_agent,
                "medical": medical_agent,
                "tools": tools_agent,
                "general": general_agent
            },
            default_chain = default_chain
        )

    async def handle_query(self, query: str) -> str:
        result = await self.multi_route_chain.arun({"input": query})
        return result