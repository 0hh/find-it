from fastapi import FastAPI

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

ITEMS = [
    Item(1, "Abstellkammer",None, [] ,[]),
    Item(2, "Oberstes Regal",1 , [], []),
    Item(3, "Regal 1", 1 , [], []),
]

@app.get("/items")
async def read_all_items():
    return ITEMS
"""
get breadcrumb path of an item
get children of a container
get location of an Item
change location of an Item
"""