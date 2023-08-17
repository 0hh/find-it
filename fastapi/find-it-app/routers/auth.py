from typing import Annotated
from fastapi import  APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Users
from passlib.context import CryptContext
from starlette import status

router = APIRouter()


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


 #   +----+---------------+--------------+-----------+-----------------+-----------+-------+
 #   | id |     email     |   username   | full_name | hashed_password | is_active | role  |
 #   +----+---------------+--------------+-----------+-----------------+-----------+-------+
 #   | 1  | dimi@mail.com | Ouzo61       | Dimi Tru  | $2a$04$rwDX3d0q | 1         | admin |
 #   | 2  | theo@mail.com | PsychboyJack | Theo Geo  | 6t6m2/nupouCCO1 | 1         | user  |
 #   +----+---------------+--------------+-----------+-----------------+-----------+-------+

class CreateUserRequest(BaseModel):
    email: str
    username: str
    full_name: str
    hashed_password: str
    role: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
db: Annotated[Session, Depends(get_db)]

@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
                      create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        full_name=create_user_request.full_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.hashed_password),
        is_active=True
    )
    db.add(create_user_model)
    db.commit()
