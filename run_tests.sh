#!/bin/bash

# Build and start the Docker containers in detached mode
echo "Building and starting Docker containers..."
docker-compose up -d

# Wait for services to start
echo "Waiting for services to start..."
sleep 30

# Run tests
echo "Running tests..."
docker-compose run test

# Stop and remove the Docker containers
echo "Stopping and removing Docker containers..."
docker-compose down

echo "Test run completed."