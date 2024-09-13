# ADAPT-CamelDEV Project

## Overview
This project implements an AI Chat Interface that allows users to interact with various language models from different providers, including GitHub Models and Gemini.

## Recent Updates
- Implemented a more structured model selection interface with nested dropdowns for model families and specific models.
- Added support for multiple GitHub Models families: Meta, Mistral, GPT, and Phi.
- Included Gemini Models in the Pro family.

For a detailed list of changes, please refer to the [CHANGELOG.md](langchain_integration/CHANGELOG.md) file.

## Features
- Web-based chat interface
- Support for multiple AI model providers
- Nested model selection (family and specific model)
- Response time tracking
- Markdown rendering for responses

## Setup and Installation
1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your environment variables in a `.env` file:
   ```
   GitHub_ADAPT-Chase_MODELS_TOKEN=your_github_token
   GITHUB_MODELS_ENDPOINT=your_github_endpoint
   Gemini_Studio_CHASE_API_KEY=your_gemini_api_key
   ```

## Running the Application
To start the Flask application, run:
```
python langchain_integration/app.py
```
Then open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage
1. Select a model family from the first dropdown.
2. Choose a specific model from the second dropdown.
3. Enter your prompt in the text area.
4. Click "Submit" or press Enter to send your request.
5. View the AI's response and the response time in the chat history.

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- GitHub Models API
- Gemini API
- Flask framework
- TailwindCSS for styling
