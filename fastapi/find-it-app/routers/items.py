from fastapi import APIRouter, Path, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Optional, Annotated
from starlette import status
from models import Items
from database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def read_all_items(db: Annotated[Session, Depends(get_db)]):
    """ Dependency injection of the opening db beforehand"""
    return db.query(Items).all()



# class Item:
#     id: int
#     item_name: str
#     location_id: int
#     contains_ids: List[int]
#     tags: List[str]

#     def __init__(self, id, item_name, location_id, contains_ids, tags):
#         self.id = id
#         self.item_name = item_name
#         self.location_id = location_id
#         self.contains_ids = contains_ids
#         self.tags = tags


# class ItemRequest(BaseModel):
#     id: Optional[
#         int
#     ]  # the type optional from typing allows id to be null in the request, backend then can assign id
#     item_name: str = Field(
#         min_length=3, max_length=64, description="Name of the requested item"
#     )
#     location_id: Optional[int] = Field(description="ID of the location")
#     contains_ids: List[Optional[int]] = Field(
#         description="List of IDs contained within the item"
#     )
#     tags: List[str] = Field(description="List of tags associated with the item")

#     class Config:
#         schema_extra = {
#             "example": {
#                 "item_name": "Fünfteiliges Bit-Set Bosch Professional",
#                 "location_id": 4,
#                 "contains_ids": [23, 24, 25, 26, 27],
#                 "tags": ["Akkuschrauber", "Bosch", "Werkzeug", "Kreuz", "Schlitz"],
#             }
#         }


# ITEMS = [
#     Item(1, "Abstellkammer", None, [], []),
#     Item(2, "Oberstes Regal", 1, [3, 4], []),
#     Item(3, "Klebeband", 2, [], []),
#     Item(4, "Werkzeugkasten", 2, [5, 6], []),
#     Item(5, "Hammer", 4, [], []),
#     Item(6, "Zange", 4, [], []),
# ]




# @router.get("/item/{id}", status_code=status.HTTP_200_OK)
# async def read_complete_item_by_id(id: int = Path(gt=0)):
#     for item in ITEMS:
#         if item.id == id:
#             return item
#     raise HTTPException(status_code=404, detail="Item not found")


# @router.get("/item-name/{id}", status_code=status.HTTP_200_OK)
# async def read_item_name_by_id(id: int):
#     for item in ITEMS:
#         if item.id == id:
#             return item.item_name
#         raise HTTPException(status_code=404, detail="Item not found")


# @router.get("/item/breadcrumb/{id}", status_code=status.HTTP_200_OK)
# async def read_item_breadcrumb_by_id(id: int):
#     breadcrumb = []
#     current_item = find_item_by_id(id)

#     while current_item:
#         breadcrumb.append(current_item.item_name)
#         if current_item.location_id is None:
#             break
#         current_item = find_item_by_id(current_item.location_id)

#     return breadcrumb[::-1]


# @router.get("/item/container/{item-name}/", status_code=status.HTTP_200_OK)
# async def read_item_location_id_by_name(item_name: str):
#     location_ids_to_return = []
#     for item in ITEMS:
#         if item.item_name == item_name:
#             location_ids_to_return.append(item.location_id)
#     return location_ids_to_return


# @router.post("/item/", status_code=status.HTTP_201_CREATED)
# async def create_new_item(item_request: ItemRequest):
#     new_item = Item(**item_request.dict())
#     ITEMS.append(find_free_id(new_item))


# @router.put("/item/", status_code=status.HTTP_204_NO_CONTENT)
# async def update_item(item: ItemRequest):
#     item_changed = False
#     for i in range(len(ITEMS)):
#         if ITEMS[i].id == item.id:
#             ITEMS[i] = item
#             item_changed = True
#     if not item_changed:
#         raise HTTPException(status_code=404, detail="Item not found")


# @router.delete("/items/{id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delte_item_by_id(id: int):
#     item_changed = False
#     for i in range(len(ITEMS)):
#         if ITEMS[i].id == id:
#             ITEMS.pop(i)
#             item_changed = True
#             break
#     if not item_changed:
#         raise HTTPException(status_code=404, detail="Item not found")


# def find_free_id(item: Item):
#     """Create a new id by checking the last item of the dictionary"""
#     item.id = 1 if len(ITEMS) == 0 else ITEMS[-1].id + 1
#     return item


# def find_item_by_id(id):
#     """Find and return the item object from the list using its id."""
#     for item in ITEMS:
#         if item.id == id:
#             return item
#     return None

