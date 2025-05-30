from app.agents.legal_agent import LegalExpertAgent
from app.agents.finance_agent import FinanceExpertAgent
from app.agents.medical_agent import MedicalExpertAgent
from app.agents.tools_agent import ToolsAgent

class CoordinatorAgent:
    def __init__(self):
        self.legal_agent = LegalExpertAgent()
        self.finance_agent = FinanceExpertAgent()
        self.medical_agent = MedicalExpertAgent()
        self.tools_agent = ToolsAgent()

    async def handle_query(self, query: str) -> str:
        if any(keyword in query.lower() for keyword in ["contract", "law", "legal"]):
            return await self.legal_agent.respond(query)
        if any(keyword in query.lower() for keyword in ["investment", "tax", "finance"]):
            return await self.finance_agent.respond(query)
        if any(keyword in query.lower() for keyword in ["symptom", "diagnosis", "medical"]):
            return await self.medical_agent.respond(query)
        if any(keyword in query.lower() for keyword in ["calculate", "compute", "python"]):
            return self.tools_agent.execute_tool(query)
        return "Domain not supported yet."