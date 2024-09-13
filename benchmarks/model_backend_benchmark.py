import asyncio
import time
from typing import List, Dict
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

class ModelBackendBenchmark:
    def __init__(self, model_configs: List[Dict]):
        self.models = [ModelFactory.create(**config) for config in model_configs]

    async def run_benchmark(self, num_iterations: int = 10):
        results = {}
        for model in self.models:
            model_name = model.model_name
            results[model_name] = {
                "text_generation": [],
                "token_counting": [],
                "embeddings": [],
                "image_generation": [],
                "image_analysis": [],
                "speech_to_text": [],
                "text_to_speech": [],
            }

            for _ in range(num_iterations):
                # Text Generation Benchmark
                start_time = time.time()
                await model.generate("Explain the concept of artificial intelligence.", max_tokens=100, temperature=0.7)
                results[model_name]["text_generation"].append(time.time() - start_time)

                # Token Counting Benchmark
                text = "This is a sample text for token counting benchmark."
                start_time = time.time()
                await model.get_token_count(text)
                results[model_name]["token_counting"].append(time.time() - start_time)

                # Embeddings Benchmark
                try:
                    start_time = time.time()
                    await model.embeddings(text)
                    results[model_name]["embeddings"].append(time.time() - start_time)
                except NotImplementedError:
                    results[model_name]["embeddings"].append(None)

                # Image Generation Benchmark
                start_time = time.time()
                await model.generate_image("A beautiful sunset over a calm ocean")
                results[model_name]["image_generation"].append(time.time() - start_time)

                # Image Analysis Benchmark
                start_time = time.time()
                await model.analyze_image("path/to/test/image.jpg")  # Replace with an actual test image path
                results[model_name]["image_analysis"].append(time.time() - start_time)

                # Speech-to-Text Benchmark
                start_time = time.time()
                await model.speech_to_text("path/to/test/audio.wav")  # Replace with an actual test audio path
                results[model_name]["speech_to_text"].append(time.time() - start_time)

                # Text-to-Speech Benchmark
                start_time = time.time()
                await model.text_to_speech("This is a test sentence for text-to-speech conversion.", "path/to/output/audio.wav")
                results[model_name]["text_to_speech"].append(time.time() - start_time)

        return results

    def print_results(self, results: Dict):
        for model_name, model_results in results.items():
            print(f"\nResults for {model_name}:")
            for operation, times in model_results.items():
                if all(t is not None for t in times):
                    avg_time = sum(times) / len(times)
                    print(f"  {operation}: Average time = {avg_time:.4f}s")
                else:
                    print(f"  {operation}: Not supported or error occurred")

async def main():
    model_configs = [
        {
            "model_platform": ModelPlatformType.GITHUB,
            "model_type": ModelType.GITHUB_COPILOT,
            "model_config_dict": {},
            "api_key": "your_github_api_key"
        },
        {
            "model_platform": ModelPlatformType.GEMINI,
            "model_type": ModelType.GEMINI_1_5_PRO,
            "model_config_dict": {},
            "api_key": "your_gemini_api_key"
        }
    ]

    benchmark = ModelBackendBenchmark(model_configs)
    results = await benchmark.run_benchmark()
    benchmark.print_results(results)

if __name__ == "__main__":
    asyncio.run(main())