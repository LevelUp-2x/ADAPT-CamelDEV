import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAI
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.prompts import ChatPromptTemplate
from langchain.schema import AgentAction, AgentFinish
from typing import List, Union
import re
import ray
from PIL import Image
import io

print("Script started")

# Get the full path of the .env file
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
print(f"Attempting to load .env file from: {env_path}")

# Check if the .env file exists
if os.path.exists(env_path):
    print(f".env file found at {env_path}")
else:
    print(f".env file not found at {env_path}")

# Load environment variables
try:
    load_dotenv(dotenv_path=env_path)
    print("Environment variables loaded successfully")
except Exception as e:
    print(f"Error loading .env file: {e}")

# Print environment variables for debugging
print("AZURE_OPENAI_ENDPOINT:", os.getenv("AZURE_OPENAI_ENDPOINT"))
print("AZURE_OPENAI_API_KEY:", os.getenv("AZURE_OPENAI_API_KEY"))
print("AZURE_OPENAI_API_VERSION:", os.getenv("AZURE_OPENAI_API_VERSION"))
print("AZURE_DEPLOYMENT_NAME:", os.getenv("AZURE_DEPLOYMENT_NAME"))
print("AZURE_MODEL_NAME:", os.getenv("AZURE_MODEL_NAME"))

print("Initializing Ray")
# Initialize Ray for distributed computing
ray_address = os.getenv("RAY_ADDRESS")
if ray_address:
    ray.init(address=ray_address)
else:
    ray.init(local_mode=True)
print("Ray initialized")

# Define more sophisticated tools
@ray.remote
def search_tool(query: str) -> str:
    return f"search result for: {query}"

@ray.remote
def calculator_tool(expression: str) -> float:
    return eval(expression)

@ray.remote
def image_analysis_tool(image_path: str) -> str:
    return f"Analysis result for image: {image_path}"

@ray.remote
def ethics_check_tool(action: str) -> bool:
    return True

print("Defining tools")
tools = [
    Tool(
        name="Search",
        func=lambda x: ray.get(search_tool.remote(x)),
        description="useful for when you need to answer questions about current events"
    ),
    Tool(
        name="Calculator",
        func=lambda x: ray.get(calculator_tool.remote(x)),
        description="useful for when you need to perform mathematical calculations"
    ),
    Tool(
        name="ImageAnalysis",
        func=lambda x: ray.get(image_analysis_tool.remote(x)),
        description="useful for when you need to analyze an image"
    ),
    Tool(
        name="EthicsCheck",
        func=lambda x: ray.get(ethics_check_tool.remote(x)),
        description="use this to check if an action is ethically acceptable"
    )
]
print("Tools defined")

# Enhanced prompt template with ethics consideration
template = """Answer the following questions as best you can, while adhering to ethical guidelines. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do and consider the ethical implications
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
EthicsCheck: use the EthicsCheck tool to ensure your action is ethical
... (this Thought/Action/Action Input/Observation/EthicsCheck can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Question: {input}
{agent_scratchpad}"""

print("Creating prompt template")
prompt = ChatPromptTemplate.from_template(template)
print("Prompt template created")

print("Initializing AzureOpenAI")
try:
    llm = AzureOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        deployment_name=os.getenv("AZURE_DEPLOYMENT_NAME"),
        model_name=os.getenv("AZURE_MODEL_NAME"),
        temperature=0
    )
    print("AzureOpenAI initialized successfully")
except Exception as e:
    print(f"Error initializing AzureOpenAI: {e}")
    raise

print("Creating agent")
agent = create_react_agent(llm, tools, prompt)
print("Agent created")

print("Creating agent executor")
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
print("Agent executor created")

# Implement dynamic, self-organizing hierarchy
class AgentHierarchy:
    def __init__(self, agents):
        self.agents = agents

    def assign_task(self, task):
        return self.agents[0]

print("Creating agent hierarchy")
hierarchy = AgentHierarchy([agent_executor])
print("Agent hierarchy created")

def main():
    print("Starting main execution")
    task = "What is the weather like in New York? Also, analyze this image of the NYC skyline: nyc_skyline.jpg"
    print(f"Assigning task: {task}")
    try:
        assigned_agent = hierarchy.assign_task(task)
        print("Task assigned, invoking agent")
        result = assigned_agent.invoke({"input": task})
        print("Agent execution complete")
        print("Result:", result)
    except Exception as e:
        print(f"Error during agent execution: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred in the main execution: {e}")
    finally:
        print("Shutting down Ray")
        ray.shutdown()
        print("Ray shut down, script complete")