from fastapi import FastAPI

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

ITEMS = [
    Item(1, "Abstellkammer",None, [] ,[]),
    Item(2, "Oberstes Regal",1 , [3, 4], []),
    Item(3, "Klebeband", 2 , [], []),
    Item(4, "Werkzeugkasten", 2 , [5, 6], []),
    Item(5, "Klebeband", 4 , [], []),
    Item(6, "Klebeband", 4 , [], []),
]

@app.get("/items")
async def read_all_items():
    return ITEMS
