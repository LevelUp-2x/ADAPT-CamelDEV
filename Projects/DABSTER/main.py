from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
from typing import List, Dict

app = FastAPI()

class Document(BaseModel):
    title: str
    content: str
    entities: List[str] = []

class Query(BaseModel):
    text: str

class GraphQuery(BaseModel):
    entity_id: int
    max_depth: int = 2

@app.get("/")
async def root():
    return {"message": "Welcome to DABSTER - Database-Augmented Boosted System for Tracking, Engaging, and Retrieving"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/process_document")
async def process_document(document: Document):
    async with httpx.AsyncClient() as client:
        # Ingest document
        rag_response = await client.post("http://localhost:8001/ingest", json=document.dict())
        if rag_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to ingest document")
        
        doc_data = rag_response.json()
        
        # Create entities and relationships
        for entity_name in document.entities:
            entity_response = await client.post("http://localhost:8002/entity", 
                                                json={"name": entity_name, "entity_type": "general"})
            if entity_response.status_code != 200:
                continue
            
            entity_data = entity_response.json()
            
            # Create relationship between document and entity
            await client.post("http://localhost:8002/relationship", 
                              json={"relationship_type": "contains",
                                    "entity_from_id": doc_data["id"],
                                    "entity_to_id": entity_data["id"],
                                    "document_id": doc_data["id"]})
        
        # Store in long-term memory
        await client.post("http://localhost:8003/store_long_term", 
                          json={"title": document.title, "content": document.content})
    
    return {"message": "Document processed successfully"}

@app.post("/query")
async def query(query: Query):
    async with httpx.AsyncClient() as client:
        # Search documents using RAG
        search_response = await client.get(f"http://localhost:8001/search?query={query.text}")
        if search_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to search documents")
        
        documents = search_response.json()
        
        # Query graph for related entities
        graph_queries = []
        for doc in documents:
            graph_query = GraphQuery(entity_id=doc['id'])
            graph_response = await client.get(f"http://localhost:8002/query_graph", params=graph_query.dict())
            if graph_response.status_code == 200:
                graph_queries.append(graph_response.json())
        
        # Store query in short-term memory
        await client.post("http://localhost:8003/store_short_term", 
                          params={"key": "last_query"},
                          json={"content": query.text})
    
    return {"documents": documents, "graph_queries": graph_queries}

@app.post("/find_connections")
async def find_connections(start_entity_id: int, end_entity_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8002/find_shortest_path?start_entity_id={start_entity_id}&end_entity_id={end_entity_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to find connections")
        
        return response.json()

@app.post("/consolidate_memory")
async def consolidate_memory():
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8003/consolidate_memory")
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to consolidate memory")
    
    return {"message": "Memory consolidated successfully"}

@app.post("/load_langchain_docs")
async def load_langchain_docs():
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8001/load_langchain_docs")
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to load LangChain docs")
    
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)