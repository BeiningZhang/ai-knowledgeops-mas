from typing import List, Dict
from langchain.chains.base import Chain
from app.agents.base_agent import BaseAgent

class AsyncAgentChainAdapter(Chain):
    def __init__(self, agent: BaseAgent):
        self.agent = agent

    @property
    def input_keys(self) -> List[str]:
        return ["input"]

    @property
    def output_keys(self) -> List[str]:
        return ["output"]

    async def _acall(self, inputs: Dict[str, str], run_manager=None) -> Dict[str, str]:
        result = await self.agent.respond(inputs["input"])
        return {"output": result}

    def _call(self, inputs: Dict[str, str], run_manager=None) -> Dict[str, str]:
        raise NotImplementedError("Use the async version with 'acall'.")