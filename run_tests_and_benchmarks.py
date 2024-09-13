 import asyncio
import pytest
import time
from benchmarks.model_backend_benchmark import ModelBackendBenchmark
from camel.types import ModelPlatformType, ModelType

async def run_system_tests():
    print("Running system-wide tests...")
    start_time = time.time()
    pytest.main(["-v", "tests/system_tests/test_adapt_with_new_models.py"])
    end_time = time.time()
    print(f"System-wide tests completed in {end_time - start_time:.2f} seconds")

async def run_benchmarks():
    print("Running benchmarks...")
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

async def main():
    await run_system_tests()
    print("\n" + "="*50 + "\n")
    await run_benchmarks()

if __name__ == "__main__":
    asyncio.run(main())