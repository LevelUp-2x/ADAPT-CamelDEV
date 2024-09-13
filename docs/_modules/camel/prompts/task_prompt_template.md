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

# Source code for camel.prompts.task_prompt_template

    
    
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
    from typing import Any, Dict
    
    from camel.prompts.ai_society import (
        AISocietyPromptTemplateDict,
        TextPromptDict,
    )
    from camel.prompts.code import CodePromptTemplateDict
    from camel.prompts.evaluation import (
        EvaluationPromptTemplateDict,
    )
    from camel.prompts.generate_text_embedding_data import (
        GenerateTextEmbeddingDataPromptTemplateDict,
    )
    from camel.prompts.image_craft import ImageCraftPromptTemplateDict
    from camel.prompts.misalignment import MisalignmentPromptTemplateDict
    from camel.prompts.multi_condition_image_craft import (
        MultiConditionImageCraftPromptTemplateDict,
    )
    from camel.prompts.object_recognition import (
        ObjectRecognitionPromptTemplateDict,
    )
    from camel.prompts.role_description_prompt_template import (
        RoleDescriptionPromptTemplateDict,
    )
    from camel.prompts.solution_extraction import (
        SolutionExtractionPromptTemplateDict,
    )
    from camel.prompts.translation import TranslationPromptTemplateDict
    from camel.prompts.video_description_prompt import (
        VideoDescriptionPromptTemplateDict,
    )
    from camel.types import TaskType
    
    
    
    
    [[docs]](../../../camel.prompts.html#camel.prompts.task_prompt_template.TaskPromptTemplateDict)class TaskPromptTemplateDict(Dict[Any, TextPromptDict]):
        r"""A dictionary (:obj:`Dict[Any, TextPromptDict]`) of task prompt
        templates keyed by task type. This dictionary is used to map from
        a task type to its corresponding prompt template dictionary.
    
        Args:
            *args: Positional arguments passed to the :obj:`dict` constructor.
            **kwargs: Keyword arguments passed to the :obj:`dict` constructor.
        """
    
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            super().__init__(*args, **kwargs)
            self.update(
                {
                    TaskType.AI_SOCIETY: AISocietyPromptTemplateDict(),
                    TaskType.CODE: CodePromptTemplateDict(),
                    TaskType.MISALIGNMENT: MisalignmentPromptTemplateDict(),
                    TaskType.TRANSLATION: TranslationPromptTemplateDict(),
                    TaskType.EVALUATION: EvaluationPromptTemplateDict(),
                    TaskType.SOLUTION_EXTRACTION: SolutionExtractionPromptTemplateDict(),  # noqa: E501
                    TaskType.ROLE_DESCRIPTION: RoleDescriptionPromptTemplateDict(),
                    TaskType.OBJECT_RECOGNITION: ObjectRecognitionPromptTemplateDict(),  # noqa: E501
                    TaskType.GENERATE_TEXT_EMBEDDING_DATA: GenerateTextEmbeddingDataPromptTemplateDict(),  # noqa: E501
                    TaskType.IMAGE_CRAFT: ImageCraftPromptTemplateDict(),
                    TaskType.MULTI_CONDITION_IMAGE_CRAFT: MultiConditionImageCraftPromptTemplateDict(),  # noqa: E501
                    TaskType.VIDEO_DESCRIPTION: VideoDescriptionPromptTemplateDict(),  # noqa: E501
                }
            )
    
    
    

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

