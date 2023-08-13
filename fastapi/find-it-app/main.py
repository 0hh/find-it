from fastapi import FastAPI

app = FastAPI()

ITEMS = [
    {"title": "Lizettis Frontend", 'author': 'Jimmilony'},
    {"title": "Lizetti hothot", 'author': 'Dimi'},
    {"title": "Hello Lizetti", 'author': 'LxD'},
]
@app.get("/books")
async def read_all_books():
    return ITEMS