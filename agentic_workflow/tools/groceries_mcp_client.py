import requests

MCP_SERVER_BASE_URL = "http://localhost:8085"


def mcp_search_items(items: list[str]) :
    """
    Search for items in the Groceries MCP inventory.

    Args:
        items (list[str]): List of item names to search for.
    
    Returns:
        dict: A dictionary containing available and not available items.

    """

    response = requests.post(
        f"{MCP_SERVER_BASE_URL}/search_items",
        json={"items" : items}
    )

    return response.json()

def mcp_add_to_cart(item_id: str, qty: int, user_id: str) :
    """
        Add an item to the user's cart in the Groceries MCP.

        Args:
            item_id (str): The ID of the item to add.
            qty (int): The quantity of the item to add.
            user_id (str): The ID of the user.

        Returns :
            list : A list of items in the user's cart after addition.
     """

    response = requests.post(
        f"{MCP_SERVER_BASE_URL}/add_to_cart",
        json={
            "item_id" : item_id,
            "qty" : qty,
            "user_id" : user_id
        }
    )

    return response.json()


def mcp_checkout(user_id : str) :
    """
        Checkout the user's cart in the Groceries MCP.

        Args:
            user_id (str): The ID of the user.

        Returns :
            dict : A summary of the checkout including total price (AED).
     """
    
    print(f"input pass to mcp_checkout: user_id - {user_id}")
    
    response = requests.get(
        f"{MCP_SERVER_BASE_URL}/checkout?user_id={user_id}"
    )

    return response.json()

def get_all_inventory():
    """
        Get all inventory items from the Groceries MCP.

        Returns :
            list : A list of all inventory items.
     """
    
    print("inside get_all_inventory")
    
    response = requests.get(
        f"{MCP_SERVER_BASE_URL}/get_all_inventory"
    )

    return response.json()