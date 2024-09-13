# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
from typing import Any, Dict, Optional, Union

from camel.models.anthropic_model import AnthropicModel
from camel.models.azure_openai_model import AzureOpenAIModel
from camel.models.adapt_model_backend import AdaptModelBackend
from camel.models.github_model_backend import GitHubModelBackend
from camel.models.gemini_model_backend import GeminiModelBackend
from camel.models.groq_model import GroqModel
from camel.models.litellm_model import LiteLLMModel
from camel.models.mistral_model import MistralModel
from camel.models.ollama_model import OllamaModel
from camel.models.open_source_model import OpenSourceModel
from camel.models.openai_compatibility_model import OpenAICompatibilityModel
from camel.models.openai_model import OpenAIModel
from camel.models.reka_model import RekaModel
from camel.models.samba_model import SambaModel
from camel.models.stub_model import StubModel
from camel.models.togetherai_model import TogetherAIModel
from camel.models.vllm_model import VLLMModel
from camel.models.zhipuai_model import ZhipuAIModel
from camel.types import ModelPlatformType, ModelType
from camel.utils import BaseTokenCounter

import logging

logger = logging.getLogger(__name__)

class ModelFactoryError(Exception):
    """Base exception class for ModelFactory errors."""

class ModelFactory:
    r"""Factory of backend models."""

    @staticmethod
    def create(
        model_platform: ModelPlatformType,
        model_type: Union[ModelType, str],
        model_config_dict: Dict,
        token_counter: Optional[BaseTokenCounter] = None,
        api_key: Optional[str] = None,
        url: Optional[str] = None,
    ) -> AdaptModelBackend:
        r"""Creates an instance of `AdaptModelBackend` of the specified type.

        Args:
            model_platform (ModelPlatformType): Platform from which the model
                originates.
            model_type (Union[ModelType, str]): Model for which a backend is
                created can be a `str` for open source platforms.
            model_config_dict (Dict): A dictionary that will be fed into
                the backend constructor.
            token_counter (Optional[BaseTokenCounter]): Token counter to use
                for the model. If not provided, OpenAITokenCounter(ModelType.
                GPT_3_5_TURBO) will be used if the model platform didn't
                provide official token counter.
            api_key (Optional[str]): The API key for authenticating with the
                model service.
            url (Optional[str]): The url to the model service.

        Raises:
            ModelFactoryError: If there is no backend for the model or if there's an error during creation.

        Returns:
            AdaptModelBackend: The initialized backend.
        """
        logger.info(f"Creating model backend for platform: {model_platform}, type: {model_type}")
        
        try:
            model_class = ModelFactory._get_model_class(model_platform, model_type)
            
            if model_class in (OpenSourceModel, OllamaModel, TogetherAIModel):
                return model_class(model_type, model_config_dict, url, token_counter)
            elif model_class in (GeminiModelBackend, GitHubModelBackend):
                return model_class(model_type=model_type, api_key=api_key, **model_config_dict)
            else:
                return model_class(model_type, model_config_dict, api_key, url, token_counter)
        
        except Exception as e:
            logger.error(f"Error creating model backend: {str(e)}")
            raise ModelFactoryError(f"Failed to create model backend: {str(e)}") from e

    @staticmethod
    def _get_model_class(model_platform: ModelPlatformType, model_type: Union[ModelType, str]) -> Any:
        if isinstance(model_type, ModelType):
            if model_platform.is_open_source and model_type.is_open_source:
                return OpenSourceModel
            elif model_platform.is_openai and model_type.is_openai:
                return OpenAIModel
            elif model_platform.is_azure and model_type.is_azure_openai:
                return AzureOpenAIModel
            elif model_platform.is_anthropic and model_type.is_anthropic:
                return AnthropicModel
            elif model_type.is_groq:
                return GroqModel
            elif model_platform.is_zhipuai and model_type.is_zhipuai:
                return ZhipuAIModel
            elif model_platform.is_gemini and model_type.is_gemini:
                return GeminiModelBackend
            elif model_platform.is_github and model_type.is_github:
                return GitHubModelBackend
            elif model_platform.is_mistral and model_type.is_mistral:
                return MistralModel
            elif model_platform.is_reka and model_type.is_reka:
                return RekaModel
            elif model_type == ModelType.STUB:
                return StubModel
        elif isinstance(model_type, str):
            if model_platform.is_ollama:
                return OllamaModel
            elif model_platform.is_vllm:
                return VLLMModel
            elif model_platform.is_litellm:
                return LiteLLMModel
            elif model_platform.is_openai_compatibility_model:
                return OpenAICompatibilityModel
            elif model_platform.is_samba:
                return SambaModel
            elif model_platform.is_together:
                return TogetherAIModel
        
        logger.error(f"Unknown pair of model platform `{model_platform}` and model type `{model_type}`.")
        raise ModelFactoryError(f"Unknown pair of model platform `{model_platform}` and model type `{model_type}`.")
