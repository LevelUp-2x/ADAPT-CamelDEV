from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from camel.models.langchain_wrappers import GitHubLangChainWrapper, GeminiLangChainWrapper
from camel.prompts.prompt_manager import PromptManager

class ConversationMemoryManager:
    def __init__(self):
        self.memories = {}

    def create_memory(self, agent_id: str) -> ConversationBufferMemory:
        """
        Create a new ConversationBufferMemory for an agent.
        """
        memory = ConversationBufferMemory()
        self.memories[agent_id] = memory
        return memory

    def get_memory(self, agent_id: str) -> ConversationBufferMemory:
        """
        Retrieve the memory for a specific agent.
        """
        return self.memories.get(agent_id)

    def create_conversation_chain(self, agent_id: str, llm: GitHubLangChainWrapper | GeminiLangChainWrapper, prompt_manager: PromptManager, prompt_name: str) -> ConversationChain:
        """
        Create a ConversationChain with memory for an agent.
        """
        memory = self.get_memory(agent_id)
        if not memory:
            memory = self.create_memory(agent_id)

        prompt_template = prompt_manager.get_prompt_template(prompt_name)
        if not prompt_template:
            raise ValueError(f"Prompt template '{prompt_name}' not found.")

        return ConversationChain(
            llm=llm,
            memory=memory,
            prompt=prompt_template
        )

# Example usage:
memory_manager = ConversationMemoryManager()
prompt_manager = PromptManager()

# Add a conversation prompt template
prompt_manager.add_prompt_template(
    "conversation",
    "The following is a conversation between a human and an AI assistant. The AI assistant is helpful, creative, clever, and very friendly.\n\nHuman: {human_input}\nAI:",
    ["human_input"]
)

def example_conversation(agent_id: str, llm: GitHubLangChainWrapper | GeminiLangChainWrapper, human_input: str):
    conversation_chain = memory_manager.create_conversation_chain(agent_id, llm, prompt_manager, "conversation")
    response = conversation_chain.predict(human_input=human_input)
    print(f"AI: {response}")

# To use this in your project:
# github_model = GitHubLangChainWrapper(your_github_model_instance)
# example_conversation("agent1", github_model, "Hello, how are you?")
# example_conversation("agent1", github_model, "What did we just talk about?")

# The second call will include context from the first conversation due to the memory system