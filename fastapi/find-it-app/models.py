from database import Base
from sqlalchemy import Column, Integer, String


class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
    location_id = Column(Integer)


"""
{
  "item_name": "Fünfteiliges Bit-Set Bosch Professional",
  "location_id": 4,
  "contains_ids": [
    23,
    24,
    25,
    26,
    27
  ],
  "tags": [
    "Akkuschrauber",
    "Bosch",
    "Werkzeug",
    "Kreuz",
    "Schlitz"
  ]
}
    
"""
