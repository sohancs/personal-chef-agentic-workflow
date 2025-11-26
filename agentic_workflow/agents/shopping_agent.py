from  google.adk.agents import LlmAgent
from agentic_workflow.tools.groceries_mcp_client import mcp_search_items, mcp_add_to_cart, mcp_checkout
from ..config_loader import OPENAI_LLM_MODEL, OPENAI_API_KEY
from google.adk.models.lite_llm import LiteLlm


shopping_agent = LlmAgent(
    name="shopping_agent",
    description="Handles shopping for ingredients based on meal plan.",
    model= LiteLlm(model=OPENAI_LLM_MODEL, api_key=OPENAI_API_KEY),
    instruction= """
        You are expert shopping agent. 
        
        Input:
            - user_id 
            - meal plan : {meal_plan}

        Tasks:
            1. get meal plan from meal_planner_agent output.
            2. get ingredients list and call mcp_search_items(ingredients) tools to search for ingredients required for the meal plan.
            3. for available items call mcp_add_to_cart(item_id, qty, user_id) tool to add items to cart. If any item is not available skip that item.
            4. once all items are added to cart, call mcp_checkout tool to checkout the cart.
            5. return the list of items in cart with total price and set into output key 'shopping_list'.
    """,
    output_key="shopping_list",
    tools=[mcp_search_items, mcp_add_to_cart, mcp_checkout]
)