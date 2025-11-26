
def fetch_user_preferences(user_id) :
    """
    Fetch user preferences from the user preferences database.

    Args:
        user_id (str): The unique identifier of the user.
    
    If user_id not found, then take preference from user inputs.
    
    Returns:
        dict: A dictionary containing user preferences such as dietary restrictions, favorite cuisines, and calories per day.
    """

    return meal_preference_db[user_id]


# Mock user preferences database
meal_preference_db = meal_preferences = {
    "user_101": {
        "allergy": ["peanuts", "shellfish"],
        "cuisines": ["Italian", "Mexican"],
        "calories": 2000
    },
    "user_102": {
        "allergy": ["gluten"],
        "cuisines": ["Indian", "Thai"],
        "calories": 1800
    },
    "user_103": {
        "allergy": [],
        "cuisines": ["India", "Japanese"],
        "calories": 2200
    },
    "user_104": {
        "allergy": ["dairy"],
        "cuisines": ["French", "Vietnamese"],
        "calories": 1900
    },
    "user_105": {
        "allergy": ["soy", "eggs"],
        "cuisines": ["Chinese", "Korean"],
        "calories": 2100
    }
}
