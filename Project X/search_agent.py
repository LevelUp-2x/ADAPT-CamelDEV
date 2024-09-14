import os
import requests
import json
from dotenv import load_dotenv
from duckduckgo_search import DDGS
from logger import logger
import wikipedia
from tenacity import retry, stop_after_attempt, wait_exponential
from functools import lru_cache

print("Starting search_agent.py")

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)
print("Environment variables loaded")

# GitHub Models configuration
GITHUB_MODELS_TOKEN = os.getenv("GitHub_ADAPT-Chase_MODELS_TOKEN")
GITHUB_MODELS_ENDPOINT = os.getenv("GITHUB_MODELS_ENDPOINT")
GITHUB_MODEL = os.getenv("META_LLAMA_3_70B_INSTRUCT")

# API keys for tools
WOLFRAM_ALPHA_APP_ID = os.getenv("WOLFRAM_ALPHA_APP_ID")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
OWM_API_KEY = os.getenv("OWM_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
ALGOLIA_APP_ID = os.getenv("Algolia_Application_ID")
ALGOLIA_API_KEY = os.getenv("Algolia_Search_API_KEY")

print("API keys loaded")

# Initialize API clients
# ... (rest of the initialization code remains unchanged)

logger.info(f"GitHub Models Token: {GITHUB_MODELS_TOKEN[:5] if GITHUB_MODELS_TOKEN else 'Not set'}...")
logger.info(f"GitHub Models Endpoint: {GITHUB_MODELS_ENDPOINT}")
logger.info(f"GitHub Model: {GITHUB_MODEL}")

# ... (rest of the search functions remain unchanged)

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def github_models_chat(prompt):
    print(f"Sending request to GitHub Models: {prompt[:50]}...")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GITHUB_MODELS_TOKEN}"
    }
    data = {
        "model": GITHUB_MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(GITHUB_MODELS_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        logger.error(f"Error with GitHub Models API: {str(e)}")
        raise Exception(f"Error with GitHub Models API: {str(e)}")

def search_agent(question):
    logger.info(f"Received question: {question}")
    print(f"Processing question: {question}")
    
    try:
        # Perform searches using different tools
        duckduckgo_results = search_duckduckgo(question)
        wikipedia_result = search_wikipedia(question)
        wolfram_result = search_wolfram_alpha(question)
        news_results = search_news(question)
        google_results = search_google(question)
        stackoverflow_results = search_stack_overflow(question)
        weather_result = get_weather("New York")  # Default to New York, can be made dynamic
        serper_results = search_serper(question)
        tavily_results = search_tavily(question)
        algolia_results = search_algolia(question)

        print("All searches completed")

        # Construct prompt for the language model
        prompt = f"""Given the following search results, please answer the question: "{question}"

DuckDuckGo Results:
{duckduckgo_results}

Wikipedia Result:
{wikipedia_result}

Wolfram Alpha Result:
{wolfram_result}

News Results:
{news_results}

Google Results:
{google_results}

Stack Overflow Results:
{stackoverflow_results}

Weather in New York:
{weather_result}

Serper Results:
{serper_results}

Tavily Results:
{tavily_results}

Algolia Results:
{algolia_results}

Please provide a concise and informative answer based on all the available search results. If the exact information is not available, provide the most relevant information you can find and suggest how the user might obtain more accurate or up-to-date information."""

        print("Prompt constructed, sending to GitHub Models API")

        # Get response from GitHub Models API
        answer = github_models_chat(prompt)
        
        logger.info(f"Generated answer: {answer}")
        print("Answer generated")
        return answer
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")
        return f"An error occurred while processing your request: {str(e)}"

if __name__ == "__main__":
    print("Starting main execution")
    while True:
        question = input("Enter your question (or 'quit' to exit): ")
        if question.lower() == 'quit':
            break
        result = search_agent(question)
        print(f"Answer: {result}\n")
    print("Execution completed")