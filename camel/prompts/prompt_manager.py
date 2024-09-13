from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import Dict, Any
from camel.models.langchain_wrappers import GitHubLangChainWrapper, GeminiLangChainWrapper

class PromptManager:
    def __init__(self):
        self.prompt_templates: Dict[str, PromptTemplate] = {}

    def add_prompt_template(self, name: str, template: str, input_variables: list):
        """
        Add a new prompt template to the manager.
        """
        self.prompt_templates[name] = PromptTemplate(
            input_variables=input_variables,
            template=template
        )

    def get_prompt_template(self, name: str) -> PromptTemplate:
        """
        Retrieve a prompt template by name.
        """
        return self.prompt_templates.get(name)

    def create_chain(self, name: str, llm: Any) -> LLMChain:
        """
        Create an LLMChain using a prompt template and an LLM.
        """
        prompt_template = self.get_prompt_template(name)
        if not prompt_template:
            raise ValueError(f"Prompt template '{name}' not found.")
        
        return LLMChain(llm=llm, prompt=prompt_template)

# Example usage:
prompt_manager = PromptManager()

# Add some example prompt templates
prompt_manager.add_prompt_template(
    "code_explanation",
    "Explain the following code:\n\n{code}\n\nExplanation:",
    ["code"]
)

prompt_manager.add_prompt_template(
    "task_planning",
    "Create a plan to accomplish the following task:\n\nTask: {task}\n\nPlan:",
    ["task"]
)

# Example of creating and using a chain
def example_chain_usage(github_model: GitHubLangChainWrapper, task: str):
    chain = prompt_manager.create_chain("task_planning", github_model)
    result = chain.run(task=task)
    print(f"Task planning result: {result}")

# To use this in your project:
# github_model = GitHubLangChainWrapper(your_github_model_instance)
# example_chain_usage(github_model, "Develop a new feature for user authentication")

# You can add more prompt templates and create chains as needed for various tasks in your AI agent hierarchy