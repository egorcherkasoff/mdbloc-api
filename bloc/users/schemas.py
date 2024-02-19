from typing import Optional
import uuid
from pydantic import BaseModel, Field, UUID4
from fastapi_users import schemas as s


class UserCreate(s.BaseUserCreate):
    username: str = Field(min_length=6, max_length=64, pattern="^[a-zA-Z0-9_]*$")


class UserRead(s.BaseUser[uuid.UUID]):
    username: str


class UserUpdate(s.BaseUserUpdate):
    pass
