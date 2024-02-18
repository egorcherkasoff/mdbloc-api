from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from bloc.models import Publication
from bloc.schemas import PublicationUpdate, Response, PublicationIn, PublicationOut
from pydantic import UUID4


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
    response_model=PublicationOut,
    responses={404: {"model": Response}},
)
async def get_publication(publication_id: UUID4):
    """Эндпоинт для получения статьи по id"""
    publication = await Publication.find_one(Publication.id == publication_id)
    if publication is not None:
        return PublicationOut(**publication.model_dump())
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Такой статьи не существует"},
    )


@publication_router.patch(
    path="/{publication_id}",
    response_model=PublicationOut,
    responses={404: {"model": Response}},
)
async def update_publication(publication_id: UUID4, publication: PublicationUpdate):
    """Эндпоинт для обновления статьи по id"""
    updated_publication = await Publication.find_one(Publication.id == publication_id)
    if updated_publication is not None:
        # проходим в цикле по каждому полю в запросе и ставим его вместо текущего в статье
        for field, value in publication.model_dump(exclude_unset=True).items():
            if value is not None:
                setattr(updated_publication, field, value)
            else:
                continue

        await updated_publication.save()
        return PublicationOut(**updated_publication.model_dump())
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Такой статьи не существует"},
    )
