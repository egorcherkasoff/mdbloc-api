from beanie import Document, Indexed, Link
from typing import Optional
import pymongo
from pydantic import Field, field_validator, ValidationError, ValidationInfo, UUID4
import uuid
from fastapi_users.db import BeanieUserDatabase, BeanieBaseUser


class User(BeanieBaseUser, Document):
    """Модель пользователя"""

    id: UUID4 = Field(default_factory=uuid.uuid4)
    username: str = Field(min_length=6, max_length=64, pattern="^[a-zA-Z0-9_]*$")
    # avatar: str

    class Settings(BeanieBaseUser.Settings):
        name = "users"
        indexes = [
            [
                ("username", pymongo.TEXT),
            ],
        ]


async def get_user_db():
    yield BeanieUserDatabase(User)
