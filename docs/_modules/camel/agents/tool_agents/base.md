Skip to main content

__Back to top

__ `Ctrl`+`K`

[ ![](https://raw.githubusercontent.com/camel-
ai/camel/master/misc/primary_logo.png) CAMEL 0.1.9 ](../../../../index.html)

Get Started

  * [Installation and Setup](../../../../get_started/setup.html)

Agents

  * [Creating Your First Agent](../../../../agents/single_agent.html)
  * [Creating Your First Agent Society](../../../../agents/role_playing.html)
  * [Embodied Agents](../../../../agents/embodied_agents.html)
  * [Critic Agents and Tree Search](../../../../agents/critic_agents_and_tree_search.html)

Key Modules

  * [Loaders](../../../../key_modules/loaders.html)
  * [Storages](../../../../key_modules/storages.html)
  * [Embeddings](../../../../key_modules/embeddings.html)
  * [Retrievers](../../../../key_modules/retrievers.html)

Tutorial and Cookbooks

  * [🐫 Agents with RAG](../../../../tutorials_and_cookbooks/agents_with_rag.html)

API References

  * [camel](../../../../modules.html) __
    * [Camel Package](../../../../camel.html) __
      * [camel.agents package](../../../../camel.agents.html)
      * [camel.prompts package](../../../../camel.prompts.html)

__

#

# Source code for camel.agents.tool_agents.base

    
    
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
    from camel.agents import BaseAgent
    
    
    
    
    [[docs]](../../../../camel.agents.tool_agents.html#camel.agents.BaseToolAgent)class BaseToolAgent(BaseAgent):
        r"""Creates a :obj:`BaseToolAgent` object with the specified name and
            description.
    
        Args:
            name (str): The name of the tool agent.
            description (str): The description of the tool agent.
        """
    
        def __init__(self, name: str, description: str) -> None:
            self.name = name
            self.description = description
    
    
    
    [[docs]](../../../../camel.agents.tool_agents.html#camel.agents.BaseToolAgent.reset)    def reset(self) -> None:
            r"""Resets the agent to its initial state."""
            pass
    
    
    
    
    
    [[docs]](../../../../camel.agents.tool_agents.html#camel.agents.BaseToolAgent.step)    def step(self) -> None:
            r"""Performs a single step of the agent."""
            pass
    
    
    
        def __str__(self) -> str:
            return f"{self.name}: {self.description}"
    
    
    

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

