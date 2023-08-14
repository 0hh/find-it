from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Item:
    id: int
    item_name: str
    location_id: int
    contains_ids: list 
    tags: list
    
    def __init__(self, id, item_name, location_id, contains_ids, tags):
        self.id = id
        self.item_name = item_name
        self.location_id = location_id
        self.children = contains_ids
        self.tags = tags

class ItemRequest(BaseModel):
    id: int
    item_name: str
    location_id: int
    contains_ids: list 
    tags: list


ITEMS = [
    Item(1, "Abstellkammer",None, [] ,[]),
    Item(2, "Oberstes Regal",1 , [3, 4], []),
    Item(3, "Klebeband", 2 , [], []),
    Item(4, "Werkzeugkasten", 2 , [5, 6], []),
    Item(5, "Hammer", 4 , [], []),
    Item(6, "Zange", 4 , [], []),
]

@app.get("/items")
async def read_all_items():
    return ITEMS

@app.post("/create-item")
async def create_item(item_request: ItemRequest):
    new_item = Item(**item_request.dict())
    ITEMS.append(new_item)


