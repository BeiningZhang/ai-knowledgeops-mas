from abc import ABC, abstractmethod

class BaseAgent(ABC):
    @abstractmethod
    async def respond(self, query: str) -> str:
        pass