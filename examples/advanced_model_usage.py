import asyncio
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

# Initialize models
github_model = ModelFactory.create(
    model_platform=ModelPlatformType.GITHUB,
    model_type=ModelType.GITHUB_COPILOT,
    model_config_dict={},
    api_key="your_github_api_key"
)

gemini_model = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_1_5_PRO,
    model_config_dict={},
    api_key="your_gemini_api_key"
)

async def code_generation_and_explanation():
    """
    This example demonstrates using GitHub Copilot to generate code
    and Gemini to explain the generated code.
    """
    # Generate code using GitHub Copilot
    code_prompt = "Write a Python function to implement the merge sort algorithm."
    code = await github_model.generate(code_prompt, max_tokens=300, temperature=0.7)
    
    print("Generated Code:")
    print(code)
    
    # Use Gemini to explain the code
    explanation_prompt = f"Explain the following Python code in simple terms:\n\n{code}"
    explanation = await gemini_model.generate(explanation_prompt, max_tokens=200, temperature=0.5)
    
    print("\nCode Explanation:")
    print(explanation)

async def collaborative_problem_solving():
    """
    This example shows how to use both models collaboratively
    to solve a complex problem.
    """
    problem = "Design a system to manage a smart home, including temperature control, lighting, and security."
    
    # Use Gemini for high-level system design
    design_prompt = f"Provide a high-level design for the following system:\n{problem}"
    high_level_design = await gemini_model.generate(design_prompt, max_tokens=300, temperature=0.7)
    
    print("High-level System Design:")
    print(high_level_design)
    
    # Use GitHub Copilot to generate code structure based on the design
    code_structure_prompt = f"Based on this high-level design, provide a Python code structure with class definitions and main methods:\n{high_level_design}"
    code_structure = await github_model.generate(code_structure_prompt, max_tokens=500, temperature=0.7)
    
    print("\nCode Structure:")
    print(code_structure)

async def iterative_code_improvement():
    """
    This example demonstrates an iterative process of code generation and improvement
    using both models.
    """
    initial_prompt = "Write a Python function to find the longest palindromic substring in a given string."
    
    # Generate initial code with GitHub Copilot
    initial_code = await github_model.generate(initial_prompt, max_tokens=300, temperature=0.7)
    
    print("Initial Code:")
    print(initial_code)
    
    # Use Gemini to analyze and suggest improvements
    analysis_prompt = f"Analyze the following code and suggest improvements for efficiency and readability:\n\n{initial_code}"
    analysis = await gemini_model.generate(analysis_prompt, max_tokens=200, temperature=0.5)
    
    print("\nCode Analysis and Suggestions:")
    print(analysis)
    
    # Use GitHub Copilot to implement the suggested improvements
    improvement_prompt = f"Improve the following code based on these suggestions:\n\nCode:\n{initial_code}\n\nSuggestions:\n{analysis}"
    improved_code = await github_model.generate(improvement_prompt, max_tokens=400, temperature=0.7)
    
    print("\nImproved Code:")
    print(improved_code)

async def main():
    await code_generation_and_explanation()
    print("\n" + "="*50 + "\n")
    await collaborative_problem_solving()
    print("\n" + "="*50 + "\n")
    await iterative_code_improvement()

if __name__ == "__main__":
    asyncio.run(main())