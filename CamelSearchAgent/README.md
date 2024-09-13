# CAMEL Search Agent

This project implements a search agent using the CAMEL framework with LangChain and DuckDuckGo search integration.

## Setup

1. Ensure you have Python 3.10 or later installed.

2. Clone this repository:
   ```
   git clone <repository_url>
   cd <repository_directory>
   ```

3. Install the required packages:
   ```
   pip install langchain langchain_community langchain_openai python-dotenv duckduckgo-search
   ```

4. Set up your OpenAI API key:
   - Open the `.env` file in the root directory of the project.
   - Replace `your_openai_api_key_here` with your actual OpenAI API key:
     ```
     OPENAI_API_KEY=your_actual_api_key_here
     ```
   - Save the file.

   **Important:** Never commit your actual API key to version control. Make sure `.env` is included in your `.gitignore` file.

## Running the Search Agent

To run the search agent:

1. Open a terminal in the project directory.
2. Run the following command:
   ```
   python search_agent.py
   ```

The agent will ask a predefined question about the current weather in New York City. You can modify the question in the `search_agent.py` file to ask different questions.

## Customizing the Agent

You can customize the agent's behavior by modifying the `search_agent.py` file. You can change the search tool, add new tools, or modify the prompt template to suit your needs.

## Troubleshooting

If you encounter any issues related to the OpenAI API key, make sure:
- You've correctly added your API key to the `.env` file.
- The `.env` file is in the same directory as `search_agent.py`.
- You have an active OpenAI API subscription with available credits.

For any other issues, please check the error messages and ensure all dependencies are correctly installed.

## License

[Include your license information here]

## Contributing

[Include contribution guidelines if applicable]