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
    * Camel Package __
      * [camel.agents package](camel.agents.html)
      * [camel.prompts package](camel.prompts.html)

__

  * [ __ .rst ](_sources/camel.rst "Download source file")
  * __ .pdf

__

# Camel Package

##  Contents

  * Subpackages
  * Submodules
  * camel.configs module
    * `AnthropicConfig`
      * `AnthropicConfig.max_tokens`
      * `AnthropicConfig.metadata`
      * `AnthropicConfig.model_computed_fields`
      * `AnthropicConfig.model_config`
      * `AnthropicConfig.model_fields`
      * `AnthropicConfig.stop_sequences`
      * `AnthropicConfig.stream`
      * `AnthropicConfig.temperature`
      * `AnthropicConfig.top_k`
      * `AnthropicConfig.top_p`
    * `BaseConfig`
      * `BaseConfig.as_dict()`
      * `BaseConfig.fields_type_checking()`
      * `BaseConfig.model_computed_fields`
      * `BaseConfig.model_config`
      * `BaseConfig.model_fields`
      * `BaseConfig.tools`
    * `ChatGPTConfig`
      * `ChatGPTConfig.frequency_penalty`
      * `ChatGPTConfig.logit_bias`
      * `ChatGPTConfig.max_tokens`
      * `ChatGPTConfig.model_computed_fields`
      * `ChatGPTConfig.model_config`
      * `ChatGPTConfig.model_fields`
      * `ChatGPTConfig.n`
      * `ChatGPTConfig.presence_penalty`
      * `ChatGPTConfig.response_format`
      * `ChatGPTConfig.stop`
      * `ChatGPTConfig.stream`
      * `ChatGPTConfig.temperature`
      * `ChatGPTConfig.tool_choice`
      * `ChatGPTConfig.top_p`
      * `ChatGPTConfig.user`
    * `GeminiConfig`
      * `GeminiConfig.candidate_count`
      * `GeminiConfig.fields_type_checking()`
      * `GeminiConfig.max_output_tokens`
      * `GeminiConfig.model_computed_fields`
      * `GeminiConfig.model_config`
      * `GeminiConfig.model_fields`
      * `GeminiConfig.request_options`
      * `GeminiConfig.response_mime_type`
      * `GeminiConfig.response_schema`
      * `GeminiConfig.safety_settings`
      * `GeminiConfig.stop_sequences`
      * `GeminiConfig.temperature`
      * `GeminiConfig.tool_config`
      * `GeminiConfig.top_k`
      * `GeminiConfig.top_p`
    * `GroqConfig`
      * `GroqConfig.frequency_penalty`
      * `GroqConfig.max_tokens`
      * `GroqConfig.model_computed_fields`
      * `GroqConfig.model_config`
      * `GroqConfig.model_fields`
      * `GroqConfig.n`
      * `GroqConfig.presence_penalty`
      * `GroqConfig.response_format`
      * `GroqConfig.stop`
      * `GroqConfig.stream`
      * `GroqConfig.temperature`
      * `GroqConfig.tool_choice`
      * `GroqConfig.top_p`
      * `GroqConfig.user`
    * `LiteLLMConfig`
      * `LiteLLMConfig.api_version`
      * `LiteLLMConfig.custom_llm_provider`
      * `LiteLLMConfig.deployment_id`
      * `LiteLLMConfig.extra_headers`
      * `LiteLLMConfig.frequency_penalty`
      * `LiteLLMConfig.logit_bias`
      * `LiteLLMConfig.logprobs`
      * `LiteLLMConfig.max_retries`
      * `LiteLLMConfig.max_tokens`
      * `LiteLLMConfig.mock_response`
      * `LiteLLMConfig.model_computed_fields`
      * `LiteLLMConfig.model_config`
      * `LiteLLMConfig.model_fields`
      * `LiteLLMConfig.n`
      * `LiteLLMConfig.presence_penalty`
      * `LiteLLMConfig.response_format`
      * `LiteLLMConfig.seed`
      * `LiteLLMConfig.stop`
      * `LiteLLMConfig.stream`
      * `LiteLLMConfig.stream_options`
      * `LiteLLMConfig.temperature`
      * `LiteLLMConfig.timeout`
      * `LiteLLMConfig.tool_choice`
      * `LiteLLMConfig.top_logprobs`
      * `LiteLLMConfig.top_p`
      * `LiteLLMConfig.user`
    * `MistralConfig`
      * `MistralConfig.fields_type_checking()`
      * `MistralConfig.max_tokens`
      * `MistralConfig.min_tokens`
      * `MistralConfig.model_computed_fields`
      * `MistralConfig.model_config`
      * `MistralConfig.model_fields`
      * `MistralConfig.random_seed`
      * `MistralConfig.response_format`
      * `MistralConfig.safe_prompt`
      * `MistralConfig.stop`
      * `MistralConfig.temperature`
      * `MistralConfig.tool_choice`
      * `MistralConfig.top_p`
    * `OllamaConfig`
      * `OllamaConfig.frequency_penalty`
      * `OllamaConfig.max_tokens`
      * `OllamaConfig.model_computed_fields`
      * `OllamaConfig.model_config`
      * `OllamaConfig.model_fields`
      * `OllamaConfig.presence_penalty`
      * `OllamaConfig.response_format`
      * `OllamaConfig.stop`
      * `OllamaConfig.stream`
      * `OllamaConfig.temperature`
      * `OllamaConfig.top_p`
    * `OpenSourceConfig`
      * `OpenSourceConfig.api_params`
      * `OpenSourceConfig.model_computed_fields`
      * `OpenSourceConfig.model_config`
      * `OpenSourceConfig.model_fields`
      * `OpenSourceConfig.model_path`
      * `OpenSourceConfig.server_url`
    * `RekaConfig`
      * `RekaConfig.as_dict()`
      * `RekaConfig.frequency_penalty`
      * `RekaConfig.max_tokens`
      * `RekaConfig.model_computed_fields`
      * `RekaConfig.model_config`
      * `RekaConfig.model_fields`
      * `RekaConfig.presence_penalty`
      * `RekaConfig.seed`
      * `RekaConfig.stop`
      * `RekaConfig.temperature`
      * `RekaConfig.top_k`
      * `RekaConfig.top_p`
      * `RekaConfig.use_search_engine`
    * `SambaCloudAPIConfig`
      * `SambaCloudAPIConfig.frequency_penalty`
      * `SambaCloudAPIConfig.logit_bias`
      * `SambaCloudAPIConfig.max_tokens`
      * `SambaCloudAPIConfig.model_computed_fields`
      * `SambaCloudAPIConfig.model_config`
      * `SambaCloudAPIConfig.model_fields`
      * `SambaCloudAPIConfig.n`
      * `SambaCloudAPIConfig.presence_penalty`
      * `SambaCloudAPIConfig.response_format`
      * `SambaCloudAPIConfig.stop`
      * `SambaCloudAPIConfig.stream`
      * `SambaCloudAPIConfig.temperature`
      * `SambaCloudAPIConfig.tool_choice`
      * `SambaCloudAPIConfig.top_p`
      * `SambaCloudAPIConfig.user`
    * `SambaFastAPIConfig`
      * `SambaFastAPIConfig.as_dict()`
      * `SambaFastAPIConfig.max_tokens`
      * `SambaFastAPIConfig.model_computed_fields`
      * `SambaFastAPIConfig.model_config`
      * `SambaFastAPIConfig.model_fields`
      * `SambaFastAPIConfig.stop`
      * `SambaFastAPIConfig.stream`
      * `SambaFastAPIConfig.stream_options`
    * `SambaVerseAPIConfig`
      * `SambaVerseAPIConfig.as_dict()`
      * `SambaVerseAPIConfig.max_tokens`
      * `SambaVerseAPIConfig.model_computed_fields`
      * `SambaVerseAPIConfig.model_config`
      * `SambaVerseAPIConfig.model_fields`
      * `SambaVerseAPIConfig.repetition_penalty`
      * `SambaVerseAPIConfig.stop`
      * `SambaVerseAPIConfig.stream`
      * `SambaVerseAPIConfig.temperature`
      * `SambaVerseAPIConfig.top_k`
      * `SambaVerseAPIConfig.top_p`
    * `TogetherAIConfig`
      * `TogetherAIConfig.as_dict()`
      * `TogetherAIConfig.frequency_penalty`
      * `TogetherAIConfig.logit_bias`
      * `TogetherAIConfig.max_tokens`
      * `TogetherAIConfig.model_computed_fields`
      * `TogetherAIConfig.model_config`
      * `TogetherAIConfig.model_fields`
      * `TogetherAIConfig.n`
      * `TogetherAIConfig.presence_penalty`
      * `TogetherAIConfig.response_format`
      * `TogetherAIConfig.stop`
      * `TogetherAIConfig.stream`
      * `TogetherAIConfig.temperature`
      * `TogetherAIConfig.top_p`
      * `TogetherAIConfig.user`
    * `VLLMConfig`
      * `VLLMConfig.frequency_penalty`
      * `VLLMConfig.logit_bias`
      * `VLLMConfig.max_tokens`
      * `VLLMConfig.model_computed_fields`
      * `VLLMConfig.model_config`
      * `VLLMConfig.model_fields`
      * `VLLMConfig.n`
      * `VLLMConfig.presence_penalty`
      * `VLLMConfig.response_format`
      * `VLLMConfig.stop`
      * `VLLMConfig.stream`
      * `VLLMConfig.temperature`
      * `VLLMConfig.top_p`
      * `VLLMConfig.user`
    * `ZhipuAIConfig`
      * `ZhipuAIConfig.max_tokens`
      * `ZhipuAIConfig.model_computed_fields`
      * `ZhipuAIConfig.model_config`
      * `ZhipuAIConfig.model_fields`
      * `ZhipuAIConfig.stop`
      * `ZhipuAIConfig.stream`
      * `ZhipuAIConfig.temperature`
      * `ZhipuAIConfig.tool_choice`
      * `ZhipuAIConfig.top_p`
  * camel.generators module
    * `AISocietyTaskPromptGenerator`
      * `AISocietyTaskPromptGenerator.from_role_files()`
      * `AISocietyTaskPromptGenerator.from_role_generator()`
    * `CodeTaskPromptGenerator`
      * `CodeTaskPromptGenerator.from_role_files()`
      * `CodeTaskPromptGenerator.from_role_generator()`
    * `RoleNameGenerator`
      * `RoleNameGenerator.from_role_files()`
    * `SingleTxtGenerator`
      * `SingleTxtGenerator.from_role_files()`
    * `SystemMessageGenerator`
      * `SystemMessageGenerator.from_dict()`
      * `SystemMessageGenerator.from_dicts()`
      * `SystemMessageGenerator.validate_meta_dict_keys()`
  * camel.human module
    * `Human`
      * `Human.name`
      * `Human.logger_color`
      * `Human.input_button`
      * `Human.kill_button`
      * `Human.options_dict`
      * `Human.display_options()`
      * `Human.get_input()`
      * `Human.parse_input()`
      * `Human.reduce_step()`
  * camel.messages module
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
      * `FunctionCallingMessage.func_name`
      * `FunctionCallingMessage.result`
      * `FunctionCallingMessage.to_openai_assistant_message()`
      * `FunctionCallingMessage.to_openai_function_message()`
      * `FunctionCallingMessage.to_openai_message()`
    * `OpenAIAssistantMessage`
    * `OpenAISystemMessage`
    * `OpenAIUserMessage`
  * camel.types module
    * `AudioModelType`
      * `AudioModelType.TTS_1`
      * `AudioModelType.TTS_1_HD`
      * `AudioModelType.is_openai`
    * `ChatCompletion`
      * `ChatCompletion.choices`
      * `ChatCompletion.created`
      * `ChatCompletion.id`
      * `ChatCompletion.model`
      * `ChatCompletion.model_computed_fields`
      * `ChatCompletion.model_config`
      * `ChatCompletion.model_fields`
      * `ChatCompletion.object`
      * `ChatCompletion.service_tier`
      * `ChatCompletion.system_fingerprint`
      * `ChatCompletion.usage`
    * `ChatCompletionAssistantMessageParam`
      * `ChatCompletionAssistantMessageParam.content`
      * `ChatCompletionAssistantMessageParam.function_call`
      * `ChatCompletionAssistantMessageParam.name`
      * `ChatCompletionAssistantMessageParam.refusal`
      * `ChatCompletionAssistantMessageParam.role`
      * `ChatCompletionAssistantMessageParam.tool_calls`
    * `ChatCompletionChunk`
      * `ChatCompletionChunk.choices`
      * `ChatCompletionChunk.created`
      * `ChatCompletionChunk.id`
      * `ChatCompletionChunk.model`
      * `ChatCompletionChunk.model_computed_fields`
      * `ChatCompletionChunk.model_config`
      * `ChatCompletionChunk.model_fields`
      * `ChatCompletionChunk.object`
      * `ChatCompletionChunk.service_tier`
      * `ChatCompletionChunk.system_fingerprint`
      * `ChatCompletionChunk.usage`
    * `ChatCompletionFunctionMessageParam`
      * `ChatCompletionFunctionMessageParam.content`
      * `ChatCompletionFunctionMessageParam.name`
      * `ChatCompletionFunctionMessageParam.role`
    * `ChatCompletionMessage`
      * `ChatCompletionMessage.content`
      * `ChatCompletionMessage.function_call`
      * `ChatCompletionMessage.model_computed_fields`
      * `ChatCompletionMessage.model_config`
      * `ChatCompletionMessage.model_fields`
      * `ChatCompletionMessage.refusal`
      * `ChatCompletionMessage.role`
      * `ChatCompletionMessage.tool_calls`
    * `ChatCompletionSystemMessageParam`
      * `ChatCompletionSystemMessageParam.content`
      * `ChatCompletionSystemMessageParam.name`
      * `ChatCompletionSystemMessageParam.role`
    * `ChatCompletionUserMessageParam`
      * `ChatCompletionUserMessageParam.content`
      * `ChatCompletionUserMessageParam.name`
      * `ChatCompletionUserMessageParam.role`
    * `Choice`
      * `Choice.finish_reason`
      * `Choice.index`
      * `Choice.logprobs`
      * `Choice.message`
      * `Choice.model_computed_fields`
      * `Choice.model_config`
      * `Choice.model_fields`
    * `CompletionUsage`
      * `CompletionUsage.completion_tokens`
      * `CompletionUsage.completion_tokens_details`
      * `CompletionUsage.model_computed_fields`
      * `CompletionUsage.model_config`
      * `CompletionUsage.model_fields`
      * `CompletionUsage.prompt_tokens`
      * `CompletionUsage.total_tokens`
    * `EmbeddingModelType`
      * `EmbeddingModelType.MISTRAL_EMBED`
      * `EmbeddingModelType.TEXT_EMBEDDING_3_LARGE`
      * `EmbeddingModelType.TEXT_EMBEDDING_3_SMALL`
      * `EmbeddingModelType.TEXT_EMBEDDING_ADA_2`
      * `EmbeddingModelType.is_mistral`
      * `EmbeddingModelType.is_openai`
      * `EmbeddingModelType.output_dim`
    * `ModelPlatformType`
      * `ModelPlatformType.ANTHROPIC`
      * `ModelPlatformType.AZURE`
      * `ModelPlatformType.DEFAULT`
      * `ModelPlatformType.GEMINI`
      * `ModelPlatformType.GROQ`
      * `ModelPlatformType.LITELLM`
      * `ModelPlatformType.MISTRAL`
      * `ModelPlatformType.OLLAMA`
      * `ModelPlatformType.OPENAI`
      * `ModelPlatformType.OPENAI_COMPATIBILITY_MODEL`
      * `ModelPlatformType.OPEN_SOURCE`
      * `ModelPlatformType.REKA`
      * `ModelPlatformType.SAMBA`
      * `ModelPlatformType.TOGETHER`
      * `ModelPlatformType.VLLM`
      * `ModelPlatformType.ZHIPU`
      * `ModelPlatformType.is_anthropic`
      * `ModelPlatformType.is_azure`
      * `ModelPlatformType.is_gemini`
      * `ModelPlatformType.is_groq`
      * `ModelPlatformType.is_litellm`
      * `ModelPlatformType.is_mistral`
      * `ModelPlatformType.is_ollama`
      * `ModelPlatformType.is_open_source`
      * `ModelPlatformType.is_openai`
      * `ModelPlatformType.is_openai_compatibility_model`
      * `ModelPlatformType.is_reka`
      * `ModelPlatformType.is_samba`
      * `ModelPlatformType.is_together`
      * `ModelPlatformType.is_vllm`
      * `ModelPlatformType.is_zhipuai`
    * `ModelType`
      * `ModelType.CLAUDE_2_0`
      * `ModelType.CLAUDE_2_1`
      * `ModelType.CLAUDE_3_5_SONNET`
      * `ModelType.CLAUDE_3_HAIKU`
      * `ModelType.CLAUDE_3_OPUS`
      * `ModelType.CLAUDE_3_SONNET`
      * `ModelType.CLAUDE_INSTANT_1_2`
      * `ModelType.GEMINI_1_5_FLASH`
      * `ModelType.GEMINI_1_5_PRO`
      * `ModelType.GLM_3_TURBO`
      * `ModelType.GLM_4`
      * `ModelType.GLM_4V`
      * `ModelType.GLM_4_OPEN_SOURCE`
      * `ModelType.GPT_3_5_TURBO`
      * `ModelType.GPT_4`
      * `ModelType.GPT_4O`
      * `ModelType.GPT_4O_MINI`
      * `ModelType.GPT_4_TURBO`
      * `ModelType.GROQ_GEMMA_2_9B_IT`
      * `ModelType.GROQ_GEMMA_7B_IT`
      * `ModelType.GROQ_LLAMA_3_1_405B`
      * `ModelType.GROQ_LLAMA_3_1_70B`
      * `ModelType.GROQ_LLAMA_3_1_8B`
      * `ModelType.GROQ_LLAMA_3_70B`
      * `ModelType.GROQ_LLAMA_3_8B`
      * `ModelType.GROQ_MIXTRAL_8_7B`
      * `ModelType.LLAMA_2`
      * `ModelType.LLAMA_3`
      * `ModelType.MISTRAL_7B`
      * `ModelType.MISTRAL_CODESTRAL`
      * `ModelType.MISTRAL_CODESTRAL_MAMBA`
      * `ModelType.MISTRAL_LARGE`
      * `ModelType.MISTRAL_MIXTRAL_8x22B`
      * `ModelType.MISTRAL_MIXTRAL_8x7B`
      * `ModelType.MISTRAL_NEMO`
      * `ModelType.NEMOTRON_4_REWARD`
      * `ModelType.O1_MINI`
      * `ModelType.O1_PREVIEW`
      * `ModelType.QWEN_2`
      * `ModelType.REKA_CORE`
      * `ModelType.REKA_EDGE`
      * `ModelType.REKA_FLASH`
      * `ModelType.STUB`
      * `ModelType.VICUNA`
      * `ModelType.VICUNA_16K`
      * `ModelType.is_anthropic`
      * `ModelType.is_azure_openai`
      * `ModelType.is_gemini`
      * `ModelType.is_groq`
      * `ModelType.is_mistral`
      * `ModelType.is_nvidia`
      * `ModelType.is_open_source`
      * `ModelType.is_openai`
      * `ModelType.is_reka`
      * `ModelType.is_zhipuai`
      * `ModelType.supports_tool_calling`
      * `ModelType.token_limit`
      * `ModelType.validate_model_name()`
      * `ModelType.value_for_tiktoken`
    * `OpenAIBackendRole`
      * `OpenAIBackendRole.ASSISTANT`
      * `OpenAIBackendRole.FUNCTION`
      * `OpenAIBackendRole.SYSTEM`
      * `OpenAIBackendRole.TOOL`
      * `OpenAIBackendRole.USER`
    * `OpenAIImageType`
      * `OpenAIImageType.GIF`
      * `OpenAIImageType.JPEG`
      * `OpenAIImageType.JPG`
      * `OpenAIImageType.PNG`
      * `OpenAIImageType.WEBP`
    * `OpenAIVisionDetailType`
      * `OpenAIVisionDetailType.AUTO`
      * `OpenAIVisionDetailType.HIGH`
      * `OpenAIVisionDetailType.LOW`
    * `OpenAPIName`
      * `OpenAPIName.BIZTOC`
      * `OpenAPIName.COURSERA`
      * `OpenAPIName.CREATE_QR_CODE`
      * `OpenAPIName.KLARNA`
      * `OpenAPIName.NASA_APOD`
      * `OpenAPIName.OUTSCHOOL`
      * `OpenAPIName.SPEAK`
      * `OpenAPIName.WEB_SCRAPER`
    * `RoleType`
      * `RoleType.ASSISTANT`
      * `RoleType.CRITIC`
      * `RoleType.DEFAULT`
      * `RoleType.EMBODIMENT`
      * `RoleType.USER`
    * `StorageType`
      * `StorageType.MILVUS`
      * `StorageType.QDRANT`
    * `TaskType`
      * `TaskType.AI_SOCIETY`
      * `TaskType.CODE`
      * `TaskType.DEFAULT`
      * `TaskType.EVALUATION`
      * `TaskType.GENERATE_TEXT_EMBEDDING_DATA`
      * `TaskType.IMAGE_CRAFT`
      * `TaskType.MISALIGNMENT`
      * `TaskType.MULTI_CONDITION_IMAGE_CRAFT`
      * `TaskType.OBJECT_RECOGNITION`
      * `TaskType.ROLE_DESCRIPTION`
      * `TaskType.SOLUTION_EXTRACTION`
      * `TaskType.TRANSLATION`
      * `TaskType.VIDEO_DESCRIPTION`
    * `TerminationMode`
      * `TerminationMode.ALL`
      * `TerminationMode.ANY`
    * `VectorDistance`
      * `VectorDistance.COSINE`
      * `VectorDistance.DOT`
      * `VectorDistance.EUCLIDEAN`
    * `VoiceType`
      * `VoiceType.ALLOY`
      * `VoiceType.ECHO`
      * `VoiceType.FABLE`
      * `VoiceType.NOVA`
      * `VoiceType.ONYX`
      * `VoiceType.SHIMMER`
      * `VoiceType.is_openai`
  * camel.utils module
    * `AgentOpsMeta`
    * `AnthropicTokenCounter`
      * `AnthropicTokenCounter.count_tokens_from_messages()`
    * `BaseTokenCounter`
      * `BaseTokenCounter.count_tokens_from_messages()`
    * `Constants`
      * `Constants.DEFAULT_SIMILARITY_THRESHOLD`
      * `Constants.DEFAULT_TOP_K_RESULTS`
      * `Constants.FUNC_NAME_FOR_STRUCTURED_OUTPUT`
      * `Constants.VIDEO_DEFAULT_IMAGE_SIZE`
      * `Constants.VIDEO_DEFAULT_PLUG_PYAV`
      * `Constants.VIDEO_IMAGE_EXTRACTION_INTERVAL`
    * `GeminiTokenCounter`
      * `GeminiTokenCounter.count_tokens_from_messages()`
    * `LiteLLMTokenCounter`
      * `LiteLLMTokenCounter.calculate_cost_from_response()`
      * `LiteLLMTokenCounter.completion_cost`
      * `LiteLLMTokenCounter.count_tokens_from_messages()`
      * `LiteLLMTokenCounter.token_counter`
    * `MistralTokenCounter`
      * `MistralTokenCounter.count_tokens_from_messages()`
    * `OpenAITokenCounter`
      * `OpenAITokenCounter.count_tokens_from_messages()`
    * `OpenSourceTokenCounter`
      * `OpenSourceTokenCounter.count_tokens_from_messages()`
    * `agentops_decorator()`
    * `api_keys_required()`
    * `check_server_running()`
    * `create_chunks()`
    * `dependencies_required()`
    * `download_tasks()`
    * `func_string_to_callable()`
    * `get_first_int()`
    * `get_model_encoding()`
    * `get_prompt_template_key_words()`
    * `get_pydantic_major_version()`
    * `get_pydantic_object_schema()`
    * `get_system_information()`
    * `get_task_list()`
    * `handle_http_error()`
    * `is_docker_running()`
    * `json_to_function_code()`
    * `print_text_animated()`
    * `text_extract_from_web()`
    * `to_pascal()`
    * `track_agent()`
  * Module contents

# Camel Package#

## Subpackages#

  * [camel.agents package](camel.agents.html)
    * [Submodules](camel.agents.html#submodules)
    * [camel.agents.chat_agent module](camel.agents.html#module-camel.agents.chat_agent)
      * [`ChatAgent`](camel.agents.html#camel.agents.chat_agent.ChatAgent)
        * [`ChatAgent.get_info()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.get_info)
        * [`ChatAgent.get_usage_dict()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.get_usage_dict)
        * [`ChatAgent.handle_batch_response()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.handle_batch_response)
        * [`ChatAgent.handle_stream_response()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.handle_stream_response)
        * [`ChatAgent.init_messages()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.init_messages)
        * [`ChatAgent.is_tools_added()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.is_tools_added)
        * [`ChatAgent.record_message()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.record_message)
        * [`ChatAgent.reset()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.reset)
        * [`ChatAgent.set_output_language()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.set_output_language)
        * [`ChatAgent.step()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.step)
        * [`ChatAgent.step_async()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.step_async)
        * [`ChatAgent.step_tool_call()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.step_tool_call)
        * [`ChatAgent.step_tool_call_async()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.step_tool_call_async)
        * [`ChatAgent.system_message`](camel.agents.html#camel.agents.chat_agent.ChatAgent.system_message)
        * [`ChatAgent.update_memory()`](camel.agents.html#camel.agents.chat_agent.ChatAgent.update_memory)
      * [`FunctionCallingRecord`](camel.agents.html#camel.agents.chat_agent.FunctionCallingRecord)
        * [`FunctionCallingRecord.func_name`](camel.agents.html#camel.agents.chat_agent.FunctionCallingRecord.func_name)
        * [`FunctionCallingRecord.args`](camel.agents.html#camel.agents.chat_agent.FunctionCallingRecord.args)
        * [`FunctionCallingRecord.result`](camel.agents.html#camel.agents.chat_agent.FunctionCallingRecord.result)
        * [`FunctionCallingRecord.args`](camel.agents.html#id0)
        * [`FunctionCallingRecord.as_dict()`](camel.agents.html#camel.agents.chat_agent.FunctionCallingRecord.as_dict)
        * [`FunctionCallingRecord.func_name`](camel.agents.html#id1)
        * [`FunctionCallingRecord.model_computed_fields`](camel.agents.html#camel.agents.chat_agent.FunctionCallingRecord.model_computed_fields)
        * [`FunctionCallingRecord.model_config`](camel.agents.html#camel.agents.chat_agent.FunctionCallingRecord.model_config)
        * [`FunctionCallingRecord.model_fields`](camel.agents.html#camel.agents.chat_agent.FunctionCallingRecord.model_fields)
        * [`FunctionCallingRecord.result`](camel.agents.html#id2)
    * [camel.agents.role_playing module](camel.agents.html#camel-agents-role-playing-module)
    * [camel.agents.task_agent module](camel.agents.html#module-camel.agents.task_agent)
      * [`TaskCreationAgent`](camel.agents.html#camel.agents.task_agent.TaskCreationAgent)
        * [`TaskCreationAgent.task_creation_prompt`](camel.agents.html#camel.agents.task_agent.TaskCreationAgent.task_creation_prompt)
        * [`TaskCreationAgent.run()`](camel.agents.html#camel.agents.task_agent.TaskCreationAgent.run)
      * [`TaskPlannerAgent`](camel.agents.html#camel.agents.task_agent.TaskPlannerAgent)
        * [`TaskPlannerAgent.task_planner_prompt`](camel.agents.html#camel.agents.task_agent.TaskPlannerAgent.task_planner_prompt)
        * [`TaskPlannerAgent.run()`](camel.agents.html#camel.agents.task_agent.TaskPlannerAgent.run)
      * [`TaskPrioritizationAgent`](camel.agents.html#camel.agents.task_agent.TaskPrioritizationAgent)
        * [`TaskPrioritizationAgent.task_prioritization_prompt`](camel.agents.html#camel.agents.task_agent.TaskPrioritizationAgent.task_prioritization_prompt)
        * [`TaskPrioritizationAgent.run()`](camel.agents.html#camel.agents.task_agent.TaskPrioritizationAgent.run)
      * [`TaskSpecifyAgent`](camel.agents.html#camel.agents.task_agent.TaskSpecifyAgent)
        * [`TaskSpecifyAgent.DEFAULT_WORD_LIMIT`](camel.agents.html#camel.agents.task_agent.TaskSpecifyAgent.DEFAULT_WORD_LIMIT)
        * [`TaskSpecifyAgent.task_specify_prompt`](camel.agents.html#camel.agents.task_agent.TaskSpecifyAgent.task_specify_prompt)
        * [`TaskSpecifyAgent.DEFAULT_WORD_LIMIT`](camel.agents.html#id4)
        * [`TaskSpecifyAgent.run()`](camel.agents.html#camel.agents.task_agent.TaskSpecifyAgent.run)
    * [Module contents](camel.agents.html#module-camel.agents)
      * [`BaseAgent`](camel.agents.html#camel.agents.BaseAgent)
        * [`BaseAgent.reset()`](camel.agents.html#camel.agents.BaseAgent.reset)
        * [`BaseAgent.step()`](camel.agents.html#camel.agents.BaseAgent.step)
      * [`BaseToolAgent`](camel.agents.html#camel.agents.BaseToolAgent)
        * [`BaseToolAgent.reset()`](camel.agents.html#camel.agents.BaseToolAgent.reset)
        * [`BaseToolAgent.step()`](camel.agents.html#camel.agents.BaseToolAgent.step)
      * [`ChatAgent`](camel.agents.html#camel.agents.ChatAgent)
        * [`ChatAgent.get_info()`](camel.agents.html#camel.agents.ChatAgent.get_info)
        * [`ChatAgent.get_usage_dict()`](camel.agents.html#camel.agents.ChatAgent.get_usage_dict)
        * [`ChatAgent.handle_batch_response()`](camel.agents.html#camel.agents.ChatAgent.handle_batch_response)
        * [`ChatAgent.handle_stream_response()`](camel.agents.html#camel.agents.ChatAgent.handle_stream_response)
        * [`ChatAgent.init_messages()`](camel.agents.html#camel.agents.ChatAgent.init_messages)
        * [`ChatAgent.is_tools_added()`](camel.agents.html#camel.agents.ChatAgent.is_tools_added)
        * [`ChatAgent.record_message()`](camel.agents.html#camel.agents.ChatAgent.record_message)
        * [`ChatAgent.reset()`](camel.agents.html#camel.agents.ChatAgent.reset)
        * [`ChatAgent.set_output_language()`](camel.agents.html#camel.agents.ChatAgent.set_output_language)
        * [`ChatAgent.step()`](camel.agents.html#camel.agents.ChatAgent.step)
        * [`ChatAgent.step_async()`](camel.agents.html#camel.agents.ChatAgent.step_async)
        * [`ChatAgent.step_tool_call()`](camel.agents.html#camel.agents.ChatAgent.step_tool_call)
        * [`ChatAgent.step_tool_call_async()`](camel.agents.html#camel.agents.ChatAgent.step_tool_call_async)
        * [`ChatAgent.system_message`](camel.agents.html#camel.agents.ChatAgent.system_message)
        * [`ChatAgent.update_memory()`](camel.agents.html#camel.agents.ChatAgent.update_memory)
      * [`CriticAgent`](camel.agents.html#camel.agents.CriticAgent)
        * [`CriticAgent.flatten_options()`](camel.agents.html#camel.agents.CriticAgent.flatten_options)
        * [`CriticAgent.get_option()`](camel.agents.html#camel.agents.CriticAgent.get_option)
        * [`CriticAgent.parse_critic()`](camel.agents.html#camel.agents.CriticAgent.parse_critic)
        * [`CriticAgent.reduce_step()`](camel.agents.html#camel.agents.CriticAgent.reduce_step)
      * [`EmbodiedAgent`](camel.agents.html#camel.agents.EmbodiedAgent)
        * [`EmbodiedAgent.get_tool_agent_names()`](camel.agents.html#camel.agents.EmbodiedAgent.get_tool_agent_names)
        * [`EmbodiedAgent.step()`](camel.agents.html#camel.agents.EmbodiedAgent.step)
      * [`HuggingFaceToolAgent`](camel.agents.html#camel.agents.HuggingFaceToolAgent)
        * [`HuggingFaceToolAgent.chat()`](camel.agents.html#camel.agents.HuggingFaceToolAgent.chat)
        * [`HuggingFaceToolAgent.reset()`](camel.agents.html#camel.agents.HuggingFaceToolAgent.reset)
        * [`HuggingFaceToolAgent.step()`](camel.agents.html#camel.agents.HuggingFaceToolAgent.step)
      * [`KnowledgeGraphAgent`](camel.agents.html#camel.agents.KnowledgeGraphAgent)
        * [`KnowledgeGraphAgent.task_prompt`](camel.agents.html#camel.agents.KnowledgeGraphAgent.task_prompt)
        * [`KnowledgeGraphAgent.run()`](camel.agents.html#camel.agents.KnowledgeGraphAgent.run)
      * [`RoleAssignmentAgent`](camel.agents.html#camel.agents.RoleAssignmentAgent)
        * [`RoleAssignmentAgent.role_assignment_prompt`](camel.agents.html#camel.agents.RoleAssignmentAgent.role_assignment_prompt)
        * [`RoleAssignmentAgent.run()`](camel.agents.html#camel.agents.RoleAssignmentAgent.run)
      * [`SearchAgent`](camel.agents.html#camel.agents.SearchAgent)
        * [`SearchAgent.continue_search()`](camel.agents.html#camel.agents.SearchAgent.continue_search)
        * [`SearchAgent.summarize_text()`](camel.agents.html#camel.agents.SearchAgent.summarize_text)
      * [`TaskCreationAgent`](camel.agents.html#camel.agents.TaskCreationAgent)
        * [`TaskCreationAgent.task_creation_prompt`](camel.agents.html#camel.agents.TaskCreationAgent.task_creation_prompt)
        * [`TaskCreationAgent.run()`](camel.agents.html#camel.agents.TaskCreationAgent.run)
      * [`TaskPlannerAgent`](camel.agents.html#camel.agents.TaskPlannerAgent)
        * [`TaskPlannerAgent.task_planner_prompt`](camel.agents.html#camel.agents.TaskPlannerAgent.task_planner_prompt)
        * [`TaskPlannerAgent.run()`](camel.agents.html#camel.agents.TaskPlannerAgent.run)
      * [`TaskPrioritizationAgent`](camel.agents.html#camel.agents.TaskPrioritizationAgent)
        * [`TaskPrioritizationAgent.task_prioritization_prompt`](camel.agents.html#camel.agents.TaskPrioritizationAgent.task_prioritization_prompt)
        * [`TaskPrioritizationAgent.run()`](camel.agents.html#camel.agents.TaskPrioritizationAgent.run)
      * [`TaskSpecifyAgent`](camel.agents.html#camel.agents.TaskSpecifyAgent)
        * [`TaskSpecifyAgent.DEFAULT_WORD_LIMIT`](camel.agents.html#camel.agents.TaskSpecifyAgent.DEFAULT_WORD_LIMIT)
        * [`TaskSpecifyAgent.task_specify_prompt`](camel.agents.html#camel.agents.TaskSpecifyAgent.task_specify_prompt)
        * [`TaskSpecifyAgent.DEFAULT_WORD_LIMIT`](camel.agents.html#id7)
        * [`TaskSpecifyAgent.memory`](camel.agents.html#camel.agents.TaskSpecifyAgent.memory)
        * [`TaskSpecifyAgent.model_backend`](camel.agents.html#camel.agents.TaskSpecifyAgent.model_backend)
        * [`TaskSpecifyAgent.model_type`](camel.agents.html#camel.agents.TaskSpecifyAgent.model_type)
        * [`TaskSpecifyAgent.orig_sys_message`](camel.agents.html#camel.agents.TaskSpecifyAgent.orig_sys_message)
        * [`TaskSpecifyAgent.output_language`](camel.agents.html#camel.agents.TaskSpecifyAgent.output_language)
        * [`TaskSpecifyAgent.role_name`](camel.agents.html#camel.agents.TaskSpecifyAgent.role_name)
        * [`TaskSpecifyAgent.role_type`](camel.agents.html#camel.agents.TaskSpecifyAgent.role_type)
        * [`TaskSpecifyAgent.run()`](camel.agents.html#camel.agents.TaskSpecifyAgent.run)
        * [`TaskSpecifyAgent.task_specify_prompt`](camel.agents.html#id8)
        * [`TaskSpecifyAgent.terminated`](camel.agents.html#camel.agents.TaskSpecifyAgent.terminated)
  * [camel.prompts package](camel.prompts.html)
    * [Submodules](camel.prompts.html#submodules)
    * [camel.prompts.ai_society module](camel.prompts.html#module-camel.prompts.ai_society)
      * [`AISocietyPromptTemplateDict`](camel.prompts.html#camel.prompts.ai_society.AISocietyPromptTemplateDict)
        * [`AISocietyPromptTemplateDict.GENERATE_ASSISTANTS`](camel.prompts.html#camel.prompts.ai_society.AISocietyPromptTemplateDict.GENERATE_ASSISTANTS)
        * [`AISocietyPromptTemplateDict.GENERATE_USERS`](camel.prompts.html#camel.prompts.ai_society.AISocietyPromptTemplateDict.GENERATE_USERS)
        * [`AISocietyPromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#camel.prompts.ai_society.AISocietyPromptTemplateDict.GENERATE_TASKS)
        * [`AISocietyPromptTemplateDict.TASK_SPECIFY_PROMPT`](camel.prompts.html#camel.prompts.ai_society.AISocietyPromptTemplateDict.TASK_SPECIFY_PROMPT)
        * [`AISocietyPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.ai_society.AISocietyPromptTemplateDict.ASSISTANT_PROMPT)
        * [`AISocietyPromptTemplateDict.USER_PROMPT`](camel.prompts.html#camel.prompts.ai_society.AISocietyPromptTemplateDict.USER_PROMPT)
        * [`AISocietyPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#id0)
        * [`AISocietyPromptTemplateDict.CRITIC_PROMPT`](camel.prompts.html#camel.prompts.ai_society.AISocietyPromptTemplateDict.CRITIC_PROMPT)
        * [`AISocietyPromptTemplateDict.GENERATE_ASSISTANTS`](camel.prompts.html#id1)
        * [`AISocietyPromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#id2)
        * [`AISocietyPromptTemplateDict.GENERATE_USERS`](camel.prompts.html#id3)
        * [`AISocietyPromptTemplateDict.TASK_SPECIFY_PROMPT`](camel.prompts.html#id4)
        * [`AISocietyPromptTemplateDict.USER_PROMPT`](camel.prompts.html#id5)
    * [camel.prompts.base module](camel.prompts.html#module-camel.prompts.base)
      * [`CodePrompt`](camel.prompts.html#camel.prompts.base.CodePrompt)
        * [`CodePrompt.code_type`](camel.prompts.html#camel.prompts.base.CodePrompt.code_type)
        * [`CodePrompt.capitalize()`](camel.prompts.html#camel.prompts.base.CodePrompt.capitalize)
        * [`CodePrompt.casefold()`](camel.prompts.html#camel.prompts.base.CodePrompt.casefold)
        * [`CodePrompt.center()`](camel.prompts.html#camel.prompts.base.CodePrompt.center)
        * [`CodePrompt.code_type`](camel.prompts.html#id6)
        * [`CodePrompt.count()`](camel.prompts.html#camel.prompts.base.CodePrompt.count)
        * [`CodePrompt.encode()`](camel.prompts.html#camel.prompts.base.CodePrompt.encode)
        * [`CodePrompt.endswith()`](camel.prompts.html#camel.prompts.base.CodePrompt.endswith)
        * [`CodePrompt.execute()`](camel.prompts.html#camel.prompts.base.CodePrompt.execute)
        * [`CodePrompt.expandtabs()`](camel.prompts.html#camel.prompts.base.CodePrompt.expandtabs)
        * [`CodePrompt.find()`](camel.prompts.html#camel.prompts.base.CodePrompt.find)
        * [`CodePrompt.format()`](camel.prompts.html#camel.prompts.base.CodePrompt.format)
        * [`CodePrompt.format_map()`](camel.prompts.html#camel.prompts.base.CodePrompt.format_map)
        * [`CodePrompt.index()`](camel.prompts.html#camel.prompts.base.CodePrompt.index)
        * [`CodePrompt.isalnum()`](camel.prompts.html#camel.prompts.base.CodePrompt.isalnum)
        * [`CodePrompt.isalpha()`](camel.prompts.html#camel.prompts.base.CodePrompt.isalpha)
        * [`CodePrompt.isascii()`](camel.prompts.html#camel.prompts.base.CodePrompt.isascii)
        * [`CodePrompt.isdecimal()`](camel.prompts.html#camel.prompts.base.CodePrompt.isdecimal)
        * [`CodePrompt.isdigit()`](camel.prompts.html#camel.prompts.base.CodePrompt.isdigit)
        * [`CodePrompt.isidentifier()`](camel.prompts.html#camel.prompts.base.CodePrompt.isidentifier)
        * [`CodePrompt.islower()`](camel.prompts.html#camel.prompts.base.CodePrompt.islower)
        * [`CodePrompt.isnumeric()`](camel.prompts.html#camel.prompts.base.CodePrompt.isnumeric)
        * [`CodePrompt.isprintable()`](camel.prompts.html#camel.prompts.base.CodePrompt.isprintable)
        * [`CodePrompt.isspace()`](camel.prompts.html#camel.prompts.base.CodePrompt.isspace)
        * [`CodePrompt.istitle()`](camel.prompts.html#camel.prompts.base.CodePrompt.istitle)
        * [`CodePrompt.isupper()`](camel.prompts.html#camel.prompts.base.CodePrompt.isupper)
        * [`CodePrompt.join()`](camel.prompts.html#camel.prompts.base.CodePrompt.join)
        * [`CodePrompt.ljust()`](camel.prompts.html#camel.prompts.base.CodePrompt.ljust)
        * [`CodePrompt.lower()`](camel.prompts.html#camel.prompts.base.CodePrompt.lower)
        * [`CodePrompt.lstrip()`](camel.prompts.html#camel.prompts.base.CodePrompt.lstrip)
        * [`CodePrompt.maketrans()`](camel.prompts.html#camel.prompts.base.CodePrompt.maketrans)
        * [`CodePrompt.partition()`](camel.prompts.html#camel.prompts.base.CodePrompt.partition)
        * [`CodePrompt.removeprefix()`](camel.prompts.html#camel.prompts.base.CodePrompt.removeprefix)
        * [`CodePrompt.removesuffix()`](camel.prompts.html#camel.prompts.base.CodePrompt.removesuffix)
        * [`CodePrompt.replace()`](camel.prompts.html#camel.prompts.base.CodePrompt.replace)
        * [`CodePrompt.rfind()`](camel.prompts.html#camel.prompts.base.CodePrompt.rfind)
        * [`CodePrompt.rindex()`](camel.prompts.html#camel.prompts.base.CodePrompt.rindex)
        * [`CodePrompt.rjust()`](camel.prompts.html#camel.prompts.base.CodePrompt.rjust)
        * [`CodePrompt.rpartition()`](camel.prompts.html#camel.prompts.base.CodePrompt.rpartition)
        * [`CodePrompt.rsplit()`](camel.prompts.html#camel.prompts.base.CodePrompt.rsplit)
        * [`CodePrompt.rstrip()`](camel.prompts.html#camel.prompts.base.CodePrompt.rstrip)
        * [`CodePrompt.set_code_type()`](camel.prompts.html#camel.prompts.base.CodePrompt.set_code_type)
        * [`CodePrompt.split()`](camel.prompts.html#camel.prompts.base.CodePrompt.split)
        * [`CodePrompt.splitlines()`](camel.prompts.html#camel.prompts.base.CodePrompt.splitlines)
        * [`CodePrompt.startswith()`](camel.prompts.html#camel.prompts.base.CodePrompt.startswith)
        * [`CodePrompt.strip()`](camel.prompts.html#camel.prompts.base.CodePrompt.strip)
        * [`CodePrompt.swapcase()`](camel.prompts.html#camel.prompts.base.CodePrompt.swapcase)
        * [`CodePrompt.title()`](camel.prompts.html#camel.prompts.base.CodePrompt.title)
        * [`CodePrompt.translate()`](camel.prompts.html#camel.prompts.base.CodePrompt.translate)
        * [`CodePrompt.upper()`](camel.prompts.html#camel.prompts.base.CodePrompt.upper)
        * [`CodePrompt.zfill()`](camel.prompts.html#camel.prompts.base.CodePrompt.zfill)
      * [`TextPrompt`](camel.prompts.html#camel.prompts.base.TextPrompt)
        * [`TextPrompt.key_words`](camel.prompts.html#camel.prompts.base.TextPrompt.key_words)
        * [`TextPrompt.capitalize()`](camel.prompts.html#camel.prompts.base.TextPrompt.capitalize)
        * [`TextPrompt.casefold()`](camel.prompts.html#camel.prompts.base.TextPrompt.casefold)
        * [`TextPrompt.center()`](camel.prompts.html#camel.prompts.base.TextPrompt.center)
        * [`TextPrompt.count()`](camel.prompts.html#camel.prompts.base.TextPrompt.count)
        * [`TextPrompt.encode()`](camel.prompts.html#camel.prompts.base.TextPrompt.encode)
        * [`TextPrompt.endswith()`](camel.prompts.html#camel.prompts.base.TextPrompt.endswith)
        * [`TextPrompt.expandtabs()`](camel.prompts.html#camel.prompts.base.TextPrompt.expandtabs)
        * [`TextPrompt.find()`](camel.prompts.html#camel.prompts.base.TextPrompt.find)
        * [`TextPrompt.format()`](camel.prompts.html#camel.prompts.base.TextPrompt.format)
        * [`TextPrompt.format_map()`](camel.prompts.html#camel.prompts.base.TextPrompt.format_map)
        * [`TextPrompt.index()`](camel.prompts.html#camel.prompts.base.TextPrompt.index)
        * [`TextPrompt.isalnum()`](camel.prompts.html#camel.prompts.base.TextPrompt.isalnum)
        * [`TextPrompt.isalpha()`](camel.prompts.html#camel.prompts.base.TextPrompt.isalpha)
        * [`TextPrompt.isascii()`](camel.prompts.html#camel.prompts.base.TextPrompt.isascii)
        * [`TextPrompt.isdecimal()`](camel.prompts.html#camel.prompts.base.TextPrompt.isdecimal)
        * [`TextPrompt.isdigit()`](camel.prompts.html#camel.prompts.base.TextPrompt.isdigit)
        * [`TextPrompt.isidentifier()`](camel.prompts.html#camel.prompts.base.TextPrompt.isidentifier)
        * [`TextPrompt.islower()`](camel.prompts.html#camel.prompts.base.TextPrompt.islower)
        * [`TextPrompt.isnumeric()`](camel.prompts.html#camel.prompts.base.TextPrompt.isnumeric)
        * [`TextPrompt.isprintable()`](camel.prompts.html#camel.prompts.base.TextPrompt.isprintable)
        * [`TextPrompt.isspace()`](camel.prompts.html#camel.prompts.base.TextPrompt.isspace)
        * [`TextPrompt.istitle()`](camel.prompts.html#camel.prompts.base.TextPrompt.istitle)
        * [`TextPrompt.isupper()`](camel.prompts.html#camel.prompts.base.TextPrompt.isupper)
        * [`TextPrompt.join()`](camel.prompts.html#camel.prompts.base.TextPrompt.join)
        * [`TextPrompt.key_words`](camel.prompts.html#id7)
        * [`TextPrompt.ljust()`](camel.prompts.html#camel.prompts.base.TextPrompt.ljust)
        * [`TextPrompt.lower()`](camel.prompts.html#camel.prompts.base.TextPrompt.lower)
        * [`TextPrompt.lstrip()`](camel.prompts.html#camel.prompts.base.TextPrompt.lstrip)
        * [`TextPrompt.maketrans()`](camel.prompts.html#camel.prompts.base.TextPrompt.maketrans)
        * [`TextPrompt.partition()`](camel.prompts.html#camel.prompts.base.TextPrompt.partition)
        * [`TextPrompt.removeprefix()`](camel.prompts.html#camel.prompts.base.TextPrompt.removeprefix)
        * [`TextPrompt.removesuffix()`](camel.prompts.html#camel.prompts.base.TextPrompt.removesuffix)
        * [`TextPrompt.replace()`](camel.prompts.html#camel.prompts.base.TextPrompt.replace)
        * [`TextPrompt.rfind()`](camel.prompts.html#camel.prompts.base.TextPrompt.rfind)
        * [`TextPrompt.rindex()`](camel.prompts.html#camel.prompts.base.TextPrompt.rindex)
        * [`TextPrompt.rjust()`](camel.prompts.html#camel.prompts.base.TextPrompt.rjust)
        * [`TextPrompt.rpartition()`](camel.prompts.html#camel.prompts.base.TextPrompt.rpartition)
        * [`TextPrompt.rsplit()`](camel.prompts.html#camel.prompts.base.TextPrompt.rsplit)
        * [`TextPrompt.rstrip()`](camel.prompts.html#camel.prompts.base.TextPrompt.rstrip)
        * [`TextPrompt.split()`](camel.prompts.html#camel.prompts.base.TextPrompt.split)
        * [`TextPrompt.splitlines()`](camel.prompts.html#camel.prompts.base.TextPrompt.splitlines)
        * [`TextPrompt.startswith()`](camel.prompts.html#camel.prompts.base.TextPrompt.startswith)
        * [`TextPrompt.strip()`](camel.prompts.html#camel.prompts.base.TextPrompt.strip)
        * [`TextPrompt.swapcase()`](camel.prompts.html#camel.prompts.base.TextPrompt.swapcase)
        * [`TextPrompt.title()`](camel.prompts.html#camel.prompts.base.TextPrompt.title)
        * [`TextPrompt.translate()`](camel.prompts.html#camel.prompts.base.TextPrompt.translate)
        * [`TextPrompt.upper()`](camel.prompts.html#camel.prompts.base.TextPrompt.upper)
        * [`TextPrompt.zfill()`](camel.prompts.html#camel.prompts.base.TextPrompt.zfill)
      * [`TextPromptDict`](camel.prompts.html#camel.prompts.base.TextPromptDict)
        * [`TextPromptDict.EMBODIMENT_PROMPT`](camel.prompts.html#camel.prompts.base.TextPromptDict.EMBODIMENT_PROMPT)
      * [`return_prompt_wrapper()`](camel.prompts.html#camel.prompts.base.return_prompt_wrapper)
      * [`wrap_prompt_functions()`](camel.prompts.html#camel.prompts.base.wrap_prompt_functions)
    * [camel.prompts.code module](camel.prompts.html#module-camel.prompts.code)
      * [`CodePromptTemplateDict`](camel.prompts.html#camel.prompts.code.CodePromptTemplateDict)
        * [`CodePromptTemplateDict.GENERATE_LANGUAGES`](camel.prompts.html#camel.prompts.code.CodePromptTemplateDict.GENERATE_LANGUAGES)
        * [`CodePromptTemplateDict.GENERATE_DOMAINS`](camel.prompts.html#camel.prompts.code.CodePromptTemplateDict.GENERATE_DOMAINS)
        * [`CodePromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#camel.prompts.code.CodePromptTemplateDict.GENERATE_TASKS)
        * [`CodePromptTemplateDict.TASK_SPECIFY_PROMPT`](camel.prompts.html#camel.prompts.code.CodePromptTemplateDict.TASK_SPECIFY_PROMPT)
        * [`CodePromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.code.CodePromptTemplateDict.ASSISTANT_PROMPT)
        * [`CodePromptTemplateDict.USER_PROMPT`](camel.prompts.html#camel.prompts.code.CodePromptTemplateDict.USER_PROMPT)
        * [`CodePromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#id8)
        * [`CodePromptTemplateDict.GENERATE_DOMAINS`](camel.prompts.html#id9)
        * [`CodePromptTemplateDict.GENERATE_LANGUAGES`](camel.prompts.html#id10)
        * [`CodePromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#id11)
        * [`CodePromptTemplateDict.TASK_SPECIFY_PROMPT`](camel.prompts.html#id12)
        * [`CodePromptTemplateDict.USER_PROMPT`](camel.prompts.html#id13)
    * [camel.prompts.misalignment module](camel.prompts.html#module-camel.prompts.misalignment)
      * [`MisalignmentPromptTemplateDict`](camel.prompts.html#camel.prompts.misalignment.MisalignmentPromptTemplateDict)
        * [`MisalignmentPromptTemplateDict.DAN_PROMPT`](camel.prompts.html#camel.prompts.misalignment.MisalignmentPromptTemplateDict.DAN_PROMPT)
        * [`MisalignmentPromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#camel.prompts.misalignment.MisalignmentPromptTemplateDict.GENERATE_TASKS)
        * [`MisalignmentPromptTemplateDict.TASK_SPECIFY_PROMPT`](camel.prompts.html#camel.prompts.misalignment.MisalignmentPromptTemplateDict.TASK_SPECIFY_PROMPT)
        * [`MisalignmentPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.misalignment.MisalignmentPromptTemplateDict.ASSISTANT_PROMPT)
        * [`MisalignmentPromptTemplateDict.USER_PROMPT`](camel.prompts.html#camel.prompts.misalignment.MisalignmentPromptTemplateDict.USER_PROMPT)
        * [`MisalignmentPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#id14)
        * [`MisalignmentPromptTemplateDict.DAN_PROMPT`](camel.prompts.html#id15)
        * [`MisalignmentPromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#id16)
        * [`MisalignmentPromptTemplateDict.TASK_SPECIFY_PROMPT`](camel.prompts.html#id17)
        * [`MisalignmentPromptTemplateDict.USER_PROMPT`](camel.prompts.html#id18)
    * [camel.prompts.prompt_templates module](camel.prompts.html#module-camel.prompts.prompt_templates)
      * [`PromptTemplateGenerator`](camel.prompts.html#camel.prompts.prompt_templates.PromptTemplateGenerator)
        * [`PromptTemplateGenerator.get_generate_tasks_prompt()`](camel.prompts.html#camel.prompts.prompt_templates.PromptTemplateGenerator.get_generate_tasks_prompt)
        * [`PromptTemplateGenerator.get_prompt_from_key()`](camel.prompts.html#camel.prompts.prompt_templates.PromptTemplateGenerator.get_prompt_from_key)
        * [`PromptTemplateGenerator.get_system_prompt()`](camel.prompts.html#camel.prompts.prompt_templates.PromptTemplateGenerator.get_system_prompt)
        * [`PromptTemplateGenerator.get_task_specify_prompt()`](camel.prompts.html#camel.prompts.prompt_templates.PromptTemplateGenerator.get_task_specify_prompt)
    * [camel.prompts.task_prompt_template module](camel.prompts.html#module-camel.prompts.task_prompt_template)
      * [`TaskPromptTemplateDict`](camel.prompts.html#camel.prompts.task_prompt_template.TaskPromptTemplateDict)
    * [camel.prompts.translation module](camel.prompts.html#module-camel.prompts.translation)
      * [`TranslationPromptTemplateDict`](camel.prompts.html#camel.prompts.translation.TranslationPromptTemplateDict)
        * [`TranslationPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.translation.TranslationPromptTemplateDict.ASSISTANT_PROMPT)
        * [`TranslationPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#id19)
    * [Module contents](camel.prompts.html#module-camel.prompts)
      * [`AISocietyPromptTemplateDict`](camel.prompts.html#camel.prompts.AISocietyPromptTemplateDict)
        * [`AISocietyPromptTemplateDict.GENERATE_ASSISTANTS`](camel.prompts.html#camel.prompts.AISocietyPromptTemplateDict.GENERATE_ASSISTANTS)
        * [`AISocietyPromptTemplateDict.GENERATE_USERS`](camel.prompts.html#camel.prompts.AISocietyPromptTemplateDict.GENERATE_USERS)
        * [`AISocietyPromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#camel.prompts.AISocietyPromptTemplateDict.GENERATE_TASKS)
        * [`AISocietyPromptTemplateDict.TASK_SPECIFY_PROMPT`](camel.prompts.html#camel.prompts.AISocietyPromptTemplateDict.TASK_SPECIFY_PROMPT)
        * [`AISocietyPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.AISocietyPromptTemplateDict.ASSISTANT_PROMPT)
        * [`AISocietyPromptTemplateDict.USER_PROMPT`](camel.prompts.html#camel.prompts.AISocietyPromptTemplateDict.USER_PROMPT)
        * [`AISocietyPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#id20)
        * [`AISocietyPromptTemplateDict.CRITIC_PROMPT`](camel.prompts.html#camel.prompts.AISocietyPromptTemplateDict.CRITIC_PROMPT)
        * [`AISocietyPromptTemplateDict.GENERATE_ASSISTANTS`](camel.prompts.html#id21)
        * [`AISocietyPromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#id22)
        * [`AISocietyPromptTemplateDict.GENERATE_USERS`](camel.prompts.html#id23)
        * [`AISocietyPromptTemplateDict.TASK_SPECIFY_PROMPT`](camel.prompts.html#id24)
        * [`AISocietyPromptTemplateDict.USER_PROMPT`](camel.prompts.html#id25)
      * [`CodePrompt`](camel.prompts.html#camel.prompts.CodePrompt)
        * [`CodePrompt.code_type`](camel.prompts.html#camel.prompts.CodePrompt.code_type)
        * [`CodePrompt.capitalize()`](camel.prompts.html#camel.prompts.CodePrompt.capitalize)
        * [`CodePrompt.casefold()`](camel.prompts.html#camel.prompts.CodePrompt.casefold)
        * [`CodePrompt.center()`](camel.prompts.html#camel.prompts.CodePrompt.center)
        * [`CodePrompt.code_type`](camel.prompts.html#id26)
        * [`CodePrompt.count()`](camel.prompts.html#camel.prompts.CodePrompt.count)
        * [`CodePrompt.encode()`](camel.prompts.html#camel.prompts.CodePrompt.encode)
        * [`CodePrompt.endswith()`](camel.prompts.html#camel.prompts.CodePrompt.endswith)
        * [`CodePrompt.execute()`](camel.prompts.html#camel.prompts.CodePrompt.execute)
        * [`CodePrompt.expandtabs()`](camel.prompts.html#camel.prompts.CodePrompt.expandtabs)
        * [`CodePrompt.find()`](camel.prompts.html#camel.prompts.CodePrompt.find)
        * [`CodePrompt.format()`](camel.prompts.html#camel.prompts.CodePrompt.format)
        * [`CodePrompt.format_map()`](camel.prompts.html#camel.prompts.CodePrompt.format_map)
        * [`CodePrompt.index()`](camel.prompts.html#camel.prompts.CodePrompt.index)
        * [`CodePrompt.isalnum()`](camel.prompts.html#camel.prompts.CodePrompt.isalnum)
        * [`CodePrompt.isalpha()`](camel.prompts.html#camel.prompts.CodePrompt.isalpha)
        * [`CodePrompt.isascii()`](camel.prompts.html#camel.prompts.CodePrompt.isascii)
        * [`CodePrompt.isdecimal()`](camel.prompts.html#camel.prompts.CodePrompt.isdecimal)
        * [`CodePrompt.isdigit()`](camel.prompts.html#camel.prompts.CodePrompt.isdigit)
        * [`CodePrompt.isidentifier()`](camel.prompts.html#camel.prompts.CodePrompt.isidentifier)
        * [`CodePrompt.islower()`](camel.prompts.html#camel.prompts.CodePrompt.islower)
        * [`CodePrompt.isnumeric()`](camel.prompts.html#camel.prompts.CodePrompt.isnumeric)
        * [`CodePrompt.isprintable()`](camel.prompts.html#camel.prompts.CodePrompt.isprintable)
        * [`CodePrompt.isspace()`](camel.prompts.html#camel.prompts.CodePrompt.isspace)
        * [`CodePrompt.istitle()`](camel.prompts.html#camel.prompts.CodePrompt.istitle)
        * [`CodePrompt.isupper()`](camel.prompts.html#camel.prompts.CodePrompt.isupper)
        * [`CodePrompt.join()`](camel.prompts.html#camel.prompts.CodePrompt.join)
        * [`CodePrompt.ljust()`](camel.prompts.html#camel.prompts.CodePrompt.ljust)
        * [`CodePrompt.lower()`](camel.prompts.html#camel.prompts.CodePrompt.lower)
        * [`CodePrompt.lstrip()`](camel.prompts.html#camel.prompts.CodePrompt.lstrip)
        * [`CodePrompt.maketrans()`](camel.prompts.html#camel.prompts.CodePrompt.maketrans)
        * [`CodePrompt.partition()`](camel.prompts.html#camel.prompts.CodePrompt.partition)
        * [`CodePrompt.removeprefix()`](camel.prompts.html#camel.prompts.CodePrompt.removeprefix)
        * [`CodePrompt.removesuffix()`](camel.prompts.html#camel.prompts.CodePrompt.removesuffix)
        * [`CodePrompt.replace()`](camel.prompts.html#camel.prompts.CodePrompt.replace)
        * [`CodePrompt.rfind()`](camel.prompts.html#camel.prompts.CodePrompt.rfind)
        * [`CodePrompt.rindex()`](camel.prompts.html#camel.prompts.CodePrompt.rindex)
        * [`CodePrompt.rjust()`](camel.prompts.html#camel.prompts.CodePrompt.rjust)
        * [`CodePrompt.rpartition()`](camel.prompts.html#camel.prompts.CodePrompt.rpartition)
        * [`CodePrompt.rsplit()`](camel.prompts.html#camel.prompts.CodePrompt.rsplit)
        * [`CodePrompt.rstrip()`](camel.prompts.html#camel.prompts.CodePrompt.rstrip)
        * [`CodePrompt.set_code_type()`](camel.prompts.html#camel.prompts.CodePrompt.set_code_type)
        * [`CodePrompt.split()`](camel.prompts.html#camel.prompts.CodePrompt.split)
        * [`CodePrompt.splitlines()`](camel.prompts.html#camel.prompts.CodePrompt.splitlines)
        * [`CodePrompt.startswith()`](camel.prompts.html#camel.prompts.CodePrompt.startswith)
        * [`CodePrompt.strip()`](camel.prompts.html#camel.prompts.CodePrompt.strip)
        * [`CodePrompt.swapcase()`](camel.prompts.html#camel.prompts.CodePrompt.swapcase)
        * [`CodePrompt.title()`](camel.prompts.html#camel.prompts.CodePrompt.title)
        * [`CodePrompt.translate()`](camel.prompts.html#camel.prompts.CodePrompt.translate)
        * [`CodePrompt.upper()`](camel.prompts.html#camel.prompts.CodePrompt.upper)
        * [`CodePrompt.zfill()`](camel.prompts.html#camel.prompts.CodePrompt.zfill)
      * [`CodePromptTemplateDict`](camel.prompts.html#camel.prompts.CodePromptTemplateDict)
        * [`CodePromptTemplateDict.GENERATE_LANGUAGES`](camel.prompts.html#camel.prompts.CodePromptTemplateDict.GENERATE_LANGUAGES)
        * [`CodePromptTemplateDict.GENERATE_DOMAINS`](camel.prompts.html#camel.prompts.CodePromptTemplateDict.GENERATE_DOMAINS)
        * [`CodePromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#camel.prompts.CodePromptTemplateDict.GENERATE_TASKS)
        * [`CodePromptTemplateDict.TASK_SPECIFY_PROMPT`](camel.prompts.html#camel.prompts.CodePromptTemplateDict.TASK_SPECIFY_PROMPT)
        * [`CodePromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.CodePromptTemplateDict.ASSISTANT_PROMPT)
        * [`CodePromptTemplateDict.USER_PROMPT`](camel.prompts.html#camel.prompts.CodePromptTemplateDict.USER_PROMPT)
        * [`CodePromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#id27)
        * [`CodePromptTemplateDict.GENERATE_DOMAINS`](camel.prompts.html#id28)
        * [`CodePromptTemplateDict.GENERATE_LANGUAGES`](camel.prompts.html#id29)
        * [`CodePromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#id30)
        * [`CodePromptTemplateDict.TASK_SPECIFY_PROMPT`](camel.prompts.html#id31)
        * [`CodePromptTemplateDict.USER_PROMPT`](camel.prompts.html#id32)
      * [`EvaluationPromptTemplateDict`](camel.prompts.html#camel.prompts.EvaluationPromptTemplateDict)
        * [`EvaluationPromptTemplateDict.GENERATE_QUESTIONS`](camel.prompts.html#camel.prompts.EvaluationPromptTemplateDict.GENERATE_QUESTIONS)
        * [`EvaluationPromptTemplateDict.GENERATE_QUESTIONS`](camel.prompts.html#id33)
      * [`GenerateTextEmbeddingDataPromptTemplateDict`](camel.prompts.html#camel.prompts.GenerateTextEmbeddingDataPromptTemplateDict)
        * [`GenerateTextEmbeddingDataPromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#camel.prompts.GenerateTextEmbeddingDataPromptTemplateDict.GENERATE_TASKS)
        * [`GenerateTextEmbeddingDataPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.GenerateTextEmbeddingDataPromptTemplateDict.ASSISTANT_PROMPT)
        * [`GenerateTextEmbeddingDataPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#id34)
        * [`GenerateTextEmbeddingDataPromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#id35)
      * [`ImageCraftPromptTemplateDict`](camel.prompts.html#camel.prompts.ImageCraftPromptTemplateDict)
        * [`ImageCraftPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.ImageCraftPromptTemplateDict.ASSISTANT_PROMPT)
      * [`MisalignmentPromptTemplateDict`](camel.prompts.html#camel.prompts.MisalignmentPromptTemplateDict)
        * [`MisalignmentPromptTemplateDict.DAN_PROMPT`](camel.prompts.html#camel.prompts.MisalignmentPromptTemplateDict.DAN_PROMPT)
        * [`MisalignmentPromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#camel.prompts.MisalignmentPromptTemplateDict.GENERATE_TASKS)
        * [`MisalignmentPromptTemplateDict.TASK_SPECIFY_PROMPT`](camel.prompts.html#camel.prompts.MisalignmentPromptTemplateDict.TASK_SPECIFY_PROMPT)
        * [`MisalignmentPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.MisalignmentPromptTemplateDict.ASSISTANT_PROMPT)
        * [`MisalignmentPromptTemplateDict.USER_PROMPT`](camel.prompts.html#camel.prompts.MisalignmentPromptTemplateDict.USER_PROMPT)
        * [`MisalignmentPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#id36)
        * [`MisalignmentPromptTemplateDict.DAN_PROMPT`](camel.prompts.html#id37)
        * [`MisalignmentPromptTemplateDict.GENERATE_TASKS`](camel.prompts.html#id38)
        * [`MisalignmentPromptTemplateDict.TASK_SPECIFY_PROMPT`](camel.prompts.html#id39)
        * [`MisalignmentPromptTemplateDict.USER_PROMPT`](camel.prompts.html#id40)
      * [`MultiConditionImageCraftPromptTemplateDict`](camel.prompts.html#camel.prompts.MultiConditionImageCraftPromptTemplateDict)
        * [`MultiConditionImageCraftPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.MultiConditionImageCraftPromptTemplateDict.ASSISTANT_PROMPT)
      * [`ObjectRecognitionPromptTemplateDict`](camel.prompts.html#camel.prompts.ObjectRecognitionPromptTemplateDict)
        * [`ObjectRecognitionPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.ObjectRecognitionPromptTemplateDict.ASSISTANT_PROMPT)
      * [`PromptTemplateGenerator`](camel.prompts.html#camel.prompts.PromptTemplateGenerator)
        * [`PromptTemplateGenerator.get_generate_tasks_prompt()`](camel.prompts.html#camel.prompts.PromptTemplateGenerator.get_generate_tasks_prompt)
        * [`PromptTemplateGenerator.get_prompt_from_key()`](camel.prompts.html#camel.prompts.PromptTemplateGenerator.get_prompt_from_key)
        * [`PromptTemplateGenerator.get_system_prompt()`](camel.prompts.html#camel.prompts.PromptTemplateGenerator.get_system_prompt)
        * [`PromptTemplateGenerator.get_task_specify_prompt()`](camel.prompts.html#camel.prompts.PromptTemplateGenerator.get_task_specify_prompt)
      * [`RoleDescriptionPromptTemplateDict`](camel.prompts.html#camel.prompts.RoleDescriptionPromptTemplateDict)
        * [`RoleDescriptionPromptTemplateDict.ROLE_DESCRIPTION_PROMPT`](camel.prompts.html#camel.prompts.RoleDescriptionPromptTemplateDict.ROLE_DESCRIPTION_PROMPT)
        * [`RoleDescriptionPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.RoleDescriptionPromptTemplateDict.ASSISTANT_PROMPT)
        * [`RoleDescriptionPromptTemplateDict.USER_PROMPT`](camel.prompts.html#camel.prompts.RoleDescriptionPromptTemplateDict.USER_PROMPT)
        * [`RoleDescriptionPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#id41)
        * [`RoleDescriptionPromptTemplateDict.ROLE_DESCRIPTION_PROMPT`](camel.prompts.html#id42)
        * [`RoleDescriptionPromptTemplateDict.USER_PROMPT`](camel.prompts.html#id43)
      * [`SolutionExtractionPromptTemplateDict`](camel.prompts.html#camel.prompts.SolutionExtractionPromptTemplateDict)
        * [`SolutionExtractionPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.SolutionExtractionPromptTemplateDict.ASSISTANT_PROMPT)
        * [`SolutionExtractionPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#id44)
      * [`TaskPromptTemplateDict`](camel.prompts.html#camel.prompts.TaskPromptTemplateDict)
      * [`TextPrompt`](camel.prompts.html#camel.prompts.TextPrompt)
        * [`TextPrompt.key_words`](camel.prompts.html#camel.prompts.TextPrompt.key_words)
        * [`TextPrompt.capitalize()`](camel.prompts.html#camel.prompts.TextPrompt.capitalize)
        * [`TextPrompt.casefold()`](camel.prompts.html#camel.prompts.TextPrompt.casefold)
        * [`TextPrompt.center()`](camel.prompts.html#camel.prompts.TextPrompt.center)
        * [`TextPrompt.count()`](camel.prompts.html#camel.prompts.TextPrompt.count)
        * [`TextPrompt.encode()`](camel.prompts.html#camel.prompts.TextPrompt.encode)
        * [`TextPrompt.endswith()`](camel.prompts.html#camel.prompts.TextPrompt.endswith)
        * [`TextPrompt.expandtabs()`](camel.prompts.html#camel.prompts.TextPrompt.expandtabs)
        * [`TextPrompt.find()`](camel.prompts.html#camel.prompts.TextPrompt.find)
        * [`TextPrompt.format()`](camel.prompts.html#camel.prompts.TextPrompt.format)
        * [`TextPrompt.format_map()`](camel.prompts.html#camel.prompts.TextPrompt.format_map)
        * [`TextPrompt.index()`](camel.prompts.html#camel.prompts.TextPrompt.index)
        * [`TextPrompt.isalnum()`](camel.prompts.html#camel.prompts.TextPrompt.isalnum)
        * [`TextPrompt.isalpha()`](camel.prompts.html#camel.prompts.TextPrompt.isalpha)
        * [`TextPrompt.isascii()`](camel.prompts.html#camel.prompts.TextPrompt.isascii)
        * [`TextPrompt.isdecimal()`](camel.prompts.html#camel.prompts.TextPrompt.isdecimal)
        * [`TextPrompt.isdigit()`](camel.prompts.html#camel.prompts.TextPrompt.isdigit)
        * [`TextPrompt.isidentifier()`](camel.prompts.html#camel.prompts.TextPrompt.isidentifier)
        * [`TextPrompt.islower()`](camel.prompts.html#camel.prompts.TextPrompt.islower)
        * [`TextPrompt.isnumeric()`](camel.prompts.html#camel.prompts.TextPrompt.isnumeric)
        * [`TextPrompt.isprintable()`](camel.prompts.html#camel.prompts.TextPrompt.isprintable)
        * [`TextPrompt.isspace()`](camel.prompts.html#camel.prompts.TextPrompt.isspace)
        * [`TextPrompt.istitle()`](camel.prompts.html#camel.prompts.TextPrompt.istitle)
        * [`TextPrompt.isupper()`](camel.prompts.html#camel.prompts.TextPrompt.isupper)
        * [`TextPrompt.join()`](camel.prompts.html#camel.prompts.TextPrompt.join)
        * [`TextPrompt.key_words`](camel.prompts.html#id45)
        * [`TextPrompt.ljust()`](camel.prompts.html#camel.prompts.TextPrompt.ljust)
        * [`TextPrompt.lower()`](camel.prompts.html#camel.prompts.TextPrompt.lower)
        * [`TextPrompt.lstrip()`](camel.prompts.html#camel.prompts.TextPrompt.lstrip)
        * [`TextPrompt.maketrans()`](camel.prompts.html#camel.prompts.TextPrompt.maketrans)
        * [`TextPrompt.partition()`](camel.prompts.html#camel.prompts.TextPrompt.partition)
        * [`TextPrompt.removeprefix()`](camel.prompts.html#camel.prompts.TextPrompt.removeprefix)
        * [`TextPrompt.removesuffix()`](camel.prompts.html#camel.prompts.TextPrompt.removesuffix)
        * [`TextPrompt.replace()`](camel.prompts.html#camel.prompts.TextPrompt.replace)
        * [`TextPrompt.rfind()`](camel.prompts.html#camel.prompts.TextPrompt.rfind)
        * [`TextPrompt.rindex()`](camel.prompts.html#camel.prompts.TextPrompt.rindex)
        * [`TextPrompt.rjust()`](camel.prompts.html#camel.prompts.TextPrompt.rjust)
        * [`TextPrompt.rpartition()`](camel.prompts.html#camel.prompts.TextPrompt.rpartition)
        * [`TextPrompt.rsplit()`](camel.prompts.html#camel.prompts.TextPrompt.rsplit)
        * [`TextPrompt.rstrip()`](camel.prompts.html#camel.prompts.TextPrompt.rstrip)
        * [`TextPrompt.split()`](camel.prompts.html#camel.prompts.TextPrompt.split)
        * [`TextPrompt.splitlines()`](camel.prompts.html#camel.prompts.TextPrompt.splitlines)
        * [`TextPrompt.startswith()`](camel.prompts.html#camel.prompts.TextPrompt.startswith)
        * [`TextPrompt.strip()`](camel.prompts.html#camel.prompts.TextPrompt.strip)
        * [`TextPrompt.swapcase()`](camel.prompts.html#camel.prompts.TextPrompt.swapcase)
        * [`TextPrompt.title()`](camel.prompts.html#camel.prompts.TextPrompt.title)
        * [`TextPrompt.translate()`](camel.prompts.html#camel.prompts.TextPrompt.translate)
        * [`TextPrompt.upper()`](camel.prompts.html#camel.prompts.TextPrompt.upper)
        * [`TextPrompt.zfill()`](camel.prompts.html#camel.prompts.TextPrompt.zfill)
      * [`TextPromptDict`](camel.prompts.html#camel.prompts.TextPromptDict)
        * [`TextPromptDict.EMBODIMENT_PROMPT`](camel.prompts.html#camel.prompts.TextPromptDict.EMBODIMENT_PROMPT)
      * [`TranslationPromptTemplateDict`](camel.prompts.html#camel.prompts.TranslationPromptTemplateDict)
        * [`TranslationPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.TranslationPromptTemplateDict.ASSISTANT_PROMPT)
        * [`TranslationPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#id46)
      * [`VideoDescriptionPromptTemplateDict`](camel.prompts.html#camel.prompts.VideoDescriptionPromptTemplateDict)
        * [`VideoDescriptionPromptTemplateDict.ASSISTANT_PROMPT`](camel.prompts.html#camel.prompts.VideoDescriptionPromptTemplateDict.ASSISTANT_PROMPT)

## Submodules#

## camel.configs module#

_class _camel.configs.AnthropicConfig(_*_ , _tools : List[Any] | None = None_, _max_tokens : int = 256_, _stop_sequences : List[str] | NotGiven = NOT_GIVEN_, _temperature : float = 1_, _top_p : float | NotGiven = NOT_GIVEN_, _top_k : int | NotGiven = NOT_GIVEN_, _metadata : NotGiven = NOT_GIVEN_, _stream : bool = False_)[[source]](_modules/camel/configs/anthropic_config.html#AnthropicConfig)#
    

Bases: `BaseConfig`

Defines the parameters for generating chat completions using the Anthropic
API.

See: <https://docs.anthropic.com/claude/reference/complete_post> :param
max_tokens: The maximum number of tokens to

> generate before stopping. Note that Anthropic models may stop before
> reaching this maximum. This parameter only specifies the absolute maximum
> number of tokens to generate. (default: `256`)

Parameters:

    

  * **stop_sequences** (_List_ _[__str_ _]__,__optional_) – Sequences that will cause the model to stop generating completion text. Anthropic models stop on “nnHuman:”, and may include additional built-in stop sequences in the future. By providing the stop_sequences parameter, you may include additional strings that will cause the model to stop generating.

  * **temperature** (_float_ _,__optional_) – Amount of randomness injected into the response. Defaults to 1. Ranges from 0 to 1. Use temp closer to 0 for analytical / multiple choice, and closer to 1 for creative and generative tasks. (default: `1`)

  * **top_p** (_float_ _,__optional_) – Use nucleus sampling. In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by top_p. You should either alter temperature or top_p, but not both. (default: `0.7`)

  * **top_k** (_int_ _,__optional_) – Only sample from the top K options for each subsequent token. Used to remove “long tail” low probability responses. (default: `5`)

  * **metadata** – An object describing metadata about the request.

  * **stream** (_bool_ _,__optional_) – 

Whether to incrementally stream the response using server-sent events.

> (default: `False`)

max_tokens _: int_#

    

metadata _: NotGiven_#

    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'max_tokens':
FieldInfo(annotation=int, required=False, default=256), 'metadata':
FieldInfo(annotation=NotGiven, required=False, default=NOT_GIVEN),
'stop_sequences': FieldInfo(annotation=Union[List[str], NotGiven],
required=False, default=NOT_GIVEN), 'stream': FieldInfo(annotation=bool,
required=False, default=False), 'temperature': FieldInfo(annotation=float,
required=False, default=1), 'tools': FieldInfo(annotation=Union[List[Any],
NoneType], required=False, default=None), 'top_k':
FieldInfo(annotation=Union[int, NotGiven], required=False, default=NOT_GIVEN),
'top_p': FieldInfo(annotation=Union[float, NotGiven], required=False,
default=NOT_GIVEN)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

stop_sequences _: List[str] | NotGiven_#
    

stream _: bool_#

    

temperature _: float_#

    

top_k _: int | NotGiven_#
    

top_p _: float | NotGiven_#
    

_class _camel.configs.BaseConfig(_*_ , _tools : List[Any] | None = None_)[[source]](_modules/camel/configs/base_config.html#BaseConfig)#
    

Bases: `ABC`, `BaseModel`

as_dict() -> dict[str,
Any][[source]](_modules/camel/configs/base_config.html#BaseConfig.as_dict)#

    

_classmethod
_fields_type_checking(_tools_)[[source]](_modules/camel/configs/base_config.html#BaseConfig.fields_type_checking)#

    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'tools':
FieldInfo(annotation=Union[List[Any], NoneType], required=False,
default=None)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

tools _: List[Any] | None_#
    

A list of tools the model may call. Currently, only functions are supported as
a tool. Use this to provide a list of functions the model may generate JSON
inputs for. A max of 128 functions are supported.

_class _camel.configs.ChatGPTConfig(_*_ , _tools : List[Any] | None = None_, _temperature : float = 0.2_, _top_p : float = 1.0_, _n : int = 1_, _stream : bool = False_, _stop : str | Sequence[str] | NotGiven = NOT_GIVEN_, _max_tokens : int | NotGiven = NOT_GIVEN_, _presence_penalty : float = 0.0_, _response_format : dict | NotGiven = NOT_GIVEN_, _frequency_penalty : float = 0.0_, _logit_bias : dict = None_, _user : str = ''_, _tool_choice : dict[str, str] | str | None = None_)[[source]](_modules/camel/configs/openai_config.html#ChatGPTConfig)#
    

Bases: `BaseConfig`

Defines the parameters for generating chat completions using the OpenAI API.

Parameters:

    

  * **temperature** (_float_ _,__optional_) – Sampling temperature to use, between `0` and `2`. Higher values make the output more random, while lower values make it more focused and deterministic. (default: `0.2`)

  * **top_p** (_float_ _,__optional_) – An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So `0.1` means only the tokens comprising the top 10% probability mass are considered. (default: `1.0`)

  * **n** (_int_ _,__optional_) – How many chat completion choices to generate for each input message. (default: `1`)

  * **response_format** (_object_ _,__optional_) – An object specifying the format that the model must output. Compatible with GPT-4 Turbo and all GPT-3.5 Turbo models newer than gpt-3.5-turbo-1106. Setting to {“type”: “json_object”} enables JSON mode, which guarantees the message the model generates is valid JSON. Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if finish_reason=”length”, which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.

  * **stream** (_bool_ _,__optional_) – If True, partial message deltas will be sent as data-only server-sent events as they become available. (default: `False`)

  * **stop** (_str_ _or_ _list_ _,__optional_) – Up to `4` sequences where the API will stop generating further tokens. (default: `None`)

  * **max_tokens** (_int_ _,__optional_) – The maximum number of tokens to generate in the chat completion. The total length of input tokens and generated tokens is limited by the model’s context length. (default: `None`)

  * **presence_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model’s likelihood to talk about new topics. See more information about frequency and presence penalties. (default: `0.0`)

  * **frequency_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model’s likelihood to repeat the same line verbatim. See more information about frequency and presence penalties. (default: `0.0`)

  * **logit_bias** (_dict_ _,__optional_) – Modify the likelihood of specified tokens appearing in the completion. Accepts a json object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from `-100` to `100`. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between:obj:` -1` and `1` should decrease or increase likelihood of selection; values like `-100` or `100` should result in a ban or exclusive selection of the relevant token. (default: `{}`)

  * **user** (_str_ _,__optional_) – A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. (default: `""`)

  * **tools** (_list_ _[__OpenAIFunction_ _]__,__optional_) – A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

  * **tool_choice** (_Union_ _[__dict_ _[__str_ _,__str_ _]__,__str_ _]__,__optional_) – Controls which (if any) tool is called by the model. `"none"` means the model will not call any tool and instead generates a message. `"auto"` means the model can pick between generating a message or calling one or more tools. `"required"` means the model must call one or more tools. Specifying a particular tool via {“type”: “function”, “function”: {“name”: “my_function”}} forces the model to call that tool. `"none"` is the default when no tools are present. `"auto"` is the default if tools are present.

frequency_penalty _: float_#

    

logit_bias _: dict_#

    

max_tokens _: int | NotGiven_#
    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'frequency_penalty':
FieldInfo(annotation=float, required=False, default=0.0), 'logit_bias':
FieldInfo(annotation=dict, required=False, default_factory=dict),
'max_tokens': FieldInfo(annotation=Union[int, NotGiven], required=False,
default=NOT_GIVEN), 'n': FieldInfo(annotation=int, required=False, default=1),
'presence_penalty': FieldInfo(annotation=float, required=False, default=0.0),
'response_format': FieldInfo(annotation=Union[dict, NotGiven], required=False,
default=NOT_GIVEN), 'stop': FieldInfo(annotation=Union[str, Sequence[str],
NotGiven], required=False, default=NOT_GIVEN), 'stream':
FieldInfo(annotation=bool, required=False, default=False), 'temperature':
FieldInfo(annotation=float, required=False, default=0.2), 'tool_choice':
FieldInfo(annotation=Union[dict[str, str], str, NoneType], required=False,
default=None), 'tools': FieldInfo(annotation=Union[List[Any], NoneType],
required=False, default=None), 'top_p': FieldInfo(annotation=float,
required=False, default=1.0), 'user': FieldInfo(annotation=str,
required=False, default='')}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

n _: int_#

    

presence_penalty _: float_#

    

response_format _: dict | NotGiven_#
    

stop _: str | Sequence[str] | NotGiven_#
    

stream _: bool_#

    

temperature _: float_#

    

tool_choice _: dict[str, str] | str | None_#
    

top_p _: float_#

    

user _: str_#

    

_class _camel.configs.GeminiConfig(_*_ , _tools : List[Any] | None = None_, _candidate_count : int | None = None_, _stop_sequences : Iterable[str] | None = None_, _max_output_tokens : int | None = None_, _temperature : float | None = None_, _top_p : float | None = None_, _top_k : int | None = None_, _response_mime_type : str | None = None_, _response_schema : Any | None = None_, _safety_settings : Any | None = None_, _tool_config : Any | None = None_, _request_options : Any | None = None_)[[source]](_modules/camel/configs/gemini_config.html#GeminiConfig)#
    

Bases: `BaseConfig`

A simple dataclass used to configure the generation parameters of
GenerativeModel.generate_content.

Parameters:

    

  * **candidate_count** (_int_ _,__optional_) – Number of responses to return.

  * **stop_sequences** (_Iterable_ _[__str_ _]__,__optional_) – The set of character sequences (up to 5) that will stop output generation. If specified the API will stop at the first appearance of a stop sequence. The stop sequence will not be included as part of the response.

  * **max_output_tokens** (_int_ _,__optional_) – The maximum number of tokens to include in a candidate. If unset, this will default to output_token_limit specified in the model’s specification.

  * **temperature** (_float_ _,__optional_) – Controls the randomness of the output. Note: The default value varies by model, see the Model.temperature attribute of the Model returned the genai.get_model function. Values can range from [0.0,1.0], inclusive. A value closer to 1.0 will produce responses that are more varied and creative, while a value closer to 0.0 will typically result in more straightforward responses from the model.

  * **top_p** (_int_ _,__optional_) – The maximum cumulative probability of tokens to consider when sampling. The model uses combined Top-k and nucleus sampling. Tokens are sorted based on their assigned probabilities so that only the most likely tokens are considered. Top-k sampling directly limits the maximum number of tokens to consider, while Nucleus sampling limits number of tokens based on the cumulative probability. Note: The default value varies by model, see the Model.top_p attribute of the Model returned the genai.get_model function.

  * **top_k** (_int_ _,__optional_) – The maximum number of tokens to consider when sampling. The model uses combined Top-k and nucleus sampling.Top-k sampling considers the set of top_k most probable tokens. Defaults to 40. Note: The default value varies by model, see the Model.top_k attribute of the Model returned the genai.get_model function.

  * **response_mime_type** (_str_ _,__optional_) – Output response mimetype of the generated candidate text. Supported mimetype: text/plain: (default) Text output. application/json: JSON response in the candidates.

  * **response_schema** (_Schema_ _,__optional_) – Specifies the format of the JSON requested if response_mime_type is application/json.

  * **safety_settings** (_SafetySettingOptions_ _,__optional_) – Overrides for the model’s safety settings.

  * **tools** (_FunctionLibraryType_ _,__optional_) – protos.Tools more info coming soon.

  * **tool_config** (_ToolConfigType_ _,__optional_) – more info coming soon.

  * **request_options** (_RequestOptionsType_ _,__optional_) – Options for the request.

candidate_count _: int | None_#
    

_classmethod _fields_type_checking(_data :
Any_)[[source]](_modules/camel/configs/gemini_config.html#GeminiConfig.fields_type_checking)#

    

max_output_tokens _: int | None_#
    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'candidate_count':
FieldInfo(annotation=Union[int, NoneType], required=False, default=None),
'max_output_tokens': FieldInfo(annotation=Union[int, NoneType],
required=False, default=None), 'request_options':
FieldInfo(annotation=Union[Any, NoneType], required=False, default=None),
'response_mime_type': FieldInfo(annotation=Union[str, NoneType],
required=False, default=None), 'response_schema':
FieldInfo(annotation=Union[Any, NoneType], required=False, default=None),
'safety_settings': FieldInfo(annotation=Union[Any, NoneType], required=False,
default=None), 'stop_sequences': FieldInfo(annotation=Union[Iterable[str],
NoneType], required=False, default=None), 'temperature':
FieldInfo(annotation=Union[float, NoneType], required=False, default=None),
'tool_config': FieldInfo(annotation=Union[Any, NoneType], required=False,
default=None), 'tools': FieldInfo(annotation=Union[List[Any], NoneType],
required=False, default=None), 'top_k': FieldInfo(annotation=Union[int,
NoneType], required=False, default=None), 'top_p':
FieldInfo(annotation=Union[float, NoneType], required=False, default=None)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

request_options _: Any | None_#
    

response_mime_type _: str | None_#
    

response_schema _: Any | None_#
    

safety_settings _: Any | None_#
    

stop_sequences _: Iterable[str] | None_#
    

temperature _: float | None_#
    

tool_config _: Any | None_#
    

top_k _: int | None_#
    

top_p _: float | None_#
    

_class _camel.configs.GroqConfig(_*_ , _tools : List[Any] | None = None_, _temperature : float = 0.2_, _top_p : float = 1.0_, _n : int = 1_, _stream : bool = False_, _stop : str | Sequence[str] | NotGiven = NOT_GIVEN_, _max_tokens : int | NotGiven = NOT_GIVEN_, _presence_penalty : float = 0.0_, _response_format : dict | NotGiven = NOT_GIVEN_, _frequency_penalty : float = 0.0_, _user : str = ''_, _tool_choice : dict[str, str] | str | None = 'auto'_)[[source]](_modules/camel/configs/groq_config.html#GroqConfig)#
    

Bases: `BaseConfig`

Defines the parameters for generating chat completions using OpenAI
compatibility.

Reference: <https://console.groq.com/docs/openai>

Parameters:

    

  * **temperature** (_float_ _,__optional_) – Sampling temperature to use, between `0` and `2`. Higher values make the output more random, while lower values make it more focused and deterministic. (default: `0.2`)

  * **top_p** (_float_ _,__optional_) – An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So `0.1` means only the tokens comprising the top 10% probability mass are considered. (default: `1.0`)

  * **n** (_int_ _,__optional_) – How many chat completion choices to generate for each input message. (default: `1`)

  * **response_format** (_object_ _,__optional_) – An object specifying the format that the model must output. Compatible with GPT-4 Turbo and all GPT-3.5 Turbo models newer than gpt-3.5-turbo-1106. Setting to {“type”: “json_object”} enables JSON mode, which guarantees the message the model generates is valid JSON. Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if finish_reason=”length”, which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.

  * **stream** (_bool_ _,__optional_) – If True, partial message deltas will be sent as data-only server-sent events as they become available. (default: `False`)

  * **stop** (_str_ _or_ _list_ _,__optional_) – Up to `4` sequences where the API will stop generating further tokens. (default: `None`)

  * **max_tokens** (_int_ _,__optional_) – The maximum number of tokens to generate in the chat completion. The total length of input tokens and generated tokens is limited by the model’s context length. (default: `None`)

  * **presence_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model’s likelihood to talk about new topics. See more information about frequency and presence penalties. (default: `0.0`)

  * **frequency_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model’s likelihood to repeat the same line verbatim. See more information about frequency and presence penalties. (default: `0.0`)

  * **user** (_str_ _,__optional_) – A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. (default: `""`)

  * **tools** (_list_ _[__OpenAIFunction_ _]__,__optional_) – A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

  * **tool_choice** (_Union_ _[__dict_ _[__str_ _,__str_ _]__,__str_ _]__,__optional_) – Controls which (if any) tool is called by the model. `"none"` means the model will not call any tool and instead generates a message. `"auto"` means the model can pick between generating a message or calling one or more tools. `"required"` means the model must call one or more tools. Specifying a particular tool via {“type”: “function”, “function”: {“name”: “my_function”}} forces the model to call that tool. `"none"` is the default when no tools are present. `"auto"` is the default if tools are present.

frequency_penalty _: float_#

    

max_tokens _: int | NotGiven_#
    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'frequency_penalty':
FieldInfo(annotation=float, required=False, default=0.0), 'max_tokens':
FieldInfo(annotation=Union[int, NotGiven], required=False, default=NOT_GIVEN),
'n': FieldInfo(annotation=int, required=False, default=1), 'presence_penalty':
FieldInfo(annotation=float, required=False, default=0.0), 'response_format':
FieldInfo(annotation=Union[dict, NotGiven], required=False,
default=NOT_GIVEN), 'stop': FieldInfo(annotation=Union[str, Sequence[str],
NotGiven], required=False, default=NOT_GIVEN), 'stream':
FieldInfo(annotation=bool, required=False, default=False), 'temperature':
FieldInfo(annotation=float, required=False, default=0.2), 'tool_choice':
FieldInfo(annotation=Union[dict[str, str], str, NoneType], required=False,
default='auto'), 'tools': FieldInfo(annotation=Union[List[Any], NoneType],
required=False, default=None), 'top_p': FieldInfo(annotation=float,
required=False, default=1.0), 'user': FieldInfo(annotation=str,
required=False, default='')}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

n _: int_#

    

presence_penalty _: float_#

    

response_format _: dict | NotGiven_#
    

stop _: str | Sequence[str] | NotGiven_#
    

stream _: bool_#

    

temperature _: float_#

    

tool_choice _: dict[str, str] | str | None_#
    

top_p _: float_#

    

user _: str_#

    

_class _camel.configs.LiteLLMConfig(_*_ , _tools : List[Any] | None = None_, _timeout : float | str | None = None_, _temperature : float | None = None_, _top_p : float | None = None_, _n : int | None = None_, _stream : bool | None = None_, _stream_options : dict | None = None_, _stop : str | List[str] | None = None_, _max_tokens : int | None = None_, _presence_penalty : float | None = None_, _frequency_penalty : float | None = None_, _logit_bias : dict | None = None_, _user : str | None = None_, _response_format : dict | None = None_, _seed : int | None = None_, _tool_choice : str | dict | None = None_, _logprobs : bool | None = None_, _top_logprobs : int | None = None_, _deployment_id : str | None = None_, _extra_headers : dict | None = None_, _api_version : str | None = None_, _mock_response : str | None = None_, _custom_llm_provider : str | None = None_, _max_retries : int | None = None_)[[source]](_modules/camel/configs/litellm_config.html#LiteLLMConfig)#
    

Bases: `BaseConfig`

Defines the parameters for generating chat completions using the LiteLLM API.

Parameters:

    

  * **timeout** (_Optional_ _[__Union_ _[__float_ _,__str_ _]__]__,__optional_) – Request timeout. (default: None)

  * **temperature** (_Optional_ _[__float_ _]__,__optional_) – Temperature parameter for controlling randomness. (default: None)

  * **top_p** (_Optional_ _[__float_ _]__,__optional_) – Top-p parameter for nucleus sampling. (default: None)

  * **n** (_Optional_ _[__int_ _]__,__optional_) – Number of completions to generate. (default: None)

  * **stream** (_Optional_ _[__bool_ _]__,__optional_) – Whether to return a streaming response. (default: None)

  * **stream_options** (_Optional_ _[__dict_ _]__,__optional_) – Options for the streaming response. (default: None)

  * **stop** (_Optional_ _[__Union_ _[__str_ _,__List_ _[__str_ _]__]__]__,__optional_) – Sequences where the API will stop generating further tokens. (default: None)

  * **max_tokens** (_Optional_ _[__int_ _]__,__optional_) – Maximum number of tokens to generate. (default: None)

  * **presence_penalty** (_Optional_ _[__float_ _]__,__optional_) – Penalize new tokens based on their existence in the text so far. (default: None)

  * **frequency_penalty** (_Optional_ _[__float_ _]__,__optional_) – Penalize new tokens based on their frequency in the text so far. (default: None)

  * **logit_bias** (_Optional_ _[__dict_ _]__,__optional_) – Modify the probability of specific tokens appearing in the completion. (default: None)

  * **user** (_Optional_ _[__str_ _]__,__optional_) – A unique identifier representing the end-user. (default: None)

  * **response_format** (_Optional_ _[__dict_ _]__,__optional_) – Response format parameters. (default: None)

  * **seed** (_Optional_ _[__int_ _]__,__optional_) – Random seed. (default: None)

  * **tools** (_Optional_ _[__List_ _]__,__optional_) – List of tools. (default: None)

  * **tool_choice** (_Optional_ _[__Union_ _[__str_ _,__dict_ _]__]__,__optional_) – Tool choice parameters. (default: None)

  * **logprobs** (_Optional_ _[__bool_ _]__,__optional_) – Whether to return log probabilities of the output tokens. (default: None)

  * **top_logprobs** (_Optional_ _[__int_ _]__,__optional_) – Number of most likely tokens to return at each token position. (default: None)

  * **deployment_id** (_Optional_ _[__str_ _]__,__optional_) – Deployment ID. (default: None)

  * **extra_headers** (_Optional_ _[__dict_ _]__,__optional_) – Additional headers for the request. (default: None)

  * **api_version** (_Optional_ _[__str_ _]__,__optional_) – API version. (default: None)

  * **mock_response** (_Optional_ _[__str_ _]__,__optional_) – Mock completion response for testing or debugging. (default: None)

  * **custom_llm_provider** (_Optional_ _[__str_ _]__,__optional_) – Non-OpenAI LLM provider. (default: None)

  * **max_retries** (_Optional_ _[__int_ _]__,__optional_) – Maximum number of retries. (default: None)

api_version _: str | None_#
    

custom_llm_provider _: str | None_#
    

deployment_id _: str | None_#
    

extra_headers _: dict | None_#
    

frequency_penalty _: float | None_#
    

logit_bias _: dict | None_#
    

logprobs _: bool | None_#
    

max_retries _: int | None_#
    

max_tokens _: int | None_#
    

mock_response _: str | None_#
    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'api_version':
FieldInfo(annotation=Union[str, NoneType], required=False, default=None),
'custom_llm_provider': FieldInfo(annotation=Union[str, NoneType],
required=False, default=None), 'deployment_id':
FieldInfo(annotation=Union[str, NoneType], required=False, default=None),
'extra_headers': FieldInfo(annotation=Union[dict, NoneType], required=False,
default=None), 'frequency_penalty': FieldInfo(annotation=Union[float,
NoneType], required=False, default=None), 'logit_bias':
FieldInfo(annotation=Union[dict, NoneType], required=False, default=None),
'logprobs': FieldInfo(annotation=Union[bool, NoneType], required=False,
default=None), 'max_retries': FieldInfo(annotation=Union[int, NoneType],
required=False, default=None), 'max_tokens': FieldInfo(annotation=Union[int,
NoneType], required=False, default=None), 'mock_response':
FieldInfo(annotation=Union[str, NoneType], required=False, default=None), 'n':
FieldInfo(annotation=Union[int, NoneType], required=False, default=None),
'presence_penalty': FieldInfo(annotation=Union[float, NoneType],
required=False, default=None), 'response_format':
FieldInfo(annotation=Union[dict, NoneType], required=False, default=None),
'seed': FieldInfo(annotation=Union[int, NoneType], required=False,
default=None), 'stop': FieldInfo(annotation=Union[str, List[str], NoneType],
required=False, default=None), 'stream': FieldInfo(annotation=Union[bool,
NoneType], required=False, default=None), 'stream_options':
FieldInfo(annotation=Union[dict, NoneType], required=False, default=None),
'temperature': FieldInfo(annotation=Union[float, NoneType], required=False,
default=None), 'timeout': FieldInfo(annotation=Union[float, str, NoneType],
required=False, default=None), 'tool_choice': FieldInfo(annotation=Union[str,
dict, NoneType], required=False, default=None), 'tools':
FieldInfo(annotation=Union[List[Any], NoneType], required=False,
default=None), 'top_logprobs': FieldInfo(annotation=Union[int, NoneType],
required=False, default=None), 'top_p': FieldInfo(annotation=Union[float,
NoneType], required=False, default=None), 'user':
FieldInfo(annotation=Union[str, NoneType], required=False, default=None)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

n _: int | None_#
    

presence_penalty _: float | None_#
    

response_format _: dict | None_#
    

seed _: int | None_#
    

stop _: str | List[str] | None_#
    

stream _: bool | None_#
    

stream_options _: dict | None_#
    

temperature _: float | None_#
    

timeout _: float | str | None_#
    

tool_choice _: str | dict | None_#
    

top_logprobs _: int | None_#
    

top_p _: float | None_#
    

user _: str | None_#
    

_class _camel.configs.MistralConfig(_*_ , _tools : List[Any] | None = None_, _temperature : float | None = None_, _top_p : float | None = None_, _max_tokens : int | None = None_, _min_tokens : int | None = None_, _stop : str | list[str] | None = None_, _random_seed : int | None = None_, _safe_prompt : bool = False_, _response_format : Dict[str, str] | Any | None = None_, _tool_choice : str | None = 'auto'_)[[source]](_modules/camel/configs/mistral_config.html#MistralConfig)#
    

Bases: `BaseConfig`

Defines the parameters for generating chat completions using the Mistral API.

reference: [mistralai/client-python](https://github.com/mistralai/client-
python/blob/9d238f88c41689821d7b08570f13b43426f97fd6/src/mistralai/client.py#L195)

#TODO: Support stream mode

Parameters:

    

  * **temperature** (_Optional_ _[__float_ _]__,__optional_) – temperature the temperature to use for sampling, e.g. 0.5.

  * **top_p** (_Optional_ _[__float_ _]__,__optional_) – the cumulative probability of tokens to generate, e.g. 0.9. Defaults to None.

  * **max_tokens** (_Optional_ _[__int_ _]__,__optional_) – the maximum number of tokens to generate, e.g. 100. Defaults to None.

  * **min_tokens** (_Optional_ _[__int_ _]__,__optional_) – the minimum number of tokens to generate, e.g. 100. Defaults to None.

  * **stop** (_Optional_ _[__Union_ _[__str_ _,__list_ _[__str_ _]__]__]_) – Stop generation if this token is detected. Or if one of these tokens is detected when providing a string list.

  * **random_seed** (_Optional_ _[__int_ _]__,__optional_) – the random seed to use for sampling, e.g. 42. Defaults to None.

  * **safe_prompt** (_bool_ _,__optional_) – whether to use safe prompt, e.g. true. Defaults to False.

  * **response_format** (_Union_ _[__Dict_ _[__str_ _,__str_ _]__,__ResponseFormat_) – format of the response.

  * **tool_choice** (_str_ _,__optional_) – Controls which (if any) tool is called by the model. `"none"` means the model will not call any tool and instead generates a message. `"auto"` means the model can pick between generating a message or calling one or more tools. `"any"` means the model must call one or more tools. `"auto"` is the default value.

_classmethod
_fields_type_checking(_response_format_)[[source]](_modules/camel/configs/mistral_config.html#MistralConfig.fields_type_checking)#

    

max_tokens _: int | None_#
    

min_tokens _: int | None_#
    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'max_tokens':
FieldInfo(annotation=Union[int, NoneType], required=False, default=None),
'min_tokens': FieldInfo(annotation=Union[int, NoneType], required=False,
default=None), 'random_seed': FieldInfo(annotation=Union[int, NoneType],
required=False, default=None), 'response_format':
FieldInfo(annotation=Union[Dict[str, str], Any, NoneType], required=False,
default=None), 'safe_prompt': FieldInfo(annotation=bool, required=False,
default=False), 'stop': FieldInfo(annotation=Union[str, list[str], NoneType],
required=False, default=None), 'temperature':
FieldInfo(annotation=Union[float, NoneType], required=False, default=None),
'tool_choice': FieldInfo(annotation=Union[str, NoneType], required=False,
default='auto'), 'tools': FieldInfo(annotation=Union[List[Any], NoneType],
required=False, default=None), 'top_p': FieldInfo(annotation=Union[float,
NoneType], required=False, default=None)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

random_seed _: int | None_#
    

response_format _: Dict[str, str] | Any | None_#
    

safe_prompt _: bool_#

    

stop _: str | list[str] | None_#
    

temperature _: float | None_#
    

tool_choice _: str | None_#
    

top_p _: float | None_#
    

_class _camel.configs.OllamaConfig(_*_ , _tools : List[Any] | None = None_, _temperature : float = 0.2_, _top_p : float = 1.0_, _stream : bool = False_, _stop : str | Sequence[str] | NotGiven = NOT_GIVEN_, _max_tokens : int | NotGiven = NOT_GIVEN_, _presence_penalty : float = 0.0_, _response_format : dict | NotGiven = NOT_GIVEN_, _frequency_penalty : float = 0.0_)[[source]](_modules/camel/configs/ollama_config.html#OllamaConfig)#
    

Bases: `BaseConfig`

Defines the parameters for generating chat completions using OpenAI
compatibility

Reference:
[ollama/ollama](https://github.com/ollama/ollama/blob/main/docs/openai.md)

Parameters:

    

  * **temperature** (_float_ _,__optional_) – Sampling temperature to use, between `0` and `2`. Higher values make the output more random, while lower values make it more focused and deterministic. (default: `0.2`)

  * **top_p** (_float_ _,__optional_) – An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So `0.1` means only the tokens comprising the top 10% probability mass are considered. (default: `1.0`)

  * **response_format** (_object_ _,__optional_) – An object specifying the format that the model must output. Compatible with GPT-4 Turbo and all GPT-3.5 Turbo models newer than gpt-3.5-turbo-1106. Setting to {“type”: “json_object”} enables JSON mode, which guarantees the message the model generates is valid JSON. Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if finish_reason=”length”, which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.

  * **stream** (_bool_ _,__optional_) – If True, partial message deltas will be sent as data-only server-sent events as they become available. (default: `False`)

  * **stop** (_str_ _or_ _list_ _,__optional_) – Up to `4` sequences where the API will stop generating further tokens. (default: `None`)

  * **max_tokens** (_int_ _,__optional_) – The maximum number of tokens to generate in the chat completion. The total length of input tokens and generated tokens is limited by the model’s context length. (default: `None`)

  * **presence_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model’s likelihood to talk about new topics. See more information about frequency and presence penalties. (default: `0.0`)

  * **frequency_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model’s likelihood to repeat the same line verbatim. See more information about frequency and presence penalties. (default: `0.0`)

frequency_penalty _: float_#

    

max_tokens _: int | NotGiven_#
    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'frequency_penalty':
FieldInfo(annotation=float, required=False, default=0.0), 'max_tokens':
FieldInfo(annotation=Union[int, NotGiven], required=False, default=NOT_GIVEN),
'presence_penalty': FieldInfo(annotation=float, required=False, default=0.0),
'response_format': FieldInfo(annotation=Union[dict, NotGiven], required=False,
default=NOT_GIVEN), 'stop': FieldInfo(annotation=Union[str, Sequence[str],
NotGiven], required=False, default=NOT_GIVEN), 'stream':
FieldInfo(annotation=bool, required=False, default=False), 'temperature':
FieldInfo(annotation=float, required=False, default=0.2), 'tools':
FieldInfo(annotation=Union[List[Any], NoneType], required=False,
default=None), 'top_p': FieldInfo(annotation=float, required=False,
default=1.0)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

presence_penalty _: float_#

    

response_format _: dict | NotGiven_#
    

stop _: str | Sequence[str] | NotGiven_#
    

stream _: bool_#

    

temperature _: float_#

    

top_p _: float_#

    

_class _camel.configs.OpenSourceConfig(_*_ , _tools : List[Any] | None = None_, _model_path : str_, _server_url : str_, _api_params : ChatGPTConfig = None_)[[source]](_modules/camel/configs/openai_config.html#OpenSourceConfig)#
    

Bases: `BaseConfig`

Defines parameters for setting up open-source models and includes parameters
to be passed to chat completion function of OpenAI API.

Parameters:

    

  * **model_path** (_str_) – The path to a local folder containing the model files or the model card in HuggingFace hub.

  * **server_url** (_str_) – The URL to the server running the model inference which will be used as the API base of OpenAI API.

  * **api_params** (_ChatGPTConfig_) – An instance of :obj:ChatGPTConfig to contain the arguments to be passed to OpenAI API.

api_params _: ChatGPTConfig_#

    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'api_params':
FieldInfo(annotation=ChatGPTConfig, required=False,
default_factory=ChatGPTConfig), 'model_path': FieldInfo(annotation=str,
required=True), 'server_url': FieldInfo(annotation=str, required=True),
'tools': FieldInfo(annotation=Union[List[Any], NoneType], required=False,
default=None)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

model_path _: str_#

    

server_url _: str_#

    

_class _camel.configs.RekaConfig(_*_ , _tools : List[Any] | None = None_, _temperature : float | None = None_, _top_p : float | None = None_, _top_k : int | None = None_, _max_tokens : int | None = None_, _stop : str | list[str] | None = None_, _seed : int | None = None_, _frequency_penalty : float = 0.0_, _presence_penalty : float = 0.0_, _use_search_engine : bool | None = False_)[[source]](_modules/camel/configs/reka_config.html#RekaConfig)#
    

Bases: `BaseConfig`

Defines the parameters for generating chat completions using the Reka API.

Reference: <https://docs.reka.ai/api-reference/chat/create>

Parameters:

    

  * **temperature** (_Optional_ _[__float_ _]__,__optional_) – temperature the temperature to use for sampling, e.g. 0.5.

  * **top_p** (_Optional_ _[__float_ _]__,__optional_) – the cumulative probability of tokens to generate, e.g. 0.9. Defaults to None.

  * **top_k** (_Optional_ _[__int_ _]__,__optional_) – Parameter which forces the model to only consider the tokens with the top_k highest probabilities at the next step. Defaults to 1024.

  * **max_tokens** (_Optional_ _[__int_ _]__,__optional_) – the maximum number of tokens to generate, e.g. 100. Defaults to None.

  * **stop** (_Optional_ _[__Union_ _[__str_ _,__list_ _[__str_ _]__]__]_) – Stop generation if this token is detected. Or if one of these tokens is detected when providing a string list.

  * **seed** (_Optional_ _[__int_ _]__,__optional_) – the random seed to use for sampling, e. g. 42. Defaults to None.

  * **presence_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model’s likelihood to talk about new topics. See more information about frequency and presence penalties. (default: `0.0`)

  * **frequency_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model’s likelihood to repeat the same line verbatim. See more information about frequency and presence penalties. (default: `0.0`)

  * **use_search_engine** (_Optional_ _[__bool_ _]_) – Whether to consider using search engine to complete the request. Note that even if this is set to True, the model might decide to not use search.

as_dict() -> dict[str,
Any][[source]](_modules/camel/configs/reka_config.html#RekaConfig.as_dict)#

    

frequency_penalty _: float_#

    

max_tokens _: int | None_#
    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'frequency_penalty':
FieldInfo(annotation=float, required=False, default=0.0), 'max_tokens':
FieldInfo(annotation=Union[int, NoneType], required=False, default=None),
'presence_penalty': FieldInfo(annotation=float, required=False, default=0.0),
'seed': FieldInfo(annotation=Union[int, NoneType], required=False,
default=None), 'stop': FieldInfo(annotation=Union[str, list[str], NoneType],
required=False, default=None), 'temperature':
FieldInfo(annotation=Union[float, NoneType], required=False, default=None),
'tools': FieldInfo(annotation=Union[List[Any], NoneType], required=False,
default=None), 'top_k': FieldInfo(annotation=Union[int, NoneType],
required=False, default=None), 'top_p': FieldInfo(annotation=Union[float,
NoneType], required=False, default=None), 'use_search_engine':
FieldInfo(annotation=Union[bool, NoneType], required=False, default=False)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

presence_penalty _: float_#

    

seed _: int | None_#
    

stop _: str | list[str] | None_#
    

temperature _: float | None_#
    

top_k _: int | None_#
    

top_p _: float | None_#
    

use_search_engine _: bool | None_#
    

_class _camel.configs.SambaCloudAPIConfig(_*_ , _tools : List[Any] | None = None_, _temperature : float = 0.2_, _top_p : float = 1.0_, _n : int = 1_, _stream : bool = False_, _stop : str | Sequence[str] | NotGiven = NOT_GIVEN_, _max_tokens : int | NotGiven = NOT_GIVEN_, _presence_penalty : float = 0.0_, _response_format : dict | NotGiven = NOT_GIVEN_, _frequency_penalty : float = 0.0_, _logit_bias : dict = None_, _user : str = ''_, _tool_choice : dict[str, str] | str | None = None_)[[source]](_modules/camel/configs/samba_config.html#SambaCloudAPIConfig)#
    

Bases: `BaseConfig`

Defines the parameters for generating chat completions using the OpenAI API.

Parameters:

    

  * **temperature** (_float_ _,__optional_) – Sampling temperature to use, between `0` and `2`. Higher values make the output more random, while lower values make it more focused and deterministic. (default: `0.2`)

  * **top_p** (_float_ _,__optional_) – An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So `0.1` means only the tokens comprising the top 10% probability mass are considered. (default: `1.0`)

  * **n** (_int_ _,__optional_) – How many chat completion choices to generate for each input message. (default: `1`)

  * **response_format** (_object_ _,__optional_) – An object specifying the format that the model must output. Compatible with GPT-4 Turbo and all GPT-3.5 Turbo models newer than gpt-3.5-turbo-1106. Setting to {“type”: “json_object”} enables JSON mode, which guarantees the message the model generates is valid JSON. Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if finish_reason=”length”, which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.

  * **stream** (_bool_ _,__optional_) – If True, partial message deltas will be sent as data-only server-sent events as they become available. (default: `False`)

  * **stop** (_str_ _or_ _list_ _,__optional_) – Up to `4` sequences where the API will stop generating further tokens. (default: `None`)

  * **max_tokens** (_int_ _,__optional_) – The maximum number of tokens to generate in the chat completion. The total length of input tokens and generated tokens is limited by the model’s context length. (default: `None`)

  * **presence_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model’s likelihood to talk about new topics. See more information about frequency and presence penalties. (default: `0.0`)

  * **frequency_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model’s likelihood to repeat the same line verbatim. See more information about frequency and presence penalties. (default: `0.0`)

  * **logit_bias** (_dict_ _,__optional_) – Modify the likelihood of specified tokens appearing in the completion. Accepts a json object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from `-100` to `100`. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between:obj:` -1` and `1` should decrease or increase likelihood of selection; values like `-100` or `100` should result in a ban or exclusive selection of the relevant token. (default: `{}`)

  * **user** (_str_ _,__optional_) – A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. (default: `""`)

  * **tools** (_list_ _[__OpenAIFunction_ _]__,__optional_) – A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

  * **tool_choice** (_Union_ _[__dict_ _[__str_ _,__str_ _]__,__str_ _]__,__optional_) – Controls which (if any) tool is called by the model. `"none"` means the model will not call any tool and instead generates a message. `"auto"` means the model can pick between generating a message or calling one or more tools. `"required"` means the model must call one or more tools. Specifying a particular tool via {“type”: “function”, “function”: {“name”: “my_function”}} forces the model to call that tool. `"none"` is the default when no tools are present. `"auto"` is the default if tools are present.

frequency_penalty _: float_#

    

logit_bias _: dict_#

    

max_tokens _: int | NotGiven_#
    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'frequency_penalty':
FieldInfo(annotation=float, required=False, default=0.0), 'logit_bias':
FieldInfo(annotation=dict, required=False, default_factory=dict),
'max_tokens': FieldInfo(annotation=Union[int, NotGiven], required=False,
default=NOT_GIVEN), 'n': FieldInfo(annotation=int, required=False, default=1),
'presence_penalty': FieldInfo(annotation=float, required=False, default=0.0),
'response_format': FieldInfo(annotation=Union[dict, NotGiven], required=False,
default=NOT_GIVEN), 'stop': FieldInfo(annotation=Union[str, Sequence[str],
NotGiven], required=False, default=NOT_GIVEN), 'stream':
FieldInfo(annotation=bool, required=False, default=False), 'temperature':
FieldInfo(annotation=float, required=False, default=0.2), 'tool_choice':
FieldInfo(annotation=Union[dict[str, str], str, NoneType], required=False,
default=None), 'tools': FieldInfo(annotation=Union[List[Any], NoneType],
required=False, default=None), 'top_p': FieldInfo(annotation=float,
required=False, default=1.0), 'user': FieldInfo(annotation=str,
required=False, default='')}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

n _: int_#

    

presence_penalty _: float_#

    

response_format _: dict | NotGiven_#
    

stop _: str | Sequence[str] | NotGiven_#
    

stream _: bool_#

    

temperature _: float_#

    

tool_choice _: dict[str, str] | str | None_#
    

top_p _: float_#

    

user _: str_#

    

_class _camel.configs.SambaFastAPIConfig(_*_ , _tools : List[Any] | None = None_, _max_tokens : int | None = 2048_, _stop : str | list[str] | None = None_, _stream : bool | None = True_, _stream_options : Dict | None = {'include_usage': True}_)[[source]](_modules/camel/configs/samba_config.html#SambaFastAPIConfig)#
    

Bases: `BaseConfig`

Defines the parameters for generating chat completions using the SambaNova
Fast API.

Parameters:

    

  * **max_tokens** (_Optional_ _[__int_ _]__,__optional_) – the maximum number of tokens to generate, e.g. 100. (default: `2048`)

  * **stop** (_Optional_ _[__Union_ _[__str_ _,__list_ _[__str_ _]__]__]_) – Stop generation if this token is detected. Or if one of these tokens is detected when providing a string list. (default: `None`)

  * **stream** (_Optional_ _[__bool_ _]_) – If True, partial message deltas will be sent as data-only server-sent events as they become available. Currently SambaNova Fast API only support stream mode. (default: `True`)

  * **stream_options** (_Optional_ _[__Dict_ _]_) – Additional options for streaming. (default: `{"include_usage": True}`)

as_dict() -> dict[str,
Any][[source]](_modules/camel/configs/samba_config.html#SambaFastAPIConfig.as_dict)#

    

max_tokens _: int | None_#
    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'max_tokens':
FieldInfo(annotation=Union[int, NoneType], required=False, default=2048),
'stop': FieldInfo(annotation=Union[str, list[str], NoneType], required=False,
default=None), 'stream': FieldInfo(annotation=Union[bool, NoneType],
required=False, default=True), 'stream_options':
FieldInfo(annotation=Union[Dict, NoneType], required=False,
default={'include_usage': True}), 'tools':
FieldInfo(annotation=Union[List[Any], NoneType], required=False,
default=None)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

stop _: str | list[str] | None_#
    

stream _: bool | None_#
    

stream_options _: Dict | None_#
    

_class _camel.configs.SambaVerseAPIConfig(_*_ , _tools : List[Any] | None = None_, _temperature : float | None = 0.7_, _top_p : float | None = 0.95_, _top_k : int | None = 50_, _max_tokens : int | None = 2048_, _repetition_penalty : float | None = 1.0_, _stop : str | list[str] | None = ''_, _stream : bool | None = False_)[[source]](_modules/camel/configs/samba_config.html#SambaVerseAPIConfig)#
    

Bases: `BaseConfig`

Defines the parameters for generating chat completions using the SambaVerse
API.

Parameters:

    

  * **temperature** (_float_ _,__optional_) – Sampling temperature to use, between `0` and `2`. Higher values make the output more random, while lower values make it more focused and deterministic. (default: `0.7`)

  * **top_p** (_float_ _,__optional_) – An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So `0.1` means only the tokens comprising the top 10% probability mass are considered. (default: `0.95`)

  * **top_k** (_int_ _,__optional_) – Only sample from the top K options for each subsequent token. Used to remove “long tail” low probability responses. (default: `50`)

  * **max_tokens** (_Optional_ _[__int_ _]__,__optional_) – The maximum number of tokens to generate, e.g. 100. (default: `2048`)

  * **repetition_penalty** (_Optional_ _[__float_ _]__,__optional_) – The parameter for repetition penalty. 1.0 means no penalty. (default: `1.0`)

  * **stop** (_Optional_ _[__Union_ _[__str_ _,__list_ _[__str_ _]__]__]_) – Stop generation if this token is detected. Or if one of these tokens is detected when providing a string list. (default: `""`)

  * **stream** (_Optional_ _[__bool_ _]_) – If True, partial message deltas will be sent as data-only server-sent events as they become available. Currently SambaVerse API doesn’t support stream mode. (default: `False`)

as_dict() -> dict[str,
Any][[source]](_modules/camel/configs/samba_config.html#SambaVerseAPIConfig.as_dict)#

    

max_tokens _: int | None_#
    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'max_tokens':
FieldInfo(annotation=Union[int, NoneType], required=False, default=2048),
'repetition_penalty': FieldInfo(annotation=Union[float, NoneType],
required=False, default=1.0), 'stop': FieldInfo(annotation=Union[str,
list[str], NoneType], required=False, default=''), 'stream':
FieldInfo(annotation=Union[bool, NoneType], required=False, default=False),
'temperature': FieldInfo(annotation=Union[float, NoneType], required=False,
default=0.7), 'tools': FieldInfo(annotation=Union[List[Any], NoneType],
required=False, default=None), 'top_k': FieldInfo(annotation=Union[int,
NoneType], required=False, default=50), 'top_p':
FieldInfo(annotation=Union[float, NoneType], required=False, default=0.95)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

repetition_penalty _: float | None_#
    

stop _: str | list[str] | None_#
    

stream _: bool | None_#
    

temperature _: float | None_#
    

top_k _: int | None_#
    

top_p _: float | None_#
    

_class _camel.configs.TogetherAIConfig(_*_ , _tools : List[Any] | None = None_, _temperature : float = 0.2_, _top_p : float = 1.0_, _n : int = 1_, _stream : bool = False_, _stop : str | Sequence[str] | NotGiven = NOT_GIVEN_, _max_tokens : int | NotGiven = NOT_GIVEN_, _presence_penalty : float = 0.0_, _response_format : dict | NotGiven = NOT_GIVEN_, _frequency_penalty : float = 0.0_, _logit_bias : dict = None_, _user : str = ''_)[[source]](_modules/camel/configs/togetherai_config.html#TogetherAIConfig)#
    

Bases: `BaseConfig`

Defines the parameters for generating chat completions using the OpenAI API.

Parameters:

    

  * **temperature** (_float_ _,__optional_) – Sampling temperature to use, between `0` and `2`. Higher values make the output more random, while lower values make it more focused and deterministic. (default: `0.2`)

  * **top_p** (_float_ _,__optional_) – An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So `0.1` means only the tokens comprising the top 10% probability mass are considered. (default: `1.0`)

  * **n** (_int_ _,__optional_) – How many chat completion choices to generate for each input message. (default: `1`)

  * **response_format** (_object_ _,__optional_) – An object specifying the format that the model must output. Compatible with GPT-4 Turbo and all GPT-3.5 Turbo models newer than gpt-3.5-turbo-1106. Setting to {“type”: “json_object”} enables JSON mode, which guarantees the message the model generates is valid JSON. Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if finish_reason=”length”, which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.

  * **stream** (_bool_ _,__optional_) – If True, partial message deltas will be sent as data-only server-sent events as they become available. (default: `False`)

  * **stop** (_str_ _or_ _list_ _,__optional_) – Up to `4` sequences where the API will stop generating further tokens. (default: `None`)

  * **max_tokens** (_int_ _,__optional_) – The maximum number of tokens to generate in the chat completion. The total length of input tokens and generated tokens is limited by the model’s context length. (default: `None`)

  * **presence_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model’s likelihood to talk about new topics. See more information about frequency and presence penalties. (default: `0.0`)

  * **frequency_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model’s likelihood to repeat the same line verbatim. See more information about frequency and presence penalties. (default: `0.0`)

  * **logit_bias** (_dict_ _,__optional_) – Modify the likelihood of specified tokens appearing in the completion. Accepts a json object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from `-100` to `100`. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between:obj:` -1` and `1` should decrease or increase likelihood of selection; values like `-100` or `100` should result in a ban or exclusive selection of the relevant token. (default: `{}`)

  * **user** (_str_ _,__optional_) – A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. (default: `""`)

as_dict() -> dict[str,
Any][[source]](_modules/camel/configs/togetherai_config.html#TogetherAIConfig.as_dict)#

    

frequency_penalty _: float_#

    

logit_bias _: dict_#

    

max_tokens _: int | NotGiven_#
    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'frequency_penalty':
FieldInfo(annotation=float, required=False, default=0.0), 'logit_bias':
FieldInfo(annotation=dict, required=False, default_factory=dict),
'max_tokens': FieldInfo(annotation=Union[int, NotGiven], required=False,
default=NOT_GIVEN), 'n': FieldInfo(annotation=int, required=False, default=1),
'presence_penalty': FieldInfo(annotation=float, required=False, default=0.0),
'response_format': FieldInfo(annotation=Union[dict, NotGiven], required=False,
default=NOT_GIVEN), 'stop': FieldInfo(annotation=Union[str, Sequence[str],
NotGiven], required=False, default=NOT_GIVEN), 'stream':
FieldInfo(annotation=bool, required=False, default=False), 'temperature':
FieldInfo(annotation=float, required=False, default=0.2), 'tools':
FieldInfo(annotation=Union[List[Any], NoneType], required=False,
default=None), 'top_p': FieldInfo(annotation=float, required=False,
default=1.0), 'user': FieldInfo(annotation=str, required=False, default='')}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

n _: int_#

    

presence_penalty _: float_#

    

response_format _: dict | NotGiven_#
    

stop _: str | Sequence[str] | NotGiven_#
    

stream _: bool_#

    

temperature _: float_#

    

top_p _: float_#

    

user _: str_#

    

_class _camel.configs.VLLMConfig(_*_ , _tools : List[Any] | None = None_, _temperature : float = 0.2_, _top_p : float = 1.0_, _n : int = 1_, _stream : bool = False_, _stop : str | Sequence[str] | NotGiven = NOT_GIVEN_, _max_tokens : int | NotGiven = NOT_GIVEN_, _presence_penalty : float = 0.0_, _response_format : dict | NotGiven = NOT_GIVEN_, _frequency_penalty : float = 0.0_, _logit_bias : dict = None_, _user : str = ''_)[[source]](_modules/camel/configs/vllm_config.html#VLLMConfig)#
    

Bases: `BaseConfig`

Defines the parameters for generating chat completions using the OpenAI API.

Reference:
<https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html>

Parameters:

    

  * **temperature** (_float_ _,__optional_) – Sampling temperature to use, between `0` and `2`. Higher values make the output more random, while lower values make it more focused and deterministic. (default: `0.2`)

  * **top_p** (_float_ _,__optional_) – An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So `0.1` means only the tokens comprising the top 10% probability mass are considered. (default: `1.0`)

  * **n** (_int_ _,__optional_) – How many chat completion choices to generate for each input message. (default: `1`)

  * **response_format** (_object_ _,__optional_) – An object specifying the format that the model must output. Compatible with GPT-4 Turbo and all GPT-3.5 Turbo models newer than gpt-3.5-turbo-1106. Setting to {“type”: “json_object”} enables JSON mode, which guarantees the message the model generates is valid JSON. Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if finish_reason=”length”, which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.

  * **stream** (_bool_ _,__optional_) – If True, partial message deltas will be sent as data-only server-sent events as they become available. (default: `False`)

  * **stop** (_str_ _or_ _list_ _,__optional_) – Up to `4` sequences where the API will stop generating further tokens. (default: `None`)

  * **max_tokens** (_int_ _,__optional_) – The maximum number of tokens to generate in the chat completion. The total length of input tokens and generated tokens is limited by the model’s context length. (default: `None`)

  * **presence_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model’s likelihood to talk about new topics. See more information about frequency and presence penalties. (default: `0.0`)

  * **frequency_penalty** (_float_ _,__optional_) – Number between `-2.0` and `2.0`. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model’s likelihood to repeat the same line verbatim. See more information about frequency and presence penalties. (default: `0.0`)

  * **logit_bias** (_dict_ _,__optional_) – Modify the likelihood of specified tokens appearing in the completion. Accepts a json object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from `-100` to `100`. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between:obj:` -1` and `1` should decrease or increase likelihood of selection; values like `-100` or `100` should result in a ban or exclusive selection of the relevant token. (default: `{}`)

  * **user** (_str_ _,__optional_) – A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. (default: `""`)

frequency_penalty _: float_#

    

logit_bias _: dict_#

    

max_tokens _: int | NotGiven_#
    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'frequency_penalty':
FieldInfo(annotation=float, required=False, default=0.0), 'logit_bias':
FieldInfo(annotation=dict, required=False, default_factory=dict),
'max_tokens': FieldInfo(annotation=Union[int, NotGiven], required=False,
default=NOT_GIVEN), 'n': FieldInfo(annotation=int, required=False, default=1),
'presence_penalty': FieldInfo(annotation=float, required=False, default=0.0),
'response_format': FieldInfo(annotation=Union[dict, NotGiven], required=False,
default=NOT_GIVEN), 'stop': FieldInfo(annotation=Union[str, Sequence[str],
NotGiven], required=False, default=NOT_GIVEN), 'stream':
FieldInfo(annotation=bool, required=False, default=False), 'temperature':
FieldInfo(annotation=float, required=False, default=0.2), 'tools':
FieldInfo(annotation=Union[List[Any], NoneType], required=False,
default=None), 'top_p': FieldInfo(annotation=float, required=False,
default=1.0), 'user': FieldInfo(annotation=str, required=False, default='')}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

n _: int_#

    

presence_penalty _: float_#

    

response_format _: dict | NotGiven_#
    

stop _: str | Sequence[str] | NotGiven_#
    

stream _: bool_#

    

temperature _: float_#

    

top_p _: float_#

    

user _: str_#

    

_class _camel.configs.ZhipuAIConfig(_*_ , _tools : List[Any] | None = None_, _temperature : float = 0.2_, _top_p : float = 0.6_, _stream : bool = False_, _stop : str | Sequence[str] | NotGiven = NOT_GIVEN_, _max_tokens : int | NotGiven = NOT_GIVEN_, _tool_choice : dict[str, str] | str | None = None_)[[source]](_modules/camel/configs/zhipuai_config.html#ZhipuAIConfig)#
    

Bases: `BaseConfig`

Defines the parameters for generating chat completions using OpenAI
compatibility

Reference: <https://open.bigmodel.cn/dev/api#glm-4v>

Parameters:

    

  * **temperature** (_float_ _,__optional_) – Sampling temperature to use, between `0` and `2`. Higher values make the output more random, while lower values make it more focused and deterministic. (default: `0.2`)

  * **top_p** (_float_ _,__optional_) – An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So `0.1` means only the tokens comprising the top 10% probability mass are considered. (default: `0.6`)

  * **stream** (_bool_ _,__optional_) – If True, partial message deltas will be sent as data-only server-sent events as they become available. (default: `False`)

  * **stop** (_str_ _or_ _list_ _,__optional_) – Up to `4` sequences where the API will stop generating further tokens. (default: `None`)

  * **max_tokens** (_int_ _,__optional_) – The maximum number of tokens to generate in the chat completion. The total length of input tokens and generated tokens is limited by the model’s context length. (default: `None`)

  * **tools** (_list_ _[__OpenAIFunction_ _]__,__optional_) – A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

  * **tool_choice** (_Union_ _[__dict_ _[__str_ _,__str_ _]__,__str_ _]__,__optional_) – Controls which (if any) tool is called by the model. `"none"` means the model will not call any tool and instead generates a message. `"auto"` means the model can pick between generating a message or calling one or more tools. `"required"` means the model must call one or more tools. Specifying a particular tool via {“type”: “function”, “function”: {“name”: “my_function”}} forces the model to call that tool. `"none"` is the default when no tools are present. `"auto"` is the default if tools are present.

max_tokens _: int | NotGiven_#
    

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'arbitrary_types_allowed': True,
'extra': 'forbid', 'frozen': True, 'protected_namespaces': ()}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'max_tokens':
FieldInfo(annotation=Union[int, NotGiven], required=False, default=NOT_GIVEN),
'stop': FieldInfo(annotation=Union[str, Sequence[str], NotGiven],
required=False, default=NOT_GIVEN), 'stream': FieldInfo(annotation=bool,
required=False, default=False), 'temperature': FieldInfo(annotation=float,
required=False, default=0.2), 'tool_choice':
FieldInfo(annotation=Union[dict[str, str], str, NoneType], required=False,
default=None), 'tools': FieldInfo(annotation=Union[List[Any], NoneType],
required=False, default=None), 'top_p': FieldInfo(annotation=float,
required=False, default=0.6)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

stop _: str | Sequence[str] | NotGiven_#
    

stream _: bool_#

    

temperature _: float_#

    

tool_choice _: dict[str, str] | str | None_#
    

top_p _: float_#

    

## camel.generators module#

_class _camel.generators.AISocietyTaskPromptGenerator(_num_tasks : int =
10_)[[source]](_modules/camel/generators.html#AISocietyTaskPromptGenerator)#

    

Bases: `object`

from_role_files(_assistant_role_names_path : str =
'data/ai_society/assistant_roles.txt'_, _user_role_names_path : str =
'data/ai_society/user_roles.txt'_) -> Generator[Tuple[str, Tuple[str, str]],
None,
None][[source]](_modules/camel/generators.html#AISocietyTaskPromptGenerator.from_role_files)#

    

from_role_generator(_role_generator : Generator[Tuple, None, None]_) ->
Generator[Tuple[str, Tuple[str, str]], None,
None][[source]](_modules/camel/generators.html#AISocietyTaskPromptGenerator.from_role_generator)#

    

_class _camel.generators.CodeTaskPromptGenerator(_num_tasks : int =
50_)[[source]](_modules/camel/generators.html#CodeTaskPromptGenerator)#

    

Bases: `object`

from_role_files(_languages_path : str = 'data/code/languages.txt'_,
_domains_path : str = 'data/code/domains.txt'_) ->
Generator[Tuple[[TextPrompt](camel.prompts.html#camel.prompts.base.TextPrompt
"camel.prompts.base.TextPrompt"), str, str], None,
None][[source]](_modules/camel/generators.html#CodeTaskPromptGenerator.from_role_files)#

    

from_role_generator(_role_generator : Generator[Tuple, None, None]_) ->
Generator[str, None,
None][[source]](_modules/camel/generators.html#CodeTaskPromptGenerator.from_role_generator)#

    

_class _camel.generators.RoleNameGenerator(_assistant_role_names_path : str = 'data/ai_society/assistant_roles.txt'_, _user_role_names_path : str = 'data/ai_society/user_roles.txt'_, _assistant_role_names : List[str] | None = None_, _user_role_names : List[str] | None = None_)[[source]](_modules/camel/generators.html#RoleNameGenerator)#
    

Bases: `object`

from_role_files() -> Generator[Tuple, None,
None][[source]](_modules/camel/generators.html#RoleNameGenerator.from_role_files)#

    

_class _camel.generators.SingleTxtGenerator(_text_file_path :
str_)[[source]](_modules/camel/generators.html#SingleTxtGenerator)#

    

Bases: `object`

from_role_files() -> Generator[str, None,
None][[source]](_modules/camel/generators.html#SingleTxtGenerator.from_role_files)#

    

_class _camel.generators.SystemMessageGenerator(_task_type : TaskType = TaskType.AI_SOCIETY_, _sys_prompts : Dict[RoleType, str] | None = None_, _sys_msg_meta_dict_keys : Set[str] | None = None_)[[source]](_modules/camel/generators.html#SystemMessageGenerator)#
    

Bases: `object`

System message generator for agents.

Parameters:

    

  * **task_type** (_TaskType_ _,__optional_) – The task type. (default: `TaskType.AI_SOCIETY`)

  * **sys_prompts** (_Optional_ _[__Dict_ _[__RoleType_ _,__str_ _]__]__,__optional_) – The prompts of the system messages for each role type. (default: `None`)

  * **sys_msg_meta_dict_keys** (_Optional_ _[__Set_ _[__str_ _]__]__,__optional_) – The set of keys of the meta dictionary used to fill the prompts. (default: `None`)

from_dict(_meta_dict: ~typing.Dict[str, str], role_tuple: ~typing.Tuple[str,
~camel.types.enums.RoleType] = ('', <RoleType.DEFAULT: 'default'>)_) ->
[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")[[source]](_modules/camel/generators.html#SystemMessageGenerator.from_dict)#

    

Generates a system message from a dictionary.

Parameters:

    

  * **meta_dict** (_Dict_ _[__str_ _,__str_ _]_) – The dictionary containing the information to generate the system message.

  * **role_tuple** (_Tuple_ _[__str_ _,__RoleType_ _]__,__optional_) – The tuple containing the role name and role type. (default: (“”, RoleType.DEFAULT))

Returns:

    

The generated system message.

Return type:

    

[BaseMessage](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")

from_dicts(_meta_dicts : List[Dict[str, str]]_, _role_tuples : List[Tuple[str,
RoleType]]_) ->
List[[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")][[source]](_modules/camel/generators.html#SystemMessageGenerator.from_dicts)#

    

Generates a list of system messages from a list of dictionaries.

Parameters:

    

  * **meta_dicts** (_List_ _[__Dict_ _[__str_ _,__str_ _]__]_) – A list of dictionaries containing the information to generate the system messages.

  * **role_tuples** (_List_ _[__Tuple_ _[__str_ _,__RoleType_ _]__]_) – A list of tuples containing the role name and role type for each system message.

Returns:

    

A list of generated system messages.

Return type:

    

List[[BaseMessage](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")]

Raises:

    

**ValueError** – If the number of meta_dicts and role_tuples are different.

validate_meta_dict_keys(_meta_dict : Dict[str, str]_) ->
None[[source]](_modules/camel/generators.html#SystemMessageGenerator.validate_meta_dict_keys)#

    

Validates the keys of the meta_dict.

Parameters:

    

**meta_dict** (_Dict_ _[__str_ _,__str_ _]_) – The dictionary to validate.

## camel.human module#

_class _camel.human.Human(_name : str = 'Kill Switch Engineer'_, _logger_color
: Any = '\x1b[35m'_)[[source]](_modules/camel/human.html#Human)#

    

Bases: `object`

A class representing a human user.

Parameters:

    

  * **name** (_str_) – The name of the human user. (default: `"Kill Switch Engineer"`).

  * **logger_color** (_Any_) – The color of the menu options displayed to the user. (default: `Fore.MAGENTA`)

name#

    

The name of the human user.

Type:

    

str

logger_color#

    

The color of the menu options displayed to the user.

Type:

    

Any

input_button#

    

The text displayed for the input button.

Type:

    

str

kill_button#

    

The text displayed for the kill button.

Type:

    

str

options_dict#

    

A dictionary containing the options displayed to the user.

Type:

    

Dict[str, str]

display_options(_messages :
Sequence[[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")]_) ->
None[[source]](_modules/camel/human.html#Human.display_options)#

    

Displays the options to the user.

Parameters:

    

**messages** (_Sequence_
_[_[_BaseMessage_](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage") _]_) – A list of BaseMessage objects.

Returns:

    

None

get_input() -> str[[source]](_modules/camel/human.html#Human.get_input)#

    

Gets the input from the user.

Returns:

    

The user’s input.

Return type:

    

str

parse_input(_human_input : str_) ->
str[[source]](_modules/camel/human.html#Human.parse_input)#

    

Parses the user’s input and returns a BaseMessage object.

Parameters:

    

**human_input** (_str_) – The user’s input.

Returns:

    

A str object representing the user’s input.

Return type:

    

content

reduce_step(_messages :
Sequence[[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")]_) ->
ChatAgentResponse[[source]](_modules/camel/human.html#Human.reduce_step)#

    

Performs one step of the conversation by displaying options to the user,
getting their input, and parsing their choice.

Parameters:

    

**messages** (_Sequence_
_[_[_BaseMessage_](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage") _]_) – A list of BaseMessage objects.

Returns:

    

A ChatAgentResponse object representing the

    

user’s choice.

Return type:

    

ChatAgentResponse

## camel.messages module#

_class _camel.messages.BaseMessage(_role_name : str_, _role_type : RoleType_, _meta_dict : Dict[str, str] | None_, _content : str_, _video_bytes : bytes | None = None_, _image_list : List[Image] | None = None_, _image_detail : Literal['auto', 'low', 'high'] = 'auto'_, _video_detail : Literal['auto', 'low', 'high'] = 'low'_)[[source]](_modules/camel/messages/base.html#BaseMessage)#
    

Bases: `object`

Base class for message objects used in CAMEL chat system.

Parameters:

    

  * **role_name** (_str_) – The name of the user or assistant role.

  * **role_type** (_RoleType_) – The type of role, either `RoleType. ASSISTANT` or `RoleType.USER`.

  * **meta_dict** (_Optional_ _[__Dict_ _[__str_ _,__str_ _]__]_) – Additional metadata dictionary for the message.

  * **content** (_str_) – The content of the message.

  * **video_bytes** (_Optional_ _[__bytes_ _]_) – Optional bytes of a video associated with the message. Default is None.

  * **image_list** (_Optional_ _[__List_ _[__Image.Image_ _]__]_) – Optional list of PIL Image objects associated with the message. Default is None.

  * **image_detail** (_Literal_ _[__" auto"__,__" low"__,__" high"__]_) – Detail level of the images associated with the message. Default is “auto”.

  * **video_detail** (_Literal_ _[__" auto"__,__" low"__,__" high"__]_) – Detail level of the videos associated with the message. Default is “low”.

content _: str_#

    

create_new_instance(_content : str_) ->
[BaseMessage](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")[[source]](_modules/camel/messages/base.html#BaseMessage.create_new_instance)#

    

Create a new instance of the
[`BaseMessage`](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage") with updated content.

Parameters:

    

**content** (_str_) – The new content value.

Returns:

    

The new instance of
[`BaseMessage`](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage").

Return type:

    

[BaseMessage](camel.messages.html#camel.messages.BaseMessage
"camel.messages.BaseMessage")

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
    

_classmethod _make_assistant_message(_role_name : str_, _content : str_, _meta_dict : Dict[str, str] | None = None_, _video_bytes : bytes | None = None_, _image_list : List[Image] | None = None_, _image_detail : OpenAIVisionDetailType | str = OpenAIVisionDetailType.AUTO_, _video_detail : OpenAIVisionDetailType | str = OpenAIVisionDetailType.LOW_) -> [BaseMessage](camel.messages.html#camel.messages.base.BaseMessage "camel.messages.base.BaseMessage")[[source]](_modules/camel/messages/base.html#BaseMessage.make_assistant_message)#
    

_classmethod _make_user_message(_role_name : str_, _content : str_, _meta_dict : Dict[str, str] | None = None_, _video_bytes : bytes | None = None_, _image_list : List[Image] | None = None_, _image_detail : OpenAIVisionDetailType | str = OpenAIVisionDetailType.AUTO_, _video_detail : OpenAIVisionDetailType | str = OpenAIVisionDetailType.LOW_) -> [BaseMessage](camel.messages.html#camel.messages.base.BaseMessage "camel.messages.base.BaseMessage")[[source]](_modules/camel/messages/base.html#BaseMessage.make_user_message)#
    

meta_dict _: Dict[str, str] | None_#
    

role_name _: str_#

    

role_type _: RoleType_#

    

to_dict() ->
Dict[[source]](_modules/camel/messages/base.html#BaseMessage.to_dict)#

    

Converts the message to a dictionary.

Returns:

    

The converted dictionary.

Return type:

    

dict

to_openai_assistant_message() ->
ChatCompletionAssistantMessageParam[[source]](_modules/camel/messages/base.html#BaseMessage.to_openai_assistant_message)#

    

Converts the message to an
[`OpenAIAssistantMessage`](camel.messages.html#camel.messages.OpenAIAssistantMessage
"camel.messages.OpenAIAssistantMessage") object.

Returns:

    

The converted
[`OpenAIAssistantMessage`](camel.messages.html#camel.messages.OpenAIAssistantMessage
"camel.messages.OpenAIAssistantMessage")

    

object.

Return type:

    

OpenAIAssistantMessage

to_openai_message(_role_at_backend : OpenAIBackendRole_) -> ChatCompletionSystemMessageParam | ChatCompletionUserMessageParam | ChatCompletionAssistantMessageParam | ChatCompletionToolMessageParam | ChatCompletionFunctionMessageParam[[source]](_modules/camel/messages/base.html#BaseMessage.to_openai_message)#
    

Converts the message to an `OpenAIMessage` object.

Parameters:

    

**role_at_backend** (_OpenAIBackendRole_) – The role of the message in OpenAI
chat system.

Returns:

    

The converted `OpenAIMessage` object.

Return type:

    

OpenAIMessage

to_openai_system_message() ->
ChatCompletionSystemMessageParam[[source]](_modules/camel/messages/base.html#BaseMessage.to_openai_system_message)#

    

Converts the message to an
[`OpenAISystemMessage`](camel.messages.html#camel.messages.OpenAISystemMessage
"camel.messages.OpenAISystemMessage") object.

Returns:

    

The converted
[`OpenAISystemMessage`](camel.messages.html#camel.messages.OpenAISystemMessage
"camel.messages.OpenAISystemMessage")

    

object.

Return type:

    

OpenAISystemMessage

to_openai_user_message() ->
ChatCompletionUserMessageParam[[source]](_modules/camel/messages/base.html#BaseMessage.to_openai_user_message)#

    

Converts the message to an
[`OpenAIUserMessage`](camel.messages.html#camel.messages.OpenAIUserMessage
"camel.messages.OpenAIUserMessage") object.

Returns:

    

The converted
[`OpenAIUserMessage`](camel.messages.html#camel.messages.OpenAIUserMessage
"camel.messages.OpenAIUserMessage") object.

Return type:

    

OpenAIUserMessage

video_bytes _: bytes | None_ _ = None_#
    

video_detail _: Literal['auto', 'low', 'high']__ = 'low'_#

    

_class _camel.messages.FunctionCallingMessage(_role_name : str_, _role_type : RoleType_, _meta_dict : Dict[str, str] | None_, _content : str_, _video_bytes : bytes | None = None_, _image_list : List[Image] | None = None_, _image_detail : Literal['auto', 'low', 'high'] = 'auto'_, _video_detail : Literal['auto', 'low', 'high'] = 'low'_, _func_name : str | None = None_, _args : Dict | None = None_, _result : Any | None = None_)[[source]](_modules/camel/messages/func_message.html#FunctionCallingMessage)#
    

Bases: [`BaseMessage`](camel.messages.html#camel.messages.base.BaseMessage
"camel.messages.base.BaseMessage")

Class for message objects used specifically for function-related messages.

Parameters:

    

  * **func_name** (_Optional_ _[__str_ _]_) – The name of the function used. (default: `None`)

  * **args** (_Optional_ _[__Dict_ _]_) – The dictionary of arguments passed to the function. (default: `None`)

  * **result** (_Optional_ _[__Any_ _]_) – The result of function execution. (default: `None`)

args _: Dict | None_ _ = None_#
    

func_name _: str | None_ _ = None_#
    

result _: Any | None_ _ = None_#
    

to_openai_assistant_message() ->
ChatCompletionAssistantMessageParam[[source]](_modules/camel/messages/func_message.html#FunctionCallingMessage.to_openai_assistant_message)#

    

Converts the message to an
[`OpenAIAssistantMessage`](camel.messages.html#camel.messages.OpenAIAssistantMessage
"camel.messages.OpenAIAssistantMessage") object.

Returns:

    

The converted
[`OpenAIAssistantMessage`](camel.messages.html#camel.messages.OpenAIAssistantMessage
"camel.messages.OpenAIAssistantMessage")

    

object.

Return type:

    

OpenAIAssistantMessage

to_openai_function_message() ->
ChatCompletionFunctionMessageParam[[source]](_modules/camel/messages/func_message.html#FunctionCallingMessage.to_openai_function_message)#

    

Converts the message to an `OpenAIMessage` object with the role being
“function”.

Returns:

    

The converted `OpenAIMessage` object

    

with its role being “function”.

Return type:

    

OpenAIMessage

to_openai_message(_role_at_backend : OpenAIBackendRole_) -> ChatCompletionSystemMessageParam | ChatCompletionUserMessageParam | ChatCompletionAssistantMessageParam | ChatCompletionToolMessageParam | ChatCompletionFunctionMessageParam[[source]](_modules/camel/messages/func_message.html#FunctionCallingMessage.to_openai_message)#
    

Converts the message to an `OpenAIMessage` object.

Parameters:

    

**role_at_backend** (_OpenAIBackendRole_) – The role of the message in OpenAI
chat system.

Returns:

    

The converted `OpenAIMessage` object.

Return type:

    

OpenAIMessage

camel.messages.OpenAIAssistantMessage#

    

alias of `ChatCompletionAssistantMessageParam`

camel.messages.OpenAISystemMessage#

    

alias of `ChatCompletionSystemMessageParam`

camel.messages.OpenAIUserMessage#

    

alias of `ChatCompletionUserMessageParam`

## camel.types module#

_class
_camel.types.AudioModelType(_value_)[[source]](_modules/camel/types/enums.html#AudioModelType)#

    

Bases: `Enum`

An enumeration.

TTS_1 _ = 'tts-1'_#

    

TTS_1_HD _ = 'tts-1-hd'_#

    

_property _is_openai _: bool_#

    

Returns whether this type of audio models is an OpenAI-released model.

_class _camel.types.ChatCompletion(_** data:
Any_)[[source]](_modules/openai/types/chat/chat_completion.html#ChatCompletion)#

    

Bases: `BaseModel`

choices _: List[Choice]_#

    

A list of chat completion choices.

Can be more than one if n is greater than 1.

created _: int_#

    

The Unix timestamp (in seconds) of when the chat completion was created.

id _: str_#

    

A unique identifier for the chat completion.

model _: str_#

    

The model used for the chat completion.

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'defer_build': True, 'extra':
'allow'}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'choices':
FieldInfo(annotation=List[Choice], required=True), 'created':
FieldInfo(annotation=int, required=True), 'id': FieldInfo(annotation=str,
required=True), 'model': FieldInfo(annotation=str, required=True), 'object':
FieldInfo(annotation=Literal['chat.completion'], required=True),
'service_tier': FieldInfo(annotation=Union[Literal['scale', 'default'],
NoneType], required=False, default=None), 'system_fingerprint':
FieldInfo(annotation=Union[str, NoneType], required=False, default=None),
'usage': FieldInfo(annotation=Union[CompletionUsage, NoneType],
required=False, default=None)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

object _: Literal['chat.completion']_#

    

The object type, which is always chat.completion.

service_tier _: Literal['scale', 'default'] | None_#
    

The service tier used for processing the request.

This field is only included if the service_tier parameter is specified in the
request.

system_fingerprint _: str | None_#
    

This fingerprint represents the backend configuration that the model runs
with.

Can be used in conjunction with the seed request parameter to understand when
backend changes have been made that might impact determinism.

usage _: CompletionUsage | None_#
    

Usage statistics for the completion request.

_class
_camel.types.ChatCompletionAssistantMessageParam[[source]](_modules/openai/types/chat/chat_completion_assistant_message_param.html#ChatCompletionAssistantMessageParam)#

    

Bases: `TypedDict`

content _: str | Iterable[ChatCompletionContentPartTextParam | ChatCompletionContentPartRefusalParam] | None_#
    

The contents of the assistant message.

Required unless tool_calls or function_call is specified.

function_call _: FunctionCall | None_#
    

Deprecated and replaced by tool_calls.

The name and arguments of a function that should be called, as generated by
the model.

name _: str_#

    

An optional name for the participant.

Provides the model information to differentiate between participants of the
same role.

refusal _: str | None_#
    

The refusal message by the assistant.

role _: Required[Literal['assistant']]_#

    

The role of the messages author, in this case assistant.

tool_calls _: Iterable[ChatCompletionMessageToolCallParam]_#

    

The tool calls generated by the model, such as function calls.

_class _camel.types.ChatCompletionChunk(_** data:
Any_)[[source]](_modules/openai/types/chat/chat_completion_chunk.html#ChatCompletionChunk)#

    

Bases: `BaseModel`

choices _: List[Choice]_#

    

A list of chat completion choices.

Can contain more than one elements if n is greater than 1. Can also be empty
for the last chunk if you set stream_options: {“include_usage”: true}.

created _: int_#

    

The Unix timestamp (in seconds) of when the chat completion was created.

Each chunk has the same timestamp.

id _: str_#

    

A unique identifier for the chat completion. Each chunk has the same ID.

model _: str_#

    

The model to generate the completion.

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'defer_build': True, 'extra':
'allow'}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'choices':
FieldInfo(annotation=List[Choice], required=True), 'created':
FieldInfo(annotation=int, required=True), 'id': FieldInfo(annotation=str,
required=True), 'model': FieldInfo(annotation=str, required=True), 'object':
FieldInfo(annotation=Literal['chat.completion.chunk'], required=True),
'service_tier': FieldInfo(annotation=Union[Literal['scale', 'default'],
NoneType], required=False, default=None), 'system_fingerprint':
FieldInfo(annotation=Union[str, NoneType], required=False, default=None),
'usage': FieldInfo(annotation=Union[CompletionUsage, NoneType],
required=False, default=None)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

object _: Literal['chat.completion.chunk']_#

    

The object type, which is always chat.completion.chunk.

service_tier _: Literal['scale', 'default'] | None_#
    

The service tier used for processing the request.

This field is only included if the service_tier parameter is specified in the
request.

system_fingerprint _: str | None_#
    

This fingerprint represents the backend configuration that the model runs
with. Can be used in conjunction with the seed request parameter to understand
when backend changes have been made that might impact determinism.

usage _: CompletionUsage | None_#
    

An optional field that will only be present when you set stream_options:
{“include_usage”: true} in your request. When present, it contains a null
value except for the last chunk which contains the token usage statistics for
the entire request.

_class
_camel.types.ChatCompletionFunctionMessageParam[[source]](_modules/openai/types/chat/chat_completion_function_message_param.html#ChatCompletionFunctionMessageParam)#

    

Bases: `TypedDict`

content _: Required[str | None]_#
    

The contents of the function message.

name _: Required[str]_#

    

The name of the function to call.

role _: Required[Literal['function']]_#

    

The role of the messages author, in this case function.

_class _camel.types.ChatCompletionMessage(_** data:
Any_)[[source]](_modules/openai/types/chat/chat_completion_message.html#ChatCompletionMessage)#

    

Bases: `BaseModel`

content _: str | None_#
    

The contents of the message.

function_call _: FunctionCall | None_#
    

Deprecated and replaced by tool_calls.

The name and arguments of a function that should be called, as generated by
the model.

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'defer_build': True, 'extra':
'allow'}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'content':
FieldInfo(annotation=Union[str, NoneType], required=False, default=None),
'function_call': FieldInfo(annotation=Union[FunctionCall, NoneType],
required=False, default=None), 'refusal': FieldInfo(annotation=Union[str,
NoneType], required=False, default=None), 'role':
FieldInfo(annotation=Literal['assistant'], required=True), 'tool_calls':
FieldInfo(annotation=Union[List[ChatCompletionMessageToolCall], NoneType],
required=False, default=None)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

refusal _: str | None_#
    

The refusal message generated by the model.

role _: Literal['assistant']_#

    

The role of the author of this message.

tool_calls _: List[ChatCompletionMessageToolCall] | None_#
    

The tool calls generated by the model, such as function calls.

_class
_camel.types.ChatCompletionSystemMessageParam[[source]](_modules/openai/types/chat/chat_completion_system_message_param.html#ChatCompletionSystemMessageParam)#

    

Bases: `TypedDict`

content _: Required[str | Iterable[ChatCompletionContentPartTextParam]]_#
    

The contents of the system message.

name _: str_#

    

An optional name for the participant.

Provides the model information to differentiate between participants of the
same role.

role _: Required[Literal['system']]_#

    

The role of the messages author, in this case system.

_class
_camel.types.ChatCompletionUserMessageParam[[source]](_modules/openai/types/chat/chat_completion_user_message_param.html#ChatCompletionUserMessageParam)#

    

Bases: `TypedDict`

content _: Required[str | Iterable[ChatCompletionContentPartTextParam | ChatCompletionContentPartImageParam]]_#
    

The contents of the user message.

name _: str_#

    

An optional name for the participant.

Provides the model information to differentiate between participants of the
same role.

role _: Required[Literal['user']]_#

    

The role of the messages author, in this case user.

_class _camel.types.Choice(_** data:
Any_)[[source]](_modules/openai/types/chat/chat_completion.html#Choice)#

    

Bases: `BaseModel`

finish_reason _: Literal['stop', 'length', 'tool_calls', 'content_filter',
'function_call']_#

    

The reason the model stopped generating tokens.

This will be stop if the model hit a natural stop point or a provided stop
sequence, length if the maximum number of tokens specified in the request was
reached, content_filter if content was omitted due to a flag from our content
filters, tool_calls if the model called a tool, or function_call (deprecated)
if the model called a function.

index _: int_#

    

The index of the choice in the list of choices.

logprobs _: ChoiceLogprobs | None_#
    

Log probability information for the choice.

message _: ChatCompletionMessage_#

    

A chat completion message generated by the model.

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'defer_build': True, 'extra':
'allow'}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'finish_reason':
FieldInfo(annotation=Literal['stop', 'length', 'tool_calls', 'content_filter',
'function_call'], required=True), 'index': FieldInfo(annotation=int,
required=True), 'logprobs': FieldInfo(annotation=Union[ChoiceLogprobs,
NoneType], required=False, default=None), 'message':
FieldInfo(annotation=ChatCompletionMessage, required=True)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

_class _camel.types.CompletionUsage(_** data:
Any_)[[source]](_modules/openai/types/completion_usage.html#CompletionUsage)#

    

Bases: `BaseModel`

completion_tokens _: int_#

    

Number of tokens in the generated completion.

completion_tokens_details _: CompletionTokensDetails | None_#
    

Breakdown of tokens used in a completion.

model_computed_fields _: ClassVar[dict[str, ComputedFieldInfo]]__ = {}_#

    

A dictionary of computed field names and their corresponding ComputedFieldInfo
objects.

model_config _: ClassVar[ConfigDict]__ = {'defer_build': True, 'extra':
'allow'}_#

    

Configuration for the model, should be a dictionary conforming to
[ConfigDict][pydantic.config.ConfigDict].

model_fields _: ClassVar[dict[str, FieldInfo]]__ = {'completion_tokens':
FieldInfo(annotation=int, required=True), 'completion_tokens_details':
FieldInfo(annotation=Union[CompletionTokensDetails, NoneType], required=False,
default=None), 'prompt_tokens': FieldInfo(annotation=int, required=True),
'total_tokens': FieldInfo(annotation=int, required=True)}_#

    

Metadata about the fields defined on the model, mapping of field names to
[FieldInfo][pydantic.fields.FieldInfo].

This replaces Model.__fields__ from Pydantic V1.

prompt_tokens _: int_#

    

Number of tokens in the prompt.

total_tokens _: int_#

    

Total number of tokens used in the request (prompt + completion).

_class
_camel.types.EmbeddingModelType(_value_)[[source]](_modules/camel/types/enums.html#EmbeddingModelType)#

    

Bases: `Enum`

An enumeration.

MISTRAL_EMBED _ = 'mistral-embed'_#

    

TEXT_EMBEDDING_3_LARGE _ = 'text-embedding-3-large'_#

    

TEXT_EMBEDDING_3_SMALL _ = 'text-embedding-3-small'_#

    

TEXT_EMBEDDING_ADA_2 _ = 'text-embedding-ada-002'_#

    

_property _is_mistral _: bool_#

    

Returns whether this type of models is an Mistral-released model.

_property _is_openai _: bool_#

    

Returns whether this type of models is an OpenAI-released model.

_property _output_dim _: int_#

    

_class
_camel.types.ModelPlatformType(_value_)[[source]](_modules/camel/types/enums.html#ModelPlatformType)#

    

Bases: `Enum`

An enumeration.

ANTHROPIC _ = 'anthropic'_#

    

AZURE _ = 'azure'_#

    

DEFAULT _ = 'default'_#

    

GEMINI _ = 'gemini'_#

    

GROQ _ = 'groq'_#

    

LITELLM _ = 'litellm'_#

    

MISTRAL _ = 'mistral'_#

    

OLLAMA _ = 'ollama'_#

    

OPENAI _ = 'openai'_#

    

OPENAI_COMPATIBILITY_MODEL _ = 'openai-compatibility-model'_#

    

OPEN_SOURCE _ = 'open-source'_#

    

REKA _ = 'reka'_#

    

SAMBA _ = 'samba-nova'_#

    

TOGETHER _ = 'together'_#

    

VLLM _ = 'vllm'_#

    

ZHIPU _ = 'zhipuai'_#

    

_property _is_anthropic _: bool_#

    

Returns whether this platform is anthropic.

_property _is_azure _: bool_#

    

Returns whether this platform is azure.

_property _is_gemini _: bool_#

    

Returns whether this platform is Gemini.

_property _is_groq _: bool_#

    

Returns whether this platform is groq.

_property _is_litellm _: bool_#

    

Returns whether this platform is litellm.

_property _is_mistral _: bool_#

    

Returns whether this platform is mistral.

_property _is_ollama _: bool_#

    

Returns whether this platform is ollama.

_property _is_open_source _: bool_#

    

Returns whether this platform is opensource.

_property _is_openai _: bool_#

    

Returns whether this platform is openai.

_property _is_openai_compatibility_model _: bool_#

    

Returns whether this is a platform supporting openai compatibility

_property _is_reka _: bool_#

    

Returns whether this platform is Reka.

_property _is_samba _: bool_#

    

Returns whether this platform is Samba Nova.

_property _is_together _: bool_#

    

Returns whether this platform is together.

_property _is_vllm _: bool_#

    

Returns whether this platform is vllm.

_property _is_zhipuai _: bool_#

    

Returns whether this platform is zhipu.

_class
_camel.types.ModelType(_value_)[[source]](_modules/camel/types/enums.html#ModelType)#

    

Bases: `Enum`

An enumeration.

CLAUDE_2_0 _ = 'claude-2.0'_#

    

CLAUDE_2_1 _ = 'claude-2.1'_#

    

CLAUDE_3_5_SONNET _ = 'claude-3-5-sonnet-20240620'_#

    

CLAUDE_3_HAIKU _ = 'claude-3-haiku-20240307'_#

    

CLAUDE_3_OPUS _ = 'claude-3-opus-20240229'_#

    

CLAUDE_3_SONNET _ = 'claude-3-sonnet-20240229'_#

    

CLAUDE_INSTANT_1_2 _ = 'claude-instant-1.2'_#

    

GEMINI_1_5_FLASH _ = 'gemini-1.5-flash'_#

    

GEMINI_1_5_PRO _ = 'gemini-1.5-pro'_#

    

GLM_3_TURBO _ = 'glm-3-turbo'_#

    

GLM_4 _ = 'glm-4'_#

    

GLM_4V _ = 'glm-4v'_#

    

GLM_4_OPEN_SOURCE _ = 'glm-4-open-source'_#

    

GPT_3_5_TURBO _ = 'gpt-3.5-turbo'_#

    

GPT_4 _ = 'gpt-4'_#

    

GPT_4O _ = 'gpt-4o'_#

    

GPT_4O_MINI _ = 'gpt-4o-mini'_#

    

GPT_4_TURBO _ = 'gpt-4-turbo'_#

    

GROQ_GEMMA_2_9B_IT _ = 'gemma2-9b-it'_#

    

GROQ_GEMMA_7B_IT _ = 'gemma-7b-it'_#

    

GROQ_LLAMA_3_1_405B _ = 'llama-3.1-405b-reasoning'_#

    

GROQ_LLAMA_3_1_70B _ = 'llama-3.1-70b-versatile'_#

    

GROQ_LLAMA_3_1_8B _ = 'llama-3.1-8b-instant'_#

    

GROQ_LLAMA_3_70B _ = 'llama3-70b-8192'_#

    

GROQ_LLAMA_3_8B _ = 'llama3-8b-8192'_#

    

GROQ_MIXTRAL_8_7B _ = 'mixtral-8x7b-32768'_#

    

LLAMA_2 _ = 'llama-2'_#

    

LLAMA_3 _ = 'llama-3'_#

    

MISTRAL_7B _ = 'open-mistral-7b'_#

    

MISTRAL_CODESTRAL _ = 'codestral-latest'_#

    

MISTRAL_CODESTRAL_MAMBA _ = 'open-codestral-mamba'_#

    

MISTRAL_LARGE _ = 'mistral-large-latest'_#

    

MISTRAL_MIXTRAL_8x22B _ = 'open-mixtral-8x22b'_#

    

MISTRAL_MIXTRAL_8x7B _ = 'open-mixtral-8x7b'_#

    

MISTRAL_NEMO _ = 'open-mistral-nemo'_#

    

NEMOTRON_4_REWARD _ = 'nvidia/nemotron-4-340b-reward'_#

    

O1_MINI _ = 'o1-mini'_#

    

O1_PREVIEW _ = 'o1-preview'_#

    

QWEN_2 _ = 'qwen-2'_#

    

REKA_CORE _ = 'reka-core'_#

    

REKA_EDGE _ = 'reka-edge'_#

    

REKA_FLASH _ = 'reka-flash'_#

    

STUB _ = 'stub'_#

    

VICUNA _ = 'vicuna'_#

    

VICUNA_16K _ = 'vicuna-16k'_#

    

_property _is_anthropic _: bool_#

    

Returns whether this type of models is Anthropic-released model.

Returns:

    

Whether this type of models is anthropic.

Return type:

    

bool

_property _is_azure_openai _: bool_#

    

Returns whether this type of models is an OpenAI-released model from Azure.

_property _is_gemini _: bool_#

    

Returns whether this type of models is Gemini model.

Returns:

    

Whether this type of models is gemini.

Return type:

    

bool

_property _is_groq _: bool_#

    

Returns whether this type of models is served by Groq.

_property _is_mistral _: bool_#

    

Returns whether this type of models is served by Mistral.

_property _is_nvidia _: bool_#

    

Returns whether this type of models is Nvidia-released model.

Returns:

    

Whether this type of models is nvidia.

Return type:

    

bool

_property _is_open_source _: bool_#

    

Returns whether this type of models is open-source.

_property _is_openai _: bool_#

    

Returns whether this type of models is an OpenAI-released model.

_property _is_reka _: bool_#

    

Returns whether this type of models is Reka model.

Returns:

    

Whether this type of models is Reka.

Return type:

    

bool

_property _is_zhipuai _: bool_#

    

Returns whether this type of models is an ZhipuAI model.

_property _supports_tool_calling _: bool_#

    

_property _token_limit _: int_#

    

Returns the maximum token limit for a given model.

Returns:

    

The maximum token limit for the given model.

Return type:

    

int

validate_model_name(_model_name : str_) ->
bool[[source]](_modules/camel/types/enums.html#ModelType.validate_model_name)#

    

Checks whether the model type and the model name matches.

Parameters:

    

**model_name** (_str_) – The name of the model, e.g. “vicuna-7b-v1.5”.

Returns:

    

Whether the model type matches the model name.

Return type:

    

bool

_property _value_for_tiktoken _: str_#

    

_class
_camel.types.OpenAIBackendRole(_value_)[[source]](_modules/camel/types/enums.html#OpenAIBackendRole)#

    

Bases: `Enum`

An enumeration.

ASSISTANT _ = 'assistant'_#

    

FUNCTION _ = 'function'_#

    

SYSTEM _ = 'system'_#

    

TOOL _ = 'tool'_#

    

USER _ = 'user'_#

    

_class
_camel.types.OpenAIImageType(_value_)[[source]](_modules/camel/types/enums.html#OpenAIImageType)#

    

Bases: `Enum`

Image types supported by OpenAI vision model.

GIF _ = 'gif'_#

    

JPEG _ = 'jpeg'_#

    

JPG _ = 'jpg'_#

    

PNG _ = 'png'_#

    

WEBP _ = 'webp'_#

    

_class
_camel.types.OpenAIVisionDetailType(_value_)[[source]](_modules/camel/types/enums.html#OpenAIVisionDetailType)#

    

Bases: `Enum`

An enumeration.

AUTO _ = 'auto'_#

    

HIGH _ = 'high'_#

    

LOW _ = 'low'_#

    

_class
_camel.types.OpenAPIName(_value_)[[source]](_modules/camel/types/enums.html#OpenAPIName)#

    

Bases: `Enum`

An enumeration.

BIZTOC _ = 'biztoc'_#

    

COURSERA _ = 'coursera'_#

    

CREATE_QR_CODE _ = 'create_qr_code'_#

    

KLARNA _ = 'klarna'_#

    

NASA_APOD _ = 'nasa_apod'_#

    

OUTSCHOOL _ = 'outschool'_#

    

SPEAK _ = 'speak'_#

    

WEB_SCRAPER _ = 'web_scraper'_#

    

_class
_camel.types.RoleType(_value_)[[source]](_modules/camel/types/enums.html#RoleType)#

    

Bases: `Enum`

An enumeration.

ASSISTANT _ = 'assistant'_#

    

CRITIC _ = 'critic'_#

    

DEFAULT _ = 'default'_#

    

EMBODIMENT _ = 'embodiment'_#

    

USER _ = 'user'_#

    

_class
_camel.types.StorageType(_value_)[[source]](_modules/camel/types/enums.html#StorageType)#

    

Bases: `Enum`

An enumeration.

MILVUS _ = 'milvus'_#

    

QDRANT _ = 'qdrant'_#

    

_class
_camel.types.TaskType(_value_)[[source]](_modules/camel/types/enums.html#TaskType)#

    

Bases: `Enum`

An enumeration.

AI_SOCIETY _ = 'ai_society'_#

    

CODE _ = 'code'_#

    

DEFAULT _ = 'default'_#

    

EVALUATION _ = 'evaluation'_#

    

GENERATE_TEXT_EMBEDDING_DATA _ = 'generate_text_embedding_data'_#

    

IMAGE_CRAFT _ = 'image_craft'_#

    

MISALIGNMENT _ = 'misalignment'_#

    

MULTI_CONDITION_IMAGE_CRAFT _ = 'multi_condition_image_craft'_#

    

OBJECT_RECOGNITION _ = 'object_recognition'_#

    

ROLE_DESCRIPTION _ = 'role_description'_#

    

SOLUTION_EXTRACTION _ = 'solution_extraction'_#

    

TRANSLATION _ = 'translation'_#

    

VIDEO_DESCRIPTION _ = 'video_description'_#

    

_class
_camel.types.TerminationMode(_value_)[[source]](_modules/camel/types/enums.html#TerminationMode)#

    

Bases: `Enum`

An enumeration.

ALL _ = 'all'_#

    

ANY _ = 'any'_#

    

_class
_camel.types.VectorDistance(_value_)[[source]](_modules/camel/types/enums.html#VectorDistance)#

    

Bases: `Enum`

Distance metrics used in a vector database.

COSINE _ = 'cosine'_#

    

//en.wikipedia.org/wiki/Cosine_similarity

Type:

    

Cosine similarity. https

DOT _ = 'dot'_#

    

//en.wikipedia.org/wiki/Dot_product

Type:

    

Dot product. https

EUCLIDEAN _ = 'euclidean'_#

    

//en.wikipedia.org/wiki/Euclidean_distance

Type:

    

Euclidean distance. https

_class
_camel.types.VoiceType(_value_)[[source]](_modules/camel/types/enums.html#VoiceType)#

    

Bases: `Enum`

An enumeration.

ALLOY _ = 'alloy'_#

    

ECHO _ = 'echo'_#

    

FABLE _ = 'fable'_#

    

NOVA _ = 'nova'_#

    

ONYX _ = 'onyx'_#

    

SHIMMER _ = 'shimmer'_#

    

_property _is_openai _: bool_#

    

Returns whether this type of voice is an OpenAI-released voice.

## camel.utils module#

_class _camel.utils.AgentOpsMeta(_name_ , _bases_ ,
_dct_)[[source]](_modules/camel/utils/commons.html#AgentOpsMeta)#

    

Bases: `type`

Metaclass that automatically decorates all callable attributes with the
agentops_decorator, except for the ‘get_tools’ method.

Methods: __new__(cls, name, bases, dct):

> Creates a new class with decorated methods.

_class _camel.utils.AnthropicTokenCounter(_model_type :
ModelType_)[[source]](_modules/camel/utils/token_counting.html#AnthropicTokenCounter)#

    

Bases: `BaseTokenCounter`

count_tokens_from_messages(_messages : List[OpenAIMessage]_) ->
int[[source]](_modules/camel/utils/token_counting.html#AnthropicTokenCounter.count_tokens_from_messages)#

    

Count number of tokens in the provided message list using loaded tokenizer
specific for this type of model.

Parameters:

    

**messages** (_List_ _[__OpenAIMessage_ _]_) – Message list with the chat
history in OpenAI API format.

Returns:

    

Number of tokens in the messages.

Return type:

    

int

_class
_camel.utils.BaseTokenCounter[[source]](_modules/camel/utils/token_counting.html#BaseTokenCounter)#

    

Bases: `ABC`

Base class for token counters of different kinds of models.

_abstract _count_tokens_from_messages(_messages : List[OpenAIMessage]_) ->
int[[source]](_modules/camel/utils/token_counting.html#BaseTokenCounter.count_tokens_from_messages)#

    

Count number of tokens in the provided message list.

Parameters:

    

**messages** (_List_ _[__OpenAIMessage_ _]_) – Message list with the chat
history in OpenAI API format.

Returns:

    

Number of tokens in the messages.

Return type:

    

int

_class
_camel.utils.Constants[[source]](_modules/camel/utils/constants.html#Constants)#

    

Bases: `object`

DEFAULT_SIMILARITY_THRESHOLD _ = 0.7_#

    

DEFAULT_TOP_K_RESULTS _ = 1_#

    

FUNC_NAME_FOR_STRUCTURED_OUTPUT _ = 'return_json_response'_#

    

VIDEO_DEFAULT_IMAGE_SIZE _ = 768_#

    

VIDEO_DEFAULT_PLUG_PYAV _ = 'pyav'_#

    

VIDEO_IMAGE_EXTRACTION_INTERVAL _ = 50_#

    

_class _camel.utils.GeminiTokenCounter(_model_type :
ModelType_)[[source]](_modules/camel/utils/token_counting.html#GeminiTokenCounter)#

    

Bases: `BaseTokenCounter`

count_tokens_from_messages(_messages : List[OpenAIMessage]_) ->
int[[source]](_modules/camel/utils/token_counting.html#GeminiTokenCounter.count_tokens_from_messages)#

    

Count number of tokens in the provided message list using loaded tokenizer
specific for this type of model.

Parameters:

    

**messages** (_List_ _[__OpenAIMessage_ _]_) – Message list with the chat
history in OpenAI API format.

Returns:

    

Number of tokens in the messages.

Return type:

    

int

_class _camel.utils.LiteLLMTokenCounter(_model_type :
str_)[[source]](_modules/camel/utils/token_counting.html#LiteLLMTokenCounter)#

    

Bases: `object`

calculate_cost_from_response(_response : dict_) ->
float[[source]](_modules/camel/utils/token_counting.html#LiteLLMTokenCounter.calculate_cost_from_response)#

    

Calculate the cost of the given completion response.

Parameters:

    

**response** (_dict_) – The completion response from LiteLLM.

Returns:

    

The cost of the completion call in USD.

Return type:

    

float

_property _completion_cost#

    

count_tokens_from_messages(_messages : List[OpenAIMessage]_) ->
int[[source]](_modules/camel/utils/token_counting.html#LiteLLMTokenCounter.count_tokens_from_messages)#

    

Count number of tokens in the provided message list using the tokenizer
specific to this type of model.

Parameters:

    

**messages** (_List_ _[__OpenAIMessage_ _]_) – Message list with the chat
history in LiteLLM API format.

Returns:

    

Number of tokens in the messages.

Return type:

    

int

_property _token_counter#

    

_class _camel.utils.MistralTokenCounter(_model_type :
ModelType_)[[source]](_modules/camel/utils/token_counting.html#MistralTokenCounter)#

    

Bases: `BaseTokenCounter`

count_tokens_from_messages(_messages : List[OpenAIMessage]_) ->
int[[source]](_modules/camel/utils/token_counting.html#MistralTokenCounter.count_tokens_from_messages)#

    

Count number of tokens in the provided message list using loaded tokenizer
specific for this type of model.

Parameters:

    

**messages** (_List_ _[__OpenAIMessage_ _]_) – Message list with the chat
history in OpenAI API format.

Returns:

    

Total number of tokens in the messages.

Return type:

    

int

_class _camel.utils.OpenAITokenCounter(_model :
ModelType_)[[source]](_modules/camel/utils/token_counting.html#OpenAITokenCounter)#

    

Bases: `BaseTokenCounter`

count_tokens_from_messages(_messages : List[OpenAIMessage]_) ->
int[[source]](_modules/camel/utils/token_counting.html#OpenAITokenCounter.count_tokens_from_messages)#

    

Count number of tokens in the provided message list with the help of package
tiktoken.

Parameters:

    

**messages** (_List_ _[__OpenAIMessage_ _]_) – Message list with the chat
history in OpenAI API format.

Returns:

    

Number of tokens in the messages.

Return type:

    

int

_class _camel.utils.OpenSourceTokenCounter(_model_type : ModelType_,
_model_path :
str_)[[source]](_modules/camel/utils/token_counting.html#OpenSourceTokenCounter)#

    

Bases: `BaseTokenCounter`

count_tokens_from_messages(_messages : List[OpenAIMessage]_) ->
int[[source]](_modules/camel/utils/token_counting.html#OpenSourceTokenCounter.count_tokens_from_messages)#

    

Count number of tokens in the provided message list using loaded tokenizer
specific for this type of model.

Parameters:

    

**messages** (_List_ _[__OpenAIMessage_ _]_) – Message list with the chat
history in OpenAI API format.

Returns:

    

Number of tokens in the messages.

Return type:

    

int

camel.utils.agentops_decorator(_func_)[[source]](_modules/camel/utils/commons.html#agentops_decorator)#

    

Decorator that records the execution of a function if ToolEvent is available.

Parameters:

    

**func** (_callable_) – The function to be decorated.

Returns:

    

The wrapped function which records its execution details.

Return type:

    

callable

camel.utils.api_keys_required(_* required_keys: str_) -> Callable[[F],
F][[source]](_modules/camel/utils/commons.html#api_keys_required)#

    

A decorator to check if the required API keys are presented in the environment
variables or as an instance attribute.

Parameters:

    

**required_keys** (_str_) – The required API keys to be checked.

Returns:

    

The original function with the added check

    

for required API keys.

Return type:

    

Callable[[F], F]

Raises:

    

**ValueError** – If any of the required API keys are missing in the
environment variables and the instance attribute.

Example

    
    
    @api_keys_required('API_KEY_1', 'API_KEY_2')
    def some_api_function():
        # Function implementation...
    

camel.utils.check_server_running(_server_url : str_) ->
bool[[source]](_modules/camel/utils/commons.html#check_server_running)#

    

Check whether the port refered by the URL to the server is open.

Parameters:

    

**server_url** (_str_) – The URL to the server running LLM inference service.

Returns:

    

Whether the port is open for packets (server is running).

Return type:

    

bool

camel.utils.create_chunks(_text : str_, _n : int_) ->
List[str][[source]](_modules/camel/utils/commons.html#create_chunks)#

    

Returns successive n-sized chunks from provided text. Split a text into
smaller chunks of size n”.

Parameters:

    

  * **text** (_str_) – The text to be split.

  * **n** (_int_) – The max length of a single chunk.

Returns:

    

A list of split texts.

Return type:

    

List[str]

camel.utils.dependencies_required(_* required_modules: str_) -> Callable[[F],
F][[source]](_modules/camel/utils/commons.html#dependencies_required)#

    

A decorator to ensure that specified Python modules are available before a
function executes.

Parameters:

    

**required_modules** (_str_) – The required modules to be checked for
availability.

Returns:

    

The original function with the added check for

    

required module dependencies.

Return type:

    

Callable[[F], F]

Raises:

    

**ImportError** – If any of the required modules are not available.

Example

    
    
    @dependencies_required('numpy', 'pandas')
    def data_processing_function():
        # Function implementation...
    

camel.utils.download_tasks(_task : TaskType_, _folder_path : str_) ->
None[[source]](_modules/camel/utils/commons.html#download_tasks)#

    

Downloads task-related files from a specified URL and extracts them.

This function downloads a zip file containing tasks based on the specified
task type from a predefined URL, saves it to folder_path, and then extracts
the contents of the zip file into the same folder. After extraction, the zip
file is deleted.

Parameters:

    

  * **task** (_TaskType_) – An enum representing the type of task to download.

  * **folder_path** (_str_) – The path of the folder where the zip file will be downloaded and extracted.

camel.utils.func_string_to_callable(_code :
str_)[[source]](_modules/camel/utils/commons.html#func_string_to_callable)#

    

Convert a function code string to a callable function object.

Parameters:

    

**code** (_str_) – The function code as a string.

Returns:

    

The callable function object extracted from the

    

code string.

Return type:

    

Callable[…, Any]

camel.utils.get_first_int(_string : str_) -> int | None[[source]](_modules/camel/utils/commons.html#get_first_int)#
    

Returns the first integer number found in the given string.

If no integer number is found, returns None.

Parameters:

    

**string** (_str_) – The input string.

Returns:

    

The first integer number found in the string, or None if

    

no integer number is found.

Return type:

    

int or None

camel.utils.get_model_encoding(_value_for_tiktoken :
str_)[[source]](_modules/camel/utils/token_counting.html#get_model_encoding)#

    

Get model encoding from tiktoken.

Parameters:

    

**value_for_tiktoken** – Model value for tiktoken.

Returns:

    

Model encoding.

Return type:

    

tiktoken.Encoding

camel.utils.get_prompt_template_key_words(_template : str_) ->
Set[str][[source]](_modules/camel/utils/commons.html#get_prompt_template_key_words)#

    

Given a string template containing curly braces {}, return a set of the words
inside the braces.

Parameters:

    

**template** (_str_) – A string containing curly braces.

Returns:

    

A list of the words inside the curly braces.

Return type:

    

List[str]

Example

    
    
    >>> get_prompt_template_key_words('Hi, {name}! How are you {status}?')
    {'name', 'status'}
    

camel.utils.get_pydantic_major_version() ->
int[[source]](_modules/camel/utils/commons.html#get_pydantic_major_version)#

    

Get the major version of Pydantic.

Returns:

    

The major version number of Pydantic if installed, otherwise 0.

Return type:

    

int

camel.utils.get_pydantic_object_schema(_pydantic_params : Type[BaseModel]_) ->
Dict[[source]](_modules/camel/utils/commons.html#get_pydantic_object_schema)#

    

Get the JSON schema of a Pydantic model.

Parameters:

    

**pydantic_params** (_Type_ _[__BaseModel_ _]_) – The Pydantic model class to
retrieve the schema for.

Returns:

    

The JSON schema of the Pydantic model.

Return type:

    

dict

camel.utils.get_system_information()[[source]](_modules/camel/utils/commons.html#get_system_information)#

    

Gathers information about the operating system.

Returns:

    

A dictionary containing various pieces of OS information.

Return type:

    

dict

camel.utils.get_task_list(_task_response : str_) ->
List[str][[source]](_modules/camel/utils/commons.html#get_task_list)#

    

Parse the response of the Agent and return task list.

Parameters:

    

**task_response** (_str_) – The string response of the Agent.

Returns:

    

A list of the string tasks.

Return type:

    

List[str]

camel.utils.handle_http_error(_response : Response_) ->
str[[source]](_modules/camel/utils/commons.html#handle_http_error)#

    

Handles the HTTP errors based on the status code of the response.

Parameters:

    

**response** (_requests.Response_) – The HTTP response from the API call.

Returns:

    

The error type, based on the status code.

Return type:

    

str

camel.utils.is_docker_running() ->
bool[[source]](_modules/camel/utils/commons.html#is_docker_running)#

    

Check if the Docker daemon is running.

Returns:

    

True if the Docker daemon is running, False otherwise.

Return type:

    

bool

camel.utils.json_to_function_code(_json_obj : Dict_) ->
str[[source]](_modules/camel/utils/commons.html#json_to_function_code)#

    

Generate a Python function code from a JSON schema.

Parameters:

    

**json_obj** (_dict_) – The JSON schema object containing properties and
required fields, and json format is follow openai tools schema

Returns:

    

The generated Python function code as a string.

Return type:

    

str

camel.utils.print_text_animated(_text_ , _delay : float = 0.02_, _end : str =
''_)[[source]](_modules/camel/utils/commons.html#print_text_animated)#

    

Prints the given text with an animated effect.

Parameters:

    

  * **text** (_str_) – The text to print.

  * **delay** (_float_ _,__optional_) – The delay between each character printed. (default: `0.02`)

  * **end** (_str_ _,__optional_) – The end character to print after each character of text. (default: `""`)

camel.utils.text_extract_from_web(_url : str_) ->
str[[source]](_modules/camel/utils/commons.html#text_extract_from_web)#

    

Get the text information from given url.

Parameters:

    

**url** (_str_) – The website you want to search.

Returns:

    

All texts extract from the web.

Return type:

    

str

camel.utils.to_pascal(_snake : str_) ->
str[[source]](_modules/camel/utils/commons.html#to_pascal)#

    

Convert a snake_case string to PascalCase.

Parameters:

    

**snake** (_str_) – The snake_case string to be converted.

Returns:

    

The converted PascalCase string.

Return type:

    

str

camel.utils.track_agent(_* args_, _**
kwargs_)[[source]](_modules/camel/utils/commons.html#track_agent)#

    

## Module contents#

[ __ previous camel ](modules.html "previous page") [ next camel.agents
package __](camel.agents.html "next page")

__Contents

  * Subpackages
  * Submodules
  * camel.configs module
    * `AnthropicConfig`
      * `AnthropicConfig.max_tokens`
      * `AnthropicConfig.metadata`
      * `AnthropicConfig.model_computed_fields`
      * `AnthropicConfig.model_config`
      * `AnthropicConfig.model_fields`
      * `AnthropicConfig.stop_sequences`
      * `AnthropicConfig.stream`
      * `AnthropicConfig.temperature`
      * `AnthropicConfig.top_k`
      * `AnthropicConfig.top_p`
    * `BaseConfig`
      * `BaseConfig.as_dict()`
      * `BaseConfig.fields_type_checking()`
      * `BaseConfig.model_computed_fields`
      * `BaseConfig.model_config`
      * `BaseConfig.model_fields`
      * `BaseConfig.tools`
    * `ChatGPTConfig`
      * `ChatGPTConfig.frequency_penalty`
      * `ChatGPTConfig.logit_bias`
      * `ChatGPTConfig.max_tokens`
      * `ChatGPTConfig.model_computed_fields`
      * `ChatGPTConfig.model_config`
      * `ChatGPTConfig.model_fields`
      * `ChatGPTConfig.n`
      * `ChatGPTConfig.presence_penalty`
      * `ChatGPTConfig.response_format`
      * `ChatGPTConfig.stop`
      * `ChatGPTConfig.stream`
      * `ChatGPTConfig.temperature`
      * `ChatGPTConfig.tool_choice`
      * `ChatGPTConfig.top_p`
      * `ChatGPTConfig.user`
    * `GeminiConfig`
      * `GeminiConfig.candidate_count`
      * `GeminiConfig.fields_type_checking()`
      * `GeminiConfig.max_output_tokens`
      * `GeminiConfig.model_computed_fields`
      * `GeminiConfig.model_config`
      * `GeminiConfig.model_fields`
      * `GeminiConfig.request_options`
      * `GeminiConfig.response_mime_type`
      * `GeminiConfig.response_schema`
      * `GeminiConfig.safety_settings`
      * `GeminiConfig.stop_sequences`
      * `GeminiConfig.temperature`
      * `GeminiConfig.tool_config`
      * `GeminiConfig.top_k`
      * `GeminiConfig.top_p`
    * `GroqConfig`
      * `GroqConfig.frequency_penalty`
      * `GroqConfig.max_tokens`
      * `GroqConfig.model_computed_fields`
      * `GroqConfig.model_config`
      * `GroqConfig.model_fields`
      * `GroqConfig.n`
      * `GroqConfig.presence_penalty`
      * `GroqConfig.response_format`
      * `GroqConfig.stop`
      * `GroqConfig.stream`
      * `GroqConfig.temperature`
      * `GroqConfig.tool_choice`
      * `GroqConfig.top_p`
      * `GroqConfig.user`
    * `LiteLLMConfig`
      * `LiteLLMConfig.api_version`
      * `LiteLLMConfig.custom_llm_provider`
      * `LiteLLMConfig.deployment_id`
      * `LiteLLMConfig.extra_headers`
      * `LiteLLMConfig.frequency_penalty`
      * `LiteLLMConfig.logit_bias`
      * `LiteLLMConfig.logprobs`
      * `LiteLLMConfig.max_retries`
      * `LiteLLMConfig.max_tokens`
      * `LiteLLMConfig.mock_response`
      * `LiteLLMConfig.model_computed_fields`
      * `LiteLLMConfig.model_config`
      * `LiteLLMConfig.model_fields`
      * `LiteLLMConfig.n`
      * `LiteLLMConfig.presence_penalty`
      * `LiteLLMConfig.response_format`
      * `LiteLLMConfig.seed`
      * `LiteLLMConfig.stop`
      * `LiteLLMConfig.stream`
      * `LiteLLMConfig.stream_options`
      * `LiteLLMConfig.temperature`
      * `LiteLLMConfig.timeout`
      * `LiteLLMConfig.tool_choice`
      * `LiteLLMConfig.top_logprobs`
      * `LiteLLMConfig.top_p`
      * `LiteLLMConfig.user`
    * `MistralConfig`
      * `MistralConfig.fields_type_checking()`
      * `MistralConfig.max_tokens`
      * `MistralConfig.min_tokens`
      * `MistralConfig.model_computed_fields`
      * `MistralConfig.model_config`
      * `MistralConfig.model_fields`
      * `MistralConfig.random_seed`
      * `MistralConfig.response_format`
      * `MistralConfig.safe_prompt`
      * `MistralConfig.stop`
      * `MistralConfig.temperature`
      * `MistralConfig.tool_choice`
      * `MistralConfig.top_p`
    * `OllamaConfig`
      * `OllamaConfig.frequency_penalty`
      * `OllamaConfig.max_tokens`
      * `OllamaConfig.model_computed_fields`
      * `OllamaConfig.model_config`
      * `OllamaConfig.model_fields`
      * `OllamaConfig.presence_penalty`
      * `OllamaConfig.response_format`
      * `OllamaConfig.stop`
      * `OllamaConfig.stream`
      * `OllamaConfig.temperature`
      * `OllamaConfig.top_p`
    * `OpenSourceConfig`
      * `OpenSourceConfig.api_params`
      * `OpenSourceConfig.model_computed_fields`
      * `OpenSourceConfig.model_config`
      * `OpenSourceConfig.model_fields`
      * `OpenSourceConfig.model_path`
      * `OpenSourceConfig.server_url`
    * `RekaConfig`
      * `RekaConfig.as_dict()`
      * `RekaConfig.frequency_penalty`
      * `RekaConfig.max_tokens`
      * `RekaConfig.model_computed_fields`
      * `RekaConfig.model_config`
      * `RekaConfig.model_fields`
      * `RekaConfig.presence_penalty`
      * `RekaConfig.seed`
      * `RekaConfig.stop`
      * `RekaConfig.temperature`
      * `RekaConfig.top_k`
      * `RekaConfig.top_p`
      * `RekaConfig.use_search_engine`
    * `SambaCloudAPIConfig`
      * `SambaCloudAPIConfig.frequency_penalty`
      * `SambaCloudAPIConfig.logit_bias`
      * `SambaCloudAPIConfig.max_tokens`
      * `SambaCloudAPIConfig.model_computed_fields`
      * `SambaCloudAPIConfig.model_config`
      * `SambaCloudAPIConfig.model_fields`
      * `SambaCloudAPIConfig.n`
      * `SambaCloudAPIConfig.presence_penalty`
      * `SambaCloudAPIConfig.response_format`
      * `SambaCloudAPIConfig.stop`
      * `SambaCloudAPIConfig.stream`
      * `SambaCloudAPIConfig.temperature`
      * `SambaCloudAPIConfig.tool_choice`
      * `SambaCloudAPIConfig.top_p`
      * `SambaCloudAPIConfig.user`
    * `SambaFastAPIConfig`
      * `SambaFastAPIConfig.as_dict()`
      * `SambaFastAPIConfig.max_tokens`
      * `SambaFastAPIConfig.model_computed_fields`
      * `SambaFastAPIConfig.model_config`
      * `SambaFastAPIConfig.model_fields`
      * `SambaFastAPIConfig.stop`
      * `SambaFastAPIConfig.stream`
      * `SambaFastAPIConfig.stream_options`
    * `SambaVerseAPIConfig`
      * `SambaVerseAPIConfig.as_dict()`
      * `SambaVerseAPIConfig.max_tokens`
      * `SambaVerseAPIConfig.model_computed_fields`
      * `SambaVerseAPIConfig.model_config`
      * `SambaVerseAPIConfig.model_fields`
      * `SambaVerseAPIConfig.repetition_penalty`
      * `SambaVerseAPIConfig.stop`
      * `SambaVerseAPIConfig.stream`
      * `SambaVerseAPIConfig.temperature`
      * `SambaVerseAPIConfig.top_k`
      * `SambaVerseAPIConfig.top_p`
    * `TogetherAIConfig`
      * `TogetherAIConfig.as_dict()`
      * `TogetherAIConfig.frequency_penalty`
      * `TogetherAIConfig.logit_bias`
      * `TogetherAIConfig.max_tokens`
      * `TogetherAIConfig.model_computed_fields`
      * `TogetherAIConfig.model_config`
      * `TogetherAIConfig.model_fields`
      * `TogetherAIConfig.n`
      * `TogetherAIConfig.presence_penalty`
      * `TogetherAIConfig.response_format`
      * `TogetherAIConfig.stop`
      * `TogetherAIConfig.stream`
      * `TogetherAIConfig.temperature`
      * `TogetherAIConfig.top_p`
      * `TogetherAIConfig.user`
    * `VLLMConfig`
      * `VLLMConfig.frequency_penalty`
      * `VLLMConfig.logit_bias`
      * `VLLMConfig.max_tokens`
      * `VLLMConfig.model_computed_fields`
      * `VLLMConfig.model_config`
      * `VLLMConfig.model_fields`
      * `VLLMConfig.n`
      * `VLLMConfig.presence_penalty`
      * `VLLMConfig.response_format`
      * `VLLMConfig.stop`
      * `VLLMConfig.stream`
      * `VLLMConfig.temperature`
      * `VLLMConfig.top_p`
      * `VLLMConfig.user`
    * `ZhipuAIConfig`
      * `ZhipuAIConfig.max_tokens`
      * `ZhipuAIConfig.model_computed_fields`
      * `ZhipuAIConfig.model_config`
      * `ZhipuAIConfig.model_fields`
      * `ZhipuAIConfig.stop`
      * `ZhipuAIConfig.stream`
      * `ZhipuAIConfig.temperature`
      * `ZhipuAIConfig.tool_choice`
      * `ZhipuAIConfig.top_p`
  * camel.generators module
    * `AISocietyTaskPromptGenerator`
      * `AISocietyTaskPromptGenerator.from_role_files()`
      * `AISocietyTaskPromptGenerator.from_role_generator()`
    * `CodeTaskPromptGenerator`
      * `CodeTaskPromptGenerator.from_role_files()`
      * `CodeTaskPromptGenerator.from_role_generator()`
    * `RoleNameGenerator`
      * `RoleNameGenerator.from_role_files()`
    * `SingleTxtGenerator`
      * `SingleTxtGenerator.from_role_files()`
    * `SystemMessageGenerator`
      * `SystemMessageGenerator.from_dict()`
      * `SystemMessageGenerator.from_dicts()`
      * `SystemMessageGenerator.validate_meta_dict_keys()`
  * camel.human module
    * `Human`
      * `Human.name`
      * `Human.logger_color`
      * `Human.input_button`
      * `Human.kill_button`
      * `Human.options_dict`
      * `Human.display_options()`
      * `Human.get_input()`
      * `Human.parse_input()`
      * `Human.reduce_step()`
  * camel.messages module
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
      * `FunctionCallingMessage.func_name`
      * `FunctionCallingMessage.result`
      * `FunctionCallingMessage.to_openai_assistant_message()`
      * `FunctionCallingMessage.to_openai_function_message()`
      * `FunctionCallingMessage.to_openai_message()`
    * `OpenAIAssistantMessage`
    * `OpenAISystemMessage`
    * `OpenAIUserMessage`
  * camel.types module
    * `AudioModelType`
      * `AudioModelType.TTS_1`
      * `AudioModelType.TTS_1_HD`
      * `AudioModelType.is_openai`
    * `ChatCompletion`
      * `ChatCompletion.choices`
      * `ChatCompletion.created`
      * `ChatCompletion.id`
      * `ChatCompletion.model`
      * `ChatCompletion.model_computed_fields`
      * `ChatCompletion.model_config`
      * `ChatCompletion.model_fields`
      * `ChatCompletion.object`
      * `ChatCompletion.service_tier`
      * `ChatCompletion.system_fingerprint`
      * `ChatCompletion.usage`
    * `ChatCompletionAssistantMessageParam`
      * `ChatCompletionAssistantMessageParam.content`
      * `ChatCompletionAssistantMessageParam.function_call`
      * `ChatCompletionAssistantMessageParam.name`
      * `ChatCompletionAssistantMessageParam.refusal`
      * `ChatCompletionAssistantMessageParam.role`
      * `ChatCompletionAssistantMessageParam.tool_calls`
    * `ChatCompletionChunk`
      * `ChatCompletionChunk.choices`
      * `ChatCompletionChunk.created`
      * `ChatCompletionChunk.id`
      * `ChatCompletionChunk.model`
      * `ChatCompletionChunk.model_computed_fields`
      * `ChatCompletionChunk.model_config`
      * `ChatCompletionChunk.model_fields`
      * `ChatCompletionChunk.object`
      * `ChatCompletionChunk.service_tier`
      * `ChatCompletionChunk.system_fingerprint`
      * `ChatCompletionChunk.usage`
    * `ChatCompletionFunctionMessageParam`
      * `ChatCompletionFunctionMessageParam.content`
      * `ChatCompletionFunctionMessageParam.name`
      * `ChatCompletionFunctionMessageParam.role`
    * `ChatCompletionMessage`
      * `ChatCompletionMessage.content`
      * `ChatCompletionMessage.function_call`
      * `ChatCompletionMessage.model_computed_fields`
      * `ChatCompletionMessage.model_config`
      * `ChatCompletionMessage.model_fields`
      * `ChatCompletionMessage.refusal`
      * `ChatCompletionMessage.role`
      * `ChatCompletionMessage.tool_calls`
    * `ChatCompletionSystemMessageParam`
      * `ChatCompletionSystemMessageParam.content`
      * `ChatCompletionSystemMessageParam.name`
      * `ChatCompletionSystemMessageParam.role`
    * `ChatCompletionUserMessageParam`
      * `ChatCompletionUserMessageParam.content`
      * `ChatCompletionUserMessageParam.name`
      * `ChatCompletionUserMessageParam.role`
    * `Choice`
      * `Choice.finish_reason`
      * `Choice.index`
      * `Choice.logprobs`
      * `Choice.message`
      * `Choice.model_computed_fields`
      * `Choice.model_config`
      * `Choice.model_fields`
    * `CompletionUsage`
      * `CompletionUsage.completion_tokens`
      * `CompletionUsage.completion_tokens_details`
      * `CompletionUsage.model_computed_fields`
      * `CompletionUsage.model_config`
      * `CompletionUsage.model_fields`
      * `CompletionUsage.prompt_tokens`
      * `CompletionUsage.total_tokens`
    * `EmbeddingModelType`
      * `EmbeddingModelType.MISTRAL_EMBED`
      * `EmbeddingModelType.TEXT_EMBEDDING_3_LARGE`
      * `EmbeddingModelType.TEXT_EMBEDDING_3_SMALL`
      * `EmbeddingModelType.TEXT_EMBEDDING_ADA_2`
      * `EmbeddingModelType.is_mistral`
      * `EmbeddingModelType.is_openai`
      * `EmbeddingModelType.output_dim`
    * `ModelPlatformType`
      * `ModelPlatformType.ANTHROPIC`
      * `ModelPlatformType.AZURE`
      * `ModelPlatformType.DEFAULT`
      * `ModelPlatformType.GEMINI`
      * `ModelPlatformType.GROQ`
      * `ModelPlatformType.LITELLM`
      * `ModelPlatformType.MISTRAL`
      * `ModelPlatformType.OLLAMA`
      * `ModelPlatformType.OPENAI`
      * `ModelPlatformType.OPENAI_COMPATIBILITY_MODEL`
      * `ModelPlatformType.OPEN_SOURCE`
      * `ModelPlatformType.REKA`
      * `ModelPlatformType.SAMBA`
      * `ModelPlatformType.TOGETHER`
      * `ModelPlatformType.VLLM`
      * `ModelPlatformType.ZHIPU`
      * `ModelPlatformType.is_anthropic`
      * `ModelPlatformType.is_azure`
      * `ModelPlatformType.is_gemini`
      * `ModelPlatformType.is_groq`
      * `ModelPlatformType.is_litellm`
      * `ModelPlatformType.is_mistral`
      * `ModelPlatformType.is_ollama`
      * `ModelPlatformType.is_open_source`
      * `ModelPlatformType.is_openai`
      * `ModelPlatformType.is_openai_compatibility_model`
      * `ModelPlatformType.is_reka`
      * `ModelPlatformType.is_samba`
      * `ModelPlatformType.is_together`
      * `ModelPlatformType.is_vllm`
      * `ModelPlatformType.is_zhipuai`
    * `ModelType`
      * `ModelType.CLAUDE_2_0`
      * `ModelType.CLAUDE_2_1`
      * `ModelType.CLAUDE_3_5_SONNET`
      * `ModelType.CLAUDE_3_HAIKU`
      * `ModelType.CLAUDE_3_OPUS`
      * `ModelType.CLAUDE_3_SONNET`
      * `ModelType.CLAUDE_INSTANT_1_2`
      * `ModelType.GEMINI_1_5_FLASH`
      * `ModelType.GEMINI_1_5_PRO`
      * `ModelType.GLM_3_TURBO`
      * `ModelType.GLM_4`
      * `ModelType.GLM_4V`
      * `ModelType.GLM_4_OPEN_SOURCE`
      * `ModelType.GPT_3_5_TURBO`
      * `ModelType.GPT_4`
      * `ModelType.GPT_4O`
      * `ModelType.GPT_4O_MINI`
      * `ModelType.GPT_4_TURBO`
      * `ModelType.GROQ_GEMMA_2_9B_IT`
      * `ModelType.GROQ_GEMMA_7B_IT`
      * `ModelType.GROQ_LLAMA_3_1_405B`
      * `ModelType.GROQ_LLAMA_3_1_70B`
      * `ModelType.GROQ_LLAMA_3_1_8B`
      * `ModelType.GROQ_LLAMA_3_70B`
      * `ModelType.GROQ_LLAMA_3_8B`
      * `ModelType.GROQ_MIXTRAL_8_7B`
      * `ModelType.LLAMA_2`
      * `ModelType.LLAMA_3`
      * `ModelType.MISTRAL_7B`
      * `ModelType.MISTRAL_CODESTRAL`
      * `ModelType.MISTRAL_CODESTRAL_MAMBA`
      * `ModelType.MISTRAL_LARGE`
      * `ModelType.MISTRAL_MIXTRAL_8x22B`
      * `ModelType.MISTRAL_MIXTRAL_8x7B`
      * `ModelType.MISTRAL_NEMO`
      * `ModelType.NEMOTRON_4_REWARD`
      * `ModelType.O1_MINI`
      * `ModelType.O1_PREVIEW`
      * `ModelType.QWEN_2`
      * `ModelType.REKA_CORE`
      * `ModelType.REKA_EDGE`
      * `ModelType.REKA_FLASH`
      * `ModelType.STUB`
      * `ModelType.VICUNA`
      * `ModelType.VICUNA_16K`
      * `ModelType.is_anthropic`
      * `ModelType.is_azure_openai`
      * `ModelType.is_gemini`
      * `ModelType.is_groq`
      * `ModelType.is_mistral`
      * `ModelType.is_nvidia`
      * `ModelType.is_open_source`
      * `ModelType.is_openai`
      * `ModelType.is_reka`
      * `ModelType.is_zhipuai`
      * `ModelType.supports_tool_calling`
      * `ModelType.token_limit`
      * `ModelType.validate_model_name()`
      * `ModelType.value_for_tiktoken`
    * `OpenAIBackendRole`
      * `OpenAIBackendRole.ASSISTANT`
      * `OpenAIBackendRole.FUNCTION`
      * `OpenAIBackendRole.SYSTEM`
      * `OpenAIBackendRole.TOOL`
      * `OpenAIBackendRole.USER`
    * `OpenAIImageType`
      * `OpenAIImageType.GIF`
      * `OpenAIImageType.JPEG`
      * `OpenAIImageType.JPG`
      * `OpenAIImageType.PNG`
      * `OpenAIImageType.WEBP`
    * `OpenAIVisionDetailType`
      * `OpenAIVisionDetailType.AUTO`
      * `OpenAIVisionDetailType.HIGH`
      * `OpenAIVisionDetailType.LOW`
    * `OpenAPIName`
      * `OpenAPIName.BIZTOC`
      * `OpenAPIName.COURSERA`
      * `OpenAPIName.CREATE_QR_CODE`
      * `OpenAPIName.KLARNA`
      * `OpenAPIName.NASA_APOD`
      * `OpenAPIName.OUTSCHOOL`
      * `OpenAPIName.SPEAK`
      * `OpenAPIName.WEB_SCRAPER`
    * `RoleType`
      * `RoleType.ASSISTANT`
      * `RoleType.CRITIC`
      * `RoleType.DEFAULT`
      * `RoleType.EMBODIMENT`
      * `RoleType.USER`
    * `StorageType`
      * `StorageType.MILVUS`
      * `StorageType.QDRANT`
    * `TaskType`
      * `TaskType.AI_SOCIETY`
      * `TaskType.CODE`
      * `TaskType.DEFAULT`
      * `TaskType.EVALUATION`
      * `TaskType.GENERATE_TEXT_EMBEDDING_DATA`
      * `TaskType.IMAGE_CRAFT`
      * `TaskType.MISALIGNMENT`
      * `TaskType.MULTI_CONDITION_IMAGE_CRAFT`
      * `TaskType.OBJECT_RECOGNITION`
      * `TaskType.ROLE_DESCRIPTION`
      * `TaskType.SOLUTION_EXTRACTION`
      * `TaskType.TRANSLATION`
      * `TaskType.VIDEO_DESCRIPTION`
    * `TerminationMode`
      * `TerminationMode.ALL`
      * `TerminationMode.ANY`
    * `VectorDistance`
      * `VectorDistance.COSINE`
      * `VectorDistance.DOT`
      * `VectorDistance.EUCLIDEAN`
    * `VoiceType`
      * `VoiceType.ALLOY`
      * `VoiceType.ECHO`
      * `VoiceType.FABLE`
      * `VoiceType.NOVA`
      * `VoiceType.ONYX`
      * `VoiceType.SHIMMER`
      * `VoiceType.is_openai`
  * camel.utils module
    * `AgentOpsMeta`
    * `AnthropicTokenCounter`
      * `AnthropicTokenCounter.count_tokens_from_messages()`
    * `BaseTokenCounter`
      * `BaseTokenCounter.count_tokens_from_messages()`
    * `Constants`
      * `Constants.DEFAULT_SIMILARITY_THRESHOLD`
      * `Constants.DEFAULT_TOP_K_RESULTS`
      * `Constants.FUNC_NAME_FOR_STRUCTURED_OUTPUT`
      * `Constants.VIDEO_DEFAULT_IMAGE_SIZE`
      * `Constants.VIDEO_DEFAULT_PLUG_PYAV`
      * `Constants.VIDEO_IMAGE_EXTRACTION_INTERVAL`
    * `GeminiTokenCounter`
      * `GeminiTokenCounter.count_tokens_from_messages()`
    * `LiteLLMTokenCounter`
      * `LiteLLMTokenCounter.calculate_cost_from_response()`
      * `LiteLLMTokenCounter.completion_cost`
      * `LiteLLMTokenCounter.count_tokens_from_messages()`
      * `LiteLLMTokenCounter.token_counter`
    * `MistralTokenCounter`
      * `MistralTokenCounter.count_tokens_from_messages()`
    * `OpenAITokenCounter`
      * `OpenAITokenCounter.count_tokens_from_messages()`
    * `OpenSourceTokenCounter`
      * `OpenSourceTokenCounter.count_tokens_from_messages()`
    * `agentops_decorator()`
    * `api_keys_required()`
    * `check_server_running()`
    * `create_chunks()`
    * `dependencies_required()`
    * `download_tasks()`
    * `func_string_to_callable()`
    * `get_first_int()`
    * `get_model_encoding()`
    * `get_prompt_template_key_words()`
    * `get_pydantic_major_version()`
    * `get_pydantic_object_schema()`
    * `get_system_information()`
    * `get_task_list()`
    * `handle_http_error()`
    * `is_docker_running()`
    * `json_to_function_code()`
    * `print_text_animated()`
    * `text_extract_from_web()`
    * `to_pascal()`
    * `track_agent()`
  * Module contents

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

