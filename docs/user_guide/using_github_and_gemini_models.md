# Using GitHub and Gemini Models in ADAPT

This guide explains how to use the newly integrated GitHub and Gemini models within the ADAPT (Advanced Dynamic Agent Platform Technology) framework, including their multi-modal capabilities.

## Prerequisites

- Ensure you have the latest version of ADAPT installed.
- You need valid API keys for the GitHub Copilot API and Google's Gemini API.

## Configuring the Models

### GitHub Models

To use GitHub models (such as GitHub Copilot), you need to set up your API key:

```python
import os
os.environ['GITHUB_API_KEY'] = 'your_github_api_key_here'
```

### Gemini Models

For Gemini models, set up your API key similarly:

```python
import os
os.environ['GEMINI_API_KEY'] = 'your_gemini_api_key_here'
```

## Using the Models

### Initializing a Model

To use either a GitHub or Gemini model, you can use the `ModelFactory` class:

```python
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

# For GitHub Copilot
github_model = ModelFactory.create(
    model_platform=ModelPlatformType.GITHUB,
    model_type=ModelType.GITHUB_COPILOT,
    model_config_dict={},
    api_key=os.environ['GITHUB_API_KEY']
)

# For Gemini
gemini_model = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_1_5_PRO,
    model_config_dict={},
    api_key=os.environ['GEMINI_API_KEY']
)
```

### Text Generation

To generate text using the models:

```python
import asyncio

async def generate_text(model, prompt):
    return await model.generate(prompt, max_tokens=100, temperature=0.7)

# Using GitHub Copilot
github_response = asyncio.run(generate_text(github_model, "Write a Python function to calculate fibonacci numbers."))
print("GitHub Copilot response:", github_response)

# Using Gemini
gemini_response = asyncio.run(generate_text(gemini_model, "Explain the concept of quantum entanglement."))
print("Gemini response:", gemini_response)
```

### Getting Token Count

To get the token count of a piece of text:

```python
async def get_token_count(model, text):
    return await model.get_token_count(text)

github_tokens = asyncio.run(get_token_count(github_model, "Hello, world!"))
gemini_tokens = asyncio.run(get_token_count(gemini_model, "Hello, world!"))

print("GitHub Copilot token count:", github_tokens)
print("Gemini token count:", gemini_tokens)
```

### Generating Embeddings

To generate embeddings (note: this feature might not be available for all models):

```python
async def get_embeddings(model, text):
    try:
        return await model.embeddings(text)
    except NotImplementedError:
        print(f"Embeddings not supported for {type(model).__name__}")
        return None

github_embeddings = asyncio.run(get_embeddings(github_model, "Example text"))
gemini_embeddings = asyncio.run(get_embeddings(gemini_model, "Example text"))

if github_embeddings:
    print("GitHub Copilot embeddings:", github_embeddings[:5])  # Print first 5 values
if gemini_embeddings:
    print("Gemini embeddings:", gemini_embeddings[:5])  # Print first 5 values
```

### Image Generation

To generate images based on text prompts:

```python
async def generate_image(model, prompt):
    return await model.generate_image(prompt)

github_image_url = asyncio.run(generate_image(github_model, "A beautiful sunset over a calm ocean"))
gemini_image_url = asyncio.run(generate_image(gemini_model, "A futuristic cityscape at night"))

print("GitHub Copilot image URL:", github_image_url)
print("Gemini image URL:", gemini_image_url)
```

### Image Analysis

To analyze the content of an image:

```python
async def analyze_image(model, image_path):
    return await model.analyze_image(image_path)

github_analysis = asyncio.run(analyze_image(github_model, "path/to/image.jpg"))
gemini_analysis = asyncio.run(analyze_image(gemini_model, "path/to/image.jpg"))

print("GitHub Copilot image analysis:", github_analysis)
print("Gemini image analysis:", gemini_analysis)
```

### Speech-to-Text

To convert speech in an audio file to text:

```python
async def speech_to_text(model, audio_path):
    return await model.speech_to_text(audio_path)

github_transcription = asyncio.run(speech_to_text(github_model, "path/to/audio.wav"))
gemini_transcription = asyncio.run(speech_to_text(gemini_model, "path/to/audio.wav"))

print("GitHub Copilot transcription:", github_transcription)
print("Gemini transcription:", gemini_transcription)
```

### Text-to-Speech

To convert text to speech and save as an audio file:

```python
async def text_to_speech(model, text, output_path):
    return await model.text_to_speech(text, output_path)

github_audio_path = asyncio.run(text_to_speech(github_model, "Hello, this is a test.", "github_output.wav"))
gemini_audio_path = asyncio.run(text_to_speech(gemini_model, "Hello, this is a test.", "gemini_output.wav"))

print("GitHub Copilot audio file:", github_audio_path)
print("Gemini audio file:", gemini_audio_path)
```

### Updating API Key

If you need to update the API key for a model:

```python
github_model.set_api_key("new_github_api_key")
gemini_model.set_api_key("new_gemini_api_key")
```

### Checking Model Availability

To check if a model is available and functioning:

```python
async def check_model_availability(model):
    is_available = await model.check_availability()
    print(f"Model is available: {is_available}")

asyncio.run(check_model_availability(github_model))
asyncio.run(check_model_availability(gemini_model))
```

## Advanced Usage

For more complex scenarios and advanced usage of the GitHub and Gemini models, refer to the `advanced_model_usage.py` example in the `examples` directory. This example demonstrates:

1. Code generation and explanation: Using GitHub Copilot to generate code and Gemini to explain it.
2. Collaborative problem solving: Utilizing both models to design and implement a complex system.
3. Iterative code improvement: An iterative process of code generation, analysis, and improvement using both models.
4. Multi-modal interactions: Combining text, image, and audio capabilities for comprehensive AI-powered solutions.

To run the advanced examples:

```bash
python ADAPT-CamelDEV-Project/examples/advanced_model_usage.py
```

Make sure to replace the API keys in the script with your actual GitHub and Gemini API keys before running.

## Benchmarking

To compare the performance of different model backends, including their multi-modal capabilities, you can use the benchmarking tool provided in `benchmarks/model_backend_benchmark.py`. This tool measures the execution time for various operations across different models.

To run the benchmarks:

```bash
python ADAPT-CamelDEV-Project/benchmarks/model_backend_benchmark.py
```

The benchmark results will help you understand the relative performance of different models for various tasks, including text generation, token counting, embeddings, image generation, image analysis, speech-to-text, and text-to-speech operations.

## Best Practices

1. Always handle potential errors and exceptions when working with these models.
2. Be mindful of rate limits and usage quotas for both GitHub and Gemini APIs.
3. Keep your API keys secure and never share them in your code repositories.
4. Use appropriate model configurations based on your specific use case.
5. Regularly check model availability, especially in production environments.
6. Update API keys securely and avoid hardcoding them in your scripts.
7. When working with multi-modal capabilities, ensure you have the necessary permissions and resources (e.g., image files, audio files) available.
8. Consider the ethical implications of AI-generated content, especially for image and audio generation.

## Troubleshooting

If you encounter any issues:

1. Ensure your API keys are correct and have the necessary permissions.
2. Check your internet connection, as these models require online access.
3. Verify that you're using the latest version of ADAPT.
4. Check the ADAPT logs for any error messages or warnings.
5. Use the `check_availability()` method to verify if the model is functioning correctly.
6. If you're experiencing authentication issues, try updating your API key using the `set_api_key()` method.
7. For multi-modal operations, ensure that file paths are correct and that the files exist.
8. If a specific capability (e.g., embeddings) is not working, check if it's supported by the model you're using.

For more detailed information on using these models or for advanced usage scenarios, please refer to the ADAPT API documentation.