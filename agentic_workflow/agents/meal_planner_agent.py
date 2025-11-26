from google.adk.agents import LlmAgent
from agentic_workflow.tools.user_preferences_tool import fetch_user_preferences
from agentic_workflow.tools.youtube_search_tool import youtube_recipe_search
from ..config_loader import OPENAI_LLM_MODEL, OPENAI_API_KEY
from google.adk.models.lite_llm import LiteLlm

meal_planner_agent = LlmAgent(
    name="meal_planner_agent",
    description="Creates daily meal plan based on user preferences.",
    model= LiteLlm(model=OPENAI_LLM_MODEL, api_key=OPENAI_API_KEY),
    instruction=    """
        You are expert meal planner. Create a daily meal plan based on user preferences.

        Input:
            - user_id

        If user not available, create a meal plan based on user inputs.

        Tasks:
        1. get user preferences using calling fetch_user_preferences(user_id) tool.
        2. create a meal plan for next days considering user preferences which includes meal for breakfast, lunch, dinner.
        3. for each meal suggest 
            - dish name
            - ingredients required
            - youtube url using youtube_recipe_search(dish_name) tool.
        
        4. Return the meal plan in below format and set into output key 'meal_plan':
        {
                "breakfast" : {},
                "lunch" : {},
                "dinner" : {}
        }

    """,
    output_key="meal_plan",
    tools=[
        fetch_user_preferences, 
        youtube_recipe_search]
)