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

# Source code for openai.types.chat.chat_completion_function_message_param

    
    
    # File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
    
    from __future__ import annotations
    
    from typing import Optional
    from typing_extensions import Literal, Required, TypedDict
    
    __all__ = ["ChatCompletionFunctionMessageParam"]
    
    
    
    
    [[docs]](../../../../camel.html#camel.types.ChatCompletionFunctionMessageParam)class ChatCompletionFunctionMessageParam(TypedDict, total=False):
        content: Required[Optional[str]]
        """The contents of the function message."""
    
        name: Required[str]
        """The name of the function to call."""
    
        role: Required[Literal["function"]]
        """The role of the messages author, in this case `function`."""
    
    
    

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

