from flask import Flask, request, jsonify, render_template
import os
import requests
import logging
from dotenv import load_dotenv
import time
import google.generativeai as genai

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log')

# Load environment variables
load_dotenv()

# Configure API keys
GITHUB_MODELS_TOKEN = os.getenv("GitHub_ADAPT-Chase_MODELS_TOKEN")
GITHUB_MODELS_ENDPOINT = os.getenv("GITHUB_MODELS_ENDPOINT")
GEMINI_API_KEY = os.getenv("Gemini_Studio_CHASE_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize models
github_models = [
    "ai21-jumbo-instruct", "cohere-command-r", "cohere-command-r-plus", "meta-llama-3-70b-instruct",
    "meta-llama-3-8b-instruct", "meta-llama-11-40b-instruct", "meta-llama-31-70b-instruct",
    "meta-llama-31-8b-instruct", "mixtral-large", "mixtral-large-2407", "mistral-memo", "mistral-small",
    "gpt-4o", "gpt-4o-mini", "phi-3-medium-instruct-12b", "phi-3-medium-instruct-4b",
    "phi-3-mini-instruct-3.5b", "phi-3-mini-instruct-4k", "phi-3-small-instruct-3.5b",
    "phi-3-small-instruct-8k", "phi-3.5-mini-instruct-3.5b"
]

gemini_models = [
    "gemini-pro", "gemini-1.5-pro", "gemini-1.5-pro-latest", "gemini-1.5-pro-001",
    "gemini-1.5-flash", "gemini-1.5-flash-latest", "gemini-1.5-flash-001"
]

@app.route('/')
def index():
    return render_template('index.html', github_models=github_models, gemini_models=gemini_models)

@app.route('/multi_agent_chat', methods=['POST'])
def multi_agent_chat():
    data = request.json
    user_message = data.get('message', '')
    selected_models = data.get('models', [])
    num_loops = data.get('num_loops', 1)
    
    logging.info(f"Received request: message='{user_message}', models={selected_models}, num_loops={num_loops}")

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    responses = []

    for loop in range(num_loops):
        loop_responses = []
        for model in selected_models:
            try:
                start_time = time.time()
                if model in github_models:
                    response = get_github_model_response(model, user_message)
                elif model in gemini_models:
                    response = get_gemini_model_response(model, user_message)
                else:
                    raise ValueError(f"Unsupported model: {model}")
                
                end_time = time.time()
                response_time = end_time - start_time
                loop_responses.append({"agent": model, "response": response, "responseTime": response_time, "loop": loop + 1})
                logging.info(f"Loop {loop + 1}: {model} responded successfully in {response_time:.2f} seconds")
            except Exception as e:
                logging.error(f"Loop {loop + 1}: Error with {model} model: {str(e)}")
                loop_responses.append({"agent": model, "response": f"Error occurred: {str(e)}", "responseTime": 0, "loop": loop + 1})
        
        responses.extend(loop_responses)
        if loop < num_loops - 1:
            # Prepare the next user message based on the responses from this loop
            user_message = prepare_next_message(user_message, loop_responses)

    return jsonify({"responses": responses})

def get_github_model_response(model, user_message):
    response = requests.post(
        GITHUB_MODELS_ENDPOINT,
        headers={"Authorization": f"Bearer {GITHUB_MODELS_TOKEN}"},
        json={"model": model, "messages": [{"role": "user", "content": user_message}]}
    )
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        raise Exception(f"GitHub API error: {response.status_code} - {response.text}")

def get_gemini_model_response(model, user_message):
    gemini_model = genai.GenerativeModel(model)
    response = gemini_model.generate_content(user_message)
    return response.text

def prepare_next_message(original_message, responses):
    # Combine the original message with a summary of the responses
    summary = "\n".join([f"{r['agent']}: {r['response']}" for r in responses])
    return f"Original question: {original_message}\n\nPrevious responses:\n{summary}\n\nBased on these responses, please provide your thoughts or ask for clarification if needed."

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)