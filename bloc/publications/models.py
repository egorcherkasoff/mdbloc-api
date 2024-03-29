from beanie import Document, Indexed, Link
from typing import Optional
import pymongo
from pydantic import Field, field_validator, ValidationError, ValidationInfo, UUID4
import uuid

from bloc.users.models import User


class Publication(Document):
    """Модель статьи"""

    id: UUID4 = Field(default_factory=uuid.uuid4)
    title: str = Field(min_length=6, max_length=128)
    body: str = Field(min_length=30)
    author: Link[User]
    views: int = 0

    class Settings:
        name = "publications"
        indexes = [
            [
                ("title", pymongo.TEXT),
            ],
        ]


class Comment(Document):
    """Модель комментария"""

    body: str = Field(min_length=6, max_length=128)
    # author: User
    publication: Publication
    comment: Optional[Link["Comment"]]

    class Settings:
        name = "comments"
