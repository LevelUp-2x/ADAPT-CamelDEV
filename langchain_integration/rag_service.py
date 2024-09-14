from flask import Flask, request, jsonify
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
import logging
from logging.handlers import RotatingFileHandler
import os
from service_discovery import ServiceDiscovery
from config import get_config
import threading
import time

app = Flask(__name__)

# Configure logging
handler = RotatingFileHandler('rag_service.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# Initialize service discovery
sd = ServiceDiscovery()
SERVICE_NAME = 'rag_service'
SERVICE_HOST = '0.0.0.0'
SERVICE_PORT = get_config('RAG_SERVICE_PORT')

# Initialize components
try:
    embeddings = HuggingFaceEmbeddings()
    vector_store = FAISS.from_texts([""], embeddings)
    
    # Initialize language model
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = get_config('HUGGINGFACEHUB_API_TOKEN')
    llm = HuggingFaceHub(repo_id="google/flan-t5-base", model_kwargs={"temperature": 0.5, "max_length": 512})
    
    # Initialize RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )
    
    app.logger.info("Embeddings, vector store, and QA chain initialized successfully")
except Exception as e:
    app.logger.error(f"Error initializing components: {str(e)}")
    raise

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query_text = data.get('query')
    
    app.logger.info(f"Received query: {query_text}")
    
    try:
        # Use the QA chain to get the answer
        result = qa_chain({"query": query_text})
        
        answer = result['result']
        source_docs = result['source_documents']
        
        # Format the results
        formatted_docs = [{"content": doc.page_content, "metadata": doc.metadata} for doc in source_docs]
        
        response = {
            "answer": answer,
            "source_documents": formatted_docs
        }
        
        app.logger.info(f"Query processed successfully")
        return jsonify(response)
    except Exception as e:
        app.logger.error(f"Error processing query: {str(e)}")
        return jsonify({"error": "An error occurred while processing your query"}), 500

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.json
    document = data.get('document')
    
    app.logger.info("Received document for ingestion")
    
    try:
        # Split the document into chunks
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_text(document)
        
        # Add the chunks to the vector store
        vector_store.add_texts(texts)
        
        app.logger.info(f"Ingested {len(texts)} document chunks successfully")
        return jsonify({"message": f"Ingested {len(texts)} document chunks"})
    except Exception as e:
        app.logger.error(f"Error ingesting document: {str(e)}")
        return jsonify({"error": "An error occurred while ingesting the document"}), 500

def heartbeat():
    while True:
        sd.heartbeat(SERVICE_NAME, SERVICE_HOST, SERVICE_PORT)
        time.sleep(10)  # Send heartbeat every 10 seconds

if __name__ == '__main__':
    # Register service
    sd.register_service(SERVICE_NAME, SERVICE_HOST, SERVICE_PORT)
    
    # Start heartbeat thread
    threading.Thread(target=heartbeat, daemon=True).start()
    
    app.run(host=SERVICE_HOST, port=SERVICE_PORT, debug=get_config('DEBUG'))

    # Deregister service on shutdown
    sd.deregister_service(SERVICE_NAME)