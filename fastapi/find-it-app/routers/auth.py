from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, Field
from models import Users

router = APIRouter()

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


@router.post("/auth")
async def create_user(create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        full_name=create_user_request.full_name,
        role=create_user_request.role,
        hashed_password=create_user_request.hashed_password,
        is_active=True
    )
    return create_user_model
