from fastapi import FastAPI
from pydantic import BaseModel
from app.chains.router_chain import RouterAgent

app = FastAPI()
router_agent = RouterAgent()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_endpoint(req: QueryRequest):
    result = await router_agent.handle_query(req.query)
    return {"response": result}