import os
import requests
import json
from dotenv import load_dotenv
from duckduckgo_search import DDGS
from logger import logger
import wikipedia
import wolframalpha
from newsapi import NewsApiClient
from googleapiclient.discovery import build
from PIL import Image
import io
from stackapi import StackAPI
from pyowm import OWM
from tenacity import retry, stop_after_attempt, wait_exponential

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
try:
    wolfram_client = wolframalpha.Client(WOLFRAM_ALPHA_APP_ID)
    news_api = NewsApiClient(api_key=NEWS_API_KEY)
    google_service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    stack_api = StackAPI('stackoverflow')
    owm = OWM(OWM_API_KEY)
    mgr = owm.weather_manager()
    
    # Try to import and initialize Algolia client
    try:
        from algoliasearch.search_client import SearchClient as AlgoliaSearchClient
        algolia_client = AlgoliaSearchClient.create(ALGOLIA_APP_ID, ALGOLIA_API_KEY)
        print("Algolia client initialized")
    except ImportError:
        print("Algolia client import failed. Algolia search will not be available.")
        algolia_client = None
    
    print("API clients initialized")
except Exception as e:
    print(f"Error initializing API clients: {str(e)}")
    raise

logger.info(f"GitHub Models Token: {GITHUB_MODELS_TOKEN[:10]}...")
logger.info(f"GitHub Models Endpoint: {GITHUB_MODELS_ENDPOINT}")
logger.info(f"GitHub Model: {GITHUB_MODEL}")

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def search_duckduckgo(query):
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=5)]
    return results

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def search_wikipedia(query):
    try:
        return wikipedia.summary(query, sentences=3)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found. Please be more specific. Options: {', '.join(e.options[:5])}"
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found for the given query."

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def search_wolfram_alpha(query):
    res = wolfram_client.query(query)
    try:
        return next(res.results).text
    except StopIteration:
        return "No results found on Wolfram Alpha."

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def search_news(query):
    news = news_api.get_top_headlines(q=query, language='en', page_size=5)
    return [{"title": article["title"], "description": article["description"]} for article in news["articles"]]

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def search_google(query):
    res = google_service.cse().list(q=query, cx=GOOGLE_CSE_ID, num=5).execute()
    return [{"title": item["title"], "snippet": item["snippet"]} for item in res.get("items", [])]

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def analyze_image(image_url):
    response = requests.get(image_url)
    img = Image.open(io.BytesIO(response.content))
    return f"Image size: {img.size}, Format: {img.format}, Mode: {img.mode}"

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def search_stack_overflow(query):
    questions = stack_api.fetch('search/advanced', sort='relevance', q=query, accepted=True, limit=5)
    return [{"title": q["title"], "link": q["link"]} for q in questions["items"]]

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def get_weather(location):
    observation = mgr.weather_at_place(location)
    w = observation.weather
    return f"Temperature: {w.temperature('celsius')['temp']}°C, Status: {w.detailed_status}"

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def search_serper(query):
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def search_tavily(query):
    url = "https://api.tavily.com/search"
    params = {
        "api_key": TAVILY_API_KEY,
        "query": query
    }
    response = requests.get(url, params=params)
    return response.json()

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def search_algolia(query):
    if algolia_client:
        index = algolia_client.init_index('your_index_name')  # Replace with your actual index name
        results = index.search(query)
        return results['hits']
    else:
        return "Algolia search is not available."

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def github_models_chat(prompt):
    headers = {
        "Authorization": f"Bearer {GITHUB_MODELS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "model": GITHUB_MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    logger.info(f"Sending request to GitHub Models API: {GITHUB_MODELS_ENDPOINT}")
    response = requests.post(GITHUB_MODELS_ENDPOINT, headers=headers, json=data)
    response.raise_for_status()
    logger.info(f"Response status code: {response.status_code}")
    return response.json()['choices'][0]['message']['content']

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

Please provide a concise and informative answer based on all the search results. If the exact information is not available, provide the most relevant information you can find and suggest how the user might obtain more accurate or up-to-date information."""

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
    question = "What is the latest news about artificial intelligence?"
    result = search_agent(question)
    print(f"Question: {question}")
    print(f"Answer: {result}")
    print("Execution completed")