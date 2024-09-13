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

  * [ __ .rst ](_sources/camel.messages.rst "Download source file")
  * __ .pdf

__

# camel.messages package

##  Contents

  * Submodules
  * camel.messages.base module
    * `BaseMessage`
      * `BaseMessage.content`
      * `BaseMessage.create_new_instance()`
      * `BaseMessage.extract_text_and_code_prompts()`
      * `BaseMessage.image_detail`
      * `BaseMessage.image_list`
      * `BaseMessage.make_assistant_message()`
      * `BaseMessage.make_user_message()`
      * `BaseMessage.meta_dict`
      * `BaseMessage.role_name`
      * `BaseMessage.role_type`
      * `BaseMessage.to_dict()`
      * `BaseMessage.to_openai_assistant_message()`
      * `BaseMessage.to_openai_message()`
      * `BaseMessage.to_openai_system_message()`
      * `BaseMessage.to_openai_user_message()`
      * `BaseMessage.video_bytes`
      * `BaseMessage.video_detail`
  * camel.messages.chat_messages module
  * camel.messages.system_messages module
  * Module contents
    * `BaseMessage`
      * `BaseMessage.content`
      * `BaseMessage.create_new_instance()`
      * `BaseMessage.extract_text_and_code_prompts()`
      * `BaseMessage.image_detail`
      * `BaseMessage.image_list`
      * `BaseMessage.make_assistant_message()`
      * `BaseMessage.make_user_message()`
      * `BaseMessage.meta_dict`
      * `BaseMessage.role_name`
      * `BaseMessage.role_type`
      * `BaseMessage.to_dict()`
      * `BaseMessage.to_openai_assistant_message()`
      * `BaseMessage.to_openai_message()`
      * `BaseMessage.to_openai_system_message()`
      * `BaseMessage.to_openai_user_message()`
      * `BaseMessage.video_bytes`
      * `BaseMessage.video_detail`
    * `FunctionCallingMessage`
      * `FunctionCallingMessage.args`
      * `FunctionCallingMessage.content`
      * `FunctionCallingMessage.func_name`
      * `FunctionCallingMessage.meta_dict`
      * `FunctionCallingMessage.result`
      * `FunctionCallingMessage.role_name`
      * `FunctionCallingMessage.role_type`
      * `FunctionCallingMessage.to_openai_assistant_message()`
      * `FunctionCallingMessage.to_openai_function_message()`
      * `FunctionCallingMessage.to_openai_message()`
    * `OpenAIAssistantMessage`
    * `OpenAISystemMessage`
    * `OpenAIUserMessage`

# camel.messages package#

## Submodules#

## camel.messages.base module#

_class _camel.messages.base.BaseMessage(_role_name : str_, _role_type : [RoleType](camel.html#camel.types.RoleType "camel.types.enums.RoleType")_, _meta_dict : Dict[str, str] | None_, _content : str_, _video_bytes : bytes | None = None_, _image_list : List[Image] | None = None_, _image_detail : Literal['auto', 'low', 'high'] = 'auto'_, _video_detail : Literal['auto', 'low', 'high'] = 'low'_)[[source]](_modules/camel/messages/base.html#BaseMessage)#
    

Bases: `object`

Base class for message objects used in CAMEL chat system.

Parameters:

    

  * **role_name** (_str_) – The name of the user or assistant role.

  * **role_type** ([_RoleType_](camel.html#camel.types.RoleType "camel.types.RoleType")) – The type of role, either `RoleType. ASSISTANT` or `RoleType.USER`.

  * **meta_dict** (_Optional_ _[__Dict_ _[__str_ _,__str_ _]__]_) – Additional metadata dictionary for the message.

  * **content** (_str_) – The content of the message.

  * **video_bytes** (_Optional_ _[__bytes_ _]_) – Optional bytes of a video associated with the message. Default is None.

  * **image_list** (_Optional_ _[__List_ _[__Image.Image_ _]__]_) – Optional list of PIL Image objects associated with the message. Default is None.

  * **image_detail** (_Literal_ _[__" auto"__,__" low"__,__" high"__]_) – Detail level of the images associated with the message. Default is “auto”.

  * **video_detail** (_Literal_ _[__" auto"__,__" low"__,__" high"__]_) – Detail level of the videos associated with the message. Default is “low”.

content _: str_#

    

create_new_instance(_content : str_) ->
BaseMessage[[source]](_modules/camel/messages/base.html#BaseMessage.create_new_instance)#

    

Create a new instance of the `BaseMessage` with updated content.

Parameters:

    

**content** (_str_) – The new content value.

Returns:

    

The new instance of `BaseMessage`.

Return type:

    

BaseMessage

extract_text_and_code_prompts() ->
Tuple[List[[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")],
List[[CodePrompt](camel.prompts.html#camel.prompts.base.CodePrompt
"camel.prompts.base.CodePrompt")]][[source]](_modules/camel/messages/base.html#BaseMessage.extract_text_and_code_prompts)#

    

Extract text and code prompts from the message content.

Returns:

    

A tuple containing a

    

list of text prompts and a list of code prompts extracted from the content.

Return type:

    

Tuple[List[[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")],
List[[CodePrompt](camel.prompts.html#camel.prompts.base.CodePrompt
"camel.prompts.base.CodePrompt")]]

image_detail _: Literal['auto', 'low', 'high']__ = 'auto'_#

    

image_list _: List[Image] | None_ _ = None_#
    

_classmethod _make_assistant_message(_role_name : str_, _content : str_, _meta_dict : Dict[str, str] | None = None_, _video_bytes : bytes | None = None_, _image_list : List[Image] | None = None_, _image_detail : [OpenAIVisionDetailType](camel.html#camel.types.OpenAIVisionDetailType "camel.types.enums.OpenAIVisionDetailType") | str = OpenAIVisionDetailType.AUTO_, _video_detail : [OpenAIVisionDetailType](camel.html#camel.types.OpenAIVisionDetailType "camel.types.enums.OpenAIVisionDetailType") | str = OpenAIVisionDetailType.LOW_) -> BaseMessage[[source]](_modules/camel/messages/base.html#BaseMessage.make_assistant_message)#
    

_classmethod _make_user_message(_role_name : str_, _content : str_, _meta_dict : Dict[str, str] | None = None_, _video_bytes : bytes | None = None_, _image_list : List[Image] | None = None_, _image_detail : [OpenAIVisionDetailType](camel.html#camel.types.OpenAIVisionDetailType "camel.types.enums.OpenAIVisionDetailType") | str = OpenAIVisionDetailType.AUTO_, _video_detail : [OpenAIVisionDetailType](camel.html#camel.types.OpenAIVisionDetailType "camel.types.enums.OpenAIVisionDetailType") | str = OpenAIVisionDetailType.LOW_) -> BaseMessage[[source]](_modules/camel/messages/base.html#BaseMessage.make_user_message)#
    

meta_dict _: Dict[str, str] | None_#
    

role_name _: str_#

    

role_type _: [RoleType](camel.html#camel.types.RoleType
"camel.types.enums.RoleType")_#

    

to_dict() ->
Dict[[source]](_modules/camel/messages/base.html#BaseMessage.to_dict)#

    

Converts the message to a dictionary.

Returns:

    

The converted dictionary.

Return type:

    

dict

to_openai_assistant_message() ->
[ChatCompletionAssistantMessageParam](camel.html#camel.types.ChatCompletionAssistantMessageParam
"openai.types.chat.chat_completion_assistant_message_param.ChatCompletionAssistantMessageParam")[[source]](_modules/camel/messages/base.html#BaseMessage.to_openai_assistant_message)#

    

Converts the message to an `OpenAIAssistantMessage` object.

Returns:

    

The converted `OpenAIAssistantMessage`

    

object.

Return type:

    

OpenAIAssistantMessage

to_openai_message(_role_at_backend : [OpenAIBackendRole](camel.html#camel.types.OpenAIBackendRole "camel.types.enums.OpenAIBackendRole")_) -> [ChatCompletionSystemMessageParam](camel.html#camel.types.ChatCompletionSystemMessageParam "openai.types.chat.chat_completion_system_message_param.ChatCompletionSystemMessageParam") | [ChatCompletionUserMessageParam](camel.html#camel.types.ChatCompletionUserMessageParam "openai.types.chat.chat_completion_user_message_param.ChatCompletionUserMessageParam") | [ChatCompletionAssistantMessageParam](camel.html#camel.types.ChatCompletionAssistantMessageParam "openai.types.chat.chat_completion_assistant_message_param.ChatCompletionAssistantMessageParam") | ChatCompletionToolMessageParam | [ChatCompletionFunctionMessageParam](camel.html#camel.types.ChatCompletionFunctionMessageParam "openai.types.chat.chat_completion_function_message_param.ChatCompletionFunctionMessageParam")[[source]](_modules/camel/messages/base.html#BaseMessage.to_openai_message)#
    

Converts the message to an `OpenAIMessage` object.

Parameters:

    

**role_at_backend**
([_OpenAIBackendRole_](camel.html#camel.types.OpenAIBackendRole
"camel.types.OpenAIBackendRole")) – The role of the message in OpenAI chat
system.

Returns:

    

The converted `OpenAIMessage` object.

Return type:

    

OpenAIMessage

to_openai_system_message() ->
[ChatCompletionSystemMessageParam](camel.html#camel.types.ChatCompletionSystemMessageParam
"openai.types.chat.chat_completion_system_message_param.ChatCompletionSystemMessageParam")[[source]](_modules/camel/messages/base.html#BaseMessage.to_openai_system_message)#

    

Converts the message to an `OpenAISystemMessage` object.

Returns:

    

The converted `OpenAISystemMessage`

    

object.

Return type:

    

OpenAISystemMessage

to_openai_user_message() ->
[ChatCompletionUserMessageParam](camel.html#camel.types.ChatCompletionUserMessageParam
"openai.types.chat.chat_completion_user_message_param.ChatCompletionUserMessageParam")[[source]](_modules/camel/messages/base.html#BaseMessage.to_openai_user_message)#

    

Converts the message to an `OpenAIUserMessage` object.

Returns:

    

The converted `OpenAIUserMessage` object.

Return type:

    

OpenAIUserMessage

video_bytes _: bytes | None_ _ = None_#
    

video_detail _: Literal['auto', 'low', 'high']__ = 'low'_#

    

## camel.messages.chat_messages module#

## camel.messages.system_messages module#

## Module contents#

_class _camel.messages.BaseMessage(_role_name : str_, _role_type : [RoleType](camel.html#camel.types.RoleType "camel.types.enums.RoleType")_, _meta_dict : Dict[str, str] | None_, _content : str_, _video_bytes : bytes | None = None_, _image_list : List[Image] | None = None_, _image_detail : Literal['auto', 'low', 'high'] = 'auto'_, _video_detail : Literal['auto', 'low', 'high'] = 'low'_)[[source]](_modules/camel/messages/base.html#BaseMessage)#
    

Bases: `object`

Base class for message objects used in CAMEL chat system.

Parameters:

    

  * **role_name** (_str_) – The name of the user or assistant role.

  * **role_type** ([_RoleType_](camel.html#camel.types.RoleType "camel.types.RoleType")) – The type of role, either `RoleType. ASSISTANT` or `RoleType.USER`.

  * **meta_dict** (_Optional_ _[__Dict_ _[__str_ _,__str_ _]__]_) – Additional metadata dictionary for the message.

  * **content** (_str_) – The content of the message.

  * **video_bytes** (_Optional_ _[__bytes_ _]_) – Optional bytes of a video associated with the message. Default is None.

  * **image_list** (_Optional_ _[__List_ _[__Image.Image_ _]__]_) – Optional list of PIL Image objects associated with the message. Default is None.

  * **image_detail** (_Literal_ _[__" auto"__,__" low"__,__" high"__]_) – Detail level of the images associated with the message. Default is “auto”.

  * **video_detail** (_Literal_ _[__" auto"__,__" low"__,__" high"__]_) – Detail level of the videos associated with the message. Default is “low”.

content _: str_#

    

create_new_instance(_content : str_) ->
BaseMessage[[source]](_modules/camel/messages/base.html#BaseMessage.create_new_instance)#

    

Create a new instance of the `BaseMessage` with updated content.

Parameters:

    

**content** (_str_) – The new content value.

Returns:

    

The new instance of `BaseMessage`.

Return type:

    

BaseMessage

extract_text_and_code_prompts() ->
Tuple[List[[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")],
List[[CodePrompt](camel.prompts.html#camel.prompts.base.CodePrompt
"camel.prompts.base.CodePrompt")]][[source]](_modules/camel/messages/base.html#BaseMessage.extract_text_and_code_prompts)#

    

Extract text and code prompts from the message content.

Returns:

    

A tuple containing a

    

list of text prompts and a list of code prompts extracted from the content.

Return type:

    

Tuple[List[[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt")],
List[[CodePrompt](camel.prompts.html#camel.prompts.base.CodePrompt
"camel.prompts.base.CodePrompt")]]

image_detail _: Literal['auto', 'low', 'high']__ = 'auto'_#

    

image_list _: List[Image] | None_ _ = None_#
    

_classmethod _make_assistant_message(_role_name : str_, _content : str_, _meta_dict : Dict[str, str] | None = None_, _video_bytes : bytes | None = None_, _image_list : List[Image] | None = None_, _image_detail : [OpenAIVisionDetailType](camel.html#camel.types.OpenAIVisionDetailType "camel.types.enums.OpenAIVisionDetailType") | str = OpenAIVisionDetailType.AUTO_, _video_detail : [OpenAIVisionDetailType](camel.html#camel.types.OpenAIVisionDetailType "camel.types.enums.OpenAIVisionDetailType") | str = OpenAIVisionDetailType.LOW_) -> BaseMessage[[source]](_modules/camel/messages/base.html#BaseMessage.make_assistant_message)#
    

_classmethod _make_user_message(_role_name : str_, _content : str_, _meta_dict : Dict[str, str] | None = None_, _video_bytes : bytes | None = None_, _image_list : List[Image] | None = None_, _image_detail : [OpenAIVisionDetailType](camel.html#camel.types.OpenAIVisionDetailType "camel.types.enums.OpenAIVisionDetailType") | str = OpenAIVisionDetailType.AUTO_, _video_detail : [OpenAIVisionDetailType](camel.html#camel.types.OpenAIVisionDetailType "camel.types.enums.OpenAIVisionDetailType") | str = OpenAIVisionDetailType.LOW_) -> BaseMessage[[source]](_modules/camel/messages/base.html#BaseMessage.make_user_message)#
    

meta_dict _: Dict[str, str] | None_#
    

role_name _: str_#

    

role_type _: [RoleType](camel.html#camel.types.RoleType
"camel.types.enums.RoleType")_#

    

to_dict() ->
Dict[[source]](_modules/camel/messages/base.html#BaseMessage.to_dict)#

    

Converts the message to a dictionary.

Returns:

    

The converted dictionary.

Return type:

    

dict

to_openai_assistant_message() ->
[ChatCompletionAssistantMessageParam](camel.html#camel.types.ChatCompletionAssistantMessageParam
"openai.types.chat.chat_completion_assistant_message_param.ChatCompletionAssistantMessageParam")[[source]](_modules/camel/messages/base.html#BaseMessage.to_openai_assistant_message)#

    

Converts the message to an `OpenAIAssistantMessage` object.

Returns:

    

The converted `OpenAIAssistantMessage`

    

object.

Return type:

    

OpenAIAssistantMessage

to_openai_message(_role_at_backend : [OpenAIBackendRole](camel.html#camel.types.OpenAIBackendRole "camel.types.enums.OpenAIBackendRole")_) -> [ChatCompletionSystemMessageParam](camel.html#camel.types.ChatCompletionSystemMessageParam "openai.types.chat.chat_completion_system_message_param.ChatCompletionSystemMessageParam") | [ChatCompletionUserMessageParam](camel.html#camel.types.ChatCompletionUserMessageParam "openai.types.chat.chat_completion_user_message_param.ChatCompletionUserMessageParam") | [ChatCompletionAssistantMessageParam](camel.html#camel.types.ChatCompletionAssistantMessageParam "openai.types.chat.chat_completion_assistant_message_param.ChatCompletionAssistantMessageParam") | ChatCompletionToolMessageParam | [ChatCompletionFunctionMessageParam](camel.html#camel.types.ChatCompletionFunctionMessageParam "openai.types.chat.chat_completion_function_message_param.ChatCompletionFunctionMessageParam")[[source]](_modules/camel/messages/base.html#BaseMessage.to_openai_message)#
    

Converts the message to an `OpenAIMessage` object.

Parameters:

    

**role_at_backend**
([_OpenAIBackendRole_](camel.html#camel.types.OpenAIBackendRole
"camel.types.OpenAIBackendRole")) – The role of the message in OpenAI chat
system.

Returns:

    

The converted `OpenAIMessage` object.

Return type:

    

OpenAIMessage

to_openai_system_message() ->
[ChatCompletionSystemMessageParam](camel.html#camel.types.ChatCompletionSystemMessageParam
"openai.types.chat.chat_completion_system_message_param.ChatCompletionSystemMessageParam")[[source]](_modules/camel/messages/base.html#BaseMessage.to_openai_system_message)#

    

Converts the message to an `OpenAISystemMessage` object.

Returns:

    

The converted `OpenAISystemMessage`

    

object.

Return type:

    

OpenAISystemMessage

to_openai_user_message() ->
[ChatCompletionUserMessageParam](camel.html#camel.types.ChatCompletionUserMessageParam
"openai.types.chat.chat_completion_user_message_param.ChatCompletionUserMessageParam")[[source]](_modules/camel/messages/base.html#BaseMessage.to_openai_user_message)#

    

Converts the message to an `OpenAIUserMessage` object.

Returns:

    

The converted `OpenAIUserMessage` object.

Return type:

    

OpenAIUserMessage

video_bytes _: bytes | None_ _ = None_#
    

video_detail _: Literal['auto', 'low', 'high']__ = 'low'_#

    

_class _camel.messages.FunctionCallingMessage(_role_name : str_, _role_type : [RoleType](camel.html#camel.types.RoleType "camel.types.enums.RoleType")_, _meta_dict : Dict[str, str] | None_, _content : str_, _video_bytes : bytes | None = None_, _image_list : List[Image] | None = None_, _image_detail : Literal['auto', 'low', 'high'] = 'auto'_, _video_detail : Literal['auto', 'low', 'high'] = 'low'_, _func_name : str | None = None_, _args : Dict | None = None_, _result : Any | None = None_)[[source]](_modules/camel/messages/func_message.html#FunctionCallingMessage)#
    

Bases: `BaseMessage`

Class for message objects used specifically for function-related messages.

Parameters:

    

  * **func_name** (_Optional_ _[__str_ _]_) – The name of the function used. (default: `None`)

  * **args** (_Optional_ _[__Dict_ _]_) – The dictionary of arguments passed to the function. (default: `None`)

  * **result** (_Optional_ _[__Any_ _]_) – The result of function execution. (default: `None`)

args _: Dict | None_ _ = None_#
    

content _: str_#

    

func_name _: str | None_ _ = None_#
    

meta_dict _: Dict[str, str] | None_#
    

result _: Any | None_ _ = None_#
    

role_name _: str_#

    

role_type _: [RoleType](camel.html#camel.types.RoleType
"camel.types.RoleType")_#

    

to_openai_assistant_message() ->
[ChatCompletionAssistantMessageParam](camel.html#camel.types.ChatCompletionAssistantMessageParam
"openai.types.chat.chat_completion_assistant_message_param.ChatCompletionAssistantMessageParam")[[source]](_modules/camel/messages/func_message.html#FunctionCallingMessage.to_openai_assistant_message)#

    

Converts the message to an `OpenAIAssistantMessage` object.

Returns:

    

The converted `OpenAIAssistantMessage`

    

object.

Return type:

    

OpenAIAssistantMessage

to_openai_function_message() ->
[ChatCompletionFunctionMessageParam](camel.html#camel.types.ChatCompletionFunctionMessageParam
"openai.types.chat.chat_completion_function_message_param.ChatCompletionFunctionMessageParam")[[source]](_modules/camel/messages/func_message.html#FunctionCallingMessage.to_openai_function_message)#

    

Converts the message to an `OpenAIMessage` object with the role being
“function”.

Returns:

    

The converted `OpenAIMessage` object

    

with its role being “function”.

Return type:

    

OpenAIMessage

to_openai_message(_role_at_backend : [OpenAIBackendRole](camel.html#camel.types.OpenAIBackendRole "camel.types.enums.OpenAIBackendRole")_) -> [ChatCompletionSystemMessageParam](camel.html#camel.types.ChatCompletionSystemMessageParam "openai.types.chat.chat_completion_system_message_param.ChatCompletionSystemMessageParam") | [ChatCompletionUserMessageParam](camel.html#camel.types.ChatCompletionUserMessageParam "openai.types.chat.chat_completion_user_message_param.ChatCompletionUserMessageParam") | [ChatCompletionAssistantMessageParam](camel.html#camel.types.ChatCompletionAssistantMessageParam "openai.types.chat.chat_completion_assistant_message_param.ChatCompletionAssistantMessageParam") | ChatCompletionToolMessageParam | [ChatCompletionFunctionMessageParam](camel.html#camel.types.ChatCompletionFunctionMessageParam "openai.types.chat.chat_completion_function_message_param.ChatCompletionFunctionMessageParam")[[source]](_modules/camel/messages/func_message.html#FunctionCallingMessage.to_openai_message)#
    

Converts the message to an `OpenAIMessage` object.

Parameters:

    

**role_at_backend**
([_OpenAIBackendRole_](camel.html#camel.types.OpenAIBackendRole
"camel.types.OpenAIBackendRole")) – The role of the message in OpenAI chat
system.

Returns:

    

The converted `OpenAIMessage` object.

Return type:

    

OpenAIMessage

camel.messages.OpenAIAssistantMessage#

    

alias of
[`ChatCompletionAssistantMessageParam`](camel.html#camel.types.ChatCompletionAssistantMessageParam
"openai.types.chat.chat_completion_assistant_message_param.ChatCompletionAssistantMessageParam")

camel.messages.OpenAISystemMessage#

    

alias of
[`ChatCompletionSystemMessageParam`](camel.html#camel.types.ChatCompletionSystemMessageParam
"openai.types.chat.chat_completion_system_message_param.ChatCompletionSystemMessageParam")

camel.messages.OpenAIUserMessage#

    

alias of
[`ChatCompletionUserMessageParam`](camel.html#camel.types.ChatCompletionUserMessageParam
"openai.types.chat.chat_completion_user_message_param.ChatCompletionUserMessageParam")

__Contents

  * Submodules
  * camel.messages.base module
    * `BaseMessage`
      * `BaseMessage.content`
      * `BaseMessage.create_new_instance()`
      * `BaseMessage.extract_text_and_code_prompts()`
      * `BaseMessage.image_detail`
      * `BaseMessage.image_list`
      * `BaseMessage.make_assistant_message()`
      * `BaseMessage.make_user_message()`
      * `BaseMessage.meta_dict`
      * `BaseMessage.role_name`
      * `BaseMessage.role_type`
      * `BaseMessage.to_dict()`
      * `BaseMessage.to_openai_assistant_message()`
      * `BaseMessage.to_openai_message()`
      * `BaseMessage.to_openai_system_message()`
      * `BaseMessage.to_openai_user_message()`
      * `BaseMessage.video_bytes`
      * `BaseMessage.video_detail`
  * camel.messages.chat_messages module
  * camel.messages.system_messages module
  * Module contents
    * `BaseMessage`
      * `BaseMessage.content`
      * `BaseMessage.create_new_instance()`
      * `BaseMessage.extract_text_and_code_prompts()`
      * `BaseMessage.image_detail`
      * `BaseMessage.image_list`
      * `BaseMessage.make_assistant_message()`
      * `BaseMessage.make_user_message()`
      * `BaseMessage.meta_dict`
      * `BaseMessage.role_name`
      * `BaseMessage.role_type`
      * `BaseMessage.to_dict()`
      * `BaseMessage.to_openai_assistant_message()`
      * `BaseMessage.to_openai_message()`
      * `BaseMessage.to_openai_system_message()`
      * `BaseMessage.to_openai_user_message()`
      * `BaseMessage.video_bytes`
      * `BaseMessage.video_detail`
    * `FunctionCallingMessage`
      * `FunctionCallingMessage.args`
      * `FunctionCallingMessage.content`
      * `FunctionCallingMessage.func_name`
      * `FunctionCallingMessage.meta_dict`
      * `FunctionCallingMessage.result`
      * `FunctionCallingMessage.role_name`
      * `FunctionCallingMessage.role_type`
      * `FunctionCallingMessage.to_openai_assistant_message()`
      * `FunctionCallingMessage.to_openai_function_message()`
      * `FunctionCallingMessage.to_openai_message()`
    * `OpenAIAssistantMessage`
    * `OpenAISystemMessage`
    * `OpenAIUserMessage`

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

