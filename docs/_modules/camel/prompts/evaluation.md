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

# Source code for camel.prompts.evaluation

    
    
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
    from typing import Any
    
    from camel.prompts.base import TextPrompt, TextPromptDict
    
    
    
    
    [[docs]](../../../camel.prompts.html#camel.prompts.EvaluationPromptTemplateDict)class EvaluationPromptTemplateDict(TextPromptDict):
        r"""A dictionary containing :obj:`TextPrompt` used in the `Evaluation`
        task.
    
        Attributes:
            GENERATE_QUESTIONS (TextPrompt): A prompt to generate a set of
                questions to be used for evaluating emergence of knowledge based
                on a particular field of knowledge.
        """
    
        GENERATE_QUESTIONS = TextPrompt(
            """Generate {num_questions} {category} diverse questions.
    Here are some example questions:
    {examples}
    
    Now generate {num_questions} questions of your own. Be creative"""
        )
    
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            super().__init__(*args, **kwargs)
            self.update(
                {
                    "generate_questions": self.GENERATE_QUESTIONS,
                }
            )
    
    
    

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

