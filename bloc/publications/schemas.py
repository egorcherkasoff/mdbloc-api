from typing import Optional
from beanie import Link
from pydantic import BaseModel, Field, UUID4

from bloc.publications.models import Comment
from bloc.users.schemas import UserRead


class CommentCreate(BaseModel):
    """схема для создания комментария"""

    body: str = Field(min_length=1, max_length=256)
    comment: Optional[Link["Comment"]]


class CommentRead(BaseModel):
    """схема для отображения комментария"""

    id: UUID4
    body: str
    # comment: Optional[Link["Comment"]]


class PublicationCreate(BaseModel):
    """схема для добавления статьи"""

    title: str = Field(min_length=6, max_length=128)
    body: str = Field(min_length=30)


class PublicationUpdate(BaseModel):
    """схема для обновления статьи"""

    title: Optional[str] = Field(None, min_length=6, max_length=128)
    body: Optional[str] = Field(None, min_length=30)


class PublicationRead(BaseModel):
    """схема для отображения статьи"""

    id: UUID4
    title: str
    body: str
    author: UserRead
    views: int
    comments: Optional[list[CommentRead]] = []
