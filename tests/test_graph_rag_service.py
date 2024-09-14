import pytest
from flask import json
from ADAPT-CamelDEV-Project.langchain_integration.graph_rag_service import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert json.loads(response.data) == {"status": "healthy"}

def test_query_route(client):
    test_query = {"query": "test query"}
    response = client.post('/query', json=test_query)
    assert response.status_code == 200
    # Add more specific assertions based on the expected response structure
    assert "initial_answer" in json.loads(response.data)
    assert "graph_enhanced_documents" in json.loads(response.data)

def test_ingest_route(client):
    test_document = {"document": "This is a test document."}
    response = client.post('/ingest', json=test_document)
    assert response.status_code == 200
    assert "message" in json.loads(response.data)
    assert "Ingested" in json.loads(response.data)["message"]
    assert "updated the graph" in json.loads(response.data)["message"]

# Add more tests as needed for the Graph RAG service functionality
def test_get_subgraph(client):
    # This test might need to be adjusted based on how you expose the get_subgraph functionality
    # You might need to add a new route to test this function or test it indirectly through other routes
    pass