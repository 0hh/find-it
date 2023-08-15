from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional

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
        self.contains_ids = contains_ids
        self.tags = tags

class ItemRequest(BaseModel):
    id: Optional[int] # the type optional from typing allows id to be null in the request, backend then can assign id 
    item_name: str = Field(min_length=3, max_length=64, description="Name of the requested item")
    location_id: Optional[int] = Field(description="ID of the location")
    contains_ids: List[Optional[int]] = Field(description="List of IDs contained within the item")
    tags: List[str] = Field(description="List of tags associated with the item")

    class Config:
        schema_extra = {
            'example': {
                'item_name':'Fünfteiliges Bit-Set Bosch Professional',
                'location_id':4,
                'contains_ids': [23,24,25,26,27],
                'tags': ['Akkuschrauber','Bosch','Werkzeug', 'Kreuz', 'Schlitz']
            }
        }


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

@app.get("/item/{id}")
async def read_complete_item_by_id(id: int):
    for item in ITEMS:
        if item.id == id:
            return item

@app.get("/item-name/{id}")
async def read_item_name_by_id(id: int):
    for item in ITEMS:
        if item.id == id:
            return item.item_name

@app.get("/container/{item_name}/")
async def read_item_location_id_by_name(item_name: str):
    location_ids_to_return = []
    for item in ITEMS:
        if item.item_name == item_name:
            location_ids_to_return.append(item.location_id)
    return location_ids_to_return

@app.post("/create-item")
async def create_new_item(item_request: ItemRequest):
    new_item = Item(**item_request.dict())
    ITEMS.append(find_id(new_item))

def find_id(item: Item):
    item.id = 1 if len(ITEMS) == 0 else ITEMS[-1].id + 1 # use last element of items dictionary to determine the new id
    return item
    