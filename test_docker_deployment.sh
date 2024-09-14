#!/bin/bash

set -e

echo "Building and starting ADAPT-CamelDEV Docker container..."

# Navigate to the project directory
cd "$(dirname "$0")"

# Build and start the Docker container
docker-compose up --build -d

echo "Docker container is now running. You can access the application at http://localhost:5000"
echo "To stop the container, run: docker-compose down"
echo "To view logs, run: docker-compose logs -f"