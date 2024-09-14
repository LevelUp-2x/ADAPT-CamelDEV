import pytest
from flask import json
from unittest.mock import patch, MagicMock
from ADAPT-CamelDEV-Project.langchain_integration.agent_memory_service import app, short_term_memory, long_term_memory

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert json.loads(response.data) == {"status": "healthy"}

@patch('ADAPT-CamelDEV-Project.langchain_integration.agent_memory_service.short_term_memory')
@patch('ADAPT-CamelDEV-Project.langchain_integration.agent_memory_service.long_term_memory')
def test_store_memory(mock_long_term_memory, mock_short_term_memory, client):
    test_memory = {
        "human_input": "What is the capital of France?",
        "ai_output": "The capital of France is Paris."
    }
    response = client.post('/store_memory', json=test_memory)
    assert response.status_code == 200
    assert json.loads(response.data)["message"] == "Memory stored successfully"
    mock_short_term_memory.save_context.assert_called_once_with(
        {"human_input": "What is the capital of France?"},
        {"ai_output": "The capital of France is Paris."}
    )
    mock_long_term_memory.save_context.assert_called_once_with(
        {"human_input": "What is the capital of France?"},
        {"ai_output": "The capital of France is Paris."}
    )

@patch('ADAPT-CamelDEV-Project.langchain_integration.agent_memory_service.short_term_memory')
@patch('ADAPT-CamelDEV-Project.langchain_integration.agent_memory_service.long_term_memory')
def test_retrieve_memory(mock_long_term_memory, mock_short_term_memory, client):
    mock_short_term_memory.load_memory_variables.return_value = {"short_term": "short term memory"}
    mock_long_term_memory.load_memory_variables.return_value = {"long_term": "long term memory"}
    
    response = client.get('/retrieve_memory')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "short_term_memory" in data
    assert "long_term_memory" in data
    assert data["short_term_memory"] == {"short_term": "short term memory"}
    assert data["long_term_memory"] == {"long_term": "long term memory"}

@patch('ADAPT-CamelDEV-Project.langchain_integration.agent_memory_service.short_term_memory')
@patch('ADAPT-CamelDEV-Project.langchain_integration.agent_memory_service.long_term_memory')
def test_clear_memory(mock_long_term_memory, mock_short_term_memory, client):
    response = client.post('/clear_memory')
    assert response.status_code == 200
    assert json.loads(response.data)["message"] == "Memory cleared successfully"
    mock_short_term_memory.clear.assert_called_once()
    mock_long_term_memory.clear.assert_called_once()

@patch('ADAPT-CamelDEV-Project.langchain_integration.agent_memory_service.short_term_memory')
@patch('ADAPT-CamelDEV-Project.langchain_integration.agent_memory_service.long_term_memory')
def test_memory_cycle(mock_long_term_memory, mock_short_term_memory, client):
    # Store memory
    test_memory = {
        "human_input": "What is the capital of France?",
        "ai_output": "The capital of France is Paris."
    }
    store_response = client.post('/store_memory', json=test_memory)
    assert store_response.status_code == 200

    # Retrieve memory
    mock_short_term_memory.load_memory_variables.return_value = {"short_term": "short term memory"}
    mock_long_term_memory.load_memory_variables.return_value = {"long_term": "long term memory"}
    retrieve_response = client.get('/retrieve_memory')
    assert retrieve_response.status_code == 200
    retrieved_data = json.loads(retrieve_response.data)
    assert "short_term_memory" in retrieved_data
    assert "long_term_memory" in retrieved_data
    assert retrieved_data["short_term_memory"] == {"short_term": "short term memory"}
    assert retrieved_data["long_term_memory"] == {"long_term": "long term memory"}

    # Clear memory
    clear_response = client.post('/clear_memory')
    assert clear_response.status_code == 200

    # Verify memory is cleared
    mock_short_term_memory.load_memory_variables.return_value = {}
    mock_long_term_memory.load_memory_variables.return_value = {}
    retrieve_after_clear = client.get('/retrieve_memory')
    assert retrieve_after_clear.status_code == 200
    cleared_data = json.loads(retrieve_after_clear.data)
    assert cleared_data["short_term_memory"] == {}
    assert cleared_data["long_term_memory"] == {}

def test_store_memory_error(client):
    with patch('ADAPT-CamelDEV-Project.langchain_integration.agent_memory_service.short_term_memory.save_context', side_effect=Exception("Test error")):
        test_memory = {
            "human_input": "What is the capital of France?",
            "ai_output": "The capital of France is Paris."
        }
        response = client.post('/store_memory', json=test_memory)
        assert response.status_code == 500
        assert json.loads(response.data)["error"] == "An error occurred while storing memory"

def test_retrieve_memory_error(client):
    with patch('ADAPT-CamelDEV-Project.langchain_integration.agent_memory_service.short_term_memory.load_memory_variables', side_effect=Exception("Test error")):
        response = client.get('/retrieve_memory')
        assert response.status_code == 500
        assert json.loads(response.data)["error"] == "An error occurred while retrieving memory"

def test_clear_memory_error(client):
    with patch('ADAPT-CamelDEV-Project.langchain_integration.agent_memory_service.short_term_memory.clear', side_effect=Exception("Test error")):
        response = client.post('/clear_memory')
        assert response.status_code == 500
        assert json.loads(response.data)["error"] == "An error occurred while clearing memory"