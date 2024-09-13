from typing import List, Optional, Any, Dict
from langchain.llms.base import LLM
from langchain.callbacks.manager import CallbackManagerForLLMRun
from camel.models.github_model_backend import GitHubModelBackend
from camel.models.gemini_model_backend import GeminiModelBackend

class GitHubLangChainWrapper(LLM):
    model: GitHubModelBackend
    
    def __init__(self, model: GitHubModelBackend):
        super().__init__()
        self.model = model

    @property
    def _llm_type(self) -> str:
        return "github_copilot"

    async def _agenerate(
        self,
        prompts: List[str],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> List[str]:
        responses = []
        for prompt in prompts:
            response = await self.model.generate(prompt, max_tokens=kwargs.get("max_tokens", 100), temperature=kwargs.get("temperature", 0.7), stop=stop)
            responses.append(response)
        return responses

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        import asyncio
        return asyncio.run(self._agenerate([prompt], stop, run_manager, **kwargs))[0]

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        return {"model_name": self.model.model_name}

class GeminiLangChainWrapper(LLM):
    model: GeminiModelBackend
    
    def __init__(self, model: GeminiModelBackend):
        super().__init__()
        self.model = model

    @property
    def _llm_type(self) -> str:
        return "gemini"

    async def _agenerate(
        self,
        prompts: List[str],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> List[str]:
        responses = []
        for prompt in prompts:
            response = await self.model.generate(prompt, max_tokens=kwargs.get("max_tokens", 100), temperature=kwargs.get("temperature", 0.7), stop=stop)
            responses.append(response)
        return responses

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        import asyncio
        return asyncio.run(self._agenerate([prompt], stop, run_manager, **kwargs))[0]

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        return {"model_name": self.model.model_name}

# Example usage:
# github_model = GitHubModelBackend(...)
# github_langchain_model = GitHubLangChainWrapper(github_model)
#
# gemini_model = GeminiModelBackend(...)
# gemini_langchain_model = GeminiLangChainWrapper(gemini_model)