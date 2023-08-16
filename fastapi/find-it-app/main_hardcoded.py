from fastapi import FastAPI, Body

app = FastAPI()

ITEMS = [
    {"item_name": "Hammer", "location": "Spiegelschrank", "tag": "Werkzeug"},
    {"item_name": "Makis Makakis", "location": "Auf der Minibar", "tag": "Deko"},
    {"item_name": "Luftmatraze", "location": "Box 1", "tag": "Camping"},
    {"item_name": "Eismaschine", "location": "Vorratskammer", "tag": "Kochen"},
    {"item_name": "Boxhandschuhe", "location": "Tasche", "tag": "Sport"},
    {"item_name": "Bandagen", "location": "Tasche 2", "tag": "Sport"},
    {"item_name": "Schinenbeinschoner", "location": "Tasche 1", "tag": "Sport"},
]


@app.get("/items")
async def read_all_items():
    return ITEMS


@app.get("/items/{item_name}")
async def read_location_for_item_name(item_name: str):
    for item in ITEMS:
        if item.get("item_name").casefold() == item_name.casefold():
            return item.get("location")


@app.get("/items/{location}/")
async def read_item_by_query(location: str, tag: str):
    items_to_return = []
    for item in ITEMS:
        print(item)
        if (
            item.get("location").casefold() == location.casefold()
            and item.get("tag").casefold() == tag.casefold()
        ):
            items_to_return.append(item)
    return items_to_return


@app.get("/items/bytag/{tag}")
async def read_items_by_tag_path(tag: str):
    items_to_return = []
    for item in ITEMS:
        if item.get("tag").casefold() == tag.casefold():
            items_to_return.append(item)
    return items_to_return


@app.post("/items/create_item")
async def create_item(new_item=Body()):
    ITEMS.append(new_item)
