import pytest
from unittest.mock import patch, AsyncMock
from camel.models.github_model_backend import GitHubModelBackend, GitHubAPIError, GitHubResponseValidationError
from camel.types.enums import ModelType

@pytest.fixture
def github_model():
    return GitHubModelBackend(ModelType.GITHUB_COPILOT, "test_api_key")

@pytest.mark.asyncio
async def test_generate(github_model):
    with patch.object(github_model, '_make_api_request', new_callable=AsyncMock) as mock_request:
        mock_request.return_value = {"generated_text": "Test response"}
        result = await github_model.generate("Test prompt", 50, 0.7)
        assert result == "Test response"
        mock_request.assert_called_once_with("POST", "generate", {
            "model": github_model.model_name,
            "prompt": "Test prompt",
            "max_tokens": 50,
            "temperature": 0.7,
            "stop": None
        })

@pytest.mark.asyncio
async def test_generate_api_error(github_model):
    with patch.object(github_model, '_make_api_request', new_callable=AsyncMock) as mock_request:
        mock_request.side_effect = GitHubAPIError("API Error")
        with pytest.raises(GitHubAPIError):
            await github_model.generate("Test prompt", 50, 0.7)

@pytest.mark.asyncio
async def test_get_token_count(github_model):
    with patch.object(github_model, '_make_api_request', new_callable=AsyncMock) as mock_request:
        mock_request.return_value = {"token_count": 10}
        result = await github_model.get_token_count("Test text")
        assert result == 10
        mock_request.assert_called_once_with("POST", "token_count", {
            "model": github_model.model_name,
            "text": "Test text"
        })

@pytest.mark.asyncio
async def test_embeddings(github_model):
    with patch.object(github_model, '_make_api_request', new_callable=AsyncMock) as mock_request:
        mock_request.return_value = {"embeddings": [0.1, 0.2, 0.3]}
        result = await github_model.embeddings("Test text")
        assert result == [0.1, 0.2, 0.3]
        mock_request.assert_called_once_with("POST", "embeddings", {
            "model": github_model.model_name,
            "text": "Test text"
        })

def test_validate_response(github_model):
    valid_response = {"generated_text": "Valid response"}
    result = github_model.validate_response(valid_response)
    assert result == {"text": "Valid response"}

    with pytest.raises(GitHubResponseValidationError):
        github_model.validate_response({"error": "Invalid response"})

    with pytest.raises(GitHubResponseValidationError):
        github_model.validate_response("Not a dict")

@pytest.mark.asyncio
async def test_get_model_info(github_model):
    with patch.object(github_model, '_make_api_request', new_callable=AsyncMock) as mock_request:
        mock_request.return_value = {"model_info": "Test info"}
        result = await github_model.get_model_info()
        assert result == {"model_info": "Test info"}
        mock_request.assert_called_once_with("GET", f"info/{github_model.model_name}")

@pytest.mark.asyncio
async def test_close(github_model):
    with patch.object(github_model, 'session', new_callable=AsyncMock) as mock_session:
        await github_model.close()
        mock_session.close.assert_called_once()

@pytest.mark.asyncio
async def test_make_api_request(github_model):
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json.return_value = {"result": "success"}

    with patch('aiohttp.ClientSession.request', return_value=mock_response):
        result = await github_model._make_api_request("GET", "test_endpoint", {"param": "value"})
        assert result == {"result": "success"}

    mock_response.status = 400
    mock_response.text.return_value = "Bad request"
    with patch('aiohttp.ClientSession.request', return_value=mock_response):
        with pytest.raises(GitHubAPIError):
            await github_model._make_api_request("GET", "test_endpoint", {"param": "value"})

def test_set_api_key(github_model):
    new_api_key = "new_test_api_key"
    github_model.set_api_key(new_api_key)
    assert github_model.api_key == new_api_key

@pytest.mark.asyncio
async def test_check_availability(github_model):
    with patch.object(github_model, '_make_api_request', new_callable=AsyncMock) as mock_request:
        mock_request.return_value = {"status": "ok"}
        result = await github_model.check_availability()
        assert result == True
        mock_request.assert_called_once_with("GET", "health")

    with patch.object(github_model, '_make_api_request', new_callable=AsyncMock) as mock_request:
        mock_request.side_effect = GitHubAPIError("API Error")
        result = await github_model.check_availability()
        assert result == False

@pytest.mark.asyncio
async def test_rate_limiting(github_model):
    with patch.object(github_model, '_make_api_request', new_callable=AsyncMock) as mock_request, \
         patch('asyncio.sleep', new_callable=AsyncMock) as mock_sleep:
        mock_request.return_value = {"generated_text": "Test response"}
        
        # First call should not trigger rate limiting
        await github_model.generate("Test prompt 1", 50, 0.7)
        mock_sleep.assert_not_called()
        
        # Second call should trigger rate limiting
        await github_model.generate("Test prompt 2", 50, 0.7)
        mock_sleep.assert_called_once()

@pytest.mark.asyncio
async def test_retries(github_model):
    with patch.object(github_model, '_make_api_request', new_callable=AsyncMock) as mock_request:
        mock_request.side_effect = [
            GitHubAPIError("API Error"),
            GitHubAPIError("API Error"),
            {"generated_text": "Test response"}
        ]
        
        result = await github_model.generate("Test prompt", 50, 0.7)
        assert result == "Test response"
        assert mock_request.call_count == 3  # Two failures, one success