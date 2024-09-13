from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

class AdaptModelBackend(ABC):
    """
    Abstract base class for ADAPT model backends.
    This class defines the interface that all model backends must implement.
    """

    def __init__(self, model_name: str, **kwargs: Any):
        """
        Initialize the AdaptModelBackend.

        Args:
            model_name (str): The name of the model.
            **kwargs: Additional keyword arguments for model configuration.
        """
        self.model_name = model_name
        self.kwargs = kwargs

    @abstractmethod
    async def generate(self, prompt: str, max_tokens: int, temperature: float, 
                       stop: Optional[Union[str, List[str]]] = None) -> str:
        """
        Generate a response based on the given prompt.

        Args:
            prompt (str): The input prompt for generation.
            max_tokens (int): The maximum number of tokens to generate.
            temperature (float): Controls randomness in generation. Higher values make output more random.
            stop (Optional[Union[str, List[str]]]): Token(s) at which to stop generation.

        Returns:
            str: The generated text.
        """
        pass

    @abstractmethod
    async def get_token_count(self, text: str) -> int:
        """
        Get the number of tokens in the given text.

        Args:
            text (str): The input text.

        Returns:
            int: The number of tokens in the text.
        """
        pass

    def get_model_name(self) -> str:
        """
        Get the name of the current model.

        Returns:
            str: The name of the model.
        """
        return self.model_name

    @abstractmethod
    async def embeddings(self, text: str) -> List[float]:
        """
        Generate embeddings for the given text.

        Args:
            text (str): The input text.

        Returns:
            List[float]: The embedding vector.
        """
        pass

    @abstractmethod
    def validate_response(self, response: Any) -> Dict[str, Any]:
        """
        Validate and standardize the response from the model.

        Args:
            response (Any): The raw response from the model.

        Returns:
            Dict[str, Any]: A standardized response dictionary.
        """
        pass

    @abstractmethod
    async def close(self):
        """
        Close any open connections or resources.
        """
        pass

    @abstractmethod
    async def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the current model.

        Returns:
            Dict[str, Any]: A dictionary containing model information.
        """
        pass

    @abstractmethod
    def set_api_key(self, api_key: str):
        """
        Set or update the API key for the model.

        Args:
            api_key (str): The new API key to be used for authentication.
        """
        pass

    @abstractmethod
    async def check_availability(self) -> bool:
        """
        Check if the model is available and functioning correctly.

        Returns:
            bool: True if the model is available and functioning, False otherwise.
        """
        pass

    @abstractmethod
    async def generate_image(self, prompt: str, size: str = "1024x1024") -> str:
        """
        Generate an image based on the given prompt.

        Args:
            prompt (str): The input prompt for image generation.
            size (str): The desired size of the image (e.g., "1024x1024").

        Returns:
            str: The URL or path to the generated image.
        """
        pass

    @abstractmethod
    async def analyze_image(self, image_path: str) -> Dict[str, Any]:
        """
        Analyze the content of an image.

        Args:
            image_path (str): The path or URL to the image.

        Returns:
            Dict[str, Any]: A dictionary containing analysis results (e.g., objects, colors, text).
        """
        pass

    @abstractmethod
    async def speech_to_text(self, audio_path: str) -> str:
        """
        Convert speech in an audio file to text.

        Args:
            audio_path (str): The path to the audio file.

        Returns:
            str: The transcribed text.
        """
        pass

    @abstractmethod
    async def text_to_speech(self, text: str, output_path: str) -> str:
        """
        Convert text to speech and save as an audio file.

        Args:
            text (str): The text to convert to speech.
            output_path (str): The path where the audio file should be saved.

        Returns:
            str: The path to the generated audio file.
        """
        pass

# You might want to add more abstract methods or utility functions here
# depending on the common functionalities required across different model backends.