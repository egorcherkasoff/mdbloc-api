from typing import Optional
import uuid
from pydantic import BaseModel, Field, UUID4


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
    # author: str
    views: int
