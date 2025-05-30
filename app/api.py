from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.agents.coordinator import CoordinatorAgent

app = FastAPI()
coordinator = CoordinatorAgent()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_endpoint(req: QueryRequest):
    result = await coordinator.handle_query(req.query)
    return {"response": result}