she's like yeah yeah yeah I know I know he's like no this is fucking serious and she goes out right out it was so funny# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8002 available to the world outside this container
EXPOSE 8002

# Define environment variable
ENV ADAPT_ENV=production

# Run graph_rag_service.py when the container launches
CMD ["python", "langchain_integration/graph_rag_service.py"]