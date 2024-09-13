import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import ChatPromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import Tool

print("Script started")

# Load environment variables
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path=env_path)
print("Environment variables loaded")

# Initialize the search tool
search = DuckDuckGoSearchRun()

# Define the tool
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or general knowledge"
    )
]

# Create a prompt template
template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Question: {input}
{agent_scratchpad}"""

prompt = ChatPromptTemplate.from_template(template)
print("Prompt template created")

# Initialize AzureOpenAI
print("Initializing AzureOpenAI")
llm = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    deployment_name=os.getenv("AZURE_DEPLOYMENT_NAME"),
    model_name=os.getenv("AZURE_MODEL_NAME"),
    temperature=0
)
print("AzureOpenAI initialized")

# Create the agent
print("Creating agent")
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
print("Agent created")

def main():
    print("Starting main execution")
    task = "What is the current weather in New York City?"
    print(f"Task: {task}")
    try:
        result = agent_executor.invoke({"input": task})
        print("Agent execution complete")
        print("Result:", result)
    except Exception as e:
        print(f"Error during agent execution: {e}")

if __name__ == "__main__":
    main()
    print("Script complete")