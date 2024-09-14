from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.models.postgres_models import Document
from pydantic import BaseModel
from typing import Dict, List
import time

app = FastAPI()

# In-memory storage for short-term memory
short_term_memory: Dict[str, Dict] = {}

class MemoryItem(BaseModel):
    content: str
    timestamp: float = None

class LongTermMemoryCreate(BaseModel):
    title: str
    content: str

class LongTermMemoryResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True

@app.get("/")
async def root():
    return {"message": "Agent Memory Service"}

@app.post("/store_short_term")
async def store_short_term_memory(key: str, item: MemoryItem):
    item.timestamp = time.time()
    short_term_memory[key] = item.dict()
    return {"message": "Short-term memory stored successfully"}

@app.get("/retrieve_short_term/{key}", response_model=MemoryItem)
async def retrieve_short_term_memory(key: str):
    if key not in short_term_memory:
        raise HTTPException(status_code=404, detail="Memory item not found")
    return short_term_memory[key]

@app.post("/store_long_term", response_model=LongTermMemoryResponse)
async def store_long_term_memory(memory: LongTermMemoryCreate, db: Session = Depends(get_db)):
    db_memory = Document(**memory.dict())
    db.add(db_memory)
    db.commit()
    db.refresh(db_memory)
    return db_memory

@app.get("/retrieve_long_term/{memory_id}", response_model=LongTermMemoryResponse)
async def retrieve_long_term_memory(memory_id: int, db: Session = Depends(get_db)):
    memory = db.query(Document).filter(Document.id == memory_id).first()
    if memory is None:
        raise HTTPException(status_code=404, detail="Memory not found")
    return memory

@app.post("/consolidate_memory")
async def consolidate_memory(db: Session = Depends(get_db)):
    # Simple consolidation: move all short-term memories to long-term storage
    for key, item in short_term_memory.items():
        db_memory = Document(title=key, content=item['content'])
        db.add(db_memory)
    
    db.commit()
    short_term_memory.clear()
    
    return {"message": "Memory consolidated successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)