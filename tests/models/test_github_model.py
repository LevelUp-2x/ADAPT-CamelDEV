import unittest
import os
from camel.models.github_model import GitHubModel, GitHubModelError
from camel.types import ModelType

class TestGitHubModel(unittest.TestCase):

    def setUp(self):
        self.model_type = ModelType.AI21_JUMBO_INSTRUCT
        self.model_config_dict = {"temperature": 0.7}
        self.api_key = os.getenv('GITHUB_MODELS_TOKEN')
        if not self.api_key:
            raise ValueError("GITHUB_MODELS_TOKEN not found in environment variables")

    def test_chat_completion_success(self):
        model = GitHubModel(self.model_type, self.model_config_dict, api_key=self.api_key)
        messages = [{"role": "user", "content": "Hello, how are you?"}]
        
        response = model.chat_completion(messages)
        
        self.assertIn("choices", response)
        self.assertIsInstance(response["choices"][0]["message"]["content"], str)
        self.assertGreater(len(response["choices"][0]["message"]["content"]), 0)

    def test_chat_completion_with_invalid_api_key(self):
        model = GitHubModel(self.model_type, self.model_config_dict, api_key="invalid_key")
        messages = [{"role": "user", "content": "Hello"}]
        
        with self.assertRaises(GitHubModelError):
            model.chat_completion(messages)

    def test_init_without_api_key(self):
        with self.assertRaises(GitHubModelError):
            GitHubModel(self.model_type, self.model_config_dict)

    def test_available_models(self):
        available_models = GitHubModel.available_models()
        self.assertIsInstance(available_models, list)
        self.assertIn(ModelType.AI21_JUMBO_INSTRUCT, available_models)

if __name__ == '__main__':
    unittest.main()