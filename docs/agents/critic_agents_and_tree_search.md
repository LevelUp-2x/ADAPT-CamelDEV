Skip to main content

__Back to top

__ `Ctrl`+`K`

[ ![](https://raw.githubusercontent.com/camel-
ai/camel/master/misc/primary_logo.png) CAMEL 0.1.9 ](../index.html)

Get Started

  * [Installation and Setup](../get_started/setup.html)

Agents

  * [Creating Your First Agent](single_agent.html)
  * [Creating Your First Agent Society](role_playing.html)
  * [Embodied Agents](embodied_agents.html)
  * Critic Agents and Tree Search

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

  * [ __ .md ](../_sources/agents/critic_agents_and_tree_search.md "Download source file")
  * __ .pdf

__

# Critic Agents and Tree Search

##  Contents

  * Philosophical Bits
  * Quick Start
    * 🕹 Step 0: Preparations
    * 🕹 Step 1: Configure the Specifications for Critic Agents
    * 🕹 Step 2: Get the Critic Agents
    * 🕹 Step 3: Using Critic Agents for Task Solving
  * Remarks

# Critic Agents and Tree Search#

## Philosophical Bits#

> **Prerequisite** : We assume that you have read the section on [intro to
> role-playing](https://github.com/camel-ai/camel/wiki/Creating-Your-First-
> Agent-Society).

How do agents accomplish hard tasks? While reasoning can naturally emerge from
next-token-prediction pretraining, it is still difficult for agents to solve
complex tasks which require lots of intermediate steps. To tackle this issue,
tree search is a simple and effective framework.

A typical tree search include node expansion and node selection. In the [March
2023 paper](https://arxiv.org/abs/2303.17760), CAMEL introduces a heuristic
tree search approach with critic in the loop, where the expansion and
selection are presented below:

![](https://i.imgur.com/6x4ABpp.png)

To put it simply, a critic agent is a helper agents in the role-playing
session, which is capable of selecting proposals and provide informative
verbal feedback to the role-playing agents.

## Quick Start#

### 🕹 Step 0: Preparations#

    
    
    from camel.agents import CriticAgent
    from camel.generators import SystemMessageGenerator as sys_msg_gen
    from camel.messages import BaseMessage as bm
    from camel.types import RoleType
    

### 🕹 Step 1: Configure the Specifications for Critic Agents#

    
    
    # Set the role name and the task
    critic_role = 'a picky critic'
    
    # Create the meta_dict and the role_tuple
    meta_dict = dict(critic_role=critic_role,
                     criteria='Help better accomplish the task.')
    
    # Create the role tuple
    role_tuple = (critic_role, RoleType.CRITIC)
    
    # Generate the system message
    sys_msg = sys_msg_gen().from_dict(meta_dict=meta_dict,
                                      role_tuple=role_tuple)
    

### 🕹 Step 2: Get the Critic Agents#

With the above arguments, we have:

    
    
    critic_agent = CriticAgent(system_message=sys_msg,
                               verbose=True)
    

Let’s take a look on the default system message:

    
    
    print(critic_agent.system_message.content)
    
    >>> You are a a picky critic who teams up with a {user_role} and a >>> {assistant_role} to solve a task: {task}.
        Your job is to select an option from their proposals and provides your explanations.
        Your selection criteria are Help better accomplish the task..
        You always have to choose an option from the proposals.
    

You may overwrite the system message and configure the critic differently
based on your own needs.

### 🕹 Step 3: Using Critic Agents for Task Solving#

Our `RolePlaying()` class provide a simple way for you to add the critic in
the loop. Below we provide a basic pipeline.

    
    
    # Import necessary classes
    from camel.societies import RolePlaying
    from camel.configs import ChatGPTConfig
    from camel.types import TaskType, ModelType, ModelPlatformType
    from colorama import Fore
    from camel.utils import print_text_animated
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
    

We then need to set the kwargs for the task and each agent:

    
    
    task_kwargs = {
        'task_prompt': 'Develop a plan to TRAVEL TO THE PAST and make changes.',
        'with_task_specify': True,
        'task_specify_agent_kwargs': {'model': model}
    }
    
    user_role_kwargs = {
        'user_role_name': 'an ambitious aspiring TIME TRAVELER',
        'user_agent_kwargs': {'model': model}
    }
    
    assistant_role_kwargs = {
        'assistant_role_name': 'the best-ever experimental physicist',
        'assistant_agent_kwargs': {'model': model}
    }
    
    critic_role_kwargs = {
        'with_critic_in_the_loop': True,
        'critic_criteria': 'improve the task performance',
        'critic_kwargs': dict(verbose=True)
    }
    

Putting them together:

    
    
    society = RolePlaying(
        **task_kwargs,             # The task arguments
        **user_role_kwargs,        # The instruction sender's arguments
        **assistant_role_kwargs,   # The instruction receiver's arguments
        **critic_role_kwargs,      # The critic's arguments       
    )
    

And the helper functions to run our society:

    
    
    def is_terminated(response):
        """
        Give alerts when the session shuold be terminated.
        """
        if response.terminated:
            role = response.msg.role_type.name
            reason = response.info['termination_reasons']
            print(f'AI {role} terminated due to {reason}')
    
        return response.terminated
    
    
    
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
    
    # We omit the real content here – try it on your own!
    >>> [AI User] Option 1: ...; Option 2: ...; Option 3: ...
    >>> [Critic] I would recommend option 2. This is because ...
    >>> [AI Assistant] Option 1: ...; Option 2: ...; Option 3: ...
    >>> [Critic] I would recommend option 1. This is because ...
    >>> ...
    

In this setting, the `AI User` and `AI Assistant` will generate different
options when responding (you can simply change the `temperature` in
`model_config` to somewhat control the diversity). `AI Critic` will respond
with its option selection and reasoning; such additional context will be fed
to the two other agents and help them form better subsequent responses.

## Remarks#

While we see some performance gains from critic-in-the-loop, it may not really
solve the fundamental extrapolation problem (and [self-
consistency](https://arxiv.org/abs/2203.11171) remains a strong baseline for
many tasks). It is debatable if those agents can extrapolate by self-play
within its current scale. A more practical question is how we may
_efficiently_ introduce _informative_ feedbacks/rewards, when agents are
connected with external environments and are endowed with tools and memories.
They are expected to have a good world model and know how to make abstraction
and analogy when necessary. Stay tuned for our next update.

[ __ previous Embodied Agents ](embodied_agents.html "previous page") [ next
Loaders __](../key_modules/loaders.html "next page")

__Contents

  * Philosophical Bits
  * Quick Start
    * 🕹 Step 0: Preparations
    * 🕹 Step 1: Configure the Specifications for Critic Agents
    * 🕹 Step 2: Get the Critic Agents
    * 🕹 Step 3: Using Critic Agents for Task Solving
  * Remarks

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

