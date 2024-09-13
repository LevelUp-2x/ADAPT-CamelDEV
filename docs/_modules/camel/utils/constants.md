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

# Source code for camel.utils.constants

    
    
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
    
    
    
    
    [[docs]](../../../camel.html#camel.utils.Constants)class Constants:
        # This value defines the default size (both width and height) for images
        # extracted from a video.
        VIDEO_DEFAULT_IMAGE_SIZE = 768
    
        # This value defines the interval (in number of frames) at which images
        # are extracted from the video.
        VIDEO_IMAGE_EXTRACTION_INTERVAL = 50
    
        # Default plug of imageio to read video
        VIDEO_DEFAULT_PLUG_PYAV = "pyav"
    
        # Return response with json format
        FUNC_NAME_FOR_STRUCTURED_OUTPUT = "return_json_response"
    
        # Default top k vaule for RAG
        DEFAULT_TOP_K_RESULTS = 1
    
        # Default similarity threshold vaule for RAG
        DEFAULT_SIMILARITY_THRESHOLD = 0.7
    
    
    

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

