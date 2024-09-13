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

# Source code for camel.configs.base_config

    
    
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
    
    from abc import ABC
    from typing import Any, List, Optional
    
    from pydantic import BaseModel, ConfigDict, field_validator
    
    
    
    
    [[docs]](../../../camel.html#camel.configs.BaseConfig)class BaseConfig(ABC, BaseModel):
        model_config = ConfigDict(
            arbitrary_types_allowed=True,
            extra="forbid",
            frozen=True,
            # UserWarning: conflict with protected namespace "model_"
            protected_namespaces=(),
        )
    
        tools: Optional[List[Any]] = None
        """A list of tools the model may
        call. Currently, only functions are supported as a tool. Use this
        to provide a list of functions the model may generate JSON inputs
        for. A max of 128 functions are supported.
        """
    
    
    
    [[docs]](../../../camel.html#camel.configs.BaseConfig.fields_type_checking)    @field_validator("tools", mode="before")
        @classmethod
        def fields_type_checking(cls, tools):
            if tools is not None:
                from camel.toolkits import OpenAIFunction
    
                for tool in tools:
                    if not isinstance(tool, OpenAIFunction):
                        raise ValueError(
                            f"The tool {tool} should "
                            "be an instance of `OpenAIFunction`."
                        )
            return tools
    
    
    
    
    
    [[docs]](../../../camel.html#camel.configs.BaseConfig.as_dict)    def as_dict(self) -> dict[str, Any]:
            config_dict = self.model_dump()
    
            tools_schema = None
            if self.tools:
                from camel.toolkits import OpenAIFunction
    
                tools_schema = []
                for tool in self.tools:
                    if not isinstance(tool, OpenAIFunction):
                        raise ValueError(
                            f"The tool {tool} should "
                            "be an instance of `OpenAIFunction`."
                        )
                    tools_schema.append(tool.get_openai_tool_schema())
            config_dict["tools"] = tools_schema
            return config_dict
    
    
    

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

