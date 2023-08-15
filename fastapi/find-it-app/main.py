from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class Item:
    id: int
    item_name: str
    location_id: int
    contains_ids: List[int] 
    tags: List[str]
    
    def __init__(self, id, item_name, location_id, contains_ids, tags):
        self.id = id
        self.item_name = item_name
        self.location_id = location_id
        self.children = contains_ids
        self.tags = tags

class ItemRequest(BaseModel):
    id: int = Field(gt=0, description="Unique identifier for the item")
    item_name: str = Field(min_length=3, max_length=64, description="Name of the requested item")
    location_id: int = Field(gt=0, description="ID of the location")
    contains_ids: List[int] = Field(description="List of IDs contained within the item")
    tags: List[str] = Field(description="List of tags associated with the item") 


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


