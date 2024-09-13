Skip to main content

__Back to top

__ `Ctrl`+`K`

[ ![](https://raw.githubusercontent.com/camel-
ai/camel/master/misc/primary_logo.png) CAMEL 0.1.9 ](../../../index.html)

Get Started

  * [Installation and Setup](../../../get_started/setup.html)

Agents

  * [Creating Your First Agent](../../../agents/single_agent.html)
  * [Creating Your First Agent Society](../../../agents/role_playing.html)
  * [Embodied Agents](../../../agents/embodied_agents.html)
  * [Critic Agents and Tree Search](../../../agents/critic_agents_and_tree_search.html)

Key Modules

  * [Loaders](../../../key_modules/loaders.html)
  * [Storages](../../../key_modules/storages.html)
  * [Embeddings](../../../key_modules/embeddings.html)
  * [Retrievers](../../../key_modules/retrievers.html)

Tutorial and Cookbooks

  * [🐫 Agents with RAG](../../../tutorials_and_cookbooks/agents_with_rag.html)

API References

  * [camel](../../../modules.html) __
    * [Camel Package](../../../camel.html) __
      * [camel.agents package](../../../camel.agents.html)
      * [camel.prompts package](../../../camel.prompts.html)

__

#

# Source code for camel.configs.litellm_config

    
    
    # =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
    # Licensed under the Apache License, Version 2.0 (the “License”);
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an “AS IS” BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    # =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
    from __future__ import annotations
    
    from typing import List, Optional, Union
    
    from camel.configs.base_config import BaseConfig
    
    
    
    
    [[docs]](../../../camel.html#camel.configs.LiteLLMConfig)class LiteLLMConfig(BaseConfig):
        r"""Defines the parameters for generating chat completions using the
        LiteLLM API.
    
        Args:
            timeout (Optional[Union[float, str]], optional): Request timeout.
                (default: None)
            temperature (Optional[float], optional): Temperature parameter for
                controlling randomness. (default: None)
            top_p (Optional[float], optional): Top-p parameter for nucleus
                sampling. (default: None)
            n (Optional[int], optional): Number of completions to generate.
                (default: None)
            stream (Optional[bool], optional): Whether to return a streaming
                response. (default: None)
            stream_options (Optional[dict], optional): Options for the streaming
                response. (default: None)
            stop (Optional[Union[str, List[str]]], optional): Sequences where the
                API will stop generating further tokens. (default: None)
            max_tokens (Optional[int], optional): Maximum number of tokens to
                generate. (default: None)
            presence_penalty (Optional[float], optional): Penalize new tokens
                based on their existence in the text so far. (default: None)
            frequency_penalty (Optional[float], optional): Penalize new tokens
                based on their frequency in the text so far. (default: None)
            logit_bias (Optional[dict], optional): Modify the probability of
                specific tokens appearing in the completion. (default: None)
            user (Optional[str], optional): A unique identifier representing the
                end-user. (default: None)
            response_format (Optional[dict], optional): Response format
                parameters. (default: None)
            seed (Optional[int], optional): Random seed. (default: None)
            tools (Optional[List], optional): List of tools. (default: None)
            tool_choice (Optional[Union[str, dict]], optional): Tool choice
                parameters. (default: None)
            logprobs (Optional[bool], optional): Whether to return log
                probabilities of the output tokens. (default: None)
            top_logprobs (Optional[int], optional): Number of most likely tokens
                to return at each token position. (default: None)
            deployment_id (Optional[str], optional): Deployment ID. (default: None)
            extra_headers (Optional[dict], optional): Additional headers for the
                request. (default: None)
            api_version (Optional[str], optional): API version. (default: None)
            mock_response (Optional[str], optional): Mock completion response for
                testing or debugging. (default: None)
            custom_llm_provider (Optional[str], optional): Non-OpenAI LLM
                provider. (default: None)
            max_retries (Optional[int], optional): Maximum number of retries.
                (default: None)
        """
    
        timeout: Optional[Union[float, str]] = None
        temperature: Optional[float] = None
        top_p: Optional[float] = None
        n: Optional[int] = None
        stream: Optional[bool] = None
        stream_options: Optional[dict] = None
        stop: Optional[Union[str, List[str]]] = None
        max_tokens: Optional[int] = None
        presence_penalty: Optional[float] = None
        frequency_penalty: Optional[float] = None
        logit_bias: Optional[dict] = None
        user: Optional[str] = None
        response_format: Optional[dict] = None
        seed: Optional[int] = None
        tool_choice: Optional[Union[str, dict]] = None
        logprobs: Optional[bool] = None
        top_logprobs: Optional[int] = None
        deployment_id: Optional[str] = None
        extra_headers: Optional[dict] = None
        api_version: Optional[str] = None
        mock_response: Optional[str] = None
        custom_llm_provider: Optional[str] = None
        max_retries: Optional[int] = None
    
    
    
    
    LITELLM_API_PARAMS = {param for param in LiteLLMConfig.model_fields.keys()}
    

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

