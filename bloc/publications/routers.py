from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from bloc.users.auth import current_user
from bloc.users.models import User
from .models import Publication, Comment
from .schemas import (
    PublicationListRead,
    PublicationRead,
    PublicationCreate,
    PublicationUpdate,
)
from bloc.schemas import Response
from pydantic import UUID4
from fastapi import Depends
from bloc.config import AppConfig


router = APIRouter(prefix="/publications", tags=["publications"])


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=PublicationListRead,
    responses={404: {"model": Response}},
)
async def get_publications(page: int = 1):
    """Эндпоинт для получения всех статей"""
    # устанавливаем "границы" для поиска по странице
    pg_size = AppConfig.PAGE_SIZE
    start_from = pg_size * (page - 1)
    end_by = start_from + pg_size
    # достаем кол-во документов в колекции чтобы понять сколько всего будет страниц
    total_pages = await Publication.count() // pg_size + 1
    print(total_pages)
    publications = await Publication.find(
        fetch_links=True, skip=start_from, limit=end_by
    ).to_list()
    if publications != []:
        # формируем список статей
        publication_list = [
            PublicationRead(**publication.model_dump()) for publication in publications
        ]
        return PublicationListRead(
            page=page,
            next=page + 1 if page < total_pages else page,
            prev=page - 1 if page <= 1 else None,
            results=publication_list,
        )

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Статей с указанными вами параметрами не существует"},
    )


@router.get(
    path="/{publication_id}",
    response_model=PublicationRead,
    responses={404: {"model": Response}},
)
async def get_publication(publication_id: UUID4):
    """Эндпоинт для получения статьи по id"""
    publication = await Publication.find_one(
        Publication.id == publication_id, fetch_links=True
    )
    if publication is not None:
        return PublicationRead(**publication.model_dump())
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Такой статьи не существует"},
    )


@router.post(
    path="/", status_code=status.HTTP_201_CREATED, response_model=PublicationRead
)
async def create_publication(
    publication: PublicationCreate,
    user: User = Depends(current_user),
):
    """Эндпоинт для создания статьи"""
    if user != None:
        new_publication = Publication(**publication.model_dump(), author=user)
        await Publication.insert_one(new_publication)
        return PublicationRead(**new_publication.model_dump())


@router.patch(
    path="/{publication_id}",
    response_model=PublicationRead,
    responses={404: {"model": Response}},
)
async def update_publication(
    publication_id: UUID4,
    publication: PublicationUpdate,
    user: User = Depends(current_user),
):
    """Эндпоинт для обновления статьи по id"""
    updated_publication = await Publication.find_one(
        Publication.id == publication_id, fetch_links=True
    )
    if updated_publication.author != user:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"detail": "Нельзя обновлять чужую статью"},
        )
    if updated_publication is not None:
        # проходим в цикле по каждому полю в запросе и ставим его вместо текущего в статье
        for field, value in publication.model_dump(exclude_unset=True).items():
            setattr(updated_publication, field, value)

        await updated_publication.save()
        return PublicationRead(**updated_publication.model_dump())
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Такой статьи не существует"},
    )


@router.delete(
    path="/{publication_id}",
    responses={
        204: {"description": "Publication deleted"},
        404: {"model": Response},
    },
)
async def delete_publication(
    publication_id: UUID4,
    user: User = Depends(current_user),
):
    """Эндпоинт для удаления статьи по ID"""
    deleted_publication = await Publication.find_one(Publication.id == publication_id)
    if deleted_publication.author != user:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"detail": "Нельзя удалять чужую статью"},
        )
    if deleted_publication is not None:
        await deleted_publication.delete()
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Такой статьи не существует"},
    )
