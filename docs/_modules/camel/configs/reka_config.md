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

# Source code for camel.configs.reka_config

    
    
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
    
    from typing import Any, Optional, Union
    
    from camel.configs.base_config import BaseConfig
    
    
    
    
    [[docs]](../../../camel.html#camel.configs.RekaConfig)class RekaConfig(BaseConfig):
        r"""Defines the parameters for generating chat completions using the
        Reka API.
    
        Reference: https://docs.reka.ai/api-reference/chat/create
    
        Args:
            temperature (Optional[float], optional): temperature the temperature
                to use for sampling, e.g. 0.5.
            top_p (Optional[float], optional): the cumulative probability of
                tokens to generate, e.g. 0.9. Defaults to None.
            top_k (Optional[int], optional): Parameter which forces the model to
                only consider the tokens with the `top_k` highest probabilities at
                the next step. Defaults to 1024.
            max_tokens (Optional[int], optional): the maximum number of tokens to
                generate, e.g. 100. Defaults to None.
            stop (Optional[Union[str,list[str]]]): Stop generation if this token
                is detected. Or if one of these tokens is detected when providing
                a string list.
            seed (Optional[int], optional): the random seed to use for sampling, e.
                g. 42. Defaults to None.
            presence_penalty (float, optional): Number between :obj:`-2.0` and
                :obj:`2.0`. Positive values penalize new tokens based on whether
                they appear in the text so far, increasing the model's likelihood
                to talk about new topics. See more information about frequency and
                presence penalties. (default: :obj:`0.0`)
            frequency_penalty (float, optional): Number between :obj:`-2.0` and
                :obj:`2.0`. Positive values penalize new tokens based on their
                existing frequency in the text so far, decreasing the model's
                likelihood to repeat the same line verbatim. See more information
                about frequency and presence penalties. (default: :obj:`0.0`)
            use_search_engine (Optional[bool]): Whether to consider using search
                engine to complete the request. Note that even if this is set to
                `True`, the model might decide to not use search.
        """
    
        temperature: Optional[float] = None
        top_p: Optional[float] = None
        top_k: Optional[int] = None
        max_tokens: Optional[int] = None
        stop: Optional[Union[str, list[str]]] = None
        seed: Optional[int] = None
        frequency_penalty: float = 0.0
        presence_penalty: float = 0.0
        use_search_engine: Optional[bool] = False
    
    
    
    [[docs]](../../../camel.html#camel.configs.RekaConfig.as_dict)    def as_dict(self) -> dict[str, Any]:
            config_dict = super().as_dict()
            if "tools" in config_dict:
                del config_dict["tools"]  # Reka does not support tool calling
            return config_dict
    
    
    
    
    REKA_API_PARAMS = {param for param in RekaConfig().model_fields.keys()}
    

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

