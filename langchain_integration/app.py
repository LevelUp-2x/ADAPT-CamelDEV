from flask import Flask, request, jsonify, render_template
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import google.generativeai as genai
import os
import requests
import logging
from dotenv import load_dotenv

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
try:
    openai_model = ChatOpenAI(model_name="gpt-3.5-turbo")
    openai_memory = ConversationBufferMemory(return_messages=True)
    openai_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant."),
        ("human", "{input}"),
        ("ai", "{agent_scratchpad}")
    ])
    openai_chain = LLMChain(llm=openai_model, prompt=openai_prompt, memory=openai_memory)
    logging.info("OpenAI model initialized successfully")
except Exception as e:
    logging.error(f"Error initializing OpenAI model: {str(e)}")
    openai_chain = None

try:
    huggingface_model = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.5, "max_length": 512})
    huggingface_memory = ConversationBufferMemory(return_messages=True)
    huggingface_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant."),
        ("human", "{input}"),
        ("ai", "{agent_scratchpad}")
    ])
    huggingface_chain = LLMChain(llm=huggingface_model, prompt=huggingface_prompt, memory=huggingface_memory)
    logging.info("HuggingFace model initialized successfully")
except Exception as e:
    logging.error(f"Error initializing HuggingFace model: {str(e)}")
    huggingface_chain = None

try:
    gemini_model = genai.GenerativeModel('gemini-pro')
    logging.info("Gemini model initialized successfully")
except Exception as e:
    logging.error(f"Error initializing Gemini model: {str(e)}")
    gemini_model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multi_agent_chat', methods=['POST'])
def multi_agent_chat():
    data = request.json
    user_message = data.get('message', '')
    logging.info(f"Received user message: {user_message}")

    responses = []

    # OpenAI model
    if openai_chain:
        try:
            openai_response = openai_chain.run(input=user_message)
            responses.append({"agent": "OpenAI", "response": openai_response})
            logging.info("OpenAI model responded successfully")
        except Exception as e:
            logging.error(f"Error with OpenAI model: {str(e)}")
            responses.append({"agent": "OpenAI", "response": "Error occurred"})

    # HuggingFace model
    if huggingface_chain:
        try:
            huggingface_response = huggingface_chain.run(input=user_message)
            responses.append({"agent": "HuggingFace", "response": huggingface_response})
            logging.info("HuggingFace model responded successfully")
        except Exception as e:
            logging.error(f"Error with HuggingFace model: {str(e)}")
            responses.append({"agent": "HuggingFace", "response": "Error occurred"})

    # Gemini model
    if gemini_model:
        try:
            gemini_response = gemini_model.generate_content(user_message)
            responses.append({"agent": "Gemini", "response": gemini_response.text})
            logging.info("Gemini model responded successfully")
        except Exception as e:
            logging.error(f"Error with Gemini model: {str(e)}")
            responses.append({"agent": "Gemini", "response": "Error occurred"})

    # GitHub model (example with GPT-4)
    try:
        github_response = requests.post(
            f"{GITHUB_MODELS_ENDPOINT}/completions",
            headers={"Authorization": f"Bearer {GITHUB_MODELS_TOKEN}"},
            json={"model": "gpt-4", "prompt": user_message, "max_tokens": 150}
        )
        if github_response.status_code == 200:
            github_text = github_response.json()['choices'][0]['text']
            responses.append({"agent": "GitHub GPT-4", "response": github_text})
            logging.info("GitHub model responded successfully")
        else:
            logging.error(f"Error with GitHub model API call: {github_response.status_code}")
            responses.append({"agent": "GitHub GPT-4", "response": "Error in API call"})
    except Exception as e:
        logging.error(f"Error with GitHub model: {str(e)}")
        responses.append({"agent": "GitHub GPT-4", "response": "Error occurred"})

    return jsonify({"responses": responses})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)