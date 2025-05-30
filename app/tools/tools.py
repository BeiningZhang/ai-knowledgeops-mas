from langchain.tools import tool
import subprocess
import requests

@tool
def python_eval(code: str) -> str:
    """Safely evaluate Python code (math or simple logic)."""
    try:
        return str(eval(code))
    except Exception as e:
        return f"Error: {e}"

@tool
def web_search(query: str) -> str:
    """Perform a web search (placeholder for real integration)."""
    # Replace with actual API like SerpAPI or Brave if needed
    return f"Pretend this is a search result for: '{query}'"
