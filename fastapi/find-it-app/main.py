from fastapi import FastAPI

app = FastAPI()

ITEMS = [
    {"item_name": "Hammer", 'location': 'Spiegelschrank'},
    {"item_name": "Makis Makakis", 'location': 'Auf der Minibar'},
    {"item_name": "Lizetti", 'location': 'Couch'},
    ]

@app.get("/items")
async def read_all_items():
    return {ITEMS}

@app.get("/items/{item_name}")
async def read_item(item_name: str):
    for item in ITEMS:
        if item.get('item_name').casefold() == item_name.casefold():
            return item.get('location')