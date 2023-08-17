from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Users
from passlib.context import CryptContext
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

router = APIRouter()

# openssl rand hex 32

SECRET_KEY = "R4ND0MSTR1N685c1d783b72fd458df8e5c0c64eb14deaa8e1abdb"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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


class Token(BaseModel):
    access_token: str
    token_type: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


def authentcate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {
        "sub": username,
        "id": user_id,
    }
    expires = datetime.utcnow() + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        full_name=create_user_request.full_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.hashed_password),
        is_active=True,
    )
    db.add(create_user_model)
    db.commit()


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    user = authentcate_user(form_data.username, form_data.password, db)
    if not user:
        return "Failed Authentication"
    token = create_access_token(user.username, user.id, timedelta(minutes=60))
    return {'access_token':token, 'token_type':'bearer'}
