#!/bin/bash

set -e
set -x

echo "Starting ADAPT-CamelDEV setup..."

# Check if python3 is available
if command -v python3 &>/dev/null; then
    PYTHON_CMD=python3
elif command -v python &>/dev/null; then
    PYTHON_CMD=python
else
    echo "Error: Python is not installed or not in PATH"
    exit 1
fi

echo "Using Python command: $PYTHON_CMD"
$PYTHON_CMD --version

# Install pip if not available
if ! $PYTHON_CMD -m pip --version &>/dev/null; then
    echo "pip not found. Installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $PYTHON_CMD get-pip.py
    rm get-pip.py
fi

echo "Installing dependencies..."
$PYTHON_CMD -m pip install -r requirements.txt

echo "Loading environment variables..."
if [ -f .env ]; then
    export $(cat .env | xargs)
    echo "Environment variables loaded successfully"
else
    echo "Warning: .env file not found"
fi

echo "Starting the Flask application..."
$PYTHON_CMD langchain_integration/app.py