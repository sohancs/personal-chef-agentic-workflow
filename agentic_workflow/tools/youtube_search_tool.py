
def youtube_recipe_search(dish_name: str) :
    """
    Search for recipe videos on Youtube for given dish name.

    Args:
        dish_name (str) : Name of dish for searchhing recipe vidoes. 

    return:
        list: A list of video's title and video url pairs. Maximmum 3 videos per dish
    """

    search_query = '+'.join(dish_name.split())
    return [
        {"title" : f"{dish_name} recipe" , "url" : f"https://www.youtube.com/results?search_query={search_query}+recipe"}
    ]