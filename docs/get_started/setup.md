Skip to main content

__Back to top

__ `Ctrl`+`K`

[ ![](https://raw.githubusercontent.com/camel-
ai/camel/master/misc/primary_logo.png) CAMEL 0.1.9 ](../index.html)

Get Started

  * Installation and Setup

Agents

  * [Creating Your First Agent](../agents/single_agent.html)
  * [Creating Your First Agent Society](../agents/role_playing.html)
  * [Embodied Agents](../agents/embodied_agents.html)
  * [Critic Agents and Tree Search](../agents/critic_agents_and_tree_search.html)

Key Modules

  * [Loaders](../key_modules/loaders.html)
  * [Storages](../key_modules/storages.html)
  * [Embeddings](../key_modules/embeddings.html)
  * [Retrievers](../key_modules/retrievers.html)

Tutorial and Cookbooks

  * [🐫 Agents with RAG](../tutorials_and_cookbooks/agents_with_rag.html)

API References

  * [camel](../modules.html) __
    * [Camel Package](../camel.html) __
      * [camel.agents package](../camel.agents.html)
      * [camel.prompts package](../camel.prompts.html)

__

  * [ __ .md ](../_sources/get_started/setup.md "Download source file")
  * __ .pdf

__

# Installation and Setup

##  Contents

  * 🕹 Installation
    * [Option 1] Install from PyPI
    * [Option 2] Install from Source
      * Install from Source with Poetry
      * Install from Source with Conda and Pip
  * 🕹 API Setup
    * [Option 1] Using OpenAI API
      * Unix-like System (Linux / MacOS)
      * Windows
    * [Option 2] Using Local Models
      * Example: Using Ollama to set Llama 3 locally

# Installation and Setup#

## 🕹 Installation#

### [Option 1] Install from PyPI#

To install the base CAMEL library:

    
    
    pip install camel-ai
    

Some features require extra dependencies:

  * To install with all dependencies:
    
        pip install 'camel-ai[all]'
    

  * To use the HuggingFace agents:
    
        pip install 'camel-ai[huggingface-agent]'
    

  * To enable RAG or use agent memory:
    
        pip install 'camel-ai[tools]'
    

### [Option 2] Install from Source#

#### Install from Source with Poetry#

    
    
    # Make sure your python version is later than 3.10
    # You can use pyenv to manage multiple python verisons in your sytstem
    
    # Clone github repo
    git clone https://github.com/camel-ai/camel.git
    
    # Change directory into project directory
    cd camel
    
    # If you didn't install peotry before
    pip install poetry  # (Optional)
    
    # We suggest using python 3.10
    poetry env use python3.10  # (Optional)
    
    # Activate CAMEL virtual environment
    poetry shell
    
    # Install the base CAMEL library
    # It takes about 90 seconds
    poetry install
    
    # Install CAMEL with all dependencies
    poetry install -E all  # (Optional)
    
    # Exit the virtual environment
    exit
    

#### Install from Source with Conda and Pip#

    
    
    # Create a conda virtual environment
    conda create --name camel python=3.10
    
    # Activate CAMEL conda environment
    conda activate camel
    
    # Clone github repo
    git clone -b v0.1.9 https://github.com/camel-ai/camel.git
    
    # Change directory into project directory
    cd camel
    
    # Install CAMEL from source
    pip install -e .
    
    # Or if you want to use all other extra packages
    pip install -e '.[all]' # (Optional)
    

## 🕹 API Setup#

Our agents can be deployed with either OpenAI API or your local models.

### [Option 1] Using OpenAI API#

Assessing the OpenAI API requires the API key, which you may obtained from
[here](https://platform.openai.com/account/api-keys). We here provide
instructions for different OS.

#### Unix-like System (Linux / MacOS)#

    
    
    echo 'export OPENAI_API_KEY="your_api_key"' >> ~/.zshrc
    
    # If you are using other proxy services like Azure
    echo 'export OPENAI_API_BASE_URL="your_base_url"' >> ~/.zshrc # (Optional)
    
    # Let the change take place
    source ~/.zshrc
    

Replace `~/.zshrc` with `~/.bashrc` if you are using bash.

#### Windows#

If you are using Command Prompt:

    
    
    set OPENAI_API_KEY="your_api_key"
    
    # If you are using other proxy services like Azure
    set OPENAI_API_BASE_URL="your_base_url" # (Optional)
    

Or if you are using PowerShell:

    
    
    $env:OPENAI_API_KEY="your_api_key"
    
    # If you are using other proxy services like Azure
    $env:OPENAI_API_BASE_URL="your_base_url" # (Optional)
    

These commands on Windows will set the environment variable for the duration
of that particular Command Prompt or PowerShell session only. You may use
`setx` or change the system properties dialog for the change to take place in
all the new sessions.

### [Option 2] Using Local Models#

In the current landscape, for those seeking highly stable content generation,
OpenAI’s GPT-3.5 turbo, GPT-4o are often recommended. However, the field is
rich with many other outstanding open-source models that also yield
commendable results. CAMEL can support developers to delve into integrating
these open-source large language models (LLMs) to achieve project outputs
based on unique input ideas.

#### Example: Using Ollama to set Llama 3 locally#

  * Download [Ollama](https://ollama.com/download).

  * After setting up Ollama, pull the Llama3 model by typing the following command into the terminal:

    
    
    ollama pull llama3
    

  * Create a ModelFile similar the one below in your project directory.

    
    
    FROM llama3
    
    # Set parameters
    PARAMETER temperature 0.8
    PARAMETER stop Result
    
    # Sets a custom system message to specify the behavior of the chat assistant
    
    # Leaving it blank for now.
    
    SYSTEM """ """
    

  * Create a script to get the base model (llama3) and create a custom model using the ModelFile above. Save this as a .sh file:

    
    
    #!/bin/zsh
    
    # variables
    model_name="llama3"
    custom_model_name="camel-llama3"
    
    #get the base model
    ollama pull $model_name
    
    #create the model file
    ollama create $custom_model_name -f ./Llama3ModelFile
    

  * Navigate to the directory where the script and ModelFile are located and run the script. Enjoy your Llama3 model, enhanced by CAMEL’s excellent agents.

    
    
    from camel.agents import ChatAgent
    from camel.messages import BaseMessage
    from camel.models import ModelFactory
    from camel.types import ModelPlatformType
    
    ollama_model = ModelFactory.create(
        model_platform=ModelPlatformType.OLLAMA,
        model_type="llama3",
        url="http://localhost:11434/v1",
        model_config_dict={"temperature": 0.4},
    )
    
    assistant_sys_msg = BaseMessage.make_assistant_message(
        role_name="Assistant",
        content="You are a helpful assistant.",
    )
    agent = ChatAgent(assistant_sys_msg, model=ollama_model, token_limit=4096)
    
    user_msg = BaseMessage.make_user_message(
        role_name="User", content="Say hi to CAMEL"
    )
    assistant_response = agent.step(user_msg)
    print(assistant_response.msg.content)
    

[ __ previous Welcome to CAMEL’s documentation! ](../index.html "previous
page") [ next Creating Your First Agent __](../agents/single_agent.html "next
page")

__Contents

  * 🕹 Installation
    * [Option 1] Install from PyPI
    * [Option 2] Install from Source
      * Install from Source with Poetry
      * Install from Source with Conda and Pip
  * 🕹 API Setup
    * [Option 1] Using OpenAI API
      * Unix-like System (Linux / MacOS)
      * Windows
    * [Option 2] Using Local Models
      * Example: Using Ollama to set Llama 3 locally

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

