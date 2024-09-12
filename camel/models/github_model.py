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
import os
import logging
from typing import Any, Dict, List, Union

import requests
from requests.exceptions import RequestException

from camel.models import BaseModelBackend
from camel.types import ModelType

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GitHubModelError(Exception):
    """Custom exception class for GitHub model errors."""
    pass

class GitHubModel(BaseModelBackend):
    def __init__(self, model_type: ModelType, model_config_dict: Dict[str, Any]):
        super().__init__(model_type, model_config_dict)
        self.endpoint = os.getenv('GITHUB_MODELS_ENDPOINT', 'https://models.inference.ai.azure.com/chat/completions')
        self.token = os.getenv('GITHUB_MODELS_TOKEN')
        if not self.token:
            logger.error("GITHUB_MODELS_TOKEN not found in environment variables")
            raise GitHubModelError("GITHUB_MODELS_TOKEN not found in environment variables")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        logger.info(f"GitHubModel initialized with endpoint: {self.endpoint}")

    def chat_completion(self, messages: List[Dict[str, str]], **kwargs: Any) -> Dict[str, Any]:
        payload = {
            "model": self.model_config_dict.get("model_name", self.model_type.value),
            "messages": messages,
            **kwargs
        }
        try:
            logger.info(f"Sending request to GitHub API. Model: {payload['model']}")
            response = requests.post(self.endpoint, json=payload, headers=self.headers)
            response.raise_for_status()
            logger.info("Received successful response from GitHub API")
            return response.json()
        except RequestException as e:
            logger.error(f"Error during API request: {str(e)}")
            if e.response is not None:
                status_code = e.response.status_code
                if status_code == 401:
                    raise GitHubModelError("Authentication failed. Please check your GitHub API token.") from e
                elif status_code == 403:
                    raise GitHubModelError("Access forbidden. Your API token might not have the necessary permissions.") from e
                elif status_code == 404:
                    raise GitHubModelError("Endpoint not found. Please check the GITHUB_MODELS_ENDPOINT environment variable.") from e
                else:
                    raise GitHubModelError(f"Request failed with status code {status_code}: {e}") from e
            else:
                raise GitHubModelError(f"Request failed: {e}") from e

    def completion(self, prompt: str, **kwargs: Any) -> Dict[str, Any]:
        messages = [{"role": "user", "content": prompt}]
        return self.chat_completion(messages, **kwargs)

    @classmethod
    def available_models(cls) -> List[ModelType]:
        return [
            ModelType.AI21_JUMBO_INSTRUCT,
            ModelType.COHERE_COMMAND_R,
            ModelType.COHERE_COMMAND_R_PLUS,
            ModelType.META_LLAMA_3_70B_INSTRUCT,
            ModelType.MIXTRAL_LARGE,
            ModelType.OPENAI_GPT4O,
            # Add other GitHub models as needed
        ]