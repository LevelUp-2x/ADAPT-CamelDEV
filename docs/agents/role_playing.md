Skip to main content

__Back to top

__ `Ctrl`+`K`

[ ![](https://raw.githubusercontent.com/camel-
ai/camel/master/misc/primary_logo.png) CAMEL 0.1.9 ](../index.html)

Get Started

  * [Installation and Setup](../get_started/setup.html)

Agents

  * [Creating Your First Agent](single_agent.html)
  * Creating Your First Agent Society
  * [Embodied Agents](embodied_agents.html)
  * [Critic Agents and Tree Search](critic_agents_and_tree_search.html)

Key Modules

  * [Loaders](../key_modules/loaders.html)
  * [Storages](../key_modules/storages.html)
  * [Embeddings](../key_modules/embeddings.html)
  * [Retrievers](../key_modules/retrievers.html)

Tutorial and Cookbooks

  * [🐫 Agents with RAG](../tutorials_and_cookbooks/agents_with_rag.html)

API References

  * [camel](../modules.html) __
    * [Camel Package](../camel.html) __
      * [camel.agents package](../camel.agents.html)
      * [camel.prompts package](../camel.prompts.html)

__

  * [ __ .md ](../_sources/agents/role_playing.md "Download source file")
  * __ .pdf

__

# Creating Your First Agent Society

##  Contents

  * Philosophical Bits
  * Quick Start
    * Step 0: Preparations
    * Step 1: Configure the Role-Playing Session
      * Set the `Task` Arguments
      * Set the `User` Arguments
      * Set the `Assistant` Arguments
    * Step 2: Kickstart Your Society
    * Step 3: Solving Tasks with Your Society
  * Remarks

# Creating Your First Agent Society#

## Philosophical Bits#

[![Colab](https://colab.research.google.com/assets/colab-
badge.svg)](https://colab.research.google.com/drive/1HU4-sxNWFTs9JOegGbKOBcgHjDfj8FX5?usp=sharing)

> _What magical trick makes us intelligent? The trick is that there is no
> trick. The power of intelligence stems from our vast diversity, not from any
> single, perfect principle._
>
> – Marvin Minsky, The Society of Mind, p. 308

In this section, we will take a spite of the task-oriented `RolyPlaying()`
class. We design this in an instruction-following manner. The essence is that
to solve a complex task, you can enable two communicative agents
collabratively working together step by step to reach solutions. The main
concepts include:

  * **Task** : a task can be as simple as an idea, initialized by an inception prompt.

  * **AI User** : the agent who is expected to provide instructions.

  * **AI Assistant** : the agent who is expected to respond with solutions that fulfills the instructions.

## Quick Start#

### Step 0: Preparations#

    
    
    # Import necessary classes
    from camel.societies import RolePlaying
    from camel.types import TaskType, ModelType, ModelPlatformType
    from camel.models import ModelFactory
    
    # Set the LLM model type and model config
    model_platform = ModelPlatformType.OPENAI
    model_type = ModelType.GPT_3_5_TURBO
    model_config = ChatGPTConfig(
        temperature=0.8,  # the sampling temperature; the higher the more random
        n=3,              # the no. of completion choices to generate for each input
        )
    
    # Create the backend model
    model = ModelFactory.create(
        model_platform=model_platform,
        model_type=model_type,
        model_config=model_config)
    

### Step 1: Configure the Role-Playing Session#

#### Set the `Task` Arguments#

    
    
    task_kwargs = {
        'task_prompt': 'Develop a plan to TRAVEL TO THE PAST and make changes.',
        'with_task_specify': True,
        'task_specify_agent_kwargs': {'model': model}
    }
    

#### Set the `User` Arguments#

You may think the user as the `instruction sender`.

    
    
    user_role_kwargs = {
        'user_role_name': 'an ambitious aspiring TIME TRAVELER',
        'user_agent_kwargs': {'model': model}
    }
    

#### Set the `Assistant` Arguments#

Again, you may think the assistant as the `instruction executor`.

    
    
    assistant_role_kwargs = {
        'assistant_role_name': 'the best-ever experimental physicist',
        'assistant_agent_kwargs': {'model': model}
    }
    

### Step 2: Kickstart Your Society#

Putting them altogether – your role-playing session is ready to go!

    
    
    society = RolePlaying(
        **task_kwargs,             # The task arguments
        **user_role_kwargs,        # The instruction sender's arguments
        **assistant_role_kwargs,   # The instruction receiver's arguments
    )
    

### Step 3: Solving Tasks with Your Society#

Hold your bytes. Prior to our travel, let’s define a small helper function.

    
    
    def is_terminated(response):
        """
        Give alerts when the session shuold be terminated.
        """
        if response.terminated:
            role = response.msg.role_type.name
            reason = response.info['termination_reasons']
            print(f'AI {role} terminated due to {reason}')
    
        return response.terminated
    

Time to chart our course – writing a simple loop for our society to proceed:

    
    
    def run(society, round_limit: int=10):
    
        # Get the initial message from the ai assistant to the ai user
        input_msg = society.init_chat()
    
        # Starting the interactive session
        for _ in range(round_limit):
    
            # Get the both responses for this round
            assistant_response, user_response = society.step(input_msg)
    
            # Check the termination condition
            if is_terminated(assistant_response) or is_terminated(user_response):
                break
    
            # Get the results
            print(f'[AI User] {user_response.msg.content}.\n')
            print(f'[AI Assistant] {assistant_response.msg.content}.\n')
    
            # Check if the task is end
            if 'CAMEL_TASK_DONE' in user_response.msg.content:
                break
    
            # Get the input message for the next round
            input_msg = assistant_response.msg
    
        return None
    

Now let’s set our code in motion:

    
    
    run(society)
    

There you have your two lovely agents working collaboratively together to
fulfill your requests. : )

    
    
    >>> [AI User] Instruction: Provide the theoretical framework for creating a stable wormhole or manipulating spacetime for controlled travel to a specific historical era in the past.
    >>> [AI Assistant] Solution: To create a theoretical framework for stable wormhole creation or spacetime manipulation for controlled time travel, we can start by considering the principles of general relativity and quantum mechanics.
    >>> ... (omitted)
    >>> [AI User] <CAMEL_TASK_DONE>.
    >>> [AI Assistant] Great! Good luck with your ambitious endeavors in time travel!.
    

## Remarks#

We hope you enjoy thie adventure with the two communicative agents. In the
following chapters, we will discuss various types of agents, and how we can
elicit complex task solving ability for large language models within our
framework. Stay tuned.

[ __ previous Creating Your First Agent ](single_agent.html "previous page") [
next Embodied Agents __](embodied_agents.html "next page")

__Contents

  * Philosophical Bits
  * Quick Start
    * Step 0: Preparations
    * Step 1: Configure the Role-Playing Session
      * Set the `Task` Arguments
      * Set the `User` Arguments
      * Set the `Assistant` Arguments
    * Step 2: Kickstart Your Society
    * Step 3: Solving Tasks with Your Society
  * Remarks

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

