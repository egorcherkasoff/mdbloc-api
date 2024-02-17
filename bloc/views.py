from fastapi import APIRouter, status
from bloc.models import Publication
from bloc.schemas import PublicationIn, PublicationOut

publication_router = APIRouter(prefix="/publications", tags=["publications"])


@publication_router.post(
    path="/", status_code=status.HTTP_201_CREATED, response_model=PublicationOut
)
async def create_publication(publication: PublicationIn):
    """Эндпоинт для создания статьи"""
    new_publication = Publication(**publication.model_dump())
    await Publication.insert_one(new_publication)
    return PublicationOut(**new_publication.model_dump())


@publication_router.get(
    path="/", status_code=status.HTTP_200_OK, response_model=list[PublicationOut]
)
async def get_publications():
    """Эндпоинт для получения всех статей"""
    publications = await Publication.find_all().to_list()
    return [PublicationOut(**publication.model_dump()) for publication in publications]


@publication_router.get(
    path="/{publication_id}",
    status_code=status.HTTP_200_OK,
    response_model=PublicationOut,
)
async def get_publication(publication_id: str):
    """Эндпоинт для получения статьи по id"""
    publication = await Publication.find_one(Publication.id == publication_id)
    return PublicationOut(**publication.model_dump())
