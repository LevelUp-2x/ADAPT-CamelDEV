# Setup and Run CAMEL Script

# Check Python version
$pythonVersion = python --version
Write-Host "Current Python version: $pythonVersion"
if ($pythonVersion -notmatch "Python 3.10"){
  Write-Host "Python 3.10 or later is required. Please install or select the correct Python version."
  exit 1
}

# Create conda environment
conda create --name adapt-cameldev python=3.10 -y

# Activate conda environment
conda activate adapt-cameldev

# Navigate to the project directory
Set-Location C:\\Users\\ChaseRemmen\\ADAPT\\ADAPT-CamelDEV

# Install CAMEL with all dependencies
pip install -e '.[all]'

# Set up API keys
$env:GITHUB_MODELS_TOKEN = "your_github_token"
$env:Gemini_Studio_CHASE_API_KEY = "your_gemini_api_key"

# Verify CAMEL installation
Write-Host "Verifying CAMEL installation..."
python -c "import camel; print(f'CAMEL version: {camel.__version__}')"

# Run unit tests
Write-Host "Running unit tests..."
python -m unittest discover -v tests

# Create a test script
$testScript = @"
from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelType, ModelPlatformType
import os

def test_camel():
    # Set up the Gemini model
    gemini_model = ModelFactory.create(
        model_platform=ModelPlatformType.GEMINI,
        model_type=ModelType.GEMINI_1_5_PRO,
        model_config_dict={"temperature": 0.7},
        api_key=os.getenv('Gemini_Studio_CHASE_API_KEY')
    )

    # Create a chat agent with the Gemini model
    assistant_sys_msg = BaseMessage.make_assistant_message(
        role_name="Assistant",
        content="You are a helpful assistant with expertise in AI and machine learning.",
    )
    gemini_agent = ChatAgent(assistant_sys_msg, model=gemini_model)

    # Test the Gemini agent
    user_msg = BaseMessage.make_user_message(
        role_name="User", content="Explain the concept of transfer learning in AI."
    )
    gemini_response = gemini_agent.step(user_msg)
    print("Gemini response:", gemini_response.msg.content)

    # Set up the GitHub model
    github_model = ModelFactory.create(
        model_platform=ModelPlatformType.GITHUB,
        model_type=ModelType.AI21_JUMBO_INSTRUCT,
        model_config_dict={},
        api_key=os.getenv('GITHUB_MODELS_TOKEN')
    )

    # Create a chat agent with the GitHub model
    github_agent = ChatAgent(assistant_sys_msg, model=github_model)

    # Test the GitHub agent
    user_msg = BaseMessage.make_user_message(
        role_name="User", content="What are some best practices for code documentation?"
    )
    github_response = github_agent.step(user_msg)
    print("GitHub response:", github_response.msg.content)

if __name__ == "__main__":
    test_camel()
"@

$testScript | Out-File -FilePath "camel_example.py" -Encoding utf8

Write-Host "Running CAMEL example..."
python camel_example.py

Write-Host "Setup and test run completed."