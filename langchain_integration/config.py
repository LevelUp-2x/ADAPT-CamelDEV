import os

# Environment
ENV = os.environ.get('ADAPT_ENV', 'development')

# Common configurations
COMMON = {
    'REDIS_HOST': 'localhost',
    'REDIS_PORT': 6379,
    'HUGGINGFACEHUB_API_TOKEN': 'your_huggingface_token_here',
}

# Development configurations
DEVELOPMENT = {
    **COMMON,
    'DEBUG': True,
    'MAIN_APP_PORT': 5000,
    'RAG_SERVICE_PORT': 8001,
    'GRAPH_RAG_SERVICE_PORT': 8002,
    'AGENT_MEMORY_SERVICE_PORT': 8003,
}

# Production configurations
PRODUCTION = {
    **COMMON,
    'DEBUG': False,
    'MAIN_APP_PORT': int(os.environ.get('MAIN_APP_PORT', 5000)),
    'RAG_SERVICE_PORT': int(os.environ.get('RAG_SERVICE_PORT', 8001)),
    'GRAPH_RAG_SERVICE_PORT': int(os.environ.get('GRAPH_RAG_SERVICE_PORT', 8002)),
    'AGENT_MEMORY_SERVICE_PORT': int(os.environ.get('AGENT_MEMORY_SERVICE_PORT', 8003)),
}

# Testing configurations
TESTING = {
    **COMMON,
    'DEBUG': True,
    'TESTING': True,
    'MAIN_APP_PORT': 5000,
    'RAG_SERVICE_PORT': 8001,
    'GRAPH_RAG_SERVICE_PORT': 8002,
    'AGENT_MEMORY_SERVICE_PORT': 8003,
}

# Select the appropriate configuration based on the environment
if ENV == 'production':
    CONFIG = PRODUCTION
elif ENV == 'testing':
    CONFIG = TESTING
else:
    CONFIG = DEVELOPMENT

# Function to get configuration
def get_config(key):
    return CONFIG.get(key)