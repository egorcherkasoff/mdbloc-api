from beanie import Document, Indexed, Link
from typing import Optional
import pymongo
from pydantic import Field, field_validator, ValidationError, ValidationInfo


class User(Document):
    """Модель пользователя"""

    username: str = Field(min_length=6, max_length=64, pattern="^[a-zA-Z0-9_]*$")
    password: str = Field(min_length=8, pattern="^[a-zA-Z0-9_]*$")
    avatar: str

    class Settings:
        name = "users"
        indexes = [
            [
                ("username", pymongo.TEXT),
            ],
        ]


class Publication(Document):
    """Модель статьи"""

    title: str = Field(min_length=6, max_length=128)
    body: str = Field(min_length=30)
    # author: User
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
