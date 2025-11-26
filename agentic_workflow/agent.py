from google.adk.agents import SequentialAgent
from agentic_workflow.agents.meal_planner_agent import meal_planner_agent
from agentic_workflow.agents.shopping_agent import shopping_agent
from agentic_workflow.agents.notification_agent import notification_agent



root_agent = SequentialAgent(name="daily_meal_planning_workflow",
                description="A workflow that plans meals, generates shopping list, and sends notification to user.",
                sub_agents=[meal_planner_agent, shopping_agent, notification_agent])