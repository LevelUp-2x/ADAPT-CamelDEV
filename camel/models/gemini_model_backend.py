import logging
from typing import Any, Dict, List, Optional, Union
import asyncio
from functools import lru_cache
import google.generativeai as genai
from google.api_core import retry
from google.generativeai.types import GenerateContentResponse
from camel.models.adapt_model_backend import AdaptModelBackend
from camel.types.enums import ModelType
import time

logger = logging.getLogger(__name__)

class GeminiModelError(Exception):
    """Base exception class for Gemini Model errors."""

class GeminiAPIError(GeminiModelError):
    """Exception raised for Gemini API errors."""

class GeminiResponseValidationError(GeminiModelError):
    """Exception raised when the API response doesn't match expected format."""

class GeminiModelBackend(AdaptModelBackend):
    """
    Implementation of AdaptModelBackend for Google's Gemini model.
    """

    def __init__(self, model_type: ModelType, api_key: str, **kwargs: Any):
        super().__init__(model_type.value, **kwargs)
        self.model_type = model_type
        self.api_key = api_key
        self.max_retries = 3
        self.base_delay = 1  # Base delay for exponential backoff in seconds
        self.rate_limit = 10  # Requests per second
        self.last_request_time = 0
        self._initialize_model()

    def _initialize_model(self):
        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
            logger.info(f"Initialized Gemini model: {self.model_name}")
        except Exception as e:
            logger.exception(f"Failed to initialize Gemini model: {self.model_name}")
            raise GeminiModelError(f"Initialization error: {str(e)}")

    async def _rate_limit(self):
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < 1 / self.rate_limit:
            await asyncio.sleep(1 / self.rate_limit - time_since_last_request)
        self.last_request_time = time.time()

    @retry.Retry(predicate=retry.if_exception_type(
        genai.types.GoogleGenerativeAIError,
        GeminiAPIError
    ))
    async def generate(self, prompt: str, max_tokens: int, temperature: float, 
                       stop: Optional[Union[str, List[str]]] = None) -> str:
        logger.info(f"Generating text with Gemini model {self.model_name}")
        
        await self._rate_limit()

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    max_output_tokens=max_tokens,
                    temperature=temperature,
                    stop_sequences=stop if isinstance(stop, list) else [stop] if stop else None
                )
            )
            logger.info("Text generation successful")
            return response.text
        except genai.types.GoogleGenerativeAIError as e:
            logger.error(f"Gemini API error during text generation: {str(e)}")
            raise GeminiAPIError(f"Gemini API error: {str(e)}")
        except Exception as e:
            logger.exception("Unexpected error during text generation")
            raise GeminiModelError(f"Text generation error: {str(e)}")

    @lru_cache(maxsize=1000)
    async def get_token_count(self, text: str) -> int:
        logger.info(f"Estimating token count for text")
        try:
            # Assuming 4 characters per token as a rough estimate
            token_count = len(text) // 4
            logger.info(f"Token count estimated: {token_count}")
            return token_count
        except Exception as e:
            logger.exception("Error estimating token count")
            raise GeminiModelError(f"Token count estimation error: {str(e)}")

    @retry.Retry(predicate=retry.if_exception_type(
        genai.types.GoogleGenerativeAIError,
        GeminiAPIError
    ))
    @lru_cache(maxsize=1000)
    async def embeddings(self, text: str) -> List[float]:
        logger.info(f"Attempting to generate embeddings for text")

        await self._rate_limit()

        try:
            # Note: As of the last update, Gemini didn't offer a separate embeddings API
            # This is a placeholder for when/if such functionality becomes available
            embedding_model = genai.GenerativeModel('embedding-001')
            result = embedding_model.embed_content(text=text)
            embeddings = result['embedding']
            logger.info("Embeddings generated successfully")
            return embeddings
        except NotImplementedError as e:
            logger.warning(str(e))
            raise
        except genai.types.GoogleGenerativeAIError as e:
            logger.error(f"Gemini API error during embeddings generation: {str(e)}")
            raise GeminiAPIError(f"Gemini API error: {str(e)}")
        except Exception as e:
            logger.exception("Unexpected error while attempting to generate embeddings")
            raise GeminiModelError(f"Embeddings generation error: {str(e)}")

    def validate_response(self, response: Any) -> Dict[str, Any]:
        logger.info("Validating Gemini API response")
        if isinstance(response, GenerateContentResponse):
            if response.text:
                logger.info("Response validation successful")
                return {"text": response.text}
            else:
                logger.error("Response does not contain text")
                raise GeminiResponseValidationError("Response does not contain text")
        else:
            logger.error(f"Invalid response type: {type(response)}")
            raise GeminiResponseValidationError(f"Invalid response type: {type(response)}")

    async def close(self):
        # No specific cleanup needed for Gemini as of now
        logger.info("Closing Gemini model backend")

    @lru_cache(maxsize=1)
    async def get_model_info(self) -> Dict[str, Any]:
        logger.info(f"Getting model info for {self.model_name}")
        try:
            # Note: This is a placeholder. Actual implementation would depend
            # on what information Gemini's API provides about its models
            model_info = {
                "model_name": self.model_name,
                "model_type": self.model_type.value,
                "provider": "Google",
                "capabilities": ["text generation", "embeddings", "image generation", "image analysis", "speech to text", "text to speech"]
            }
            logger.info("Model info retrieved successfully")
            return model_info
        except Exception as e:
            logger.exception("Error retrieving model info")
            raise GeminiModelError(f"Model info retrieval error: {str(e)}")

    def set_api_key(self, api_key: str):
        """
        Set or update the API key for the model.

        Args:
            api_key (str): The new API key to be used for authentication.
        """
        logger.info("Updating API key")
        self.api_key = api_key
        self._initialize_model()

    async def check_availability(self) -> bool:
        """
        Check if the model is available and functioning correctly.

        Returns:
            bool: True if the model is available and functioning, False otherwise.
        """
        logger.info("Checking model availability")
        try:
            # Perform a simple generation task to check availability
            response = await self.generate("Hello", max_tokens=5, temperature=0.5)
            return bool(response)
        except Exception as e:
            logger.error(f"Model is unavailable: {str(e)}")
            return False

    @retry.Retry(predicate=retry.if_exception_type(
        genai.types.GoogleGenerativeAIError,
        GeminiAPIError
    ))
    async def generate_image(self, prompt: str, size: str = "1024x1024") -> str:
        logger.info(f"Generating image with Gemini model {self.model_name}")
        
        await self._rate_limit()

        try:
            # Note: This is a placeholder. Actual implementation would depend on Gemini's image generation capabilities
            response = self.model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    max_output_tokens=100,
                    temperature=0.7
                )
            )
            # Assuming the response contains a URL to the generated image
            logger.info("Image generation successful")
            return response.text  # This should be the URL to the generated image
        except genai.types.GoogleGenerativeAIError as e:
            logger.error(f"Gemini API error during image generation: {str(e)}")
            raise GeminiAPIError(f"Gemini API error: {str(e)}")
        except Exception as e:
            logger.exception("Unexpected error during image generation")
            raise GeminiModelError(f"Image generation error: {str(e)}")

    @retry.Retry(predicate=retry.if_exception_type(
        genai.types.GoogleGenerativeAIError,
        GeminiAPIError
    ))
    async def analyze_image(self, image_path: str) -> Dict[str, Any]:
        logger.info(f"Analyzing image with Gemini model {self.model_name}")
        
        await self._rate_limit()

        try:
            # Note: This is a placeholder. Actual implementation would depend on Gemini's image analysis capabilities
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()
            response = self.model.generate_content(
                ["Analyze this image and describe what you see.", image_data],
                generation_config=genai.GenerationConfig(
                    max_output_tokens=200,
                    temperature=0.2
                )
            )
            logger.info("Image analysis successful")
            return {"analysis": response.text}
        except genai.types.GoogleGenerativeAIError as e:
            logger.error(f"Gemini API error during image analysis: {str(e)}")
            raise GeminiAPIError(f"Gemini API error: {str(e)}")
        except Exception as e:
            logger.exception("Unexpected error during image analysis")
            raise GeminiModelError(f"Image analysis error: {str(e)}")

    @retry.Retry(predicate=retry.if_exception_type(
        genai.types.GoogleGenerativeAIError,
        GeminiAPIError
    ))
    async def speech_to_text(self, audio_path: str) -> str:
        logger.info(f"Converting speech to text with Gemini model {self.model_name}")
        
        await self._rate_limit()

        try:
            # Note: This is a placeholder. Actual implementation would depend on Gemini's speech-to-text capabilities
            # For now, we'll assume the audio file is transcribed to text
            with open(audio_path, 'rb') as audio_file:
                audio_data = audio_file.read()
            response = self.model.generate_content(
                ["Transcribe this audio to text.", audio_data],
                generation_config=genai.GenerationConfig(
                    max_output_tokens=500,
                    temperature=0.2
                )
            )
            logger.info("Speech to text conversion successful")
            return response.text
        except genai.types.GoogleGenerativeAIError as e:
            logger.error(f"Gemini API error during speech to text conversion: {str(e)}")
            raise GeminiAPIError(f"Gemini API error: {str(e)}")
        except Exception as e:
            logger.exception("Unexpected error during speech to text conversion")
            raise GeminiModelError(f"Speech to text conversion error: {str(e)}")

    @retry.Retry(predicate=retry.if_exception_type(
        genai.types.GoogleGenerativeAIError,
        GeminiAPIError
    ))
    async def text_to_speech(self, text: str, output_path: str) -> str:
        logger.info(f"Converting text to speech with Gemini model {self.model_name}")
        
        await self._rate_limit()

        try:
            # Note: This is a placeholder. Actual implementation would depend on Gemini's text-to-speech capabilities
            # For now, we'll assume the text is converted to an audio file
            response = self.model.generate_content(
                f"Convert this text to speech: {text}",
                generation_config=genai.GenerationConfig(
                    max_output_tokens=100,
                    temperature=0.2
                )
            )
            # In a real implementation, we would save the audio data to the output_path
            # For now, we'll just write the response text to the file
            with open(output_path, 'w') as output_file:
                output_file.write(response.text)
            logger.info("Text to speech conversion successful")
            return output_path
        except genai.types.GoogleGenerativeAIError as e:
            logger.error(f"Gemini API error during text to speech conversion: {str(e)}")
            raise GeminiAPIError(f"Gemini API error: {str(e)}")
        except Exception as e:
            logger.exception("Unexpected error during text to speech conversion")
            raise GeminiModelError(f"Text to speech conversion error: {str(e)}")

# Note: This implementation is based on the current understanding of the Gemini API.
# It may need to be adjusted as the API evolves or if more details become available.