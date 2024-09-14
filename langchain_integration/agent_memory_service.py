from flask import Flask, request, jsonify
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.llms import HuggingFaceHub
import logging
from logging.handlers import RotatingFileHandler
import os
from service_discovery import ServiceDiscovery
from config import get_config
import threading
import time

app = Flask(__name__)

# Configure logging
handler = RotatingFileHandler('agent_memory_service.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# Initialize service discovery
sd = ServiceDiscovery()
SERVICE_NAME = 'agent_memory_service'
SERVICE_HOST = '0.0.0.0'
SERVICE_PORT = get_config('AGENT_MEMORY_SERVICE_PORT')

# Initialize language model for summary memory
os.environ["HUGGINGFACEHUB_API_TOKEN"] = get_config('HUGGINGFACEHUB_API_TOKEN')
llm = HuggingFaceHub(repo_id="google/flan-t5-base", model_kwargs={"temperature": 0.5, "max_length": 512})

# Initialize memories
short_term_memory = ConversationBufferMemory(k=5)  # Keeps last 5 interactions
long_term_memory = ConversationSummaryMemory(llm=llm)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/store_memory', methods=['POST'])
def store_memory():
    data = request.json
    human_input = data.get('human_input')
    ai_output = data.get('ai_output')
    
    app.logger.info(f"Storing memory: Human: {human_input}, AI: {ai_output}")
    
    try:
        # Store in short-term memory
        short_term_memory.save_context({"human_input": human_input}, {"ai_output": ai_output})
        
        # Store in long-term memory
        long_term_memory.save_context({"human_input": human_input}, {"ai_output": ai_output})
        
        return jsonify({"message": "Memory stored successfully"}), 200
    except Exception as e:
        app.logger.error(f"Error storing memory: {str(e)}")
        return jsonify({"error": "An error occurred while storing memory"}), 500

@app.route('/retrieve_memory', methods=['GET'])
def retrieve_memory():
    try:
        # Retrieve short-term memory
        short_term = short_term_memory.load_memory_variables({})
        
        # Retrieve long-term memory
        long_term = long_term_memory.load_memory_variables({})
        
        return jsonify({
            "short_term_memory": short_term,
            "long_term_memory": long_term
        }), 200
    except Exception as e:
        app.logger.error(f"Error retrieving memory: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving memory"}), 500

@app.route('/clear_memory', methods=['POST'])
def clear_memory():
    try:
        # Clear both short-term and long-term memory
        short_term_memory.clear()
        long_term_memory.clear()
        
        return jsonify({"message": "Memory cleared successfully"}), 200
    except Exception as e:
        app.logger.error(f"Error clearing memory: {str(e)}")
        return jsonify({"error": "An error occurred while clearing memory"}), 500

def heartbeat():
    while True:
        sd.heartbeat(SERVICE_NAME, SERVICE_HOST, SERVICE_PORT)
        time.sleep(10)  # Send heartbeat every 10 seconds

if __name__ == '__main__':
    # Register service
    sd.register_service(SERVICE_NAME, SERVICE_HOST, SERVICE_PORT)
    
    # Start heartbeat thread
    threading.Thread(target=heartbeat, daemon=True).start()
    
    app.run(host=SERVICE_HOST, port=SERVICE_PORT, debug=get_config('DEBUG'))

    # Deregister service on shutdown
    sd.deregister_service(SERVICE_NAME)