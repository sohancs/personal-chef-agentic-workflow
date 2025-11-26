from pydantic import BaseModel
from typing import List


class SearchItemsRequest(BaseModel):
    items : List[str]

class SearchItemsResponse(BaseModel):
    available_items : List[str]
    not_available_items : List[str]


class AddToCartRequest(BaseModel):
    item_id : str
    qty : int
    user_id : str


class GetItemPriceRequest(BaseModel):
    item_id : str