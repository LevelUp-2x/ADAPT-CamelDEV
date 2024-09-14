from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.models.postgres_models import Document, Entity
from pydantic import BaseModel
from typing import List
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document as LangchainDocument
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

app = FastAPI()

# Initialize HuggingFace embeddings
embeddings = HuggingFaceEmbeddings()

# Initialize FAISS vector store
vector_store = FAISS.from_texts([""], embeddings)

class DocumentCreate(BaseModel):
    title: str
    content: str
    entities: List[str] = []

class DocumentResponse(BaseModel):
    id: int
    title: str
    content: str
    entities: List[str]

    class Config:
        orm_mode = True

@app.get("/")
async def root():
    return {"message": "RAG Service"}

@app.post("/ingest", response_model=DocumentResponse)
async def ingest_document(document: DocumentCreate, db: Session = Depends(get_db)):
    # Create database entry
    db_document = Document(title=document.title, content=document.content)
    
    for entity_name in document.entities:
        entity = db.query(Entity).filter(Entity.name == entity_name).first()
        if not entity:
            entity = Entity(name=entity_name)
        db_document.entities.append(entity)
    
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    
    # Add document to vector store
    langchain_doc = LangchainDocument(page_content=document.content, metadata={"title": document.title, "id": db_document.id})
    vector_store.add_documents([langchain_doc])
    
    return db_document

@app.get("/retrieve/{document_id}", response_model=DocumentResponse)
async def retrieve_document(document_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == document_id).first()
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@app.get("/search", response_model=List[DocumentResponse])
async def search_documents(query: str, db: Session = Depends(get_db)):
    # Perform similarity search using FAISS
    similar_docs = vector_store.similarity_search(query, k=5)
    
    # Retrieve full documents from database
    doc_ids = [doc.metadata["id"] for doc in similar_docs]
    documents = db.query(Document).filter(Document.id.in_(doc_ids)).all()
    
    return documents

@app.post("/load_langchain_docs")
async def load_langchain_docs():
    docs_path = "C:\\Users\\ChaseRemmen\\ADAPT\\ADAPT-CamelDEV\\LangChain_Docs"
    loader = DirectoryLoader(docs_path, glob="**/*.md")
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    
    global vector_store
    vector_store = FAISS.from_documents(texts, embeddings)
    
    return {"message": f"Loaded and indexed {len(texts)} document chunks from LangChain docs"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)