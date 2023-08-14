from fastapi import FastAPI

app = FastAPI()

class Item:
    id: int
    item_name: str
    parent_location_id: int
    children: list # containees?
    tags: list
    
    def __init__(self, id, item_name, parent_location, child_location, tag):
        self.id = id
        self.item_name = item_name
        self.parent_location = parent_location
        self.children = child_location
        self.tags = tags

ITEMS = [
    Item(
        1, "Hammer",
        2, # Parent:Werkzeugkiste
        None ,
        ["Werkzeug"]),

    Item(
        2, "Werkzeugkiste",
        3, # Parent:Regal 1
         None,
         ["Werkzeug"]),

    Item(
        3,
        "Regal 1", "Spiegelschrank",None ,["Werkzeug"])
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