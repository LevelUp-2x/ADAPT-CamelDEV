# CAMEL Adaptation Blueprint

## Overview

This document outlines the blueprint for adapting the CAMEL project to meet the specific needs of our ADAPT-CamelDEV implementation. We'll focus on integrating our GitHub and Gemini models into a streamlined and effective system.

## Key Concepts from CAMEL Documentation

- **Practical Artificial General Intelligence:**  CAMEL aims to develop AI systems with real-world applications.
- **LLM-Based Multi-Agent Framework:** The core of CAMEL lies in its use of large language models (LLMs) for building multi-agent systems.
- **Scalability and Flexibility:** The framework is designed for scalability and flexibility, enabling diverse applications and research exploration.

## Core Components for ADAPT-CamelDEV

Based on our initial analysis, we'll focus on adapting the following core components from CAMEL:

- **ChatAgent:** The primary agent class for handling conversations and interactions.
- **BaseMessage:** The class responsible for managing messages exchanged between agents and users.
- **ModelFactory:** The module that handles the initialization and selection of different LLM models, including our GitHub and Gemini models.
- **GitHub Toolkit:** We'll adapt or develop a custom toolkit to leverage CAMEL functionalities for interacting with GitHub repositories.
- **RolePlaying:** The class responsible for setting up and managing role-playing scenarios between two agents.

We'll exclude components that are not directly relevant to our implementation, such as embodied agents or specific retrieval mechanisms.

## Data Flow

1. **User Input:** The user provides input, which is encapsulated in a `BaseMessage` object.
2. **Agent Processing:** The `ChatAgent` receives the `BaseMessage` and utilizes the appropriate `TextPrompt` or `CodePrompt` to interact with the chosen LLM.
3. **Model Interaction:** The LLM processes the prompt and generates a response.
4. **Response Generation:** The `ChatAgent` receives the LLM's response, packages it into a `BaseMessage`, and returns it to the user.

## Message Handling

- **BaseMessage Class:** The foundation for all message objects in CAMEL, ensuring a consistent structure.
- **Message Creation:** CAMEL provides convenience methods for creating user and assistant messages.
- **Message Conversion:** The `BaseMessage` class offers methods for converting messages to different formats, including OpenAI message formats.

## Model Integration

- **ModelFactory:** Our GitHub and Gemini models will be integrated into the `ModelFactory`, allowing for seamless selection and initialization within the `ChatAgent`.

## ChatAgent Details

- **Role Definition:** The `ChatAgent`'s role and behavior are defined using a system message (`BaseMessage`).
- **Interaction:** The `.step()` method is used for interacting with the agent, providing a user message (`BaseMessage`) and receiving the agent's response (`BaseMessage`).
- **Tool Integration:** External tools can be integrated into the `ChatAgent` using `camel.toolkits`, providing access to specialized functionalities.
- **Memory Management:** The `ChatAgent` uses `ChatHistoryMemory` by default for in-context learning. External databases can be integrated for long-term memory management.
- **Additional Functionalities:** The `ChatAgent` class includes methods for resetting the agent's state (`reset()`), setting the output language (`set_output_language()`), and using open-source LLMs.

## Role-Playing Implementation

- **RolePlaying Class:** Facilitates multi-agent interactions, specifically for role-playing between an "AI User" and an "AI Assistant."
- **Task Definition:** The `RolePlaying` class allows defining a task using an inception prompt, setting the overall goal for the agents.
- **Agent Configuration:** Separate argument dictionaries define the roles, characteristics, and models for the AI User and AI Assistant.
- **Interaction Loop:** The `RolePlaying` class manages the conversation flow between the agents through the `init_chat()` and `step()` methods, enabling iterative communication and problem-solving.

## Embodied Agents

- **EmbodiedAgent Class:** Extends the `ChatAgent`'s capabilities by enabling interaction with an environment through code execution and tool usage.
- **Code Interpretation:**  Utilizes a code interpreter (default: `SubProcessInterpreter`) to execute code snippets, enabling interactions with the operating system and external services.
- **Tool Agent Integration:** Can integrate with tool agents to access and utilize specialized functionalities.
- **User Confirmation:** Requests user confirmation before executing potentially impactful actions in the environment.

## Data Loading

- **Base IO:** Provides fundamental file I/O operations, supporting various file formats. Represents files as `File` objects.
- **Unstructured IO:** Handles unstructured data processing, offering tools for parsing, cleaning, extracting information, chunking, and staging elements for different platforms. Particularly useful for RAG applications.

## Data Storage

- **Storage Module:** Provides a framework for managing persistent data storage, encompassing both key-value and vector storage systems.
- **Key-Value Storages:** Suitable for storing structured data as key-value pairs, useful for conversation history and agent states. Examples include `InMemoryKeyValueStorage` and `JsonStorage`.
- **VectorDB Storages:** Designed for storing and retrieving vector embeddings, often used for semantic search. Examples include `MilvusStorage` and `QdrantStorage`.

## Embeddings

- **Purpose:** Transform various data types (text, images, etc.) into numerical vectors, capturing essential features and semantic meaning.
- **Text Embeddings:** Focus on converting text into vectors, enabling semantic comparison and analysis. CAMEL supports OpenAI Embeddings and SentenceTransformerEncoder for this purpose.
- **Image Embeddings (WIP):**  Aim to represent images as vectors for image-based tasks (currently under development).

## Retrievers

- **Purpose:** Retrieve relevant information from large datasets based on user queries or agent requests.
- **Vector Retriever:** Uses vector representations (embeddings) for semantic search, comparing query embeddings to stored document embeddings.
- **Keyword Retriever:** Relies on exact keyword matching between queries and documents.
- **Auto Retriever:** Simplifies the retrieval process by handling embedding, storage, and querying, particularly useful for multiple data sources.

## Toolkit Design

- **Prompt Utilization:** Our GitHub toolkit will leverage the `TextPrompt` and `CodePrompt` classes to interact with the GitHub model, facilitating tasks like code analysis, documentation generation, and issue management.
- **Code Execution:** The `CodePrompt`'s `execute` method can be used to execute code snippets retrieved from GitHub or generated by the model, enabling automated code testing and validation.

## Error Handling and Logging

(To be defined in detail as we progress through the documentation)

This blueprint will be continuously updated as we analyze the CAMEL documentation and refine our understanding of its components and functionalities.