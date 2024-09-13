Skip to main content

__Back to top

__ `Ctrl`+`K`

[ ![](https://raw.githubusercontent.com/camel-
ai/camel/master/misc/primary_logo.png) CAMEL 0.1.9 ](index.html)

Get Started

  * [Installation and Setup](get_started/setup.html)

Agents

  * [Creating Your First Agent](agents/single_agent.html)
  * [Creating Your First Agent Society](agents/role_playing.html)
  * [Embodied Agents](agents/embodied_agents.html)
  * [Critic Agents and Tree Search](agents/critic_agents_and_tree_search.html)

Key Modules

  * [Loaders](key_modules/loaders.html)
  * [Storages](key_modules/storages.html)
  * [Embeddings](key_modules/embeddings.html)
  * [Retrievers](key_modules/retrievers.html)

Tutorial and Cookbooks

  * [🐫 Agents with RAG](tutorials_and_cookbooks/agents_with_rag.html)

API References

  * [camel](modules.html) __
    * [Camel Package](camel.html) __
      * [camel.agents package](camel.agents.html)
      * [camel.prompts package](camel.prompts.html)

__

  * [ __ .rst ](_sources/camel.agents.tool_agents.rst "Download source file")
  * __ .pdf

__

# camel.agents.tool_agents package

##  Contents

  * Submodules
  * camel.agents.tool_agents.base module
    * `BaseToolAgent`
      * `BaseToolAgent.reset()`
      * `BaseToolAgent.step()`
  * camel.agents.tool_agents.hugging_face_tool_agent module
    * `HuggingFaceToolAgent`
      * `HuggingFaceToolAgent.chat()`
      * `HuggingFaceToolAgent.reset()`
      * `HuggingFaceToolAgent.step()`
  * Module contents
    * `BaseToolAgent`
      * `BaseToolAgent.reset()`
      * `BaseToolAgent.step()`
    * `HuggingFaceToolAgent`
      * `HuggingFaceToolAgent.chat()`
      * `HuggingFaceToolAgent.reset()`
      * `HuggingFaceToolAgent.step()`

# camel.agents.tool_agents package#

## Submodules#

## camel.agents.tool_agents.base module#

_class _camel.agents.tool_agents.base.BaseToolAgent(_name : str_, _description
: str_)[[source]](_modules/camel/agents/tool_agents/base.html#BaseToolAgent)#

    

Bases: [`BaseAgent`](camel.agents.html#camel.agents.BaseAgent
"camel.agents.base.BaseAgent")

Creates a `BaseToolAgent` object with the specified name and

    

description.

Parameters:

    

  * **name** (_str_) – The name of the tool agent.

  * **description** (_str_) – The description of the tool agent.

reset() ->
None[[source]](_modules/camel/agents/tool_agents/base.html#BaseToolAgent.reset)#

    

Resets the agent to its initial state.

step() ->
None[[source]](_modules/camel/agents/tool_agents/base.html#BaseToolAgent.step)#

    

Performs a single step of the agent.

## camel.agents.tool_agents.hugging_face_tool_agent module#

_class
_camel.agents.tool_agents.hugging_face_tool_agent.HuggingFaceToolAgent(_name :
str_, _* args: Any_, _remote : bool = True_, _** kwargs:
Any_)[[source]](_modules/camel/agents/tool_agents/hugging_face_tool_agent.html#HuggingFaceToolAgent)#

    

Bases: `BaseToolAgent`

Tool agent for calling HuggingFace models. This agent is a wrapper

    

around agents from the transformers library. For more information about the
available models, please see the transformers documentation at
<https://huggingface.co/docs/transformers/transformers_agents>.

Parameters:

    

  * **name** (_str_) – The name of the agent.

  * ***args** (_Any_) – Additional positional arguments to pass to the underlying Agent class.

  * **remote** (_bool_ _,__optional_) – Flag indicating whether to run the agent remotely. (default: `True`)

  * ****kwargs** (_Any_) – Additional keyword arguments to pass to the underlying Agent class.

chat(_* args: Any_, _remote : bool | None = None_, _** kwargs: Any_) -> Any[[source]](_modules/camel/agents/tool_agents/hugging_face_tool_agent.html#HuggingFaceToolAgent.chat)#
    

Runs the agent in a chat conversation mode.

Parameters:

    

  * ***args** (_Any_) – Positional arguments to pass to the agent.

  * **remote** (_bool_ _,__optional_) – Flag indicating whether to run the agent remotely. Overrides the default setting. (default: `None`)

  * ****kwargs** (_Any_) – Keyword arguments to pass to the agent.

Returns:

    

The response from the agent.

Return type:

    

str

reset() ->
None[[source]](_modules/camel/agents/tool_agents/hugging_face_tool_agent.html#HuggingFaceToolAgent.reset)#

    

Resets the chat history of the agent.

step(_* args: Any_, _remote : bool | None = None_, _** kwargs: Any_) -> Any[[source]](_modules/camel/agents/tool_agents/hugging_face_tool_agent.html#HuggingFaceToolAgent.step)#
    

Runs the agent in single execution mode.

Parameters:

    

  * ***args** (_Any_) – Positional arguments to pass to the agent.

  * **remote** (_bool_ _,__optional_) – Flag indicating whether to run the agent remotely. Overrides the default setting. (default: `None`)

  * ****kwargs** (_Any_) – Keyword arguments to pass to the agent.

Returns:

    

The response from the agent.

Return type:

    

str

## Module contents#

_class _camel.agents.tool_agents.BaseToolAgent(_name : str_, _description :
str_)[[source]](_modules/camel/agents/tool_agents/base.html#BaseToolAgent)#

    

Bases: [`BaseAgent`](camel.agents.html#camel.agents.BaseAgent
"camel.agents.base.BaseAgent")

Creates a `BaseToolAgent` object with the specified name and

    

description.

Parameters:

    

  * **name** (_str_) – The name of the tool agent.

  * **description** (_str_) – The description of the tool agent.

reset() ->
None[[source]](_modules/camel/agents/tool_agents/base.html#BaseToolAgent.reset)#

    

Resets the agent to its initial state.

step() ->
None[[source]](_modules/camel/agents/tool_agents/base.html#BaseToolAgent.step)#

    

Performs a single step of the agent.

_class _camel.agents.tool_agents.HuggingFaceToolAgent(_name : str_, _* args:
Any_, _remote : bool = True_, _** kwargs:
Any_)[[source]](_modules/camel/agents/tool_agents/hugging_face_tool_agent.html#HuggingFaceToolAgent)#

    

Bases: `BaseToolAgent`

Tool agent for calling HuggingFace models. This agent is a wrapper

    

around agents from the transformers library. For more information about the
available models, please see the transformers documentation at
<https://huggingface.co/docs/transformers/transformers_agents>.

Parameters:

    

  * **name** (_str_) – The name of the agent.

  * ***args** (_Any_) – Additional positional arguments to pass to the underlying Agent class.

  * **remote** (_bool_ _,__optional_) – Flag indicating whether to run the agent remotely. (default: `True`)

  * ****kwargs** (_Any_) – Additional keyword arguments to pass to the underlying Agent class.

chat(_* args: Any_, _remote : bool | None = None_, _** kwargs: Any_) -> Any[[source]](_modules/camel/agents/tool_agents/hugging_face_tool_agent.html#HuggingFaceToolAgent.chat)#
    

Runs the agent in a chat conversation mode.

Parameters:

    

  * ***args** (_Any_) – Positional arguments to pass to the agent.

  * **remote** (_bool_ _,__optional_) – Flag indicating whether to run the agent remotely. Overrides the default setting. (default: `None`)

  * ****kwargs** (_Any_) – Keyword arguments to pass to the agent.

Returns:

    

The response from the agent.

Return type:

    

str

reset() ->
None[[source]](_modules/camel/agents/tool_agents/hugging_face_tool_agent.html#HuggingFaceToolAgent.reset)#

    

Resets the chat history of the agent.

step(_* args: Any_, _remote : bool | None = None_, _** kwargs: Any_) -> Any[[source]](_modules/camel/agents/tool_agents/hugging_face_tool_agent.html#HuggingFaceToolAgent.step)#
    

Runs the agent in single execution mode.

Parameters:

    

  * ***args** (_Any_) – Positional arguments to pass to the agent.

  * **remote** (_bool_ _,__optional_) – Flag indicating whether to run the agent remotely. Overrides the default setting. (default: `None`)

  * ****kwargs** (_Any_) – Keyword arguments to pass to the agent.

Returns:

    

The response from the agent.

Return type:

    

str

__Contents

  * Submodules
  * camel.agents.tool_agents.base module
    * `BaseToolAgent`
      * `BaseToolAgent.reset()`
      * `BaseToolAgent.step()`
  * camel.agents.tool_agents.hugging_face_tool_agent module
    * `HuggingFaceToolAgent`
      * `HuggingFaceToolAgent.chat()`
      * `HuggingFaceToolAgent.reset()`
      * `HuggingFaceToolAgent.step()`
  * Module contents
    * `BaseToolAgent`
      * `BaseToolAgent.reset()`
      * `BaseToolAgent.step()`
    * `HuggingFaceToolAgent`
      * `HuggingFaceToolAgent.chat()`
      * `HuggingFaceToolAgent.reset()`
      * `HuggingFaceToolAgent.step()`

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

