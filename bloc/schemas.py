from typing import Optional
import uuid
from pydantic import BaseModel, Field, UUID4
from fastapi_users import schemas as s


class Response(BaseModel):
    detail: str


class PublicationIn(BaseModel):
    """схема для добавления статьи"""

    title: str = Field(min_length=6, max_length=128)
    body: str = Field(min_length=30)


class PublicationUpdate(BaseModel):
    """схема для обновления статьи"""

    title: Optional[str] = Field(None, min_length=6, max_length=128)
    body: Optional[str] = Field(None, min_length=30)


class PublicationOut(BaseModel):
    """схема для отображения статьи"""

    id: UUID4
    title: str
    body: str
    # author: str
    views: int


class UserIn(s.BaseUserCreate):
    username: str = Field(min_length=6, max_length=64, pattern="^[a-zA-Z0-9_]*$")


class UserOut(s.BaseUser[uuid.UUID]):
    username: str


class UserUpdate(s.BaseUserUpdate):
    pass
