#!/bin/bash

# Start RAG Service
uvicorn src.rag_service.rag_service:app --host 0.0.0.0 --port 8001 &

# Start Graph RAG Service
uvicorn src.graph_rag_service.graph_rag_service:app --host 0.0.0.0 --port 8002 &

# Start Agent Memory Service
uvicorn src.agent_memory_service.agent_memory_service:app --host 0.0.0.0 --port 8003 &

# Start main application
python main.py &

echo "All DABSTER services have been started."
echo "Main application is running on http://localhost:8000"
echo "RAG Service is running on http://localhost:8001"
echo "Graph RAG Service is running on http://localhost:8002"
echo "Agent Memory Service is running on http://localhost:8003"

# Wait for all background processes to finish
wait