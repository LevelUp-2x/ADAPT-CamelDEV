import pytest
import requests
from flask import json
from unittest.mock import patch

# Assuming these are the correct URLs for our services in the Docker environment
MAIN_APP_URL = "http://main_app:5000"
RAG_SERVICE_URL = "http://rag_service:8001"
GRAPH_RAG_SERVICE_URL = "http://graph_rag_service:8002"
AGENT_MEMORY_SERVICE_URL = "http://agent_memory_service:8003"

@pytest.fixture
def mock_requests():
    with patch('requests.post') as mock_post, patch('requests.get') as mock_get:
        yield mock_post, mock_get

def test_end_to_end_query(mock_requests):
    mock_post, mock_get = mock_requests
    
    # Test document ingestion
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"message": "Document ingested successfully"}
    ingest_data = {"document": "This is a test document about artificial intelligence."}
    ingest_response = requests.post(f"{MAIN_APP_URL}/ingest", json=ingest_data)
    assert ingest_response.status_code == 200

    # Test querying
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "rag_answer": "AI is a field of computer science.",
        "graph_rag_answer": "Artificial Intelligence is a broad field of computer science.",
        "rag_documents": [{"content": "AI document 1"}, {"content": "AI document 2"}],
        "graph_rag_documents": [{"content": "Graph AI document 1"}, {"content": "Graph AI document 2"}]
    }
    query_data = {"query": "What is artificial intelligence?"}
    query_response = requests.post(f"{MAIN_APP_URL}/query", json=query_data)
    assert query_response.status_code == 200
    
    query_result = query_response.json()
    assert "rag_answer" in query_result
    assert "graph_rag_answer" in query_result
    assert "rag_documents" in query_result
    assert "graph_rag_documents" in query_result

    # Test memory storage and retrieval
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "short_term_memory": {"recent_queries": ["What is AI?"]},
        "long_term_memory": {"AI_definition": "Artificial Intelligence is a field of computer science"}
    }
    memory_response = requests.get(f"{MAIN_APP_URL}/get_memory")
    assert memory_response.status_code == 200
    
    memory_result = memory_response.json()
    assert "short_term_memory" in memory_result
    assert "long_term_memory" in memory_result

def test_rag_service_integration(mock_requests):
    mock_post, _ = mock_requests
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "answer": "Machine learning is a subset of AI.",
        "source_documents": [{"content": "ML document 1"}, {"content": "ML document 2"}]
    }
    
    query_data = {"query": "What is machine learning?"}
    response = requests.post(f"{RAG_SERVICE_URL}/query", json=query_data)
    assert response.status_code == 200
    
    result = response.json()
    assert "answer" in result
    assert "source_documents" in result

def test_graph_rag_service_integration(mock_requests):
    mock_post, _ = mock_requests
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "initial_answer": "Deep learning is a subset of machine learning.",
        "graph_enhanced_documents": [{"content": "DL document 1"}, {"content": "DL document 2"}]
    }
    
    query_data = {"query": "Explain deep learning."}
    response = requests.post(f"{GRAPH_RAG_SERVICE_URL}/query", json=query_data)
    assert response.status_code == 200
    
    result = response.json()
    assert "initial_answer" in result
    assert "graph_enhanced_documents" in result

def test_agent_memory_service_integration(mock_requests):
    mock_post, mock_get = mock_requests
    
    # Test storing memory
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"message": "Memory stored successfully"}
    memory_data = {
        "human_input": "What is reinforcement learning?",
        "ai_output": "Reinforcement learning is a type of machine learning..."
    }
    store_response = requests.post(f"{AGENT_MEMORY_SERVICE_URL}/store_memory", json=memory_data)
    assert store_response.status_code == 200

    # Test retrieving memory
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "short_term_memory": {"recent_queries": ["What is reinforcement learning?"]},
        "long_term_memory": {"RL_definition": "Reinforcement learning is a type of machine learning..."}
    }
    retrieve_response = requests.get(f"{AGENT_MEMORY_SERVICE_URL}/retrieve_memory")
    assert retrieve_response.status_code == 200
    
    retrieve_result = retrieve_response.json()
    assert "short_term_memory" in retrieve_result
    assert "long_term_memory" in retrieve_result

    # Test clearing memory
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"message": "Memory cleared successfully"}
    clear_response = requests.post(f"{AGENT_MEMORY_SERVICE_URL}/clear_memory")
    assert clear_response.status_code == 200

def test_error_handling(mock_requests):
    mock_post, _ = mock_requests
    mock_post.return_value.status_code = 500
    mock_post.return_value.json.return_value = {"error": "Internal server error"}

    query_data = {"query": "This query will cause an error"}
    response = requests.post(f"{MAIN_APP_URL}/query", json=query_data)
    assert response.status_code == 500
    assert "error" in response.json()

# Add more integration tests as needed