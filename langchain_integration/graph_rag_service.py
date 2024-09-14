from flask import Flask, request, jsonify
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import logging
from logging.handlers import RotatingFileHandler
import os
from service_discovery import ServiceDiscovery
from config import get_config
import threading
import time

app = Flask(__name__)

# Configure logging
handler = RotatingFileHandler('graph_rag_service.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# Initialize service discovery
sd = ServiceDiscovery()
SERVICE_NAME = 'graph_rag_service'
SERVICE_HOST = '0.0.0.0'
SERVICE_PORT = get_config('GRAPH_RAG_SERVICE_PORT')

try:
    # Initialize embeddings and vector store
    embeddings = HuggingFaceEmbeddings()
    vector_store = FAISS.from_texts([""], embeddings)

    # Initialize graph
    G = nx.Graph()

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

    app.logger.info("Embeddings, vector store, graph, and QA chain initialized successfully")
except Exception as e:
    app.logger.error(f"Error initializing components: {str(e)}")
    raise

def get_subgraph(G, center_node, max_depth=2):
    subgraph = nx.ego_graph(G, center_node, radius=max_depth)
    return subgraph

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query_text = data.get('query')
    
    app.logger.info(f"Received query: {query_text}")
    
    try:
        # Use the QA chain to get the initial answer and relevant documents
        result = qa_chain({"query": query_text})
        
        initial_answer = result['result']
        source_docs = result['source_documents']
        
        # Get related nodes from the graph
        related_nodes = set()
        for doc in source_docs:
            doc_id = doc.metadata.get('id')
            if doc_id in G:
                subgraph = get_subgraph(G, doc_id)
                related_nodes.update(subgraph.nodes())
        
        # Retrieve documents for related nodes
        related_docs = [vector_store.docstore.search(node) for node in related_nodes if node in vector_store.docstore.docstore]
        
        # Combine and rank results
        all_docs = source_docs + related_docs
        query_embedding = embeddings.embed_query(query_text)
        all_embeddings = [embeddings.embed_query(doc.page_content) for doc in all_docs]
        similarities = cosine_similarity([query_embedding], all_embeddings)[0]
        
        ranked_results = sorted(zip(all_docs, similarities), key=lambda x: x[1], reverse=True)
        
        top_docs = ranked_results[:5]
        
        # Format the results
        formatted_docs = [{"content": doc.page_content, "metadata": doc.metadata, "similarity": float(sim)} 
                          for doc, sim in top_docs]
        
        response = {
            "initial_answer": initial_answer,
            "graph_enhanced_documents": formatted_docs
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
        doc_ids = vector_store.add_texts(texts)
        
        # Add nodes and edges to the graph
        for i, doc_id in enumerate(doc_ids):
            G.add_node(doc_id, content=texts[i])
            if i > 0:
                G.add_edge(doc_ids[i-1], doc_id)
        
        app.logger.info(f"Ingested {len(texts)} document chunks and updated the graph")
        return jsonify({"message": f"Ingested {len(texts)} document chunks and updated the graph"})
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