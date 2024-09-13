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

# Source code for camel.configs.mistral_config

    
    
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
    
    from typing import Any, Dict, Optional, Union
    
    from pydantic import field_validator
    
    from camel.configs.base_config import BaseConfig
    
    
    
    
    [[docs]](../../../camel.html#camel.configs.MistralConfig)class MistralConfig(BaseConfig):
        r"""Defines the parameters for generating chat completions using the
        Mistral API.
    
        reference: https://github.com/mistralai/client-python/blob/9d238f88c41689821d7b08570f13b43426f97fd6/src/mistralai/client.py#L195
    
        #TODO: Support stream mode
    
        Args:
            temperature (Optional[float], optional): temperature the temperature
                to use for sampling, e.g. 0.5.
            top_p (Optional[float], optional): the cumulative probability of
                tokens to generate, e.g. 0.9. Defaults to None.
            max_tokens (Optional[int], optional): the maximum number of tokens to
                generate, e.g. 100. Defaults to None.
            min_tokens (Optional[int], optional): the minimum number of tokens to
                generate, e.g. 100. Defaults to None.
            stop (Optional[Union[str,list[str]]]): Stop generation if this token
                is detected. Or if one of these tokens is detected when providing
                a string list.
            random_seed (Optional[int], optional): the random seed to use for
                sampling, e.g. 42. Defaults to None.
            safe_prompt (bool, optional): whether to use safe prompt, e.g. true.
                Defaults to False.
            response_format (Union[Dict[str, str], ResponseFormat): format of the
                response.
            tool_choice (str, optional): Controls which (if
                any) tool is called by the model. :obj:`"none"` means the model
                will not call any tool and instead generates a message.
                :obj:`"auto"` means the model can pick between generating a
                message or calling one or more tools.  :obj:`"any"` means the
                model must call one or more tools. :obj:`"auto"` is the default
                value.
        """
    
        temperature: Optional[float] = None
        top_p: Optional[float] = None
        max_tokens: Optional[int] = None
        min_tokens: Optional[int] = None
        stop: Optional[Union[str, list[str]]] = None
        random_seed: Optional[int] = None
        safe_prompt: bool = False
        response_format: Optional[Union[Dict[str, str], Any]] = None
        tool_choice: Optional[str] = "auto"
    
    
    
    [[docs]](../../../camel.html#camel.configs.MistralConfig.fields_type_checking)    @field_validator("response_format", mode="before")
        @classmethod
        def fields_type_checking(cls, response_format):
            if response_format and not isinstance(response_format, dict):
                from mistralai.models import ResponseFormat
    
                if not isinstance(response_format, ResponseFormat):
                    raise ValueError(
                        f"The tool {response_format} should be an instance "
                        "of `mistralai.models.ResponseFormat`."
                    )
            return response_format
    
    
    
    
    MISTRAL_API_PARAMS = {param for param in MistralConfig().model_fields.keys()}
    

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

