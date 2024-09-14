from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.models.postgres_models import Entity, Relationship
from pydantic import BaseModel
from typing import List, Dict
import networkx as nx

app = FastAPI()

# Initialize a NetworkX graph
G = nx.Graph()

class EntityCreate(BaseModel):
    name: str
    entity_type: str

class EntityResponse(BaseModel):
    id: int
    name: str
    entity_type: str

    class Config:
        orm_mode = True

class RelationshipCreate(BaseModel):
    relationship_type: str
    entity_from_id: int
    entity_to_id: int
    document_id: int

class RelationshipResponse(BaseModel):
    id: int
    relationship_type: str
    entity_from_id: int
    entity_to_id: int
    document_id: int

    class Config:
        orm_mode = True

@app.get("/")
async def root():
    return {"message": "Graph RAG Service"}

@app.post("/entity", response_model=EntityResponse)
async def create_entity(entity: EntityCreate, db: Session = Depends(get_db)):
    db_entity = Entity(**entity.dict())
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    
    # Add node to NetworkX graph
    G.add_node(db_entity.id, name=db_entity.name, entity_type=db_entity.entity_type)
    
    return db_entity

@app.get("/entity/{entity_id}", response_model=EntityResponse)
async def get_entity(entity_id: int, db: Session = Depends(get_db)):
    entity = db.query(Entity).filter(Entity.id == entity_id).first()
    if entity is None:
        raise HTTPException(status_code=404, detail="Entity not found")
    return entity

@app.post("/relationship", response_model=RelationshipResponse)
async def create_relationship(relationship: RelationshipCreate, db: Session = Depends(get_db)):
    db_relationship = Relationship(**relationship.dict())
    db.add(db_relationship)
    db.commit()
    db.refresh(db_relationship)
    
    # Add edge to NetworkX graph
    G.add_edge(db_relationship.entity_from_id, db_relationship.entity_to_id, 
               type=db_relationship.relationship_type, document_id=db_relationship.document_id)
    
    return db_relationship

@app.get("/relationship/{relationship_id}", response_model=RelationshipResponse)
async def get_relationship(relationship_id: int, db: Session = Depends(get_db)):
    relationship = db.query(Relationship).filter(Relationship.id == relationship_id).first()
    if relationship is None:
        raise HTTPException(status_code=404, detail="Relationship not found")
    return relationship

@app.get("/query_graph", response_model=Dict[str, List])
async def query_graph(entity_id: int, max_depth: int = 2):
    if not G.has_node(entity_id):
        raise HTTPException(status_code=404, detail="Entity not found in graph")
    
    # Perform BFS to get subgraph
    subgraph = nx.ego_graph(G, entity_id, radius=max_depth)
    
    # Get all paths from the entity to other nodes in the subgraph
    paths = nx.single_source_shortest_path(subgraph, entity_id)
    
    # Format the result
    result = {
        "nodes": [{"id": n, "name": G.nodes[n].get("name"), "entity_type": G.nodes[n].get("entity_type")} 
                  for n in subgraph.nodes],
        "edges": [{"source": u, "target": v, "type": d.get("type")} 
                  for u, v, d in subgraph.edges(data=True)],
        "paths": [{"target": target, "path": path} for target, path in paths.items() if target != entity_id]
    }
    
    return result

@app.get("/find_shortest_path")
async def find_shortest_path(start_entity_id: int, end_entity_id: int):
    if not G.has_node(start_entity_id) or not G.has_node(end_entity_id):
        raise HTTPException(status_code=404, detail="One or both entities not found in graph")
    
    try:
        path = nx.shortest_path(G, start_entity_id, end_entity_id)
        return {"path": path}
    except nx.NetworkXNoPath:
        return {"message": "No path exists between the given entities"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)