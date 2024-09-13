import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from camel.models.gemini_model_backend import GeminiModelBackend, GeminiAPIError, GeminiResponseValidationError
from camel.types.enums import ModelType
import google.generativeai as genai

@pytest.fixture
def gemini_model():
    with patch('google.generativeai.configure'):
        with patch('google.generativeai.GenerativeModel'):
            return GeminiModelBackend(ModelType.GEMINI_1_5_PRO, "test_api_key")

@pytest.mark.asyncio
async def test_generate(gemini_model):
    mock_response = MagicMock()
    mock_response.text = "Generated text"
    gemini_model.model.generate_content.return_value = mock_response

    result = await gemini_model.generate("Test prompt", 50, 0.7)
    assert result == "Generated text"
    gemini_model.model.generate_content.assert_called_once()

@pytest.mark.asyncio
async def test_generate_api_error(gemini_model):
    gemini_model.model.generate_content.side_effect = genai.types.GoogleGenerativeAIError("API Error")
    with pytest.raises(GeminiAPIError):
        await gemini_model.generate("Test prompt", 50, 0.7)

@pytest.mark.asyncio
async def test_get_token_count(gemini_model):
    result = await gemini_model.get_token_count("This is a test text")
    assert result == 5  # 21 characters / 4 = 5.25, rounded down to 5

@pytest.mark.asyncio
async def test_embeddings(gemini_model):
    mock_embedding_model = MagicMock()
    mock_embedding_model.embed_content.return_value = {'embedding': [0.1, 0.2, 0.3]}
    with patch('google.generativeai.GenerativeModel', return_value=mock_embedding_model):
        result = await gemini_model.embeddings("Test text")
        assert result == [0.1, 0.2, 0.3]

def test_validate_response(gemini_model):
    mock_response = MagicMock(spec=genai.types.GenerateContentResponse)
    mock_response.text = "Valid response"
    result = gemini_model.validate_response(mock_response)
    assert result == {"text": "Valid response"}

    with pytest.raises(GeminiResponseValidationError):
        gemini_model.validate_response(MagicMock(spec=genai.types.GenerateContentResponse, text=None))

    with pytest.raises(GeminiResponseValidationError):
        gemini_model.validate_response("Not a GenerateContentResponse")

@pytest.mark.asyncio
async def test_get_model_info(gemini_model):
    result = await gemini_model.get_model_info()
    assert result == {
        "model_name": gemini_model.model_name,
        "model_type": ModelType.GEMINI_1_5_PRO.value,
        "provider": "Google",
        "capabilities": ["text generation", "embeddings"]
    }

@pytest.mark.asyncio
async def test_close(gemini_model):
    # Since there's no specific cleanup for Gemini, we just ensure it doesn't raise an exception
    await gemini_model.close()

def test_set_api_key(gemini_model):
    new_api_key = "new_test_api_key"
    with patch('google.generativeai.configure') as mock_configure:
        gemini_model.set_api_key(new_api_key)
        assert gemini_model.api_key == new_api_key
        mock_configure.assert_called_once_with(api_key=new_api_key)

@pytest.mark.asyncio
async def test_check_availability(gemini_model):
    with patch.object(gemini_model, 'generate', new_callable=AsyncMock) as mock_generate:
        mock_generate.return_value = "Hello"
        result = await gemini_model.check_availability()
        assert result == True
        mock_generate.assert_called_once_with("Hello", max_tokens=5, temperature=0.5)

    with patch.object(gemini_model, 'generate', new_callable=AsyncMock) as mock_generate:
        mock_generate.side_effect = GeminiAPIError("API Error")
        result = await gemini_model.check_availability()
        assert result == False

@pytest.mark.asyncio
async def test_rate_limiting(gemini_model):
    with patch.object(gemini_model, 'model') as mock_model, \
         patch('asyncio.sleep', new_callable=AsyncMock) as mock_sleep:
        mock_response = MagicMock()
        mock_response.text = "Generated text"
        mock_model.generate_content.return_value = mock_response
        
        # First call should not trigger rate limiting
        await gemini_model.generate("Test prompt 1", 50, 0.7)
        mock_sleep.assert_not_called()
        
        # Second call should trigger rate limiting
        await gemini_model.generate("Test prompt 2", 50, 0.7)
        mock_sleep.assert_called_once()

@pytest.mark.asyncio
async def test_retries(gemini_model):
    with patch.object(gemini_model, 'model') as mock_model:
        mock_model.generate_content.side_effect = [
            genai.types.GoogleGenerativeAIError("API Error"),
            genai.types.GoogleGenerativeAIError("API Error"),
            MagicMock(text="Generated text")
        ]
        
        result = await gemini_model.generate("Test prompt", 50, 0.7)
        assert result == "Generated text"
        assert mock_model.generate_content.call_count == 3  # Two failures, one success