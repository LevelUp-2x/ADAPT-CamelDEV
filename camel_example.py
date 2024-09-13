from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelType, ModelPlatformType

def main():
    # Set up the Gemini model
    gemini_model = ModelFactory.create(
        model_platform=ModelPlatformType.GEMINI,
        model_type=ModelType.GEMINI_PRO,
        model_config_dict={"temperature": 0.7},
        api_key=os.getenv('Gemini_Studio_CHASE_API_KEY') or os.getenv('Gemini_Studio_LIQUIDMOVZ_API_KEY')
    )

    # Create a chat agent with the Gemini model
    assistant_sys_msg = BaseMessage.make_assistant_message(
        role_name="Assistant",
        content="You are a helpful assistant.",
    )
    gemini_agent = ChatAgent(assistant_sys_msg, model=gemini_model)

    # Test the Gemini agent
    user_msg = BaseMessage.make_user_message(
        role_name="User", content="Explain what CAMEL is in one sentence."
    )
    gemini_response = gemini_agent.step(user_msg)
    print("Gemini response:", gemini_response.msg.content)

if __name__ == "__main__":
    main()
