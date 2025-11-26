from google.adk.agents import LlmAgent
from agentic_workflow.tools.telegram_tool import send_telegram_msg
from ..config_loader import OPENAI_LLM_MODEL, OPENAI_API_KEY
from google.adk.models.lite_llm import LiteLlm

notification_agent = LlmAgent(
    name="notfication_agent",
    description="Sends meal plan and shopping list notification to user via telegram.",
    model= LiteLlm(model=OPENAI_LLM_MODEL, api_key=OPENAI_API_KEY),
    instruction= """
        You are expert notifcaiton agent and responsible to send notification to user in human friendly format via telegram.
        
        Input : 
            - user_id
            - meal plan : {meal_plan}
            - shopping list with total price : {shopping_list}

        If user not available, use user_id as 'User'.

        Steps:
            1. Write a human friendly message.
            2. call send_telegram_msg tool to send message via telegram.
            3. return the response from telegram tool.
            4. send two messages, first message contains meal plan and second message contains shopping list with total price.
    
    """,
    tools=[send_telegram_msg]
)
