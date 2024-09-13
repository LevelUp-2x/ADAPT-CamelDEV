import logging
from typing import Any, Dict, List, Optional, Union
import aiohttp
import asyncio
from functools import lru_cache
from camel.models.adapt_model_backend import AdaptModelBackend
from camel.types.enums import ModelType
import time

logger = logging.getLogger(__name__)

class GitHubModelError(Exception):
    """Base exception class for GitHub Model errors."""

class GitHubAPIError(GitHubModelError):
    """Exception raised for GitHub API errors."""

class GitHubResponseValidationError(GitHubModelError):
    """Exception raised when the API response doesn't match expected format."""

class GitHubModelBackend(AdaptModelBackend):
    """
    Implementation of AdaptModelBackend for GitHub Models.
    """

    def __init__(self, model_type: ModelType, api_key: str, **kwargs: Any):
        super().__init__(model_type.value, **kwargs)
        self.model_type = model_type
        self.api_key = api_key
        self.api_base_url = "https://api.github.com/models"  # Placeholder URL
        self.session = None
        self.max_retries = 3
        self.base_delay = 1  # Base delay for exponential backoff in seconds
        self.rate_limit = 10  # Requests per second
        self.last_request_time = 0

    async def _ensure_session(self):
        if self.session is None:
            connector = aiohttp.TCPConnector(limit=100, keepalive_timeout=60)  # Increased keepalive timeout
            self.session = aiohttp.ClientSession(connector=connector)

    async def _make_api_request(self, method: str, endpoint: str, payload: Dict[str, Any] = None) -> Dict[str, Any]:
        await self._ensure_session()
        url = f"{self.api_base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        # Implement rate limiting
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < 1 / self.rate_limit:
            await asyncio.sleep(1 / self.rate_limit - time_since_last_request)

        for attempt in range(self.max_retries):
            try:
                async with self.session.request(method, url, json=payload, headers=headers) as response:
                    self.last_request_time = time.time()
                    if response.status == 200:
                        return await response.json()
                    elif response.status == 429:  # Too Many Requests
                        retry_after = int(response.headers.get('Retry-After', self.base_delay * (2 ** attempt)))
                        logger.warning(f"Rate limited. Retrying after {retry_after} seconds.")
                        await asyncio.sleep(retry_after)
                    else:
                        error_msg = await response.text()
                        logger.error(f"GitHub API error: {response.status} - {error_msg}")
                        raise GitHubAPIError(f"GitHub API error: {response.status} - {error_msg}")
            except aiohttp.ClientError as e:
                logger.exception(f"Network error occurred while making request to {url}")
                if attempt == self.max_retries - 1:
                    raise GitHubModelError(f"Network error: {str(e)}")
                await asyncio.sleep(self.base_delay * (2 ** attempt))

        raise GitHubModelError("Max retries reached")

    async def generate(self, prompt: str, max_tokens: int, temperature: float, 
                       stop: Optional[Union[str, List[str]]] = None) -> str:
        logger.info(f"Generating text with model {self.model_name}")
        
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stop": stop
        }

        try:
            result = await self._make_api_request("POST", "generate", payload)
            logger.info("Text generation successful")
            return result["generated_text"]
        except GitHubModelError as e:
            logger.error(f"Error in text generation: {str(e)}")
            raise

    @lru_cache(maxsize=1000)
    async def get_token_count(self, text: str) -> int:
        logger.info(f"Getting token count for text")

        payload = {
            "model": self.model_name,
            "text": text
        }

        try:
            result = await self._make_api_request("POST", "token_count", payload)
            logger.info("Token count retrieved successfully")
            return result["token_count"]
        except GitHubModelError as e:
            logger.error(f"Error in getting token count: {str(e)}")
            raise

    @lru_cache(maxsize=1000)
    async def embeddings(self, text: str) -> List[float]:
        logger.info(f"Generating embeddings for text")

        payload = {
            "model": self.model_name,
            "text": text
        }

        try:
            result = await self._make_api_request("POST", "embeddings", payload)
            logger.info("Embeddings generated successfully")
            return result["embeddings"]
        except GitHubModelError as e:
            logger.error(f"Error in generating embeddings: {str(e)}")
            raise

    def validate_response(self, response: Any) -> Dict[str, Any]:
        logger.info("Validating API response")
        if isinstance(response, dict):
            if "error" in response:
                logger.error(f"Error in API response: {response['error']}")
                raise GitHubResponseValidationError(f"API error: {response['error']}")
            elif "generated_text" in response:
                logger.info("Response validation successful")
                return {"text": response["generated_text"]}
        logger.error("Invalid response format")
        raise GitHubResponseValidationError("Invalid response format")

    async def close(self):
        if self.session:
            logger.info("Closing aiohttp session")
            await self.session.close()

    @lru_cache(maxsize=1)
    async def get_model_info(self) -> Dict[str, Any]:
        logger.info(f"Getting model info for {self.model_name}")

        try:
            result = await self._make_api_request("GET", f"info/{self.model_name}")
            logger.info("Model info retrieved successfully")
            return result
        except GitHubModelError as e:
            logger.error(f"Error in getting model info: {str(e)}")
            raise

    def set_api_key(self, api_key: str):
        """
        Set or update the API key for the model.

        Args:
            api_key (str): The new API key to be used for authentication.
        """
        logger.info("Updating API key")
        self.api_key = api_key

    async def check_availability(self) -> bool:
        """
        Check if the model is available and functioning correctly.

        Returns:
            bool: True if the model is available and functioning, False otherwise.
        """
        logger.info("Checking model availability")
        try:
            await self._make_api_request("GET", "health")
            logger.info("Model is available")
            return True
        except GitHubModelError:
            logger.error("Model is unavailable")
            return False

    async def generate_image(self, prompt: str, size: str = "1024x1024") -> str:
        logger.info(f"Generating image with model {self.model_name}")
        
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "size": size
        }

        try:
            result = await self._make_api_request("POST", "generate_image", payload)
            logger.info("Image generation successful")
            return result["image_url"]
        except GitHubModelError as e:
            logger.error(f"Error in image generation: {str(e)}")
            raise

    async def analyze_image(self, image_path: str) -> Dict[str, Any]:
        logger.info(f"Analyzing image with model {self.model_name}")
        
        payload = {
            "model": self.model_name,
            "image_path": image_path
        }

        try:
            result = await self._make_api_request("POST", "analyze_image", payload)
            logger.info("Image analysis successful")
            return result["analysis"]
        except GitHubModelError as e:
            logger.error(f"Error in image analysis: {str(e)}")
            raise

    async def speech_to_text(self, audio_path: str) -> str:
        logger.info(f"Converting speech to text with model {self.model_name}")
        
        payload = {
            "model": self.model_name,
            "audio_path": audio_path
        }

        try:
            result = await self._make_api_request("POST", "speech_to_text", payload)
            logger.info("Speech to text conversion successful")
            return result["transcription"]
        except GitHubModelError as e:
            logger.error(f"Error in speech to text conversion: {str(e)}")
            raise

    async def text_to_speech(self, text: str, output_path: str) -> str:
        logger.info(f"Converting text to speech with model {self.model_name}")
        
        payload = {
            "model": self.model_name,
            "text": text,
            "output_path": output_path
        }

        try:
            result = await self._make_api_request("POST", "text_to_speech", payload)
            logger.info("Text to speech conversion successful")
            return result["audio_path"]
        except GitHubModelError as e:
            logger.error(f"Error in text to speech conversion: {str(e)}")
            raise

# Note: This implementation is based on assumptions about the GitHub Models API.
# It will need to be adjusted once we have access to the actual API documentation.