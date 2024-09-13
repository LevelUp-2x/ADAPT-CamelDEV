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
      * camel.agents package
      * [camel.prompts package](camel.prompts.html)

__

  * [ __ .rst ](_sources/camel.agents.rst "Download source file")
  * __ .pdf

__

# camel.agents package

##  Contents

  * Submodules
  * camel.agents.chat_agent module
    * `ChatAgent`
      * `ChatAgent.get_info()`
      * `ChatAgent.get_usage_dict()`
      * `ChatAgent.handle_batch_response()`
      * `ChatAgent.handle_stream_response()`
      * `ChatAgent.init_messages()`
      * `ChatAgent.is_tools_added()`
      * `ChatAgent.record_message()`
      * `ChatAgent.reset()`
      * `ChatAgent.set_output_language()`
      * `ChatAgent.step()`
      * `ChatAgent.step_async()`
      * `ChatAgent.step_tool_call()`
      * `ChatAgent.step_tool_call_async()`
      * `ChatAgent.system_message`
      * `ChatAgent.update_memory()`
    * `FunctionCallingRecord`
      * `FunctionCallingRecord.func_name`
      * `FunctionCallingRecord.args`
      * `FunctionCallingRecord.result`
      * `FunctionCallingRecord.args`
      * `FunctionCallingRecord.as_dict()`
      * `FunctionCallingRecord.func_name`
      * `FunctionCallingRecord.model_computed_fields`
      * `FunctionCallingRecord.model_config`
      * `FunctionCallingRecord.model_fields`
      * `FunctionCallingRecord.result`
  * camel.agents.role_playing module
  * camel.agents.task_agent module
    * `TaskCreationAgent`
      * `TaskCreationAgent.task_creation_prompt`
      * `TaskCreationAgent.run()`
    * `TaskPlannerAgent`
      * `TaskPlannerAgent.task_planner_prompt`
      * `TaskPlannerAgent.run()`
    * `TaskPrioritizationAgent`
      * `TaskPrioritizationAgent.task_prioritization_prompt`
      * `TaskPrioritizationAgent.run()`
    * `TaskSpecifyAgent`
      * `TaskSpecifyAgent.DEFAULT_WORD_LIMIT`
      * `TaskSpecifyAgent.task_specify_prompt`
      * `TaskSpecifyAgent.DEFAULT_WORD_LIMIT`
      * `TaskSpecifyAgent.run()`
  * Module contents
    * `BaseAgent`
      * `BaseAgent.reset()`
      * `BaseAgent.step()`
    * `BaseToolAgent`
      * `BaseToolAgent.reset()`
      * `BaseToolAgent.step()`
    * `ChatAgent`
      * `ChatAgent.get_info()`
      * `ChatAgent.get_usage_dict()`
      * `ChatAgent.handle_batch_response()`
      * `ChatAgent.handle_stream_response()`
      * `ChatAgent.init_messages()`
      * `ChatAgent.is_tools_added()`
      * `ChatAgent.record_message()`
      * `ChatAgent.reset()`
      * `ChatAgent.set_output_language()`
      * `ChatAgent.step()`
      * `ChatAgent.step_async()`
      * `ChatAgent.step_tool_call()`
      * `ChatAgent.step_tool_call_async()`
      * `ChatAgent.system_message`
      * `ChatAgent.update_memory()`
    * `CriticAgent`
      * `CriticAgent.flatten_options()`
      * `CriticAgent.get_option()`
      * `CriticAgent.parse_critic()`
      * `CriticAgent.reduce_step()`
    * `EmbodiedAgent`
      * `EmbodiedAgent.get_tool_agent_names()`
      * `EmbodiedAgent.step()`
    * `HuggingFaceToolAgent`
      * `HuggingFaceToolAgent.chat()`
      * `HuggingFaceToolAgent.reset()`
      * `HuggingFaceToolAgent.step()`
    * `KnowledgeGraphAgent`
      * `KnowledgeGraphAgent.task_prompt`
      * `KnowledgeGraphAgent.run()`
    * `RoleAssignmentAgent`
      * `RoleAssignmentAgent.role_assignment_prompt`
      * `RoleAssignmentAgent.run()`
    * `SearchAgent`
      * `SearchAgent.continue_search()`
      * `SearchAgent.summarize_text()`
    * `TaskCreationAgent`
      * `TaskCreationAgent.task_creation_prompt`
      * `TaskCreationAgent.run()`
    * `TaskPlannerAgent`
      * `TaskPlannerAgent.task_planner_prompt`
      * `TaskPlannerAgent.run()`
    * `TaskPrioritizationAgent`
      * `TaskPrioritizationAgent.task_prioritization_prompt`
      * `TaskPrioritizationAgent.run()`
    * `TaskSpecifyAgent`
      * `TaskSpecifyAgent.DEFAULT_WORD_LIMIT`
      * `TaskSpecifyAgent.task_specify_prompt`
      * `TaskSpecifyAgent.DEFAULT_WORD_LIMIT`
      * `TaskSpecifyAgent.memory`
      * `TaskSpecifyAgent.model_backend`
      * `TaskSpecifyAgent.model_type`
      * `TaskSpecifyAgent.orig_sys_message`
      * `TaskSpecifyAgent.output_language`
      * `TaskSpecifyAgent.role_name`
      * `TaskSpecifyAgent.role_type`
      * `TaskSpecifyAgent.run()`
      * `TaskSpecifyAgent.task_specify_prompt`
      * `TaskSpecifyAgent.terminated`

# camel.agents package#

## Submodules#

## camel.agents.chat_agent module#

_class _camel.agents.chat_agent.ChatAgent(_system_message : [BaseMessage](camel.messages.html#camel.messages.BaseMessage "camel.messages.BaseMessage")_, _model : BaseModelBackend | None = None_, _memory : AgentMemory | None = None_, _message_window_size : int | None = None_, _token_limit : int | None = None_, _output_language : str | None = None_, _tools : List[OpenAIFunction] | None = None_, _external_tools : List[OpenAIFunction] | None = None_, _response_terminators : List[ResponseTerminator] | None = None_)[[source]](_modules/camel/agents/chat_agent.html#ChatAgent)#
    

Bases: `BaseAgent`

Class for managing conversations of CAMEL Chat Agents.

Parameters:

    

  * **system_message** ([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage "camel.messages.BaseMessage")) – The system message for the chat agent.

  * **model** (_BaseModelBackend_ _,__optional_) – The model backend to use for generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

  * **memory** (_AgentMemory_ _,__optional_) – The agent memory for managing chat messages. If None, a `ChatHistoryMemory` will be used. (default: `None`)

  * **message_window_size** (_int_ _,__optional_) – The maximum number of previous messages to include in the context window. If None, no windowing is performed. (default: `None`)

  * **token_limit** (_int_ _,__optional_) – The maximum number of tokens in a context. The context will be automatically pruned to fulfill the limitation. If None, it will be set according to the backend model. (default: `None`)

  * **output_language** (_str_ _,__optional_) – The language to be output by the agent. (default: `None`)

  * **tools** (_List_ _[__OpenAIFunction_ _]__,__optional_) – List of available `OpenAIFunction`. (default: `None`)

  * **external_tools** (_List_ _[__OpenAIFunction_ _]__,__optional_) – List of external tools (`OpenAIFunction`) bind to one chat agent. When these tools are called, the agent will directly return the request instead of processing it. (default: `None`)

  * **response_terminators** (_List_ _[__ResponseTerminator_ _]__,__optional_) – List of `ResponseTerminator` bind to one chat agent. (default: `None`)

get_info(_session_id : str | None_, _usage : Dict[str, int] | None_, _termination_reasons : List[str]_, _num_tokens : int_, _tool_calls : List[FunctionCallingRecord]_, _external_tool_request : ChatCompletionMessageToolCall | None = None_) -> Dict[str, Any][[source]](_modules/camel/agents/chat_agent.html#ChatAgent.get_info)#
    

Returns a dictionary containing information about the chat session.

Parameters:

    

  * **session_id** (_str_ _,__optional_) – The ID of the chat session.

  * **usage** (_Dict_ _[__str_ _,__int_ _]__,__optional_) – Information about the usage of the LLM model.

  * **termination_reasons** (_List_ _[__str_ _]_) – The reasons for the termination of the chat session.

  * **num_tokens** (_int_) – The number of tokens used in the chat session.

  * **tool_calls** (_List_ _[__FunctionCallingRecord_ _]_) – The list of function calling records, containing the information of called tools.

  * **external_tool_request** – (Optional[ChatCompletionMessageToolCall], optional): The tool calling request of external tools from the model. These requests are directly returned to the user instead of being processed by the agent automatically. (default: `None`)

Returns:

    

The chat session information.

Return type:

    

Dict[str, Any]

get_usage_dict(_output_messages :
List[[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")]_, _prompt_tokens : int_) -> Dict[str,
int][[source]](_modules/camel/agents/chat_agent.html#ChatAgent.get_usage_dict)#

    

Get usage dictionary when using the stream mode.

Parameters:

    

  * **output_messages** (_list_) – List of output messages.

  * **prompt_tokens** (_int_) – Number of input prompt tokens.

Returns:

    

Usage dictionary.

Return type:

    

dict

handle_batch_response(_response :
[ChatCompletion](camel.html#camel.types.ChatCompletion
"openai.types.chat.chat_completion.ChatCompletion")_) ->
Tuple[List[[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")], List[str], Dict[str, int],
str][[source]](_modules/camel/agents/chat_agent.html#ChatAgent.handle_batch_response)#

    

Parameters:

    

**response** (_dict_) – Model response.

Returns:

    

A tuple of list of output ChatMessage, list of

    

finish reasons, usage dictionary, and response id.

Return type:

    

tuple

handle_stream_response(_response :
Stream[[ChatCompletionChunk](camel.html#camel.types.ChatCompletionChunk
"camel.types.ChatCompletionChunk")]_, _prompt_tokens : int_) ->
Tuple[List[[BaseMessage](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")], List[str], Dict[str, int],
str][[source]](_modules/camel/agents/chat_agent.html#ChatAgent.handle_stream_response)#

    

Parameters:

    

  * **response** (_dict_) – Model response.

  * **prompt_tokens** (_int_) – Number of input prompt tokens.

Returns:

    

A tuple of list of output ChatMessage, list of

    

finish reasons, usage dictionary, and response id.

Return type:

    

tuple

init_messages() ->
None[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.init_messages)#

    

Initializes the stored messages list with the initial system message.

is_tools_added() ->
bool[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.is_tools_added)#

    

Whether OpenAI function calling is enabled for this agent.

Returns:

    

Whether OpenAI function calling is enabled for this

    

agent, determined by whether the dictionary of tools is empty.

Return type:

    

bool

record_message(_message :
[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")_) ->
None[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.record_message)#

    

Records the externally provided message into the agent memory as if it were an
answer of the `ChatAgent` from the backend. Currently, the choice of the
critic is submitted with this method.

Parameters:

    

**message** ([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")) – An external message to be recorded in the
memory.

reset()[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.reset)#

    

Resets the `ChatAgent` to its initial state and returns the stored messages.

Returns:

    

The stored messages.

Return type:

    

List[[BaseMessage](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")]

set_output_language(_output_language : str_) ->
[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.set_output_language)#

    

Sets the output language for the system message. This method updates the
output language for the system message. The output language determines the
language in which the output text should be generated.

Parameters:

    

**output_language** (_str_) – The desired output language.

Returns:

    

The updated system message object.

Return type:

    

[BaseMessage](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")

step(_input_message : [BaseMessage](camel.messages.html#camel.messages.base.BaseMessage "camel.messages.base.BaseMessage")_, _output_schema : Type[BaseModel] | None = None_) -> ChatAgentResponse[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.step)#
    

Performs a single step in the chat session by generating a response to the
input message.

Parameters:

    

  * **input_message** ([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage "camel.messages.BaseMessage")) – The input message to the agent. Its role field that specifies the role at backend may be either user or assistant but it will be set to user anyway since for the self agent any incoming message is external.

  * **output_schema** (_Optional_ _[__Type_ _[__BaseModel_ _]__]__,__optional_) – A pydantic model class that includes value types and field descriptions used to generate a structured response by LLM. This schema helps in defining the expected output format. (default: `None`)

Returns:

    

A struct containing the output messages,

    

a boolean indicating whether the chat session has terminated, and information
about the chat session.

Return type:

    

ChatAgentResponse

_async _step_async(_input_message : [BaseMessage](camel.messages.html#camel.messages.base.BaseMessage "camel.messages.base.BaseMessage")_, _output_schema : Type[BaseModel] | None = None_) -> ChatAgentResponse[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.step_async)#
    

Performs a single step in the chat session by generating a response to the
input message. This agent step can call async function calls.

Parameters:

    

  * **input_message** ([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage "camel.messages.BaseMessage")) – The input message to the agent. Its role field that specifies the role at backend may be either user or assistant but it will be set to user anyway since for the self agent any incoming message is external.

  * **output_schema** (_Optional_ _[__Type_ _[__BaseModel_ _]__]__,__optional_) – A pydantic model class that includes value types and field descriptions used to generate a structured response by LLM. This schema helps in defining the expected output format. (default: `None`)

Returns:

    

A struct containing the output messages,

    

a boolean indicating whether the chat session has terminated, and information
about the chat session.

Return type:

    

ChatAgentResponse

step_tool_call(_response :
[ChatCompletion](camel.html#camel.types.ChatCompletion
"openai.types.chat.chat_completion.ChatCompletion")_) ->
Tuple[[FunctionCallingMessage](camel.messages.html#camel.messages.FunctionCallingMessage
"camel.messages.func_message.FunctionCallingMessage"),
[FunctionCallingMessage](camel.messages.html#camel.messages.FunctionCallingMessage
"camel.messages.func_message.FunctionCallingMessage"),
FunctionCallingRecord][[source]](_modules/camel/agents/chat_agent.html#ChatAgent.step_tool_call)#

    

Execute the function with arguments following the model’s response.

Parameters:

    

**response** (_Dict_ _[__str_ _,__Any_ _]_) – The response obtained by calling
the model.

Returns:

    

A tuple consisting of two obj:FunctionCallingMessage,

    

one about the arguments and the other about the execution result, and a struct
for logging information about this function call.

Return type:

    

tuple

_async _step_tool_call_async(_response :
[ChatCompletion](camel.html#camel.types.ChatCompletion
"openai.types.chat.chat_completion.ChatCompletion")_) ->
Tuple[[FunctionCallingMessage](camel.messages.html#camel.messages.FunctionCallingMessage
"camel.messages.func_message.FunctionCallingMessage"),
[FunctionCallingMessage](camel.messages.html#camel.messages.FunctionCallingMessage
"camel.messages.func_message.FunctionCallingMessage"),
FunctionCallingRecord][[source]](_modules/camel/agents/chat_agent.html#ChatAgent.step_tool_call_async)#

    

Execute the async function with arguments following the model’s response.

Parameters:

    

**response** (_Dict_ _[__str_ _,__Any_ _]_) – The response obtained by calling
the model.

Returns:

    

A tuple consisting of two obj:FunctionCallingMessage,

    

one about the arguments and the other about the execution result, and a struct
for logging information about this function call.

Return type:

    

tuple

_property _system_message _:
[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")_#

    

The getter method for the property `system_message`.

Returns:

    

The system message of this agent.

Return type:

    

[BaseMessage](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")

update_memory(_message :
[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")_, _role :
[OpenAIBackendRole](camel.html#camel.types.OpenAIBackendRole
"camel.types.enums.OpenAIBackendRole")_) ->
None[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.update_memory)#

    

Updates the agent memory with a new message.

Parameters:

    

  * **message** ([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage "camel.messages.BaseMessage")) – The new message to add to the stored messages.

  * **role** ([_OpenAIBackendRole_](camel.html#camel.types.OpenAIBackendRole "camel.types.OpenAIBackendRole")) – The backend role type.

_class _camel.agents.chat_agent.FunctionCallingRecord(_*_ , _func_name : str_,
_args : Dict[str, Any]_, _result :
Any_)[[source]](_modules/camel/agents/chat_agent.html#FunctionCallingRecord)#

    

Bases: `BaseModel`

Historical records of functions called in the conversation.

func_name#

    

The name of the function being called.

Type:

    

str

args#

    

The dictionary of arguments passed to the function.

Type:

    

Dict[str, Any]

result#

    

The execution result of calling this function.

Type:

    

Any

args _: Dict[str, Any]_#

    

as_dict() -> dict[str,
Any][[source]](_modules/camel/agents/chat_agent.html#FunctionCallingRecord.as_dict)#

    

func_name _: str_#

    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'args':
FieldInfo(annotation=Dict[str, Any], required=True), 'func_name':
FieldInfo(annotation=str, required=True), 'result': FieldInfo(annotation=Any,
required=True)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

result _: Any_#

    

## camel.agents.role_playing module#

## camel.agents.task_agent module#

_class _camel.agents.task_agent.TaskCreationAgent(_role_name : str_, _objective : str | [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")_, _model : BaseModelBackend | None = None_, _output_language : str | None = None_, _message_window_size : int | None = None_, _max_task_num : int | None = 3_)[[source]](_modules/camel/agents/task_agent.html#TaskCreationAgent)#
    

Bases: `ChatAgent`

An agent that helps create new tasks based on the objective and last completed
task. Compared to `TaskPlannerAgent`, it’s still a task planner, but it has
more context information like last task and incomplete task list. Modified
from [BabyAGI](https://github.com/yoheinakajima/babyagi).

task_creation_prompt#

    

A prompt for the agent to create new tasks.

Type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

Parameters:

    

  * **role_name** (_str_) – The role name of the Agent to create the task.

  * **objective** (_Union_ _[__str_ _,_[_TextPrompt_](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt") _]_) – The objective of the Agent to perform the task.

  * **model** (_BaseModelBackend_ _,__optional_) – The LLM backend to use for generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

  * **output_language** (_str_ _,__optional_) – The language to be output by the agent. (default: `None`)

  * **message_window_size** (_int_ _,__optional_) – The maximum number of previous messages to include in the context window. If None, no windowing is performed. (default: `None`)

  * **max_task_num** (_int_ _,__optional_) – The maximum number of planned tasks in one round. (default: :obj:3)

run(_task_list : List[str]_) ->
List[str][[source]](_modules/camel/agents/task_agent.html#TaskCreationAgent.run)#

    

Generate subtasks based on the previous task results and incomplete task list.

Parameters:

    

**task_list** (_List_ _[__str_ _]_) – The completed or in-progress tasks which
should not overlap with new created tasks.

Returns:

    

The new task list generated by the Agent.

Return type:

    

List[str]

_class _camel.agents.task_agent.TaskPlannerAgent(_model : BaseModelBackend | None = None_, _output_language : str | None = None_)[[source]](_modules/camel/agents/task_agent.html#TaskPlannerAgent)#
    

Bases: `ChatAgent`

An agent that helps divide a task into subtasks based on the input task
prompt.

task_planner_prompt#

    

A prompt for the agent to divide the task into subtasks.

Type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

Parameters:

    

  * **model** (_BaseModelBackend_ _,__optional_) – The model backend to use for generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

  * **output_language** (_str_ _,__optional_) – The language to be output by the agent. (default: `None`)

run(_task_prompt : str | [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")_) -> [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")[[source]](_modules/camel/agents/task_agent.html#TaskPlannerAgent.run)#
    

Generate subtasks based on the input task prompt.

Parameters:

    

**task_prompt** (_Union_ _[__str_
_,_[_TextPrompt_](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt") _]_) – The prompt for the task to be divided
into subtasks.

Returns:

    

A prompt for the subtasks generated by the agent.

Return type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

_class _camel.agents.task_agent.TaskPrioritizationAgent(_objective : str | [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")_, _model : BaseModelBackend | None = None_, _output_language : str | None = None_, _message_window_size : int | None = None_)[[source]](_modules/camel/agents/task_agent.html#TaskPrioritizationAgent)#
    

Bases: `ChatAgent`

An agent that helps re-prioritize the task list and returns numbered
prioritized list. Modified from
[BabyAGI](https://github.com/yoheinakajima/babyagi).

task_prioritization_prompt#

    

A prompt for the agent to prioritize tasks.

Type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

Parameters:

    

  * **objective** (_Union_ _[__str_ _,_[_TextPrompt_](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt") _]_) – The objective of the Agent to perform the task.

  * **model** (_BaseModelBackend_ _,__optional_) – The LLM backend to use for generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

  * **output_language** (_str_ _,__optional_) – The language to be output by the agent. (default: `None`)

  * **message_window_size** (_int_ _,__optional_) – The maximum number of previous messages to include in the context window. If None, no windowing is performed. (default: `None`)

run(_task_list : List[str]_) ->
List[str][[source]](_modules/camel/agents/task_agent.html#TaskPrioritizationAgent.run)#

    

Prioritize the task list given the agent objective.

Parameters:

    

**task_list** (_List_ _[__str_ _]_) – The unprioritized tasks of agent.

Returns:

    

The new prioritized task list generated by the Agent.

Return type:

    

List[str]

_class _camel.agents.task_agent.TaskSpecifyAgent(_model : BaseModelBackend | None = None_, _task_type : [TaskType](camel.html#camel.types.TaskType "camel.types.enums.TaskType") = TaskType.AI_SOCIETY_, _task_specify_prompt : str | [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt") | None = None_, _word_limit : int = 50_, _output_language : str | None = None_)[[source]](_modules/camel/agents/task_agent.html#TaskSpecifyAgent)#
    

Bases: `ChatAgent`

An agent that specifies a given task prompt by prompting the user to provide
more details.

DEFAULT_WORD_LIMIT#

    

The default word limit for the task prompt.

Type:

    

int

task_specify_prompt#

    

The prompt for specifying the task.

Type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

Parameters:

    

  * **model** (_BaseModelBackend_ _,__optional_) – The model backend to use for generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

  * **task_type** ([_TaskType_](camel.html#camel.types.TaskType "camel.types.TaskType") _,__optional_) – The type of task for which to generate a prompt. (default: `TaskType.AI_SOCIETY`)

  * **task_specify_prompt** (_Union_ _[__str_ _,_[_TextPrompt_](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt") _]__,__optional_) – The prompt for specifying the task. (default: `None`)

  * **word_limit** (_int_ _,__optional_) – The word limit for the task prompt. (default: `50`)

  * **output_language** (_str_ _,__optional_) – The language to be output by the agent. (default: `None`)

DEFAULT_WORD_LIMIT _ = 50_#

    

run(_task_prompt : str | [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")_, _meta_dict : Dict[str, Any] | None = None_) -> [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")[[source]](_modules/camel/agents/task_agent.html#TaskSpecifyAgent.run)#
    

Specify the given task prompt by providing more details.

Parameters:

    

  * **task_prompt** (_Union_ _[__str_ _,_[_TextPrompt_](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt") _]_) – The original task prompt.

  * **meta_dict** (_Dict_ _[__str_ _,__Any_ _]__,__optional_) – A dictionary containing additional information to include in the prompt. (default: `None`)

Returns:

    

The specified task prompt.

Return type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

## Module contents#

_class
_camel.agents.BaseAgent[[source]](_modules/camel/agents/base.html#BaseAgent)#

    

Bases: `ABC`

An abstract base class for all CAMEL agents.

_abstract _reset(_* args: Any_, _** kwargs: Any_) ->
Any[[source]](_modules/camel/agents/base.html#BaseAgent.reset)#

    

Resets the agent to its initial state.

_abstract _step(_* args: Any_, _** kwargs: Any_) ->
Any[[source]](_modules/camel/agents/base.html#BaseAgent.step)#

    

Performs a single step of the agent.

_class _camel.agents.BaseToolAgent(_name : str_, _description :
str_)[[source]](_modules/camel/agents/tool_agents/base.html#BaseToolAgent)#

    

Bases: `BaseAgent`

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

_class _camel.agents.ChatAgent(_system_message : [BaseMessage](camel.messages.html#camel.messages.BaseMessage "camel.messages.BaseMessage")_, _model : BaseModelBackend | None = None_, _memory : AgentMemory | None = None_, _message_window_size : int | None = None_, _token_limit : int | None = None_, _output_language : str | None = None_, _tools : List[OpenAIFunction] | None = None_, _external_tools : List[OpenAIFunction] | None = None_, _response_terminators : List[ResponseTerminator] | None = None_)[[source]](_modules/camel/agents/chat_agent.html#ChatAgent)#
    

Bases: `BaseAgent`

Class for managing conversations of CAMEL Chat Agents.

Parameters:

    

  * **system_message** ([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage "camel.messages.BaseMessage")) – The system message for the chat agent.

  * **model** (_BaseModelBackend_ _,__optional_) – The model backend to use for generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

  * **memory** (_AgentMemory_ _,__optional_) – The agent memory for managing chat messages. If None, a `ChatHistoryMemory` will be used. (default: `None`)

  * **message_window_size** (_int_ _,__optional_) – The maximum number of previous messages to include in the context window. If None, no windowing is performed. (default: `None`)

  * **token_limit** (_int_ _,__optional_) – The maximum number of tokens in a context. The context will be automatically pruned to fulfill the limitation. If None, it will be set according to the backend model. (default: `None`)

  * **output_language** (_str_ _,__optional_) – The language to be output by the agent. (default: `None`)

  * **tools** (_List_ _[__OpenAIFunction_ _]__,__optional_) – List of available `OpenAIFunction`. (default: `None`)

  * **external_tools** (_List_ _[__OpenAIFunction_ _]__,__optional_) – List of external tools (`OpenAIFunction`) bind to one chat agent. When these tools are called, the agent will directly return the request instead of processing it. (default: `None`)

  * **response_terminators** (_List_ _[__ResponseTerminator_ _]__,__optional_) – List of `ResponseTerminator` bind to one chat agent. (default: `None`)

get_info(_session_id : str | None_, _usage : Dict[str, int] | None_, _termination_reasons : List[str]_, _num_tokens : int_, _tool_calls : List[FunctionCallingRecord]_, _external_tool_request : ChatCompletionMessageToolCall | None = None_) -> Dict[str, Any][[source]](_modules/camel/agents/chat_agent.html#ChatAgent.get_info)#
    

Returns a dictionary containing information about the chat session.

Parameters:

    

  * **session_id** (_str_ _,__optional_) – The ID of the chat session.

  * **usage** (_Dict_ _[__str_ _,__int_ _]__,__optional_) – Information about the usage of the LLM model.

  * **termination_reasons** (_List_ _[__str_ _]_) – The reasons for the termination of the chat session.

  * **num_tokens** (_int_) – The number of tokens used in the chat session.

  * **tool_calls** (_List_ _[__FunctionCallingRecord_ _]_) – The list of function calling records, containing the information of called tools.

  * **external_tool_request** – (Optional[ChatCompletionMessageToolCall], optional): The tool calling request of external tools from the model. These requests are directly returned to the user instead of being processed by the agent automatically. (default: `None`)

Returns:

    

The chat session information.

Return type:

    

Dict[str, Any]

get_usage_dict(_output_messages :
List[[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")]_, _prompt_tokens : int_) -> Dict[str,
int][[source]](_modules/camel/agents/chat_agent.html#ChatAgent.get_usage_dict)#

    

Get usage dictionary when using the stream mode.

Parameters:

    

  * **output_messages** (_list_) – List of output messages.

  * **prompt_tokens** (_int_) – Number of input prompt tokens.

Returns:

    

Usage dictionary.

Return type:

    

dict

handle_batch_response(_response :
[ChatCompletion](camel.html#camel.types.ChatCompletion
"openai.types.chat.chat_completion.ChatCompletion")_) ->
Tuple[List[[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")], List[str], Dict[str, int],
str][[source]](_modules/camel/agents/chat_agent.html#ChatAgent.handle_batch_response)#

    

Parameters:

    

**response** (_dict_) – Model response.

Returns:

    

A tuple of list of output ChatMessage, list of

    

finish reasons, usage dictionary, and response id.

Return type:

    

tuple

handle_stream_response(_response :
Stream[[ChatCompletionChunk](camel.html#camel.types.ChatCompletionChunk
"camel.types.ChatCompletionChunk")]_, _prompt_tokens : int_) ->
Tuple[List[[BaseMessage](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")], List[str], Dict[str, int],
str][[source]](_modules/camel/agents/chat_agent.html#ChatAgent.handle_stream_response)#

    

Parameters:

    

  * **response** (_dict_) – Model response.

  * **prompt_tokens** (_int_) – Number of input prompt tokens.

Returns:

    

A tuple of list of output ChatMessage, list of

    

finish reasons, usage dictionary, and response id.

Return type:

    

tuple

init_messages() ->
None[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.init_messages)#

    

Initializes the stored messages list with the initial system message.

is_tools_added() ->
bool[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.is_tools_added)#

    

Whether OpenAI function calling is enabled for this agent.

Returns:

    

Whether OpenAI function calling is enabled for this

    

agent, determined by whether the dictionary of tools is empty.

Return type:

    

bool

record_message(_message :
[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")_) ->
None[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.record_message)#

    

Records the externally provided message into the agent memory as if it were an
answer of the `ChatAgent` from the backend. Currently, the choice of the
critic is submitted with this method.

Parameters:

    

**message** ([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")) – An external message to be recorded in the
memory.

reset()[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.reset)#

    

Resets the `ChatAgent` to its initial state and returns the stored messages.

Returns:

    

The stored messages.

Return type:

    

List[[BaseMessage](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")]

set_output_language(_output_language : str_) ->
[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.set_output_language)#

    

Sets the output language for the system message. This method updates the
output language for the system message. The output language determines the
language in which the output text should be generated.

Parameters:

    

**output_language** (_str_) – The desired output language.

Returns:

    

The updated system message object.

Return type:

    

[BaseMessage](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")

step(_input_message : [BaseMessage](camel.messages.html#camel.messages.base.BaseMessage "camel.messages.base.BaseMessage")_, _output_schema : Type[BaseModel] | None = None_) -> ChatAgentResponse[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.step)#
    

Performs a single step in the chat session by generating a response to the
input message.

Parameters:

    

  * **input_message** ([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage "camel.messages.BaseMessage")) – The input message to the agent. Its role field that specifies the role at backend may be either user or assistant but it will be set to user anyway since for the self agent any incoming message is external.

  * **output_schema** (_Optional_ _[__Type_ _[__BaseModel_ _]__]__,__optional_) – A pydantic model class that includes value types and field descriptions used to generate a structured response by LLM. This schema helps in defining the expected output format. (default: `None`)

Returns:

    

A struct containing the output messages,

    

a boolean indicating whether the chat session has terminated, and information
about the chat session.

Return type:

    

ChatAgentResponse

_async _step_async(_input_message : [BaseMessage](camel.messages.html#camel.messages.base.BaseMessage "camel.messages.base.BaseMessage")_, _output_schema : Type[BaseModel] | None = None_) -> ChatAgentResponse[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.step_async)#
    

Performs a single step in the chat session by generating a response to the
input message. This agent step can call async function calls.

Parameters:

    

  * **input_message** ([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage "camel.messages.BaseMessage")) – The input message to the agent. Its role field that specifies the role at backend may be either user or assistant but it will be set to user anyway since for the self agent any incoming message is external.

  * **output_schema** (_Optional_ _[__Type_ _[__BaseModel_ _]__]__,__optional_) – A pydantic model class that includes value types and field descriptions used to generate a structured response by LLM. This schema helps in defining the expected output format. (default: `None`)

Returns:

    

A struct containing the output messages,

    

a boolean indicating whether the chat session has terminated, and information
about the chat session.

Return type:

    

ChatAgentResponse

step_tool_call(_response :
[ChatCompletion](camel.html#camel.types.ChatCompletion
"openai.types.chat.chat_completion.ChatCompletion")_) ->
Tuple[[FunctionCallingMessage](camel.messages.html#camel.messages.FunctionCallingMessage
"camel.messages.func_message.FunctionCallingMessage"),
[FunctionCallingMessage](camel.messages.html#camel.messages.FunctionCallingMessage
"camel.messages.func_message.FunctionCallingMessage"),
FunctionCallingRecord][[source]](_modules/camel/agents/chat_agent.html#ChatAgent.step_tool_call)#

    

Execute the function with arguments following the model’s response.

Parameters:

    

**response** (_Dict_ _[__str_ _,__Any_ _]_) – The response obtained by calling
the model.

Returns:

    

A tuple consisting of two obj:FunctionCallingMessage,

    

one about the arguments and the other about the execution result, and a struct
for logging information about this function call.

Return type:

    

tuple

_async _step_tool_call_async(_response :
[ChatCompletion](camel.html#camel.types.ChatCompletion
"openai.types.chat.chat_completion.ChatCompletion")_) ->
Tuple[[FunctionCallingMessage](camel.messages.html#camel.messages.FunctionCallingMessage
"camel.messages.func_message.FunctionCallingMessage"),
[FunctionCallingMessage](camel.messages.html#camel.messages.FunctionCallingMessage
"camel.messages.func_message.FunctionCallingMessage"),
FunctionCallingRecord][[source]](_modules/camel/agents/chat_agent.html#ChatAgent.step_tool_call_async)#

    

Execute the async function with arguments following the model’s response.

Parameters:

    

**response** (_Dict_ _[__str_ _,__Any_ _]_) – The response obtained by calling
the model.

Returns:

    

A tuple consisting of two obj:FunctionCallingMessage,

    

one about the arguments and the other about the execution result, and a struct
for logging information about this function call.

Return type:

    

tuple

_property _system_message _:
[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")_#

    

The getter method for the property `system_message`.

Returns:

    

The system message of this agent.

Return type:

    

[BaseMessage](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")

update_memory(_message :
[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")_, _role :
[OpenAIBackendRole](camel.html#camel.types.OpenAIBackendRole
"camel.types.enums.OpenAIBackendRole")_) ->
None[[source]](_modules/camel/agents/chat_agent.html#ChatAgent.update_memory)#

    

Updates the agent memory with a new message.

Parameters:

    

  * **message** ([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage "camel.messages.BaseMessage")) – The new message to add to the stored messages.

  * **role** ([_OpenAIBackendRole_](camel.html#camel.types.OpenAIBackendRole "camel.types.OpenAIBackendRole")) – The backend role type.

_class _camel.agents.CriticAgent(_system_message : [BaseMessage](camel.messages.html#camel.messages.base.BaseMessage "camel.messages.base.BaseMessage")_, _model : BaseModelBackend | None = None_, _memory : AgentMemory | None = None_, _message_window_size : int = 6_, _retry_attempts : int = 2_, _verbose : bool = False_, _logger_color : Any = '\x1b[35m'_)[[source]](_modules/camel/agents/critic_agent.html#CriticAgent)#
    

Bases: `ChatAgent`

A class for the critic agent that assists in selecting an option.

Parameters:

    

  * **system_message** ([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage "camel.messages.BaseMessage")) – The system message for the critic agent.

  * **model** (_BaseModelBackend_ _,__optional_) – The model backend to use for generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

  * **message_window_size** (_int_ _,__optional_) – The maximum number of previous messages to include in the context window. If None, no windowing is performed. (default: `6`)

  * **retry_attempts** (_int_ _,__optional_) – The number of retry attempts if the critic fails to return a valid option. (default: `2`)

  * **verbose** (_bool_ _,__optional_) – Whether to print the critic’s messages.

  * **logger_color** (_Any_) – The color of the menu options displayed to the user. (default: `Fore.MAGENTA`)

flatten_options(_messages :
Sequence[[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")]_) ->
str[[source]](_modules/camel/agents/critic_agent.html#CriticAgent.flatten_options)#

    

Flattens the options to the critic.

Parameters:

    

**messages** (_Sequence_
_[_[_BaseMessage_](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage") _]_) – A list of BaseMessage objects.

Returns:

    

A string containing the flattened options to the critic.

Return type:

    

str

get_option(_input_message :
[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")_) ->
str[[source]](_modules/camel/agents/critic_agent.html#CriticAgent.get_option)#

    

Gets the option selected by the critic.

Parameters:

    

**input_message**
([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")) – A BaseMessage object representing the input
message.

Returns:

    

The option selected by the critic.

Return type:

    

str

parse_critic(_critic_msg : [BaseMessage](camel.messages.html#camel.messages.base.BaseMessage "camel.messages.base.BaseMessage")_) -> str | None[[source]](_modules/camel/agents/critic_agent.html#CriticAgent.parse_critic)#
    

Parses the critic’s message and extracts the choice.

Parameters:

    

**critic_msg** ([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")) – A BaseMessage object representing the
critic’s response.

Returns:

    

The critic’s choice as a string, or None if the

    

message could not be parsed.

Return type:

    

Optional[str]

reduce_step(_input_messages :
Sequence[[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")]_) ->
ChatAgentResponse[[source]](_modules/camel/agents/critic_agent.html#CriticAgent.reduce_step)#

    

Performs one step of the conversation by flattening options to the critic,
getting the option, and parsing the choice.

Parameters:

    

**input_messages** (_Sequence_
_[_[_BaseMessage_](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage") _]_) – A list of BaseMessage objects.

Returns:

    

A ChatAgentResponse object includes the

    

critic’s choice.

Return type:

    

ChatAgentResponse

_class _camel.agents.EmbodiedAgent(_system_message : [BaseMessage](camel.messages.html#camel.messages.base.BaseMessage "camel.messages.base.BaseMessage")_, _model : BaseModelBackend | None = None_, _message_window_size : int | None = None_, _tool_agents : List[[BaseToolAgent](camel.agents.tool_agents.html#camel.agents.tool_agents.base.BaseToolAgent "camel.agents.tool_agents.base.BaseToolAgent")] | None = None_, _code_interpreter : BaseInterpreter | None = None_, _verbose : bool = False_, _logger_color : Any = '\x1b[35m'_)[[source]](_modules/camel/agents/embodied_agent.html#EmbodiedAgent)#
    

Bases: `ChatAgent`

Class for managing conversations of CAMEL Embodied Agents.

Parameters:

    

  * **system_message** ([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage "camel.messages.BaseMessage")) – The system message for the chat agent.

  * **model** (_BaseModelBackend_ _,__optional_) – The model backend to use for generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

  * **message_window_size** (_int_ _,__optional_) – The maximum number of previous messages to include in the context window. If None, no windowing is performed. (default: `None`)

  * **tool_agents** (_List_ _[__BaseToolAgent_ _]__,__optional_) – The tools agents to use in the embodied agent. (default: `None`)

  * **code_interpreter** (_BaseInterpreter_ _,__optional_) – The code interpreter to execute codes. If code_interpreter and tool_agent are both None, default to SubProcessInterpreter. If code_interpreter is None and tool_agents is not None, default to InternalPythonInterpreter. (default: `None`)

  * **verbose** (_bool_ _,__optional_) – Whether to print the critic’s messages.

  * **logger_color** (_Any_) – The color of the logger displayed to the user. (default: `Fore.MAGENTA`)

get_tool_agent_names() ->
List[str][[source]](_modules/camel/agents/embodied_agent.html#EmbodiedAgent.get_tool_agent_names)#

    

Returns the names of tool agents.

Returns:

    

The names of tool agents.

Return type:

    

List[str]

step(_input_message :
[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")_) ->
ChatAgentResponse[[source]](_modules/camel/agents/embodied_agent.html#EmbodiedAgent.step)#

    

Performs a step in the conversation.

Parameters:

    

**input_message**
([_BaseMessage_](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")) – The input message.

Returns:

    

A struct containing the output messages,

    

a boolean indicating whether the chat session has terminated, and information
about the chat session.

Return type:

    

ChatAgentResponse

_class _camel.agents.HuggingFaceToolAgent(_name : str_, _* args: Any_, _remote
: bool = True_, _** kwargs:
Any_)[[source]](_modules/camel/agents/tool_agents/hugging_face_tool_agent.html#HuggingFaceToolAgent)#

    

Bases:
[`BaseToolAgent`](camel.agents.tool_agents.html#camel.agents.tool_agents.base.BaseToolAgent
"camel.agents.tool_agents.base.BaseToolAgent")

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

_class _camel.agents.KnowledgeGraphAgent(_model : BaseModelBackend | None = None_)[[source]](_modules/camel/agents/knowledge_graph_agent.html#KnowledgeGraphAgent)#
    

Bases: `ChatAgent`

An agent that can extract node and relationship information for different
entities from given Element content.

task_prompt#

    

A prompt for the agent to extract node and relationship information for
different entities.

Type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

run(_element : str | Element_, _parse_graph_elements : bool = False_) -> str | GraphElement[[source]](_modules/camel/agents/knowledge_graph_agent.html#KnowledgeGraphAgent.run)#
    

Run the agent to extract node and relationship information.

Parameters:

    

  * **element** (_Union_ _[__str_ _,__Element_ _]_) – The input element or string.

  * **parse_graph_elements** (_bool_ _,__optional_) – Whether to parse into GraphElement. Defaults to False.

Returns:

    

The extracted node and relationship

    

information. If parse_graph_elements is True then return GraphElement, else
return str.

Return type:

    

Union[str, GraphElement]

_class _camel.agents.RoleAssignmentAgent(_model : BaseModelBackend | None = None_)[[source]](_modules/camel/agents/role_assignment_agent.html#RoleAssignmentAgent)#
    

Bases: `ChatAgent`

An agent that generates role names based on the task prompt.

Parameters:

    

**model** (_BaseModelBackend_ _,__optional_) – The model backend to use for
generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

role_assignment_prompt#

    

A prompt for the agent to generate

Type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

role names.

    

run(_task_prompt : str | [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")_, _num_roles : int = 2_) -> Dict[str, str][[source]](_modules/camel/agents/role_assignment_agent.html#RoleAssignmentAgent.run)#
    

Generate role names based on the input task prompt.

Parameters:

    

  * **task_prompt** (_Union_ _[__str_ _,_[_TextPrompt_](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt") _]_) – The prompt for the task based on which the roles are to be generated.

  * **num_roles** (_int_ _,__optional_) – The number of roles to generate. (default: `2`)

Returns:

    

A dictionary mapping role names to their

    

descriptions.

Return type:

    

Dict[str, str]

_class _camel.agents.SearchAgent(_model : BaseModelBackend | None = None_)[[source]](_modules/camel/agents/search_agent.html#SearchAgent)#
    

Bases: `ChatAgent`

An agent that summarizes text based on a query and evaluates the relevance of
an answer.

Parameters:

    

**model** (_BaseModelBackend_ _,__optional_) – The model backend to use for
generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

continue_search(_query : str_, _answer : str_) ->
bool[[source]](_modules/camel/agents/search_agent.html#SearchAgent.continue_search)#

    

Ask whether to continue search or not based on the provided answer.

Parameters:

    

  * **query** (_str_) – The question.

  * **answer** (_str_) – The answer to the question.

Returns:

    

True if the user want to continue search, False otherwise.

Return type:

    

bool

summarize_text(_text : str_, _query : str_) ->
str[[source]](_modules/camel/agents/search_agent.html#SearchAgent.summarize_text)#

    

Summarize the information from the text, base on the query.

Parameters:

    

  * **text** (_str_) – Text to summarize.

  * **query** (_str_) – What information you want.

Returns:

    

Strings with information.

Return type:

    

str

_class _camel.agents.TaskCreationAgent(_role_name : str_, _objective : str | [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")_, _model : BaseModelBackend | None = None_, _output_language : str | None = None_, _message_window_size : int | None = None_, _max_task_num : int | None = 3_)[[source]](_modules/camel/agents/task_agent.html#TaskCreationAgent)#
    

Bases: `ChatAgent`

An agent that helps create new tasks based on the objective and last completed
task. Compared to `TaskPlannerAgent`, it’s still a task planner, but it has
more context information like last task and incomplete task list. Modified
from [BabyAGI](https://github.com/yoheinakajima/babyagi).

task_creation_prompt#

    

A prompt for the agent to create new tasks.

Type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

Parameters:

    

  * **role_name** (_str_) – The role name of the Agent to create the task.

  * **objective** (_Union_ _[__str_ _,_[_TextPrompt_](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt") _]_) – The objective of the Agent to perform the task.

  * **model** (_BaseModelBackend_ _,__optional_) – The LLM backend to use for generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

  * **output_language** (_str_ _,__optional_) – The language to be output by the agent. (default: `None`)

  * **message_window_size** (_int_ _,__optional_) – The maximum number of previous messages to include in the context window. If None, no windowing is performed. (default: `None`)

  * **max_task_num** (_int_ _,__optional_) – The maximum number of planned tasks in one round. (default: :obj:3)

run(_task_list : List[str]_) ->
List[str][[source]](_modules/camel/agents/task_agent.html#TaskCreationAgent.run)#

    

Generate subtasks based on the previous task results and incomplete task list.

Parameters:

    

**task_list** (_List_ _[__str_ _]_) – The completed or in-progress tasks which
should not overlap with new created tasks.

Returns:

    

The new task list generated by the Agent.

Return type:

    

List[str]

_class _camel.agents.TaskPlannerAgent(_model : BaseModelBackend | None = None_, _output_language : str | None = None_)[[source]](_modules/camel/agents/task_agent.html#TaskPlannerAgent)#
    

Bases: `ChatAgent`

An agent that helps divide a task into subtasks based on the input task
prompt.

task_planner_prompt#

    

A prompt for the agent to divide the task into subtasks.

Type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

Parameters:

    

  * **model** (_BaseModelBackend_ _,__optional_) – The model backend to use for generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

  * **output_language** (_str_ _,__optional_) – The language to be output by the agent. (default: `None`)

run(_task_prompt : str | [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")_) -> [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")[[source]](_modules/camel/agents/task_agent.html#TaskPlannerAgent.run)#
    

Generate subtasks based on the input task prompt.

Parameters:

    

**task_prompt** (_Union_ _[__str_
_,_[_TextPrompt_](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt") _]_) – The prompt for the task to be divided
into subtasks.

Returns:

    

A prompt for the subtasks generated by the agent.

Return type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

_class _camel.agents.TaskPrioritizationAgent(_objective : str | [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")_, _model : BaseModelBackend | None = None_, _output_language : str | None = None_, _message_window_size : int | None = None_)[[source]](_modules/camel/agents/task_agent.html#TaskPrioritizationAgent)#
    

Bases: `ChatAgent`

An agent that helps re-prioritize the task list and returns numbered
prioritized list. Modified from
[BabyAGI](https://github.com/yoheinakajima/babyagi).

task_prioritization_prompt#

    

A prompt for the agent to prioritize tasks.

Type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

Parameters:

    

  * **objective** (_Union_ _[__str_ _,_[_TextPrompt_](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt") _]_) – The objective of the Agent to perform the task.

  * **model** (_BaseModelBackend_ _,__optional_) – The LLM backend to use for generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

  * **output_language** (_str_ _,__optional_) – The language to be output by the agent. (default: `None`)

  * **message_window_size** (_int_ _,__optional_) – The maximum number of previous messages to include in the context window. If None, no windowing is performed. (default: `None`)

run(_task_list : List[str]_) ->
List[str][[source]](_modules/camel/agents/task_agent.html#TaskPrioritizationAgent.run)#

    

Prioritize the task list given the agent objective.

Parameters:

    

**task_list** (_List_ _[__str_ _]_) – The unprioritized tasks of agent.

Returns:

    

The new prioritized task list generated by the Agent.

Return type:

    

List[str]

_class _camel.agents.TaskSpecifyAgent(_model : BaseModelBackend | None = None_, _task_type : [TaskType](camel.html#camel.types.TaskType "camel.types.enums.TaskType") = TaskType.AI_SOCIETY_, _task_specify_prompt : str | [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt") | None = None_, _word_limit : int = 50_, _output_language : str | None = None_)[[source]](_modules/camel/agents/task_agent.html#TaskSpecifyAgent)#
    

Bases: `ChatAgent`

An agent that specifies a given task prompt by prompting the user to provide
more details.

DEFAULT_WORD_LIMIT#

    

The default word limit for the task prompt.

Type:

    

int

task_specify_prompt#

    

The prompt for specifying the task.

Type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

Parameters:

    

  * **model** (_BaseModelBackend_ _,__optional_) – The model backend to use for generating responses. (default: `OpenAIModel` with GPT_4O_MINI)

  * **task_type** ([_TaskType_](camel.html#camel.types.TaskType "camel.types.TaskType") _,__optional_) – The type of task for which to generate a prompt. (default: `TaskType.AI_SOCIETY`)

  * **task_specify_prompt** (_Union_ _[__str_ _,_[_TextPrompt_](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt") _]__,__optional_) – The prompt for specifying the task. (default: `None`)

  * **word_limit** (_int_ _,__optional_) – The word limit for the task prompt. (default: `50`)

  * **output_language** (_str_ _,__optional_) – The language to be output by the agent. (default: `None`)

DEFAULT_WORD_LIMIT _ = 50_#

    

memory _: AgentMemory_#

    

model_backend _: BaseModelBackend_#

    

model_type _: [ModelType](camel.html#camel.types.ModelType
"camel.types.ModelType")_#

    

orig_sys_message _:
[BaseMessage](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")_#

    

output_language _: str | None_#
    

role_name _: str_#

    

role_type _: [RoleType](camel.html#camel.types.RoleType
"camel.types.RoleType")_#

    

run(_task_prompt : str | [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")_, _meta_dict : Dict[str, Any] | None = None_) -> [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")[[source]](_modules/camel/agents/task_agent.html#TaskSpecifyAgent.run)#
    

Specify the given task prompt by providing more details.

Parameters:

    

  * **task_prompt** (_Union_ _[__str_ _,_[_TextPrompt_](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt") _]_) – The original task prompt.

  * **meta_dict** (_Dict_ _[__str_ _,__Any_ _]__,__optional_) – A dictionary containing additional information to include in the prompt. (default: `None`)

Returns:

    

The specified task prompt.

Return type:

    

[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")

task_specify_prompt _: str | [TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt "camel.prompts.base.TextPrompt")_#
    

terminated _: bool_#

    

[ __ previous Camel Package ](camel.html "previous page") [ next camel.prompts
package __](camel.prompts.html "next page")

__Contents

  * Submodules
  * camel.agents.chat_agent module
    * `ChatAgent`
      * `ChatAgent.get_info()`
      * `ChatAgent.get_usage_dict()`
      * `ChatAgent.handle_batch_response()`
      * `ChatAgent.handle_stream_response()`
      * `ChatAgent.init_messages()`
      * `ChatAgent.is_tools_added()`
      * `ChatAgent.record_message()`
      * `ChatAgent.reset()`
      * `ChatAgent.set_output_language()`
      * `ChatAgent.step()`
      * `ChatAgent.step_async()`
      * `ChatAgent.step_tool_call()`
      * `ChatAgent.step_tool_call_async()`
      * `ChatAgent.system_message`
      * `ChatAgent.update_memory()`
    * `FunctionCallingRecord`
      * `FunctionCallingRecord.func_name`
      * `FunctionCallingRecord.args`
      * `FunctionCallingRecord.result`
      * `FunctionCallingRecord.args`
      * `FunctionCallingRecord.as_dict()`
      * `FunctionCallingRecord.func_name`
      * `FunctionCallingRecord.model_computed_fields`
      * `FunctionCallingRecord.model_config`
      * `FunctionCallingRecord.model_fields`
      * `FunctionCallingRecord.result`
  * camel.agents.role_playing module
  * camel.agents.task_agent module
    * `TaskCreationAgent`
      * `TaskCreationAgent.task_creation_prompt`
      * `TaskCreationAgent.run()`
    * `TaskPlannerAgent`
      * `TaskPlannerAgent.task_planner_prompt`
      * `TaskPlannerAgent.run()`
    * `TaskPrioritizationAgent`
      * `TaskPrioritizationAgent.task_prioritization_prompt`
      * `TaskPrioritizationAgent.run()`
    * `TaskSpecifyAgent`
      * `TaskSpecifyAgent.DEFAULT_WORD_LIMIT`
      * `TaskSpecifyAgent.task_specify_prompt`
      * `TaskSpecifyAgent.DEFAULT_WORD_LIMIT`
      * `TaskSpecifyAgent.run()`
  * Module contents
    * `BaseAgent`
      * `BaseAgent.reset()`
      * `BaseAgent.step()`
    * `BaseToolAgent`
      * `BaseToolAgent.reset()`
      * `BaseToolAgent.step()`
    * `ChatAgent`
      * `ChatAgent.get_info()`
      * `ChatAgent.get_usage_dict()`
      * `ChatAgent.handle_batch_response()`
      * `ChatAgent.handle_stream_response()`
      * `ChatAgent.init_messages()`
      * `ChatAgent.is_tools_added()`
      * `ChatAgent.record_message()`
      * `ChatAgent.reset()`
      * `ChatAgent.set_output_language()`
      * `ChatAgent.step()`
      * `ChatAgent.step_async()`
      * `ChatAgent.step_tool_call()`
      * `ChatAgent.step_tool_call_async()`
      * `ChatAgent.system_message`
      * `ChatAgent.update_memory()`
    * `CriticAgent`
      * `CriticAgent.flatten_options()`
      * `CriticAgent.get_option()`
      * `CriticAgent.parse_critic()`
      * `CriticAgent.reduce_step()`
    * `EmbodiedAgent`
      * `EmbodiedAgent.get_tool_agent_names()`
      * `EmbodiedAgent.step()`
    * `HuggingFaceToolAgent`
      * `HuggingFaceToolAgent.chat()`
      * `HuggingFaceToolAgent.reset()`
      * `HuggingFaceToolAgent.step()`
    * `KnowledgeGraphAgent`
      * `KnowledgeGraphAgent.task_prompt`
      * `KnowledgeGraphAgent.run()`
    * `RoleAssignmentAgent`
      * `RoleAssignmentAgent.role_assignment_prompt`
      * `RoleAssignmentAgent.run()`
    * `SearchAgent`
      * `SearchAgent.continue_search()`
      * `SearchAgent.summarize_text()`
    * `TaskCreationAgent`
      * `TaskCreationAgent.task_creation_prompt`
      * `TaskCreationAgent.run()`
    * `TaskPlannerAgent`
      * `TaskPlannerAgent.task_planner_prompt`
      * `TaskPlannerAgent.run()`
    * `TaskPrioritizationAgent`
      * `TaskPrioritizationAgent.task_prioritization_prompt`
      * `TaskPrioritizationAgent.run()`
    * `TaskSpecifyAgent`
      * `TaskSpecifyAgent.DEFAULT_WORD_LIMIT`
      * `TaskSpecifyAgent.task_specify_prompt`
      * `TaskSpecifyAgent.DEFAULT_WORD_LIMIT`
      * `TaskSpecifyAgent.memory`
      * `TaskSpecifyAgent.model_backend`
      * `TaskSpecifyAgent.model_type`
      * `TaskSpecifyAgent.orig_sys_message`
      * `TaskSpecifyAgent.output_language`
      * `TaskSpecifyAgent.role_name`
      * `TaskSpecifyAgent.role_type`
      * `TaskSpecifyAgent.run()`
      * `TaskSpecifyAgent.task_specify_prompt`
      * `TaskSpecifyAgent.terminated`

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

