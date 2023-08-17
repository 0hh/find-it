from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)

class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
    location_id = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))


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
