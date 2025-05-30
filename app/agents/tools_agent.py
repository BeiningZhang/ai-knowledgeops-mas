from langchain.agents import initialize_agent, AgentType
from langchain.llms import HuggingFaceHub
from langchain.tools import tool
import os

@tool
def python_eval(code: str) -> str:
    try:
        return str(eval(code))
    except Exception as e:
        return f"Error: {e}"

@tool
def web_search(query: str) -> str:
    return f"Pretend this is a search result for: '{query}'"

class ToolsAgent:
    def __init__(self):
        self.llm = HuggingFaceHub(
            repo_id="mistralai/Mistral-7B-Instruct-v0.1",
            huggingfacehub_api_token=os.environ.get("HF_API_TOKEN")
        )
        self.agent = initialize_agent(
            tools=[python_eval, web_search],
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )

    def execute_tool(self, query: str) -> str:
        return self.agent.run(query)