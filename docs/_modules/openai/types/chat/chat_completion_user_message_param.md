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

# Source code for openai.types.chat.chat_completion_user_message_param

    
    
    # File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
    
    from __future__ import annotations
    
    from typing import Union, Iterable
    from typing_extensions import Literal, Required, TypedDict
    
    from .chat_completion_content_part_param import ChatCompletionContentPartParam
    
    __all__ = ["ChatCompletionUserMessageParam"]
    
    
    
    
    [[docs]](../../../../camel.html#camel.messages.ChatCompletionUserMessageParam)class ChatCompletionUserMessageParam(TypedDict, total=False):
        content: Required[Union[str, Iterable[ChatCompletionContentPartParam]]]
        """The contents of the user message."""
    
        role: Required[Literal["user"]]
        """The role of the messages author, in this case `user`."""
    
        name: str
        """An optional name for the participant.
    
        Provides the model information to differentiate between participants of the same
        role.
        """
    
    
    

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

