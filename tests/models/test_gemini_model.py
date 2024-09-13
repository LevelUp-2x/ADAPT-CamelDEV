import unittest
import os
from camel.models.gemini_model import GeminiModel, GeminiModelError
from camel.types import ModelType
from camel.messages import OpenAIMessage

class TestGeminiModel(unittest.TestCase):

    def setUp(self):
        self.model_type = ModelType.GEMINI_PRO
        self.model_config_dict = {"temperature": 0.7}
        self.api_key = os.getenv('Gemini_Studio_CHASE_API_KEY') or os.getenv('Gemini_Studio_LIQUIDMOVZ_API_KEY')
        if not self.api_key:
            raise ValueError("Gemini API key not found in environment variables")

    def test_run_success(self):
        model = GeminiModel(self.model_type, self.model_config_dict, api_key=self.api_key)
        messages = [OpenAIMessage(role="user", content="Hello, how are you?")]
        
        response = model.run(messages)
        
        self.assertIn("choices", response)
        self.assertIsInstance(response["choices"][0]["message"]["content"], str)
        self.assertGreater(len(response["choices"][0]["message"]["content"]), 0)

    def test_run_with_invalid_api_key(self):
        model = GeminiModel(self.model_type, self.model_config_dict, api_key="invalid_key")
        messages = [OpenAIMessage(role="user", content="Hello")]
        
        with self.assertRaises(GeminiModelError):
            model.run(messages)

    def test_init_without_api_key(self):
        # Temporarily remove environment variables
        gemini_api_key = os.environ.pop('Gemini_Studio_CHASE_API_KEY', None)
        gemini_api_key_2 = os.environ.pop('Gemini_Studio_LIQUIDMOVZ_API_KEY', None)
        
        with self.assertRaises(GeminiModelError):
            GeminiModel(self.model_type, self.model_config_dict)
        
        # Restore environment variables
        if gemini_api_key:
            os.environ['Gemini_Studio_CHASE_API_KEY'] = gemini_api_key
        if gemini_api_key_2:
            os.environ['Gemini_Studio_LIQUIDMOVZ_API_KEY'] = gemini_api_key_2

    def test_to_gemini_req(self):
        model = GeminiModel(self.model_type, self.model_config_dict, api_key=self.api_key)
        messages = [
            OpenAIMessage(role="user", content="Hello"),
            OpenAIMessage(role="assistant", content="Hi there"),
        ]
        gemini_req = model.to_gemini_req(messages)
        self.assertEqual(len(gemini_req), 2)
        self.assertEqual(gemini_req[0]["role"], "user")
        self.assertEqual(gemini_req[1]["role"], "model")

if __name__ == '__main__':
    unittest.main()