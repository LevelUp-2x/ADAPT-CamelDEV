import os
import time
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import requests
import google.generativeai as genai
import markdown

print("Starting application...")

app = Flask(__name__)

print("Loading environment variables...")
load_dotenv()

print("Configuring API keys and endpoints...")
# GitHub Models configuration
GITHUB_MODELS_TOKEN = os.getenv("GitHub_ADAPT-Chase_MODELS_TOKEN")
GITHUB_MODELS_ENDPOINT = os.getenv("GITHUB_MODELS_ENDPOINT")
GITHUB_MODELS = {
    "Meta": {
        "Meta-Llama-3-70B-Instruct": "Meta-Llama-3-70B-Instruct",
        "Meta-Llama-3-8B-Instruct": "Meta-Llama-3-8B-Instruct",
        "Meta-Llama-3.1-405B-Instruct": "Meta-Llama-3.1-405B-Instruct",
        "Meta-Llama-3.1-70B-Instruct": "Meta-Llama-3.1-70B-Instruct",
        "Meta-Llama-3.1-8B-Instruct": "Meta-Llama-3.1-8B-Instruct"
    },
    "Mistral": {
        "Mistral-large": "Mistral-large",
        "Mistral-large-2407": "Mistral-large-2407",
        "Mistral-Nemo": "Mistral-Nemo",
        "Mistral-small": "Mistral-small"
    },
    "GPT": {
        "gpt-4o": "gpt-4o",
        "gpt-4o-mini": "gpt-4o-mini"
    },
    "Phi": {
        "Phi-3-medium-128k-instruct": "Phi-3-medium-128k-instruct",
        "Phi-3-medium-4k-instruct": "Phi-3-medium-4k-instruct",
        "Phi-3-mini-128k-instruct": "Phi-3-mini-128k-instruct",
        "Phi-3-mini-4k-instruct": "Phi-3-mini-4k-instruct",
        "Phi-3-small-128k-instruct": "Phi-3-small-128k-instruct",
        "Phi-3-small-8k-instruct": "Phi-3-small-8k-instruct",
        "Phi-3.5-mini-instruct": "Phi-3.5-mini-instruct"
    }
}

# Gemini configuration
GEMINI_API_KEY = os.getenv("Gemini_Studio_CHASE_API_KEY")
GEMINI_MODELS = {
    "Pro": ["gemini-1.0-pro", "gemini-1.0-pro-001", "gemini-1.0-pro-latest"]
}

print(f"GitHub Models Token: {GITHUB_MODELS_TOKEN[:5] if GITHUB_MODELS_TOKEN else 'Not set'}...")
print(f"GitHub Models Endpoint: {GITHUB_MODELS_ENDPOINT}")
print(f"GitHub Model Families: {', '.join(GITHUB_MODELS.keys())}")
print(f"Gemini API Key: {GEMINI_API_KEY[:5] if GEMINI_API_KEY else 'Not set'}...")
print(f"Gemini Model Families: {', '.join(GEMINI_MODELS.keys())}")

def github_models_chat(prompt, model_family, model):
    print(f"Sending request to GitHub Models ({model_family} - {model}): {prompt[:50]}...")
    headers = {
        "Authorization": f"Bearer {GITHUB_MODELS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "model": GITHUB_MODELS[model_family][model],
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(GITHUB_MODELS_ENDPOINT, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        raise Exception(f"Error with GitHub Models API: {response.text}")

def gemini_chat(prompt, model_family, model):
    print(f"Sending request to Gemini ({model_family} - {model}): {prompt[:50]}...")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt)
    return response.text

def format_response(response):
    # Convert markdown to HTML
    html = markdown.markdown(response)
    # Wrap the HTML in a div for styling
    return f'<div class="markdown-body">{html}</div>'

@app.route('/')
def index():
    print("Rendering index page...")
    return render_template('index.html', github_models=GITHUB_MODELS, gemini_models=GEMINI_MODELS)

@app.route('/chat', methods=['POST'])
def chat():
    print("Received chat request...")
    data = request.json
    prompt = data['prompt']
    model_family = data['model_family']
    model = data['model']

    start_time = time.time()
    try:
        if model_family in GITHUB_MODELS:
            response = github_models_chat(prompt, model_family, model)
            model_name = f"GitHub Models ({model_family} - {model})"
        elif model_family in GEMINI_MODELS:
            response = gemini_chat(prompt, model_family, model)
            model_name = f"Gemini ({model_family} - {model})"
        else:
            return jsonify({"error": "Invalid model selection"}), 400

        end_time = time.time()
        response_time = round(end_time - start_time, 2)
        formatted_response = format_response(response)
        print(f"Sending response: {response[:50]}...")
        return jsonify({
            "response": f"[{model_name}] {formatted_response}",
            "response_time": f"Response time: {response_time} seconds"
        })
    except Exception as e:
        end_time = time.time()
        response_time = round(end_time - start_time, 2)
        print(f"Error occurred: {str(e)}")
        return jsonify({
            "error": str(e),
            "response_time": f"Response time: {response_time} seconds"
        }), 500

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(debug=True)

print("Application setup complete.")