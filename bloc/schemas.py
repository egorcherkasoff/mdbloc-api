from pydantic import BaseModel


class PublicationIn(BaseModel):
    """схема для добавления статьи"""

    title: str
    body: str


class PublicationOut(BaseModel):
    """схема для отображения статьи"""

    title: str
    body: str
    # author: str
    views: int
