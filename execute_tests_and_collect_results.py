import subprocess
import os
import datetime
import json

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

def save_results(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def main():
    # Create a results directory
    results_dir = f"test_results_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(results_dir, exist_ok=True)

    # Run system-wide tests and benchmarks
    print("Running system-wide tests and benchmarks...")
    output, error = run_command("python ADAPT-CamelDEV-Project/run_tests_and_benchmarks.py")
    save_results(f"{results_dir}/system_tests_output.txt", output)
    save_results(f"{results_dir}/system_tests_error.txt", error)

    # Run LangChain integration tests
    print("Running LangChain integration tests...")
    output, error = run_command("pytest ADAPT-CamelDEV-Project/tests/test_langchain_integration.py -v")
    save_results(f"{results_dir}/langchain_tests_output.txt", output)
    save_results(f"{results_dir}/langchain_tests_error.txt", error)

    # Collect performance metrics
    print("Collecting performance metrics...")
    # This is a placeholder. In a real scenario, you would collect metrics from your benchmarking tools.
    performance_metrics = {
        "github_model": {
            "average_response_time": 0.5,
            "tokens_per_second": 100
        },
        "gemini_model": {
            "average_response_time": 0.4,
            "tokens_per_second": 120
        }
    }
    save_results(f"{results_dir}/performance_metrics.json", json.dumps(performance_metrics, indent=2))

    print(f"All tests completed. Results saved in {results_dir}")

if __name__ == "__main__":
    main()