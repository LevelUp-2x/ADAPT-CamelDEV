import subprocess
import os
from logger import logger

def run_command(command):
    logger.info(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        logger.info(f"Command output: {result.stdout}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed with error: {e}")
        logger.error(f"Error output: {e.stderr}")
        raise

def setup_project():
    # Activate conda environment
    logger.info("Activating conda environment: camel_search_env")
    run_command("conda activate camel_search_env")

    # Install required packages
    logger.info("Installing required packages")
    run_command("pip install flask==2.1.0 python-dotenv==0.19.2 requests==2.26.0 google-generativeai==0.3.1")
    
    # Install additional packages for our search agent
    logger.info("Installing additional packages for search agent")
    run_command("pip install langchain duckduckgo-search wikipedia wolframalpha newsapi-python google-api-python-client pyowm pillow stackapi")

    logger.info("Setup completed successfully")

if __name__ == "__main__":
    try:
        setup_project()
    except Exception as e:
        logger.exception("An error occurred during setup")