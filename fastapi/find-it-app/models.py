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
    contains_ids = Column(Integer)
    tags = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

"""
INSERT INTO items (id, item_name, location_id, contains_ids, tags, owner_id) 
VALUES (1,'Abstellkammer', null, 2, 'tag1', 1);

INSERT INTO items (id, item_name, location_id, contains_ids,  tags, owner_id)
VALUES (2,'Oberstes Regal', 1, 3, 'tag1', 1);

INSERT INTO items (id, item_name, location_id, contains_ids,  tags, owner_id)
VALUES (3,'Klebeband', 2, 2,'tag1', 1);

INSERT INTO items (id, item_name, location_id, contains_ids, tags,  owner_id)
VALUES (4,'Werkzeugkasten', 2, 5, 'tag1', 1);

INSERT INTO items (id, item_name, location_id, contains_ids,  tags, owner_id)
VALUES (5,'Hammer', 4, null, 'tag1', 1);

INSERT INTO items (id, item_name, location_id, contains_ids,  tags, owner_id)
VALUES (6,'Zange', 4,null, 'tag1', 1);

# TODO: listen aus contains und tags
{
  "item_name": "Fünfteiliges Bit-Set Bosch Professional",
  "location_id": 4,
  "contains_ids": 23,
  "tags":
    "Akkuschrauber",
"owner_id": 1


}
"""
