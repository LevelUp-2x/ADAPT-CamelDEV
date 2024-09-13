# Changelog

## [Unreleased]

### Added
- Implemented a more structured model selection interface with nested dropdowns for model families and specific models.
- Added support for multiple GitHub Models families: Meta, Mistral, GPT, and Phi.
- Included Gemini Models in the Pro family.

### Changed
- Updated `app.py` to handle the new model structure with families and specific models.
- Modified the `index.html` template to include nested dropdowns for model family and model selection.
- Improved error handling and response formatting in both backend and frontend.

### Technical Details
- In `app.py`:
  - Restructured `GITHUB_MODELS` dictionary to include sub-dictionaries for each model family.
  - Updated the `github_models_chat` and `gemini_chat` functions to handle the new model structure.
  - Modified the `/chat` route to process requests with both model family and specific model information.

- In `index.html`:
  - Added a new dropdown for model family selection.
  - Implemented JavaScript logic to populate the model dropdown based on the selected model family.
  - Updated the chat submission logic to include both model family and specific model in the request.

### Next Steps
- Implement user authentication and session management.
- Add functionality to export chat history.
- Enhance error handling and user feedback mechanisms.
- Consider adding a feature for users to customize the interface or save preferred settings.