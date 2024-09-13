import os
from dotenv import load_dotenv
import requests
import google.generativeai as genai

print("Script started")

# Load environment variables
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path=env_path)
print("Environment variables loaded")

# GitHub Models configuration
GITHUB_MODELS_TOKEN = os.getenv("GitHub_ADAPT-Chase_MODELS_TOKEN")
GITHUB_MODELS_ENDPOINT = os.getenv("GITHUB_MODELS_ENDPOINT")
GITHUB_MODEL = os.getenv("META_LLAMA_3_70B_INSTRUCT")  # You can change this to any other GitHub model

# Gemini configuration
GEMINI_API_KEY = os.getenv("Gemini_Studio_CHASE_API_KEY")
GEMINI_MODEL = "gemini-1.0-pro"  # You can change this to any other Gemini model

def github_models_chat(prompt):
    headers = {
        "Authorization": f"Bearer {GITHUB_MODELS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "model": GITHUB_MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(GITHUB_MODELS_ENDPOINT, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        raise Exception(f"Error with GitHub Models API: {response.text}")

def gemini_chat(prompt):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(GEMINI_MODEL)
    response = model.generate_content(prompt)
    return response.text

def chat_with_model(prompt, model_choice="github"):
    if model_choice == "github":
        return github_models_chat(prompt)
    elif model_choice == "gemini":
        return gemini_chat(prompt)
    else:
        raise ValueError("Invalid model choice. Choose 'github' or 'gemini'.")

print("Testing models...")

try:
    # Test GitHub Models
    github_response = chat_with_model("Say hello!", "github")
    print("Response from GitHub Models:")
    print(github_response)

    # Test Gemini
    gemini_response = chat_with_model("Say hello!", "gemini")
    print("Response from Gemini:")
    print(gemini_response)

except Exception as e:
    print(f"Error while testing models: {str(e)}")
    raise

print("Script complete")