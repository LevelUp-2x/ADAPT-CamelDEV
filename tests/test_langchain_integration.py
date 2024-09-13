import asyncio
import pytest
from camel.models.github_model_backend import GitHubModelBackend
from camel.models.gemini_model_backend import GeminiModelBackend
from camel.models.langchain_wrappers import GitHubLangChainWrapper, GeminiLangChainWrapper
from camel.types import ModelType
from camel.prompts.prompt_manager import PromptManager
from camel.memory.conversation_memory import ConversationMemoryManager

@pytest.fixture
def github_model():
    return GitHubModelBackend(ModelType.GITHUB_COPILOT, "your_github_api_key")

@pytest.fixture
def gemini_model():
    return GeminiModelBackend(ModelType.GEMINI_1_5_PRO, "your_gemini_api_key")

@pytest.fixture
def prompt_manager():
    pm = PromptManager()
    pm.add_prompt_template(
        "conversation",
        "The following is a conversation between a human and an AI assistant. The AI assistant is helpful, creative, clever, and very friendly.\n\nHuman: {human_input}\nAI:",
        ["human_input"]
    )
    return pm

@pytest.fixture
def memory_manager():
    return ConversationMemoryManager()

@pytest.mark.asyncio
async def test_github_langchain_wrapper(github_model, prompt_manager, memory_manager):
    github_langchain = GitHubLangChainWrapper(github_model)
    conversation = memory_manager.create_conversation_chain("github_agent", github_langchain, prompt_manager, "conversation")
    
    response = await conversation.apredict(human_input="Hello, can you explain what ADAPT-CamelDEV is?")
    assert isinstance(response, str)
    assert len(response) > 0
    
    # Test memory retention
    response = await conversation.apredict(human_input="What did I just ask you about?")
    assert "ADAPT-CamelDEV" in response

@pytest.mark.asyncio
async def test_gemini_langchain_wrapper(gemini_model, prompt_manager, memory_manager):
    gemini_langchain = GeminiLangChainWrapper(gemini_model)
    conversation = memory_manager.create_conversation_chain("gemini_agent", gemini_langchain, prompt_manager, "conversation")
    
    response = await conversation.apredict(human_input="What are the key features of LangChain?")
    assert isinstance(response, str)
    assert len(response) > 0
    
    # Test memory retention
    response = await conversation.apredict(human_input="Can you summarize what you just told me?")
    assert "LangChain" in response

@pytest.mark.asyncio
async def test_prompt_template_usage(github_model, prompt_manager):
    github_langchain = GitHubLangChainWrapper(github_model)
    
    prompt_manager.add_prompt_template(
        "code_explanation",
        "Explain the following code:\n\n{code}\n\nExplanation:",
        ["code"]
    )
    
    chain = prompt_manager.create_chain("code_explanation", github_langchain)
    response = await chain.arun(code="def hello_world():\n    print('Hello, World!')")
    
    assert isinstance(response, str)
    assert len(response) > 0
    assert "function" in response.lower() or "prints" in response.lower()

@pytest.mark.asyncio
async def test_multi_turn_conversation(github_model, prompt_manager, memory_manager):
    github_langchain = GitHubLangChainWrapper(github_model)
    conversation = memory_manager.create_conversation_chain("github_agent", github_langchain, prompt_manager, "conversation")
    
    responses = []
    questions = [
        "What is machine learning?",
        "Can you give an example of a machine learning algorithm?",
        "How does that algorithm work?",
        "What was the first thing I asked you about?"
    ]
    
    for question in questions:
        response = await conversation.apredict(human_input=question)
        responses.append(response)
    
    assert len(responses) == 4
    assert "machine learning" in responses[0].lower()
    assert "algorithm" in responses[1].lower()
    assert "machine learning" in responses[3].lower()

if __name__ == "__main__":
    pytest.main([__file__])

# Note: Replace 'your_github_api_key' and 'your_gemini_api_key' with actual API keys before running these tests.