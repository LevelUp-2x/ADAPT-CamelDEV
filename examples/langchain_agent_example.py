import asyncio
from camel.models.langchain_wrappers import GitHubLangChainWrapper, GeminiLangChainWrapper
from camel.models.github_model_backend import GitHubModelBackend
from camel.models.gemini_model_backend import GeminiModelBackend
from camel.prompts.prompt_manager import PromptManager
from camel.memory.conversation_memory import ConversationMemoryManager

# Initialize components
github_model = GitHubModelBackend(ModelType.GITHUB_COPILOT, "your_github_api_key")
gemini_model = GeminiModelBackend(ModelType.GEMINI_1_5_PRO, "your_gemini_api_key")

github_langchain = GitHubLangChainWrapper(github_model)
gemini_langchain = GeminiLangChainWrapper(gemini_model)

prompt_manager = PromptManager()
memory_manager = ConversationMemoryManager()

# Add conversation prompt template
prompt_manager.add_prompt_template(
    "conversation",
    "The following is a conversation between a human and an AI assistant. The AI assistant is helpful, creative, clever, and very friendly.\n\nHuman: {human_input}\nAI:",
    ["human_input"]
)

async def run_conversation(agent_id: str, llm: GitHubLangChainWrapper | GeminiLangChainWrapper, human_inputs: list[str]):
    conversation_chain = memory_manager.create_conversation_chain(agent_id, llm, prompt_manager, "conversation")
    
    for human_input in human_inputs:
        response = await conversation_chain.apredict(human_input=human_input)
        print(f"Human: {human_input}")
        print(f"AI: {response}\n")

async def main():
    # Example conversation with GitHub model
    print("Conversation with GitHub model:")
    await run_conversation("github_agent", github_langchain, [
        "Hello, how are you?",
        "Can you tell me about the ADAPT-CamelDEV project?",
        "What was the first thing I asked you?"
    ])

    print("\n" + "="*50 + "\n")

    # Example conversation with Gemini model
    print("Conversation with Gemini model:")
    await run_conversation("gemini_agent", gemini_langchain, [
        "Hi there! What can you do?",
        "Can you explain what LangChain is?",
        "What was our conversation about?"
    ])

if __name__ == "__main__":
    asyncio.run(main())

# Note: Replace 'your_github_api_key' and 'your_gemini_api_key' with actual API keys before running this example.