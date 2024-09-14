from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

SERVICE_URLS = {
    "rag": "http://localhost:8001",
    "graph_rag": "http://localhost:8002",
    "agent_memory": "http://localhost:8003",
}

@app.get("/")
async def root():
    return {"message": "DABSTER API Gateway"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def api_gateway(service: str, path: str):
    if service not in SERVICE_URLS:
        raise HTTPException(status_code=404, detail=f"Service '{service}' not found")
    
    target_url = f"{SERVICE_URLS[service]}/{path}"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method=httpx.get_method(),
                url=target_url,
                headers=httpx.get_headers(),
                params=httpx.get_query_params(),
                data=httpx.get_body(),
            )
            return JSONResponse(content=response.json(), status_code=response.status_code)
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail="Error communicating with the service")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)