from flask import Flask, request, jsonify, render_template
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import google.generativeai as genai
import os
import requests
import logging
from dotenv import load_dotenv
import time
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log')

# Load environment variables
load_dotenv()

# Configure API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GITHUB_MODELS_TOKEN = os.getenv("GITHUB_MODELS_TOKEN")
GITHUB_MODELS_ENDPOINT = os.getenv("GITHUB_MODELS_ENDPOINT")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize models and chains
models = {}

def initialize_models():
    try:
        if OPENAI_API_KEY:
            models['openai'] = {
                'gpt-3.5-turbo': ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY),
                'gpt-4': ChatOpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY)
            }
            logging.info("OpenAI models initialized successfully")
        else:
            logging.warning("OpenAI API key not found. OpenAI models will not be available.")
    except Exception as e:
        logging.error(f"Error initializing OpenAI models: {str(e)}")

    try:
        if HUGGINGFACEHUB_API_TOKEN:
            models['huggingface'] = {
                'flan-t5-xxl': HuggingFaceEndpoint(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.5, "max_length": 512}, huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN),
                'flan-t5-xl': HuggingFaceEndpoint(repo_id="google/flan-t5-xl", model_kwargs={"temperature": 0.5, "max_length": 512}, huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN)
            }
            logging.info("HuggingFace models initialized successfully")
        else:
            logging.warning("HuggingFace API token not found. HuggingFace models will not be available.")
    except Exception as e:
        logging.error(f"Error initializing HuggingFace models: {str(e)}")

    try:
        if GEMINI_API_KEY:
            models['gemini'] = {
                'gemini-pro': genai.GenerativeModel('gemini-pro')
            }
            logging.info("Gemini model initialized successfully")
        else:
            logging.warning("Gemini API key not found. Gemini model will not be available.")
    except Exception as e:
        logging.error(f"Error initializing Gemini model: {str(e)}")

    # Commenting out Mistral models due to access issues
    # try:
    #     models['mistral'] = {
    #         'mistral-nemo': AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1"),
    #         'mistral-light': AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1"),
    #         'mistral-medium': AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2"),
    #         'mistral-heavy': AutoModelForCausalLM.from_pretrained("mistralai/Mistral-8x7B-Instruct-v0.1")
    #     }
    #     logging.info("Mistral models initialized successfully")
    # except Exception as e:
    #     logging.error(f"Error initializing Mistral models: {str(e)}")

initialize_models()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multi_agent_chat', methods=['POST'])
def multi_agent_chat():
    data = request.json
    user_message = data.get('message', '')
    model_family = data.get('modelFamily', '')
    model_name = data.get('model', '')
    tool = data.get('tool', 'no-tool')
    
    logging.info(f"Received request: message='{user_message}', modelFamily='{model_family}', model='{model_name}', tool='{tool}'")

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    responses = []

    if model_family and model_name:
        try:
            start_time = time.time()
            model = models[model_family][model_name]
            response = get_model_response(model, model_family, user_message, tool)
            end_time = time.time()
            response_time = end_time - start_time
            responses.append({"agent": f"{model_family}-{model_name}", "response": response, "responseTime": response_time})
            logging.info(f"{model_family}-{model_name} model responded successfully in {response_time:.2f} seconds")
        except KeyError:
            error_msg = f"Model {model_name} not found in {model_family} family"
            logging.error(error_msg)
            responses.append({"agent": f"{model_family}-{model_name}", "response": error_msg, "responseTime": 0})
        except Exception as e:
            logging.error(f"Error with {model_family}-{model_name} model: {str(e)}")
            responses.append({"agent": f"{model_family}-{model_name}", "response": f"Error occurred: {str(e)}", "responseTime": 0})
    else:
        # If no specific model is selected, use all available models
        for family, family_models in models.items():
            for name, model in family_models.items():
                try:
                    start_time = time.time()
                    response = get_model_response(model, family, user_message, tool)
                    end_time = time.time()
                    response_time = end_time - start_time
                    responses.append({"agent": f"{family}-{name}", "response": response, "responseTime": response_time})
                    logging.info(f"{family}-{name} model responded successfully in {response_time:.2f} seconds")
                except Exception as e:
                    logging.error(f"Error with {family}-{name} model: {str(e)}")
                    responses.append({"agent": f"{family}-{name}", "response": f"Error occurred: {str(e)}", "responseTime": 0})

    return jsonify({"responses": responses})

def get_model_response(model, model_family, user_message, tool):
    try:
        if model_family == 'openai':
            return model.invoke(user_message).content
        elif model_family == 'huggingface':
            return model.invoke([user_message])[0]  # Wrapping user_message in a list
        elif model_family == 'gemini':
            return model.generate_content(user_message).text
        elif model_family == 'mistral':
            tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")
            inputs = tokenizer(user_message, return_tensors="pt")
            outputs = model.generate(**inputs, max_new_tokens=100)
            return tokenizer.decode(outputs[0], skip_special_tokens=True)
        elif model_family == 'github':
            response = requests.post(
                f"{GITHUB_MODELS_ENDPOINT}/completions",
                headers={"Authorization": f"Bearer {GITHUB_MODELS_TOKEN}"},
                json={"model": "gpt-4", "prompt": user_message, "max_tokens": 150}
            )
            if response.status_code == 200:
                return response.json()['choices'][0]['text']
            else:
                raise Exception(f"GitHub API error: {response.status_code}")
        else:
            raise ValueError(f"Unsupported model family: {model_family}")
    except Exception as e:
        logging.error(f"Error in get_model_response for {model_family}: {str(e)}")
        raise

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)