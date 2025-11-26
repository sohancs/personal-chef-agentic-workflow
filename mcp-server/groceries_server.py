from fastapi import FastAPI
from models import SearchItemsRequest, AddToCartRequest
from inventory import inventory_data

app = FastAPI(title="Groceries MCP Server")

# Load inventory data
inventory = inventory_data

cart = {}

@app.get("/heath")
def heath_check():
    return {"status" : "ok"}

@app.post("/search_items")
def search_items(request_items : SearchItemsRequest):
    print(f"input pass to search_items: request_items - {request_items}")
    requested_items = [req_item.lower() for req_item in request_items.items]
    #inventory_item_name = [item["name"].lower() for item in inventory]
   
    # avbl_items = [item for item in requested_items if any(item in inv for inv in inventory_item_name)]
    # not_avbl_items = [item for item in requested_items if not any(item in inv for inv in inventory_item_name)]

    avbl_items = [inv for inv in inventory if any(inv["name"].lower() in req_item for req_item in requested_items)]
    #not_avbl_items = [inv for inv in inventory if not any(inv["name"].lower()  in req_item for req_item in requested_items)]

    return {
        "available_items" : avbl_items
       # "not_available_items" : not_avbl_items
    }

@app.get("/get_all_inventory")
def get_all_inventory():
    print("Fetching all inventory items.")
    return inventory

@app.post("/add_to_cart")
def add_to_cart(request_items : AddToCartRequest):
    print(f"input pass to add_to_cart: request_items - {request_items}")

    req_item_id = request_items.item_id
    qty = request_items.qty
    user_id = request_items.user_id

    #check if item exists in inventory
    item = next((item for item in inventory if str(item["id"]) == req_item_id), None)
    if not item:
        return {
            "error" : f"Item with id {req_item_id} does not exist in inventory."
        }
    
    if user_id not in cart:
        cart[user_id] = []

    cart[user_id].append({"id" : req_item_id, "qty" : qty, "price" : item["price"], "user_id" : user_id})

    return cart[user_id]

@app.get("/checkout")
def checkout(user_id : str) :
    print(f"input pass to checkout: user_id - {user_id}")
    if user_id not in cart or len(cart[user_id]) == 0 :
        return {
            "error" : f"No item found in cart for user {user_id}."
        }
    
    total_price = sum(item["qty"]*item["price"] for item in cart[user_id])

    cart_summary = {
        "user_id" : user_id,
        "items" : cart[user_id],
        "total_price" : total_price
    }

    cart[user_id] = [] #clear cart after checkout

    return cart_summary

